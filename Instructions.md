# SESLAA Motion Stack — Flutter Development Instructions

## 1. PROJECT IDENTITY

**Application Name:** SESLAA Motion Stack

**Short Name:** SESLAA Motion

**Company / Copyright Owner:** Narga Engineering Private Limited

**Brand:** SESLAA

**Website:** https://seslaa.com

**Technology:** Flutter + Android + Monocular Computer Vision + AI Object Detection + Object Tracking + Motion Analysis

The application must be developed as a **Flutter-based Android application** using the existing SESLAA monocular-vision implementation as the technical reference.

---

# 2. SOURCE PROJECT

Use this repository as the primary computer-vision reference:

https://github.com/Nara-lab/seslaa_motion_monocular-vision-based-obstacle-detection

First inspect the complete repository.

Understand:

* Main.py
* Constants.py
* requirements.txt
* mrcnn/
* matcher/
* data_model/
* camera_calibration/
* weights/
* export/
* utils/
* Mask R-CNN
* object detection
* segmentation
* SIFT
* SURF
* ORB
* feature matching
* Kalman filtering
* object tracking
* motion estimation
* obstacle detection
* camera calibration
* model weights
* configuration
* dependencies

The Python implementation is the **reference algorithm**.

Do not blindly rewrite it.

---

# 3. PRIMARY OBJECTIVE

Create:

# SESLAA Motion Stack

as a **Flutter Android application** capable of using a generic Android smartphone camera for monocular computer vision.

Architecture:

```text
Flutter UI
      ↓
Flutter Camera Layer
      ↓
Platform / Native Vision Bridge
      ↓
AI Inference Engine
      ↓
Object Detection
      ↓
Segmentation
      ↓
Feature Matching
      ↓
Object Tracking
      ↓
Kalman Filter
      ↓
Motion Estimation
      ↓
Obstacle Analysis
      ↓
Flutter Visualization
```

---

# 4. FLUTTER REQUIREMENT

The application UI and application architecture must be Flutter-based.

Use:

* Flutter
* Dart
* Android
* Android NDK where required
* Platform Channels / FFI where appropriate
* Camera plugin or native CameraX bridge
* TensorFlow Lite / ONNX Runtime / other suitable mobile inference runtime
* OpenCV where required

Preferred Flutter structure:

```text id="b4s1ed"
lib/
├── main.dart
├── app/
├── core/
├── camera/
├── detection/
├── segmentation/
├── tracking/
├── matching/
├── kalman/
├── motion/
├── obstacle/
├── inference/
├── privacy/
├── settings/
├── licenses/
└── ui/
```

---

# 5. IMPORTANT ARCHITECTURE RULE

Do NOT attempt to execute the complete Python runtime inside Flutter.

Do not require:

* Python interpreter
* desktop Python
* pip
* Flask server
* local Python HTTP server
* external computer

for normal Android operation.

The final APK must work independently on a generic Android smartphone.

---

# 6. PYTHON → FLUTTER MIGRATION

Map the existing Python implementation as follows:

```text id="zzk1hv"
Python
   ↓
Algorithm Analysis
   ↓
Mobile-Compatible Implementation
```

Use:

### Dart

For:

* UI
* application state
* configuration
* settings
* user interaction
* visualization
* application logic

### Native Android / Kotlin

For:

* camera integration where required
* Android lifecycle
* hardware acceleration
* Android-specific functionality

### C++ / OpenCV

Where beneficial for:

* feature extraction
* ORB
* image processing
* high-performance tracking
* computer-vision calculations

### TensorFlow Lite / ONNX Runtime

For:

* neural-network inference

Use Flutter platform channels or FFI to communicate between Flutter and native/native-compiled vision components.

---

# 7. OBJECT DETECTION

The original project uses Mask R-CNN.

Investigate whether the existing Mask R-CNN model can be converted to:

```text id="oyv2ny"
Mask R-CNN
    ↓
TensorFlow/SavedModel
    ↓
TensorFlow Lite
    ↓
Flutter Android
```

or:

```text id="1jnhai"
Mask R-CNN
    ↓
ONNX
    ↓
ONNX Runtime Mobile
    ↓
Flutter Android
```

Use the technically best option.

Do not fabricate model files.

