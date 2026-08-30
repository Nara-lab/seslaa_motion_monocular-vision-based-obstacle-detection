from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict


@dataclass
class PipelineConfig:
    confidence_threshold: float = 0.45
    max_missed_frames: int = 8
    min_iou: float = 0.12
    event_cooldown_seconds: float = 2.0
    path_width_ratio: float = 0.36
    critical_ttc_seconds: float = 1.2
    warning_ttc_seconds: float = 2.5
    caution_ttc_seconds: float = 4.0
    min_flow_points: int = 12
    known_object_heights: Dict[str, float] = field(default_factory=lambda: {
        "person": 1.70,
        "car": 1.50,
        "truck": 2.50,
        "bus": 3.00,
        "motorcycle": 1.30,
        "bicycle": 1.30,
    })
    focal_length_px: float = 0.0
    model_path: Path | None = None
    labels_path: Path | None = None

    @classmethod
    def from_yaml(cls, path: str | Path) -> "PipelineConfig":
        try:
            import yaml
        except ImportError as error:
            raise RuntimeError("Install PyYAML to load YAML configuration") from error
        with Path(path).open(encoding="utf-8") as stream:
            return cls(**(yaml.safe_load(stream) or {}))