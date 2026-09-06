"""Canonical labels shared by detector backends and telemetry."""

GENERIC_LABELS = {
    "fashion",
    "food",
    "home goods",
    "place",
    "plant",
    "object",
    "unknown",
}

ALIASES = {
    "bike": "bicycle",
    "motorbike": "motorcycle",
    "airplane": "aircraft",
    "aeroplane": "aircraft",
    "flight": "aircraft",
    "human": "person",
    "pedestrian": "person",
}

KNOWN_OBJECT_HEIGHTS = {
    "person": 1.70,
    "car": 1.50,
    "motorcycle": 1.30,
    "bicycle": 1.30,
    "bus": 3.00,
    "truck": 2.50,
    "aircraft": 3.00,
    "animal": 0.80,
    "tree": 4.00,
    "building": 8.00,
    "traffic sign": 1.20,
}


def canonicalize(label: str) -> str | None:
    normalized = label.strip().lower()
    if not normalized or normalized in GENERIC_LABELS:
        return None
    return ALIASES.get(normalized, normalized)