Do not fabricate weights.

If the original Mask R-CNN cannot reasonably run in real time on generic Android devices:

1. Document why.
2. Benchmark it.
3. Investigate a mobile-compatible equivalent.
4. Preserve the same detection/segmentation functionality as closely as possible.
5. Document any accuracy differences.

---

# 8. FEATURE MATCHING

Preserve the existing feature-matching concept.

Support:

* ORB
* SIFT where appropriate
* SURF where technically and legally appropriate

Default:

**ORB**

because it is generally more appropriate for mobile real-time processing.

Implement the matcher as a replaceable service.

Example:

```text id="d6f2qk"
FeatureMatcher
      ├── ORBMatcher
      ├── SIFTMatcher
      └── SURFMatcher
```

---

# 9. OBJECT TRACKING

Implement persistent object tracking.

Each tracked object should contain:

```text id="1hpl3e"
trackingId
objectClass
boundingBox
confidence
position
velocity
motionState
lastSeen
trackingConfidence
```

Tracking IDs must be generated from actual tracking results.

Never hard-code IDs.

---

# 10. KALMAN FILTER

Port the existing Kalman-filter logic.

The Kalman filter should support:

* position prediction
* velocity estimation
* state prediction
* uncertainty
* timestamp handling
* lost-object prediction

Keep the implementation independent of the Flutter UI.

---

# 11. MOTION DETECTION

Implement real motion analysis.

Possible states:

```text id="l7b5ud"
STATIC
MOVING
APPROACHING
RECEDING
UNKNOWN
```

Motion must be calculated from actual image/object tracking information.

Account for camera movement where possible.

---

# 12. OBSTACLE DETECTION

Create a dedicated obstacle-analysis layer.

Inputs may include:

* object class
* bounding box
* object position
* apparent size
* tracking velocity
* motion state
* relative depth
* trajectory
* confidence

Output:

```text id="0f2ehz"
SAFE
CAUTION
WARNING
DANGER
```

Do not claim exact distance in meters unless the camera calibration and algorithm actually support accurate metric distance.

Use:

**Relative Distance**

when appropriate.

---

# 13. FLUTTER CAMERA

Use a Flutter-compatible camera implementation.

Preferred approach:

```text id="2wpxra"
Flutter Camera
      ↓
Android CameraX/native camera
      ↓
Image stream
      ↓
Vision Engine
```

Support:

* rear camera
* front camera
* camera switching
* autofocus
* orientation
* rotation
* resolution
* FPS
* lifecycle management

Do not process full-resolution frames unnecessarily.

---

# 14. FRAME PROCESSING

Create an efficient frame-processing pipeline.

```text id="2c0eq6"
Camera Frame
    ↓
Resize
    ↓
Normalize
    ↓
AI Inference
    ↓
Detection
    ↓
Tracking
    ↓
Motion
    ↓
Obstacle Analysis
    ↓
Flutter UI
```

Avoid:

* unnecessary image copies
* repeated bitmap conversion
* blocking Dart UI thread
* excessive platform-channel traffic
* processing every frame when unnecessary

Only send the minimum required information back to Flutter.

For example:

```text id="cf5y9b"
{
  objectId,
  class,
  confidence,
  boundingBox,
  motionState,
  obstacleState
}
```

rather than sending processed full-size images repeatedly.

---

# 15. PERFORMANCE

Target:

**15–30 FPS where hardware allows.**

Implement:

* asynchronous inference
* frame skipping
* resolution scaling
* background processing
* isolate where appropriate
* native processing for expensive CV operations
* GPU acceleration where available
* NNAPI where supported
* quantized model where appropriate
* memory reuse

Do not block Flutter rendering.

---

# 16. DEVICE PERFORMANCE MODES

Provide:

### PERFORMANCE

Prioritize FPS.

### BALANCED

Default.

### QUALITY

Prioritize detection quality.

The application should detect device capability and adjust processing appropriately.

Do not make unsupported performance claims.

---

# 17. FLUTTER UI

Use a professional dark AI/robotics interface.

Main screen:

