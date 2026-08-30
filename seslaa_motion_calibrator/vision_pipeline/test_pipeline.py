import unittest

from vision_pipeline.config import PipelineConfig
from vision_pipeline.models import Detection
from vision_pipeline.events import EventEngine
from vision_pipeline.evaluate import detection_metrics
from vision_pipeline.risk import assess_track, estimate_depth
from vision_pipeline.tracking import IoUTracker


class PipelineTests(unittest.TestCase):
    def test_iou_tracker_preserves_id(self):
        tracker = IoUTracker()
        first = tracker.update([Detection((10, 10, 50, 100), "person", 0.9)])
        second = tracker.update([Detection((12, 12, 52, 102), "person", 0.9)])
        self.assertEqual(first[0].track_id, second[0].track_id)

    def test_calibrated_depth_and_path_risk(self):
        config = PipelineConfig(focal_length_px=720)
        tracker = IoUTracker()
        track = tracker.update([Detection((300, 100, 340, 460), "person", 0.9)])[0]
        self.assertAlmostEqual(estimate_depth(track, config), 3.4, places=1)
        track.depth_m = 2.0
        assess_track(track, 3.0, 30, 640, config)
        self.assertEqual(track.risk, "CRITICAL")

    def test_events_are_debounced(self):
        tracker = IoUTracker()
        track = tracker.update([Detection((10, 10, 50, 100), "person", 0.9)])[0]
        engine = EventEngine(cooldown_seconds=100)
        self.assertEqual(len(engine.update([track], False)), 1)
        self.assertEqual(engine.update([track], False), [])

    def test_detection_metrics(self):
        result = detection_metrics([{"box": [0, 0, 10, 10], "label": "person"}], [{"box": [0, 0, 10, 10], "label": "person"}])
        self.assertEqual(result["precision"], 1.0)
        self.assertEqual(result["recall"], 1.0)


if __name__ == "__main__":
    unittest.main()