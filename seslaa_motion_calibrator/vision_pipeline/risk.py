from .config import PipelineConfig
from .tracking import Track


def estimate_depth(track: Track, config: PipelineConfig) -> float | None:
    expected_height = config.known_object_heights.get(track.label.lower())
    pixel_height = track.box[3] - track.box[1]
    if not expected_height or pixel_height <= 0 or config.focal_length_px <= 0:
        return None
    return expected_height * config.focal_length_px / pixel_height


def assess_track(track: Track, previous_depth: float | None, frame_rate: float, frame_width: int, config: PipelineConfig):
    if track.depth_m is None or previous_depth is None or frame_rate <= 0:
        track.ttc_s = None
    else:
        closing_rate = (previous_depth - track.depth_m) * frame_rate
        track.ttc_s = track.depth_m / closing_rate if closing_rate > 0 else None
    center_x = (track.box[0] + track.box[2]) / 2
    in_path = abs(center_x - frame_width / 2) <= frame_width * config.path_width_ratio / 2
    if not in_path or track.ttc_s is None:
        track.risk = "SAFE"
    elif track.ttc_s <= config.critical_ttc_seconds:
        track.risk = "CRITICAL"
    elif track.ttc_s <= config.warning_ttc_seconds:
        track.risk = "WARNING"
    elif track.ttc_s <= config.caution_ttc_seconds:
        track.risk = "CAUTION"
    else:
        track.risk = "SAFE"