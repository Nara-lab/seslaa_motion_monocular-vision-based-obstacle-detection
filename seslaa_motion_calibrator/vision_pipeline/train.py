import argparse
from pathlib import Path


def train_yolo(dataset: Path, epochs: int):
    try:
        from ultralytics import YOLO
    except ImportError as error:
        raise RuntimeError("Install ultralytics to train: python -m pip install ultralytics") from error
    model = YOLO("yolo11n.pt")
    return model.train(data=str(dataset), epochs=epochs, imgsz=640, device="auto")


def main():
    parser = argparse.ArgumentParser(description="Prepare a detector training run")
    parser.add_argument("dataset", type=Path)
    parser.add_argument("--backend", choices=["ultralytics-yolo", "tensorflow-lite", "opencv-dnn"], default="ultralytics-yolo")
    parser.add_argument("--epochs", type=int, default=50)
    args = parser.parse_args()
    if args.backend == "ultralytics-yolo":
        train_yolo(args.dataset, args.epochs)
    else:
        raise SystemExit(f"Backend {args.backend} requires its native trainer and annotated dataset format")


if __name__ == "__main__":
    main()