# Monocular Vision Pipeline

The runnable pipeline is `vision_pipeline`. It uses OpenCV HOG as a CPU-safe baseline and accepts an optional ONNX model through `PipelineConfig.model_path`. This keeps the system executable without silently downloading a model; a YOLO-family nano model exported to ONNX is the recommended production detector, while the existing Mask R-CNN model remains the research-quality reference.

## Run

```powershell
python -m pip install opencv-python numpy pyyaml
python -m vision_pipeline.cli 0 --focal-length 720 --output export/annotated.mp4
python -m vision_pipeline.cli data/video/example.mp4 --config vision_pipeline/config.yaml
```

Every result includes a stable track ID, box, label, confidence, relative depth when calibrated, TTC when enough temporal evidence exists, risk, and debounced events. `SAFE`, `CAUTION`, `WARNING`, and `CRITICAL` are conservative: no TTC is treated as a reliable collision prediction.

## Research and deployment choice

YOLO nano exported to ONNX is the preferred CPU/GPU/NPU transition path because it has a small model footprint and OpenCV DNN, ONNX Runtime, and Android NNAPI options. ByteTrack or SORT can replace the included IoU tracker after detector confidence calibration. MiDaS small is the advanced depth option; the current size-based depth is intentionally relative and requires focal-length calibration for meters. RAFT-small is an advanced optical-flow option; the included sparse Lucas-Kanade flow is faster on mobile.

## Training and evaluation

`dataset.py` creates a reproducible train/validation split. `train.py` documents the export contract for a backend-specific trainer. `evaluate.py` reports precision, recall, F1, and confusion counts at configurable IoU. Add sequence-level tracking, depth, event, and TTC labels before claiming those metrics in a safety evaluation.

Metric distance and collision warnings are estimates. Camera shake, occlusion, unknown object size, lighting, and lens calibration can invalidate them; deploy a redundant safety sensor for real vehicle control.