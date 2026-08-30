from dataclasses import dataclass
from time import monotonic

from .tracking import Track


@dataclass
class VisionEvent:
    event_type: str
    track_id: int
    label: str
    risk: str
    timestamp: float


class EventEngine:
    def __init__(self, cooldown_seconds=2.0):
        self.cooldown_seconds = cooldown_seconds
        self.last_events: dict[tuple[int, str], float] = {}
        self.known_ids: set[int] = set()
        self.last_risk: dict[int, str] = {}
        self.last_motion: dict[int, str] = {}

    def update(self, tracks: list[Track], camera_motion: bool) -> list[VisionEvent]:
        now = monotonic()
        events = []
        current_ids = {track.track_id for track in tracks}
        for track in tracks:
            event_type = "ENTERED" if track.track_id not in self.known_ids else None
            speed = (track.velocity_px_per_frame[0] ** 2 + track.velocity_px_per_frame[1] ** 2) ** 0.5
            motion = "MOVING" if speed >= 3 else "STATIONARY"
            if speed >= 35:
                event_type = "SUDDEN_MOVEMENT"
            elif self.last_motion.get(track.track_id) != motion:
                event_type = motion
            self.last_motion[track.track_id] = motion
            if track.ttc_s is not None and track.ttc_s <= 2.5:
                event_type = "APPROACHING"
            if self.last_risk.get(track.track_id) != track.risk and track.risk in {"WARNING", "CRITICAL"}:
                event_type = "COLLISION_RISK"
            self.last_risk[track.track_id] = track.risk
            if event_type and self._allowed(track.track_id, event_type, now):
                events.append(VisionEvent(event_type, track.track_id, track.label, track.risk, now))
        for track_id in self.known_ids - current_ids:
            if self._allowed(track_id, "EXITED", now):
                events.append(VisionEvent("EXITED", track_id, "UNKNOWN", "SAFE", now))
        if camera_motion and self._allowed(0, "CAMERA_SHAKE", now):
            events.append(VisionEvent("CAMERA_SHAKE", 0, "CAMERA", "CAUTION", now))
        self.known_ids = current_ids
        return events

    def _allowed(self, track_id, event_type, now):
        key = (track_id, event_type)
        if now - self.last_events.get(key, 0) < self.cooldown_seconds:
            return False
        self.last_events[key] = now
        return True