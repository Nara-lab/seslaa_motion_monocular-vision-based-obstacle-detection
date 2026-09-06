from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict


@dataclass
class PipelineConfig:
    confidence_threshold: float = 0.45
    max_missed_frames: int = 8
    min_confirmed_frames: int = 2
    min_iou: float = 0.12
    event_cooldown_seconds: float = 2.0
    path_width_ratio: float = 0.36
    critical_ttc_seconds: float = 1.2
    warning_ttc_seconds: float = 2.5
    caution_ttc_seconds: float = 4.0
    min_flow_points: int = 12
    known_object_heights: Dict[str, float] = field(default_factory=lambda: {
        "person": 1.70, "car": 1.50, "truck": 2.50, "bus": 3.00,
        "motorcycle": 1.30, "bicycle": 1.30, "aircraft": 3.00,
        "animal": 0.80, "tree": 4.00, "building": 8.00,
        "traffic sign": 1.20, "bird": 0.25, "cat": 0.35,
        "dog": 0.55, "horse": 1.50, "sheep": 0.80, "cow": 1.40,
        "elephant": 2.50, "bear": 1.20, "zebra": 1.40,
        "giraffe": 2.50,
    })
    focal_length_px: float = 0.0
    model_path: Path | None = Path("assets/models/yolo11n.onnx")
    labels_path: Path | None = None

    @classmethod
    def from_yaml(cls, path: str | Path) -> "PipelineConfig":
        try:
            import yaml
        except ImportError as error:
            raise RuntimeError("Install PyYAML to load YAML configuration") from error
        config_path = Path(path).resolve()
        with config_path.open(encoding="utf-8") as stream:
            values = yaml.safe_load(stream) or {}
        for key in ("model_path", "labels_path"):
            value = values.get(key)
            if value and not Path(value).is_absolute():
                values[key] = config_path.parent.parent / value
            elif value:
                values[key] = Path(value)
        return cls(**values)