from pathlib import Path
from typing import List

import cv2
import numpy as np

from .models import Detection
from .taxonomy import canonicalize


class OpenCVDetector:
    """YOLO11 detector with an OpenCV/HOG fallback."""

    def __init__(self, model_path: Path | None = None, labels_path: Path | None = None, confidence_threshold: float = 0.45):
        self.confidence_threshold = confidence_threshold
        self.yolo = None
        self.net = None
        if model_path and "yolo11" in Path(model_path).stem.lower():
            try:
                from ultralytics import YOLO
            except ImportError as error:
                raise RuntimeError(
                    "YOLO11n requires ultralytics; install vision_requirements.txt"
                ) from error
            self.yolo = YOLO(str(model_path))
        elif model_path:
            self.net = cv2.dnn.readNetFromONNX(str(model_path))
        self.labels = []
        if labels_path and Path(labels_path).exists():
            self.labels = Path(labels_path).read_text(encoding="utf-8").splitlines()
        self.hog = cv2.HOGDescriptor()
        self.hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    def detect(self, frame: np.ndarray) -> List[Detection]:
        if self.yolo is not None:
            return self._detect_yolo(frame)
        if self.net is not None:
            return self._detect_dnn(frame)
        boxes, weights = self.hog.detectMultiScale(frame, winStride=(8, 8), padding=(8, 8), scale=1.05)
        return [
            Detection((int(x), int(y), int(x + width), int(y + height)), "person", float(weight))
            for (x, y, width, height), weight in zip(boxes, weights)
            if float(weight) >= self.confidence_threshold
        ]

    def _detect_yolo(self, frame: np.ndarray) -> List[Detection]:
        results = self.yolo.predict(
            source=frame,
            imgsz=640,
            conf=self.confidence_threshold,
            device="cpu",
            verbose=False,
        )
        detections = []
        for result in results:
            names = result.names
            for box, confidence, class_id in zip(
                result.boxes.xyxy.cpu().tolist(),
                result.boxes.conf.cpu().tolist(),
                result.boxes.cls.cpu().tolist(),
            ):
                label = canonicalize(names[int(class_id)])
                if label is None:
                    continue
                detections.append(
                    Detection(
                        tuple(int(value) for value in box),
                        label,
                        float(confidence),
                    )
                )
        return detections

    def _detect_dnn(self, frame: np.ndarray) -> List[Detection]:
        height, width = frame.shape[:2]
        blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (640, 640), swapRB=True)
        self.net.setInput(blob)
        output = self.net.forward()
        detections = []
        for row in np.reshape(output, (-1, output.shape[-1])):
            if row.shape[0] < 6:
                continue
            objectness = float(row[4])
            scores = row[5:]
            class_id = int(np.argmax(scores))
            confidence = objectness * float(scores[class_id])
            if confidence < self.confidence_threshold:
                continue
            center_x, center_y, box_width, box_height = row[:4] * [width, height, width, height]
            box = (int(center_x - box_width / 2), int(center_y - box_height / 2), int(center_x + box_width / 2), int(center_y + box_height / 2))
            raw_label = self.labels[class_id] if class_id < len(self.labels) else f"class-{class_id}"
            label = canonicalize(raw_label)
            if label is not None:
                detections.append(Detection(box, label, confidence))
        return detections