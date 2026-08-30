## Build Advanced Monocular Event-Based Vision System

Deeply research and implement an **advanced Python-based monocular computer-vision pipeline** for real-time **object detection, tracking, motion/event detection, object avoidance, and warning generation**.

First inspect the existing project and `instructions.md`. Preserve the current architecture and functionality. Do not create a mock or placeholder implementation.

### Core Requirements

* Use the **single RGB camera** as the primary sensor.
* Research and select the best suitable **open-source models** for:

  * Object detection
  * Object tracking
  * Monocular depth estimation
  * Optical flow / motion estimation
  * Collision/approach prediction
  * Event detection
* Prefer modern lightweight models that can eventually be optimized for **Android/on-device inference**.
* Use Python for model development, training/fine-tuning, evaluation, and prototyping.

### Vision Pipeline

Build:

`Camera → Preprocessing → Object Detection → Tracking → Monocular Depth → Motion/Optical Flow → Relative Distance & Approach Estimation → Event Detection → Risk Assessment → Warning`

Detect and track objects such as:

* Person
* Car
* Truck
* Bus
* Motorcycle
* Bicycle
* Animal
* Static obstacles
* Unknown obstacles

Display every detected object with a **stable rectangular bounding box**, object label, confidence, tracking ID, and relevant event/risk status.

### Event-Based Intelligence

Detect events including:

* Object entering/exiting
* Object moving/stationary
* Object approaching
* Object moving away
* Sudden movement
* Obstacle appearing in path
* Potential collision
* High-risk approaching object
* Unsafe stopping distance
* Camera motion/shake

Avoid duplicate events and reduce false positives caused by lighting changes, shadows, camera vibration, reflections, and environmental noise.

### Object Avoidance & Warning

Develop a risk-assessment system that estimates:

* Relative depth/distance
* Relative velocity
* Direction of movement
* Time-to-collision (TTC), where reliably estimable
* Object position relative to the camera/vehicle path
* Collision risk level

Generate clear warnings such as:

`SAFE → CAUTION → WARNING → CRITICAL`

Warnings must be based on measurable vision signals rather than arbitrary thresholds.

### Training & Improvement

Create a complete Python training/evaluation framework:

* Dataset preparation
* Annotation support
* Data augmentation
* Model training/fine-tuning
* Validation
* Accuracy metrics
* Precision/recall
* mAP
* Tracking metrics
* Depth/error evaluation
* False-positive analysis
* Event detection accuracy
* Collision-warning evaluation

Use publicly available/open-source datasets where appropriate and clearly document licenses.

### Research Requirement

Perform deep technical research before selecting the architecture. Compare suitable current open-source approaches for detection, tracking, monocular depth, optical flow, and collision prediction.

Select the best combination based on:

**accuracy + latency + model size + Android compatibility + CPU/GPU/NPU feasibility + licensing.**

Do not blindly select the largest model. Provide a lightweight production model and an advanced research model where appropriate.

### Android/Flutter Integration

Design the Python implementation so the trained/optimized models can later be converted/deployed to the existing Android application through suitable runtimes such as:

* TensorFlow Lite
* ONNX Runtime
* MediaPipe
* NCNN
* OpenCV DNN
* Other suitable Android-compatible runtimes

The final system should be capable of transitioning from:

**Python research/training → optimized model → Android on-device inference → Flutter UI.**

### Important Safety/Accuracy Requirement

Do **not** claim that monocular vision provides guaranteed or perfectly accurate metric distance/collision prediction. Clearly identify uncertainty and confidence. The system should provide conservative warnings when confidence is insufficient.

### Deliverables

Build the actual working Python implementation, not only documentation.

Include:

1. Complete source code
2. Model-selection rationale
3. Training scripts
4. Dataset/preprocessing pipeline
5. Inference pipeline
6. Object tracking
7. Monocular depth estimation
8. Motion/event detection
9. Collision-risk estimation
10. Warning engine
11. Bounding-box visualization
12. Configuration system
13. Evaluation/testing scripts
14. Requirements/environment setup
15. Android deployment/conversion path
16. Test results and known limitations

Run the system on real camera/video data and demonstrate that objects are detected, tracked, boxed, and converted into meaningful **monocular visual events and avoidance warnings**.

If a required dependency, model, or framework is incompatible with the current environment, resolve the compatibility issue and continue rather than leaving the feature incomplete.