```text id="cr5k4k"
SESLAA MOTION STACK

Camera: REAR
FPS: 24
Objects: 5
AI: ON-DEVICE

┌─────────────────────────────┐
│                             │
│      CAMERA PREVIEW         │
│                             │
│  ┌─────────────────────┐    │
│  │ PERSON 94%          │    │
│  │ ID: 03              │    │
│  │ MOVING              │    │
│  └─────────────────────┘    │
│                             │
│       CAR 88%               │
│       ID: 07                │
│       APPROACHING           │
│                             │
└─────────────────────────────┘

Motion: ACTIVE
Obstacle: CAUTION

[ START ] [ CAMERA ] [ SETTINGS ]
```

---

# 18. FLUTTER STATE MANAGEMENT

Use a clean state-management architecture.

Choose one appropriate approach such as:

* Riverpod
* Provider
* Bloc/Cubit

Prefer a lightweight and maintainable solution.

Do not add multiple state-management frameworks.

---

# 19. SETTINGS

Provide:

* confidence threshold
* motion sensitivity
* camera
* performance mode
* inference resolution
* tracking ON/OFF
* segmentation ON/OFF
* FPS display
* snapshot
* video recording
* privacy
* local processing
* open-source licenses
* about

Default confidence:

**50%**

---

# 20. PRIVACY

All core camera processing must be local.

Default:

```text id="mwm0b5"
ON-DEVICE AI: ON
CLOUD PROCESSING: OFF
FRAME UPLOAD: OFF
```

No cloud server is required for normal operation.

Do not upload camera frames.

Do not collect unnecessary personal information.

Only request necessary Android permissions.

---

# 21. NETWORK

Core application functionality must work offline.

Do not require:

* login
* cloud API
* internet
* external server

for object detection and motion analysis.

If networking is implemented in the future, isolate it as an optional module.

---

# 22. APP ICON

Use the supplied:

`appicon.png`

as the official SESLAA Motion Stack application icon.

Generate the required Android launcher/adaptive icon resources from this file.

Do not create a different icon.

Do not replace the supplied logo.

---

# 23. BRANDING

Use:

**SESLAA Motion Stack**

throughout the application.

Company:

**Narga Engineering Private Limited**

Update:

* app name
* splash screen
* launcher label
* About page
* settings
* documentation
* package metadata
* application metadata

Do not change third-party attribution.

---

# 24. PACKAGE NAME

Use:

```text id="8q6jso"
com.seslaa.motionstack
```

Use this consistently across:

* Flutter
* Android
* Gradle
* AndroidManifest
* Kotlin
* tests

---

# 25. COPYRIGHT

Application code created specifically for Narga Engineering should contain:

```text id="o3zj5k"
Copyright © 2026 Narga Engineering Private Limited.
All rights reserved.
```

Use:

```text id="y44dqe"
SESLAA™
```

or the legally applicable SESLAA trademark designation.

Do not claim ownership of third-party libraries, models or frameworks.

---

# 26. THIRD-PARTY LICENSES

Create:

```text id="v9cr7m"
LICENSE
NOTICE
THIRD_PARTY_LICENSES.md
```

Identify licenses for:

* Flutter
* Dart
* Android libraries
* Camera libraries
* TensorFlow Lite
* ONNX Runtime
* OpenCV
* Mask R-CNN
* Python-derived code
* third-party models
* third-party datasets
* other dependencies

Preserve mandatory copyright and license notices.

Do not replace third-party ownership with Narga Engineering ownership.

---

# 27. IN-APP LICENSE SCREEN

Create:

**Settings → Open Source Licenses**

Display:

* component name
* version
* copyright
* license
* license text where required

Include Narga Engineering's application copyright separately from third-party licenses.

---

# 28. MODEL LICENSE VERIFICATION

Before packaging any AI model:

Determine:

* model source
* model owner
* model license
* commercial-use permission
* redistribution permission
* attribution requirements

If the model cannot legally be redistributed inside a commercial APK:

Do not package it.

Instead document the issue and provide a compliant integration mechanism.

---

# 29. SOURCE CODE OWNERSHIP

New SESLAA-specific Flutter/Dart/Kotlin/C++ code developed for this project should be identified as Narga Engineering code where appropriate.

Do not modify third-party source headers to falsely claim ownership.

Maintain clear separation between:

```text id="q9l4u2"
Narga Engineering Code
        +
Third-Party Components
        +
Third-Party Models
```

