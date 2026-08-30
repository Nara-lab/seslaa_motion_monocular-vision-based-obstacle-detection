from dataclasses import dataclass
from typing import List

from .models import Detection


def iou(first, second) -> float:
    left, top = max(first[0], second[0]), max(first[1], second[1])
    right, bottom = min(first[2], second[2]), min(first[3], second[3])
    intersection = max(0, right - left) * max(0, bottom - top)
    first_area = max(0, first[2] - first[0]) * max(0, first[3] - first[1])
    second_area = max(0, second[2] - second[0]) * max(0, second[3] - second[1])
    union = first_area + second_area - intersection
    return intersection / union if union else 0.0


@dataclass
class Track:
    track_id: int
    label: str
    box: tuple[int, int, int, int]
    confidence: float
    missed_frames: int = 0
    previous_box: tuple[int, int, int, int] | None = None
    velocity_px_per_frame: tuple[float, float] = (0.0, 0.0)
    depth_m: float | None = None
    ttc_s: float | None = None
    risk: str = "SAFE"

    @property
    def center(self):
        return ((self.box[0] + self.box[2]) / 2, (self.box[1] + self.box[3]) / 2)


class IoUTracker:
    def __init__(self, min_iou=0.12, max_missed_frames=8):
        self.min_iou = min_iou
        self.max_missed_frames = max_missed_frames
        self.next_id = 1
        self.tracks: dict[int, Track] = {}

    def update(self, detections: List[Detection]) -> List[Track]:
        unmatched = set(range(len(detections)))
        pairs = sorted(((iou(track.box, detection.box), track_id, index) for track_id, track in self.tracks.items() for index, detection in enumerate(detections)), reverse=True)
        matched = set()
        for score, track_id, index in pairs:
            if score < self.min_iou or track_id in matched or index not in unmatched:
                continue
            track = self.tracks[track_id]
            track.previous_box = track.box
            track.box = detections[index].box
            track.label = detections[index].label
            track.confidence = detections[index].confidence
            track.missed_frames = 0
            track.velocity_px_per_frame = self._velocity(track.previous_box, track.box)
            matched.add(track_id)
            unmatched.remove(index)
        for index in unmatched:
            detection = detections[index]
            self.tracks[self.next_id] = Track(self.next_id, detection.label, detection.box, detection.confidence)
            self.next_id += 1
        for track_id, track in list(self.tracks.items()):
            if track_id not in matched and track.missed_frames == 0 and track.previous_box is not None:
                track.missed_frames += 1
            elif track_id not in matched:
                track.missed_frames += 1
            if track.missed_frames > self.max_missed_frames:
                del self.tracks[track_id]
        return list(self.tracks.values())

    @staticmethod
    def _velocity(previous, current):
        if previous is None:
            return 0.0, 0.0
        return ((current[0] + current[2] - previous[0] - previous[2]) / 2, (current[1] + current[3] - previous[1] - previous[3]) / 2)