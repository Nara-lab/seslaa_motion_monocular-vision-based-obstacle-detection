from dataclasses import dataclass


@dataclass
class Detection:
    box: tuple[int, int, int, int]
    label: str
    confidence: float