---

# 30. OFFLINE DEMO MODE

Implement a developer/test mode.

Allow a local video to be processed through the same vision pipeline.

Purpose:

Compare:

```text id="z9em5b"
Python Reference
        VS
Flutter Android
```

Compare:

* objects
* segmentation
* tracking
* IDs
* motion
* obstacle state
* FPS

---

# 31. PYTHON REFERENCE VALIDATION

Create:

`VALIDATION_REPORT.md`

Record:

### Python

* model
* input
* detection
* tracking
* FPS

### Flutter Android

* model
* input
* detection
* tracking
* FPS

### Difference

* accuracy
* latency
* model differences
* tracking differences
* known limitations

Do not claim equivalence without testing.

---

# 32. TESTING

Implement Flutter/Dart tests for:

* detection result parsing
* confidence threshold
* object state
* tracking state
* motion state
* obstacle classification
* settings
* application state

Implement Android/native tests where required for:

* camera
* inference
* OpenCV
* native bridge
* lifecycle

---

# 33. SECURITY

Do not store sensitive camera data unnecessarily.

Do not hard-code:

* passwords
* API keys
* tokens
* private certificates

If snapshots/videos are supported:

* save only when requested
* allow deletion
* use appropriate Android storage mechanisms

---

# 34. ERROR HANDLING

Handle:

* camera permission denied
* camera unavailable
* model missing
* model load failure
* unsupported device
* insufficient memory
* inference failure
* invalid frame
* native bridge failure

The application must not crash.

Display meaningful errors.

Example:

```text id="g6n1df"
AI MODEL ERROR

The detection model could not be loaded.
Please verify the model package.
```

Never show fake detections.

---

# 35. FLUTTER PROJECT STRUCTURE

Expected structure:

```text id="j94rj6"
seslaa_motion_stack/
│
├── android/
├── assets/
│   ├── models/
│   ├── images/
│   └── licenses/
│
├── lib/
│   ├── app/
│   ├── camera/
│   ├── detection/
│   ├── segmentation/
│   ├── tracking/
│   ├── matching/
│   ├── kalman/
│   ├── motion/
│   ├── obstacle/
│   ├── inference/
│   ├── privacy/
│   ├── settings/
│   ├── licenses/
│   └── ui/
│
├── test/
│
├── LICENSE
├── NOTICE
├── THIRD_PARTY_LICENSES.md
├── README.md
├── ARCHITECTURE.md
├── ANDROID_MIGRATION_PLAN.md
└── VALIDATION_REPORT.md
```

Adapt this structure if the actual implementation requires a better organization.

---

# 36. FLUTTER DEPENDENCIES

Keep dependencies minimal.

Potential dependencies may include:

* camera
* flutter_riverpod / provider / bloc
* path_provider
* permission_handler
* tflite_flutter or appropriate inference package
* ffi where required

Do not add packages merely for convenience.

Verify each dependency's:

* version
* Android compatibility
* license
* maintenance status

---

# 37. BUILD ENVIRONMENT

Before building:

Run:

```bash
flutter doctor -v
```

Verify:

* Flutter
* Dart
* Android SDK
* Android SDK Platform
* Android build tools
* Java
* Gradle
* Android Studio

Then:

```bash
flutter pub get
```

Run:

```bash
flutter analyze
```

Fix all relevant errors.

Run tests:

```bash
flutter test
```

Then build:

```bash
flutter build apk --debug
```

Then:

```bash
flutter build apk --release
```

---

# 38. APK OUTPUT

Generate:

```text id="v3fj6s"
build/app/outputs/flutter-apk/app-debug.apk
```

and:

```text id="wxj4w8"
build/app/outputs/flutter-apk/app-release.apk
```

Rename/copy the final artifacts where appropriate to:

```text id="7c2ypd"
SESLAA-Motion-Stack-debug.apk
SESLAA-Motion-Stack-release.apk
```

Do not claim the release APK is production-signed unless an actual Narga Engineering release keystore is configured.

---

# 39. RELEASE SIGNING

If no release keystore is supplied:

Do NOT:

* invent a keystore
* invent passwords
* claim production signing

Instead:

1. Build the release APK.
2. Clearly report signing status.
3. Provide instructions for configuring Narga Engineering's actual release keystore.

