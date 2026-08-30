# Advanced Monocular Vision: Optical Flow + Night Vision

First inspect the complete existing project and **`instructions.md`** and strictly follow its requirements. Do not rewrite unrelated working components.

The goal is to build a **real, production-quality monocular computer-vision pipeline** for object detection, tracking, motion understanding, object avoidance, and warning generation using a single RGB camera.

Do not implement cosmetic UI switches or mock functionality. Every enabled feature must connect to a real working processing pipeline.

---

## 1. Research & Architecture

Perform deep technical research before implementation.

Evaluate suitable open-source approaches for:

### Object Detection

* Modern lightweight YOLO-family models
* Efficient/Android-compatible detectors
* Other suitable open-source detection architectures

### Optical Flow

Evaluate:

* Lucas–Kanade
* Farneback
* TV-L1
* RAFT
* Lightweight RAFT variants
* Sparse optical flow
* Dense optical flow

### Low-Light / Night Enhancement

Evaluate:

* Gamma correction
* CLAHE
* Adaptive exposure
* Denoising
* Local contrast enhancement
* HDR where supported
* Illumination/color normalization
* Temporal noise reduction
* Headlight/glare suppression
* Motion-aware enhancement
* Lightweight AI-based low-light enhancement

Select the best practical combination based on:

**accuracy + robustness + latency + memory + CPU/GPU/NPU usage + Android compatibility + model size + power consumption + licensing.**

Do not use multiple heavy AI models unnecessarily.

---

# 2. Overall Vision Pipeline

Implement a modular architecture:

`Camera`
↓
`Frame Preprocessing`
↓
`Night / Low-Light Enhancement`
↓
`Object Detection`
↓
`NMS + Bounding Box Validation`
↓
`Optical Flow`
↓
`Object Tracking`
↓
`Kalman Filter`
↓
`Monocular Vision / Relative Depth`
↓
`Motion & Event Analysis`
↓
`Risk Assessment`
↓
`Object Avoidance / Warning Engine`
↓
`Flutter UI`

Every module must be independently testable and configurable.

---

# 3. Advanced Optical Flow

Implement a real optical-flow module to estimate:

* Pixel-level motion
* Motion magnitude
* Motion direction
* Global scene motion
* Object-level motion
* Approaching/receding motion
* Sudden movement
* Motion consistency across frames

Use optical flow to improve object tracking and motion-event classification.

---

# 4. Camera Motion Compensation

Implement robust global-motion estimation to distinguish:

* Camera movement
* Vehicle movement
* Background movement
* Independent object movement

Use appropriate feature detection, feature matching, homography/affine estimation, or other robust motion-estimation methods.

Reduce false motion caused by:

* Camera shake
* Vehicle vibration
* Rotation
* Sudden viewpoint changes
* Environmental movement

---

# 5. Object-Level Optical Flow

For each detected object:

* Extract optical-flow information inside/around its bounding box.
* Calculate motion magnitude.
* Calculate dominant motion direction.
* Compare object motion against global camera motion.
* Estimate temporal motion consistency.

Use these signals to improve:

* Tracking
* Direction estimation
* Velocity estimation
* Approach detection
* Collision-risk estimation
* Event detection
* Bounding-box stability

---

# 6. Optical Flow Filtering

Implement robust filtering for:

* Sensor noise
* Compression artifacts
* Lighting changes
* Shadows
* Reflections
* Background motion
* Camera shake
* Flow outliers

Use temporal smoothing and robust outlier rejection while keeping latency low.

---

# 7. Kalman Filter

Implement a proper **Kalman Filter** for object tracking and motion prediction.

Use it for:

* Bounding-box stabilization
* Position prediction
* Velocity estimation
* Temporary detection-loss recovery
* Motion smoothing
* Tracking continuity
* Reduced bounding-box jitter

The Kalman Filter must be a real mathematical implementation, not a UI option without functionality.

Add:

**Settings → Kalman Filter → ON/OFF**

When disabled, tracking should continue using the alternative tracking method.

---

