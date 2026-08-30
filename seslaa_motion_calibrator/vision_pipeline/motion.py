import cv2
import numpy as np


class OpticalFlowEstimator:
    def __init__(self, min_points=12):
        self.min_points = min_points
        self.previous_gray = None

    def update(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        result = {"camera_motion": False, "global_dx": 0.0, "global_dy": 0.0, "inlier_ratio": 0.0}
        if self.previous_gray is None:
            self.previous_gray = gray
            return result
        points = cv2.goodFeaturesToTrack(self.previous_gray, maxCorners=160, qualityLevel=0.01, minDistance=7)
        if points is not None and len(points) >= self.min_points:
            next_points, status, _ = cv2.calcOpticalFlowPyrLK(self.previous_gray, gray, points, None)
            old, new = points[status.ravel() == 1], next_points[status.ravel() == 1]
            if len(old) >= self.min_points:
                transform, inliers = cv2.estimateAffinePartial2D(old, new, method=cv2.RANSAC)
                if transform is not None:
                    result["global_dx"] = float(transform[0, 2])
                    result["global_dy"] = float(transform[1, 2])
                    result["inlier_ratio"] = float(np.mean(inliers))
                    result["camera_motion"] = abs(result["global_dx"]) + abs(result["global_dy"]) > 8 and result["inlier_ratio"] > 0.45
        self.previous_gray = gray
        return result