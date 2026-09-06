"""Canonical labels shared by detector backends and telemetry."""

ALIASES = {
    "bike": "bicycle",
    "bikes": "bicycle",
    "motorbike": "motorcycle",
    "motorbikes": "motorcycle",
    "airplane": "aircraft",
    "aeroplane": "aircraft",
    "flight": "aircraft",
    "flights": "aircraft",
    "human": "person",
    "pedestrian": "person",
    "pedestrians": "person",
    "bird(s)": "bird",
    "birds": "bird",
    "animals": "animal",
    "tree(s)": "tree",
    "trees": "tree",
    "building(s)": "building",
    "buildings": "building",
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
    "bird": 0.25,
    "cat": 0.35,
    "dog": 0.55,
    "horse": 1.50,
    "sheep": 0.80,
    "cow": 1.40,
    "elephant": 2.50,
    "bear": 1.20,
    "zebra": 1.40,
    "giraffe": 2.50,
    "tree": 4.00,
    "building": 8.00,
    "traffic sign": 1.20,
}


def canonicalize(label: str) -> str | None:
    normalized = label.strip().lower()
    if not normalized:
        return None
    return ALIASES.get(normalized, normalized)