# 8. Monocular Object Vision

Implement monocular vision as an independent module.

Add:

**Settings → Monocular Object Vision → ON/OFF**

When OFF:

* Disable monocular depth/geometry processing.
* Normal object detection/tracking must continue.

When ON:

* Estimate relative depth/scene geometry.
* Estimate relative object approach/recession.
* Support collision-risk estimation.
* Provide confidence/uncertainty.

Do not represent monocular depth as guaranteed accurate metric distance.

---

# 9. Advanced Night Vision / Low-Light Filtration

Implement a real-time **low-light enhancement pipeline**.

This is not simply a brightness/contrast adjustment.

Evaluate and implement appropriate techniques such as:

* Gamma correction
* CLAHE
* Adaptive exposure
* Denoising
* Local contrast enhancement
* HDR where supported
* Illumination normalization
* Color normalization
* Temporal noise reduction
* Headlight/glare suppression
* Motion-aware filtering
* Lightweight AI low-light enhancement

The selected approach must preserve object boundaries and avoid introducing artificial objects.

---

# 10. Night Vision Architecture

Use:

`Original Camera Frame`
↓
`Brightness / Scene Analysis`
↓
`Night Mode Decision`
↓
`Low-Light Enhancement`
↓
`Object Detection`

Keep the original frame available for comparison and debugging.

Where useful, compare:

**Original Detection vs Enhanced Detection**

and automatically prefer the more reliable processing path.

---

# 11. Night Vision Modes

Add:

**Settings → Night Vision**

Options:

* Night Vision: ON/OFF
* Auto Mode
* Low-Light Enhancement
* Strong Enhancement
* HDR Enhancement
* Noise Reduction
* Headlight/Glare Reduction
* Temporal Filtering
* AI Enhancement
* Night Sensitivity

Auto Mode should determine the appropriate processing level based on scene brightness.

Live preview should indicate:

**DAY**

**LOW LIGHT**

**NIGHT VISION**

Do not claim true infrared/thermal night vision when using a normal RGB camera. This feature should be described as **low-light/night image enhancement**.

---

# 12. Night-Time Object Detection

Optimize and validate detection for:

* Pedestrians
* Cars
* Trucks
* Buses
* Motorcycles
* Bicycles
* Animals
* Road obstacles
* Static obstacles
* Unknown obstacles

Specifically test:

* Dark objects
* Backlit objects
* Headlights
* Taillights
* Streetlights
* Reflections
* Shadows
* Wet roads
* Rain
* Night glare

---

# 13. Object Avoidance & Risk Assessment

Combine:

**Object Detection + Optical Flow + Tracking + Kalman Filter + Monocular Vision**

to classify objects as:

* Stationary
* Moving
* Approaching
* Receding
* Crossing
* Potential collision risk

Estimate where technically reliable:

* Relative depth
* Relative motion
* Motion direction
* Relative velocity
* Time-to-collision (TTC)
* Object position relative to the vehicle/camera path

Generate:

**SAFE → CAUTION → WARNING → CRITICAL**

Use confidence scoring and temporal consistency.

Do not generate warnings from a single noisy frame.

---

# 14. Bounding Boxes & Tracking

Every valid detected object must display:

* Stable rectangular bounding box
* Object class
* Confidence
* Tracking ID
* Motion state
* Risk state where applicable

Correct any existing issues involving:

* Incorrect bounding-box coordinates
* Image scaling
* Rotation
* Cropping
* Aspect-ratio mismatch
* Model output conversion
* Class mapping
* NMS

Bounding boxes must align precisely with the displayed live camera image.

---

# 15. Settings

Create a professional settings structure:

### Vision

* Object Detection ON/OFF
* Monocular Object Vision ON/OFF
* Optical Flow ON/OFF
* Kalman Filter ON/OFF
* Motion Detection ON/OFF

### Optical Flow

* Flow Method
* Motion Sensitivity
* Flow Threshold
* Temporal Smoothing
* Camera Motion Compensation
* Object Motion Filtering
* Debug Visualization

### Night Vision

