import argparse
import json
from pathlib import Path


def detection_metrics(predictions, ground_truth, iou_threshold=0.5):
    matched = set()
    true_positives = 0
    false_positives = 0
    for prediction in predictions:
        candidates = [(index, _iou(prediction["box"], truth["box"])) for index, truth in enumerate(ground_truth) if index not in matched and prediction["label"] == truth["label"]]
        if candidates and max(candidates, key=lambda item: item[1])[1] >= iou_threshold:
            matched.add(max(candidates, key=lambda item: item[1])[0])
            true_positives += 1
        else:
            false_positives += 1
    false_negatives = len(ground_truth) - len(matched)
    precision = true_positives / max(1, true_positives + false_positives)
    recall = true_positives / max(1, true_positives + false_negatives)
    return {"precision": precision, "recall": recall, "f1": 2 * precision * recall / max(1e-9, precision + recall), "tp": true_positives, "fp": false_positives, "fn": false_negatives}


def _iou(first, second):
    left, top = max(first[0], second[0]), max(first[1], second[1])
    right, bottom = min(first[2], second[2]), min(first[3], second[3])
    intersection = max(0, right - left) * max(0, bottom - top)
    area_first = max(0, first[2] - first[0]) * max(0, first[3] - first[1])
    area_second = max(0, second[2] - second[0]) * max(0, second[3] - second[1])
    return intersection / max(1, area_first + area_second - intersection)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Evaluate JSON detection predictions")
    parser.add_argument("predictions", type=Path)
    parser.add_argument("ground_truth", type=Path)
    args = parser.parse_args()
    print(json.dumps(detection_metrics(json.loads(args.predictions.read_text()), json.loads(args.ground_truth.read_text())), indent=2))