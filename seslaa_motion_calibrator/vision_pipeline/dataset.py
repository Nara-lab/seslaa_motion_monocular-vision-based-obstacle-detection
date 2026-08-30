import argparse
import shutil
from pathlib import Path


def prepare_dataset(source: str | Path, destination: str | Path):
    source_path, destination_path = Path(source), Path(destination)
    images = sorted(path for path in source_path.rglob("*") if path.suffix.lower() in {".jpg", ".jpeg", ".png"})
    if not images:
        raise ValueError(f"No images found in {source_path}")
    for index, image in enumerate(images):
        split = "val" if index % 5 == 0 else "train"
        target = destination_path / split / image.name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(image, target)
    return len(images)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Prepare an image dataset split for detector fine-tuning")
    parser.add_argument("source")
    parser.add_argument("destination")
    args = parser.parse_args()
    print(f"Prepared {prepare_dataset(args.source, args.destination)} images")