* Night Vision ON/OFF
* Auto Mode
* Enhancement Level
* Noise Reduction
* Glare Reduction
* Temporal Filtering
* AI Enhancement
* Night Sensitivity

### Alerts

* Sound
* Vibration
* Voice Warning
* Warning Sensitivity

### Performance

* FPS
* Inference frequency
* Processing resolution
* Lightweight/Advanced mode
* Debug mode

Hide advanced parameters under an **Advanced Settings** section.

---

# 16. Debug Visualization

Provide optional developer/debug mode showing:

* Optical-flow vectors
* Flow field
* Global camera-motion vector
* Object-motion vector
* Tracking trajectory
* Kalman predicted position
* Bounding boxes
* Monocular depth information
* Risk score
* FPS
* Inference latency
* Processing mode

Do not show this information during normal operation unless Debug Mode is enabled.

---

# 17. Performance

Provide:

### Lightweight Mode

Prioritize:

* Real-time FPS
* Low memory
* Low power
* Android compatibility

### Advanced Mode

Prioritize:

* Higher detection accuracy
* Better optical flow
* Better motion analysis
* Better low-light processing

Automatically adapt processing resolution/frequency when necessary to maintain real-time performance.

Design the system so the Python research implementation can later be converted into an optimized Android pipeline using appropriate runtimes such as:

* TensorFlow Lite
* ONNX Runtime
* MediaPipe
* NCNN
* OpenCV DNN

---

# 18. Training & Model Improvement

If current detection accuracy is poor, do not simply change confidence thresholds.

Investigate the complete model pipeline and implement:

* Dataset preparation
* Correct annotations
* Data augmentation
* Fine-tuning/training
* Validation
* Precision/Recall
* mAP
* False-positive analysis
* False-negative analysis
* Confidence calibration
* Real-world testing

Include night/low-light training data where appropriate.

Document model and dataset licenses.

---

# 19. Real-World Validation

Test on the **physical Android device** using real camera/video data.

### Day

* Stationary camera
* Moving camera
* Vehicle movement
* Pedestrians
* Cars
* Motorcycles
* Bicycles
* Multiple objects

### Motion

* Camera vibration
* Sudden camera movement
* Approaching objects
* Receding objects
* Crossing objects

### Night

* Completely dark environments
* Street lighting
* Headlights
* Taillights
* Backlit pedestrians
* Night vehicles
* Wet roads
* Rain
* Glare
* Reflections

Measure:

* Detection accuracy
* False positives
* False negatives
* Bounding-box stability
* Tracking stability
* Optical-flow accuracy
* Monocular-vision confidence
* Warning accuracy
* FPS
* Latency
* CPU/GPU/NPU utilization
* Memory usage
* Battery impact

---

# 20. Critical Implementation Rules

1. **First inspect the entire existing project and `instructions.md`.**
2. Identify the root causes of current detection and preview problems before modifying code.
3. Do not rewrite unrelated working functionality.
4. Do not create mock implementations.
5. Do not add UI switches that are not connected to real functionality.
6. Do not rely solely on confidence-threshold changes to solve poor detection.
7. Validate camera orientation, preprocessing, model input/output, coordinate transformation, class mapping, NMS, and tracking.
8. Verify bounding boxes against the actual displayed camera frame.
9. Test every ON/OFF setting independently.
10. Optimize for the **physical Android phone**, not only the emulator.
11. Keep Python research/training modules separate from production Android runtime components.
12. Document every selected algorithm/model and why it was selected.
13. Clearly document limitations and uncertainty, especially for monocular depth and collision prediction.

### Final Goal

Deliver a **professional, real-time monocular AI vision system** that combines:

**Object Detection + Optical Flow + Camera Motion Compensation + Kalman Filter + Monocular Vision + Night/Low-Light Enhancement + Tracking + Risk Assessment**

to provide reliable:

**Detection → Tracking → Motion Understanding → Object Avoidance → Early Warning**

with a clean professional mobile UI and a technically valid path from **Python research/training to optimized on-device Android deployment**.
