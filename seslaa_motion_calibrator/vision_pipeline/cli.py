import argparse

import cv2

from .config import PipelineConfig
from .pipeline import MonocularVisionPipeline


def main():
    parser = argparse.ArgumentParser(description="Run monocular object, motion, event, and risk analysis")
    parser.add_argument("input", help="camera index or video path")
    parser.add_argument("--config")
    parser.add_argument("--output")
    parser.add_argument("--focal-length", type=float, default=0.0)
    args = parser.parse_args()
    config = PipelineConfig.from_yaml(args.config) if args.config else PipelineConfig()
    config.focal_length_px = args.focal_length
    source = int(args.input) if args.input.isdigit() else args.input
    capture = cv2.VideoCapture(source)
    if not capture.isOpened():
        raise SystemExit(f"Unable to open input: {args.input}")
    fps = capture.get(cv2.CAP_PROP_FPS) or 30.0
    pipeline = MonocularVisionPipeline(config, fps)
    writer = None
    while True:
        success, frame = capture.read()
        if not success:
            break
        result = pipeline.process(frame)
        rendered = pipeline.draw(frame, result)
        for event in result.events:
            print(f"{event.event_type} id={event.track_id} label={event.label} risk={event.risk}")
        if args.output and writer is None:
            size = (rendered.shape[1], rendered.shape[0])
            writer = cv2.VideoWriter(args.output, cv2.VideoWriter_fourcc(*"mp4v"), fps, size)
        if writer:
            writer.write(rendered)
        cv2.imshow("SESLAA monocular vision", rendered)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    capture.release()
    if writer:
        writer.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()