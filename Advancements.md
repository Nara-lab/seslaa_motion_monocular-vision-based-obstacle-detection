Redesign and improve the **entire mobile application** to a professional, modern, production-quality standard.

### Branding

* Use the existing **`appicon.png`** as the company/app logo throughout the application.
* Use **Orbitron font ONLY for the company name “SESLAA”**.
* All other application text must use a clean, modern standard UI font.
* Do not use Orbitron for buttons, settings, labels, descriptions, warnings, or general UI text.
* Create a consistent SESLAA visual identity across Home, Detection, Settings, About, dialogs, and status components.

### Complete UI Redesign

Modernize the complete application, including:

* Home
* Live Detection
* Settings
* About
* Navigation
* Cards
* Buttons
* Status indicators
* Empty/error states
* Warning screens
* Detection/event panels

Make the UI feel like a **professional automotive AI/computer-vision product**, not a basic demo application.

### Fix Live Preview

The current **live camera preview is only partially visible / approximately half the screen**.

Resolve this completely:

* Camera preview must use the available screen area correctly.
* Maintain the correct camera aspect ratio.
* Do not crop important areas unnecessarily.
* Bounding boxes must align exactly with the displayed camera image.
* Handle portrait and landscape orientations correctly.
* Verify the fix on the **physical Android phone**, not only the emulator.

### Fix Live Detection

The current live detections are **completely inaccurate**.

Do not simply adjust UI or thresholds. Investigate and fix the actual vision pipeline.

* Verify camera frame preprocessing.
* Verify image rotation/orientation.
* Verify resize/scaling.
* Verify normalization.
* Verify model input/output format.
* Verify bounding-box coordinate conversion.
* Verify class mapping.
* Verify confidence thresholds.
* Verify NMS.
* Verify tracking association.
* Verify that displayed bounding boxes correspond to the actual camera frame.

Use a reliable modern **open-source object-detection model** suitable for real-time Android deployment.

### Model Training & Improvement

Do not leave the existing model as-is if its accuracy is inadequate.

Create a proper model improvement pipeline:

* Dataset preparation
* Correct annotations
* Training/fine-tuning
* Validation
* Precision/recall and mAP evaluation
* False-positive analysis
* Confidence calibration
* Real-world camera testing
* Model optimization for mobile inference

Use appropriate open-source datasets where legally permitted and document their licenses.

Prefer a model that provides a good balance between:
**accuracy + latency + model size + Android compatibility.**

### Monocular Object Vision

The current **Monocular Object Vision is not working**.

Implement it as a **separate independent feature** with its own setting:

`Settings → Monocular Object Vision → ON/OFF`

When OFF:

* Monocular processing must be disabled.
* The normal object-detection pipeline must continue working.

When ON:

* Enable monocular vision processing.
* Estimate relative depth/scene geometry where supported.
* Detect approaching/receding objects.
* Estimate relative motion.
* Generate object-risk information.
* Clearly indicate when monocular estimates have low confidence.

Do not present estimated monocular depth as guaranteed accurate real-world distance.

### Kalman Filter

Add a dedicated option:

`Settings → Kalman Filter → ON/OFF`

Implement a proper **Kalman Filter** for object tracking and motion estimation.

Use it to improve:

* Bounding-box stability
* Object tracking
* Position prediction
* Velocity estimation
* Temporary detection loss handling
* Motion-event stability
* Reduction of bounding-box jitter

Allow the Kalman Filter to work together with object detection and tracking without introducing significant latency.

### Vision Architecture

Use a robust pipeline such as:

`Camera`
→ `Frame Preprocessing`
→ `Object Detection`
→ `NMS`
→ `Object Tracking`
→ `Kalman Filter`
→ `Monocular Vision (Optional)`
→ `Motion/Event Analysis`
→ `Risk Assessment`
→ `Warnings`
→ `UI Overlay`

Keep each component modular so it can be independently tested and improved.

### Detection UI

For every valid detection show:

* Rectangular bounding box
* Object class
* Confidence
* Tracking ID
* Motion state where applicable
* Risk level where applicable

Avoid displaying unstable or obviously incorrect detections.

### Settings

Create professional controls for:

* Object Detection ON/OFF
* Monocular Object Vision ON/OFF
* Kalman Filter ON/OFF
* Motion Detection ON/OFF
* Detection sensitivity
* Warning sensitivity
* Sound alerts
* Vibration
* Voice warnings
* Camera calibration
* Performance mode
* Debug information

### Critical Requirement

Do not treat this as only a UI redesign.

**Fix the actual computer-vision functionality, train/improve the model, correct the live camera pipeline, implement monocular vision, and integrate Kalman Filter tracking.**

First inspect the complete existing project and `instructions.md`. Identify the root causes before making changes. Preserve working functionality and avoid unnecessary rewrites.

Finally, build and test the application on the **actual Android phone**, verify the full live camera preview, verify that bounding boxes are correctly aligned, verify detection accuracy, verify Monocular Object Vision ON/OFF, and verify Kalman Filter ON/OFF.

Do not leave major features as mock implementations, placeholders, TODOs, or non-functional UI switches.