---

# 40. README

Create:

`README.md`

Include:

* SESLAA Motion Stack overview
* Flutter architecture
* Python → Flutter migration
* AI model
* inference engine
* camera pipeline
* object detection
* segmentation
* tracking
* Kalman filter
* motion detection
* obstacle analysis
* privacy
* licenses
* build instructions
* APK installation
* Android requirements
* performance
* limitations
* troubleshooting

---

# 41. ARCHITECTURE DOCUMENT

Create:

`ARCHITECTURE.md`

Explain:

```text id="e4g5n9"
Flutter UI
     ↓
Application Layer
     ↓
Vision Bridge
     ↓
Native / C++ / AI Runtime
     ↓
Camera
     ↓
Inference
     ↓
Tracking
     ↓
Motion
     ↓
Obstacle Analysis
```

Explain why each component is Flutter, Dart, Kotlin, C++, or native AI runtime.

---

# 42. MIGRATION DOCUMENT

Create:

`ANDROID_MIGRATION_PLAN.md`

Document:

* Python component
* original function
* Flutter/native equivalent
* migration status
* technical limitations
* performance considerations

Example:

```text id="r2i7d9"
Python Mask R-CNN
        ↓
TensorFlow Lite
        ↓
Native Android inference
        ↓
Flutter result bridge
```

---

# 43. DO NOT FABRICATE

Never fabricate:

* detection
* confidence
* FPS
* depth
* distance
* tracking
* accuracy
* model weights
* licenses
* copyright
* ownership
* benchmark results

If something cannot be verified:

**Report it clearly.**

---

# 44. FINAL VALIDATION

Before declaring completion:

```text id="9nwhn7"
[ ] Python repository inspected
[ ] Python architecture documented
[ ] Flutter project created
[ ] Dart architecture implemented
[ ] Android implementation integrated
[ ] Camera working
[ ] Generic Android camera supported
[ ] AI model integrated
[ ] Object detection working
[ ] Segmentation working/equivalent
[ ] Feature matching working
[ ] Object tracking working
[ ] Kalman filter working
[ ] Motion detection working
[ ] Obstacle analysis working
[ ] Confidence scores working
[ ] Tracking IDs working
[ ] Offline mode working
[ ] Privacy implemented
[ ] SESLAA branding complete
[ ] Narga Engineering ownership notices added
[ ] appicon.png integrated
[ ] Third-party licenses documented
[ ] Model licenses verified
[ ] In-app license screen implemented
[ ] flutter analyze passes
[ ] flutter test passes
[ ] debug APK generated
[ ] release APK generated
[ ] signing status documented
[ ] README completed
[ ] architecture documented
[ ] validation report completed
```

---

# 45. FINAL OUTPUT

At completion, report:

## Application

**SESLAA Motion Stack**

## Company

**Narga Engineering Private Limited**

## Framework

**Flutter**

## Package

`com.seslaa.motionstack`

## AI

Report:

* original Python model
* Android model
* inference engine
* conversion method
* model license

## Computer Vision

Report:

* object detection
* segmentation
* ORB/SIFT/SURF
* feature matching
* tracking
* Kalman filter
* motion analysis
* obstacle analysis

## Build

Report:

* Flutter version
* Dart version
* Android SDK
* compile SDK
* target SDK
* minimum SDK

## APK

Report the actual generated paths:

```text id="i0q6aa"
Debug:
<actual path>

Release:
<actual path>
```

## Testing

Report:

* `flutter analyze`
* `flutter test`
* APK build result
* device testing
* FPS
* known issues

## Licensing

Report:

* Narga Engineering-owned code
* third-party libraries
* third-party models
* licenses
* attribution requirements

---

# 46. CRITICAL RULE

The final product must be a **real Flutter Android implementation**, not a UI mockup.

The Flutter layer is responsible for the application/UI.

The native/mobile vision layer is responsible for computationally intensive computer vision and AI inference.

The existing Python repository remains the algorithmic reference.

Follow:

**ANALYZE → PORT → OPTIMIZE → BUILD → TEST → VALIDATE → GENERATE APK**

The final application is:

# SESLAA Motion Stack

**© 2026 Narga Engineering Private Limited. All rights reserved.**
