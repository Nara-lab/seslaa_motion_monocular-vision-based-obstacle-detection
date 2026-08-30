from pathlib import Path
from typing import List

import cv2
import numpy as np

from .models import Detection


class OpenCVDetector:
    """CPU-safe detector with an optional ONNX backend and HOG baseline."""

    def __init__(self, model_path: Path | None = None, labels_path: Path | None = None, confidence_threshold: float = 0.45):
        self.confidence_threshold = confidence_threshold
        self.net = cv2.dnn.readNetFromONNX(str(model_path)) if model_path else None
        self.labels = []
        if labels_path and Path(labels_path).exists():
            self.labels = Path(labels_path).read_text(encoding="utf-8").splitlines()
        self.hog = cv2.HOGDescriptor()
        self.hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    def detect(self, frame: np.ndarray) -> List[Detection]:
        if self.net is not None:
            return self._detect_dnn(frame)
        boxes, weights = self.hog.detectMultiScale(frame, winStride=(8, 8), padding=(8, 8), scale=1.05)
        return [
            Detection((int(x), int(y), int(x + width), int(y + height)), "person", float(weight))
            for (x, y, width, height), weight in zip(boxes, weights)
            if float(weight) >= self.confidence_threshold
        ]

    def _detect_dnn(self, frame: np.ndarray) -> List[Detection]:
        height, width = frame.shape[:2]
        blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (640, 640), swapRB=True)
        self.net.setInput(blob)
        output = self.net.forward()
        detections = []
        for row in np.reshape(output, (-1, output.shape[-1])):
            if row.shape[0] < 6:
                continue
            scores = row[5:]
            class_id = int(np.argmax(scores))
            confidence = float(scores[class_id])
            if confidence < self.confidence_threshold:
                continue
            center_x, center_y, box_width, box_height = row[:4] * [width, height, width, height]
            box = (int(center_x - box_width / 2), int(center_y - box_height / 2), int(center_x + box_width / 2), int(center_y + box_height / 2))
            label = self.labels[class_id] if class_id < len(self.labels) else f"class-{class_id}"
            detections.append(Detection(box, label, confidence))
        return detections