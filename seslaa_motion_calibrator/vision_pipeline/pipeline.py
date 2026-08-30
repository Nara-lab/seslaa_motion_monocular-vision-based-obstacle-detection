from dataclasses import dataclass

import cv2

from .config import PipelineConfig
from .detectors import OpenCVDetector
from .events import EventEngine, VisionEvent
from .motion import OpticalFlowEstimator
from .risk import assess_track, estimate_depth
from .tracking import IoUTracker, Track


@dataclass
class FrameResult:
    tracks: list[Track]
    events: list[VisionEvent]
    camera_motion: dict


class MonocularVisionPipeline:
    def __init__(self, config: PipelineConfig | None = None, fps: float = 30.0):
        self.config = config or PipelineConfig()
        self.fps = fps
        self.detector = OpenCVDetector(self.config.model_path, self.config.labels_path, self.config.confidence_threshold)
        self.tracker = IoUTracker(self.config.min_iou, self.config.max_missed_frames)
        self.flow = OpticalFlowEstimator(self.config.min_flow_points)
        self.events = EventEngine(self.config.event_cooldown_seconds)
        self.previous_depth: dict[int, float] = {}

    def process(self, frame) -> FrameResult:
        camera_motion = self.flow.update(frame)
        tracks = self.tracker.update(self.detector.detect(frame))
        for track in tracks:
            prior = self.previous_depth.get(track.track_id)
            track.depth_m = estimate_depth(track, self.config)
            assess_track(track, prior, self.fps, frame.shape[1], self.config)
            if track.depth_m is not None:
                self.previous_depth[track.track_id] = track.depth_m
        return FrameResult(tracks, self.events.update(tracks, camera_motion["camera_motion"]), camera_motion)

    @staticmethod
    def draw(frame, result: FrameResult):
        output = frame.copy()
        colors = {"SAFE": (80, 210, 120), "CAUTION": (0, 210, 255), "WARNING": (0, 130, 255), "CRITICAL": (0, 0, 255)}
        for track in result.tracks:
            color = colors[track.risk]
            cv2.rectangle(output, track.box[:2], track.box[2:], color, 2)
            details = f"{track.label} ID:{track.track_id} {track.confidence:.2f} {track.risk}"
            if track.ttc_s is not None:
                details += f" TTC:{track.ttc_s:.1f}s"
            cv2.putText(output, details, (track.box[0], max(18, track.box[1] - 8)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        return output