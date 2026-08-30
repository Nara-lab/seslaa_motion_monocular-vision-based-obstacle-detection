 ## COMPLETE SESLAA MOTION STACK

## FOLLOW `instructions.md` FIRST — DO NOT SKIP ANY REQUIREMENT

You are working on the **SESLAA Motion Stack** project.

The project contains an `instructions.md` file. **Read `instructions.md` completely before making any changes. Follow every applicable instruction in that file.**

Do not simplify, ignore, replace, or bypass requirements merely to make the project compile.

The objective is to deliver a **complete, buildable, installable Flutter Android application with a real on-device computer-vision pipeline**.

---

# 1. SOURCE IMPLEMENTATION

Use the existing SESLAA monocular-vision implementation as the technical reference:

https://github.com/Nara-lab/seslaa_motion_monocular-vision-based-obstacle-detection

Inspect the repository before implementing the Android/Flutter version.

Understand and preserve the existing concepts:

* Mask R-CNN
* object detection
* object segmentation
* ORB/SIFT/SURF feature matching where appropriate
* object tracking
* Kalman filtering
* motion estimation
* obstacle detection
* camera calibration
* monocular vision

Do not create a generic camera demo unrelated to the existing project.

---

# 2. FINAL PRODUCT

The final product must be:

**SESLAA Motion Stack**

A Flutter-based Android application that works on a **generic Android smartphone** using its built-in camera.

The application must perform actual:

```text
PHONE CAMERA
     ↓
IMAGE FRAME
     ↓
PRE-PROCESSING
     ↓
ON-DEVICE AI INFERENCE
     ↓
OBJECT DETECTION
     ↓
SEGMENTATION
     ↓
OBJECT TRACKING
     ↓
FEATURE MATCHING
     ↓
KALMAN FILTER
     ↓
MOTION ESTIMATION
     ↓
OBSTACLE ANALYSIS
     ↓
FLUTTER UI
```

This must be a real implementation.

**Do not deliver a UI-only prototype.**

**Do not use fake detection results.**

**Do not hard-code confidence values.**

**Do not stop after creating the Flutter screens.**

---

# 3. CRITICAL ISSUE TO RESOLVE

The previous implementation did not include a complete on-device TensorFlow/vision pipeline because the native Android plugin/dependency set was incompatible with the installed Gradle/Android SDK environment.

### THIS MUST NOW BE RESOLVED.

Do not simply report:

> "The native Android plugin is incompatible."

Instead:

1. Inspect the current Flutter version.
2. Inspect Dart version.
3. Inspect Android Gradle Plugin version.
4. Inspect Gradle version.
5. Inspect compile SDK.
6. Inspect target SDK.
7. Inspect minimum SDK.
8. Inspect installed Android SDK platforms.
9. Inspect installed Android Build Tools.
10. Inspect Java/JDK version.
11. Inspect Android NDK version if required.
12. Inspect all Flutter plugins.
13. Identify the exact incompatibility.
14. Upgrade/downgrade compatible components as necessary.
15. Install missing SDK/NDK/build dependencies if the environment allows it.
16. Replace incompatible packages with maintained compatible alternatives where necessary.
17. Rebuild.
18. Test.
19. Fix remaining errors.
20. Continue until the complete application can build.

Do not leave the vision pipeline as a placeholder because of dependency inconvenience.

---

# 4. ENVIRONMENT SETUP

First run and inspect:

```bash
flutter doctor -v
```

Also inspect:

```bash
flutter --version
dart --version
java -version
```

Inspect Android configuration:

```bash
flutter doctor --android-licenses
```

where appropriate.

Inspect:

```bash
sdkmanager --list
```

if available.

Inspect:

```bash
gradle --version
```

where appropriate.

Determine a compatible matrix:

```text
Flutter
Dart
Java
Gradle
Android Gradle Plugin
compileSdk
targetSdk
minSdk
NDK
```

Use a **known-compatible stable combination**.

Do not arbitrarily upgrade everything.

---

# 5. INSTALL MISSING DEPENDENCIES

If the environment is missing required Android SDK/build components and installation is possible:

**INSTALL THEM.**

Potential requirements include:

* Android SDK Platform
* Android SDK Build Tools
* Android SDK Command-line Tools
* Android Platform Tools
* Android NDK
* CMake
* required Java/JDK version

Use the environment's available package/SDK manager.

Do not merely document that something is missing if it can actually be installed.

After installation:

```bash
flutter doctor -v
```

must be re-run.

---

# 6. RESOLVE GRADLE/ANDROID COMPATIBILITY

Inspect:

```text
android/build.gradle
android/settings.gradle
android/gradle.properties
android/gradle/wrapper/gradle-wrapper.properties
android/app/build.gradle
```

Resolve:

* Gradle incompatibility
* Android Gradle Plugin incompatibility
* Java incompatibility
* Kotlin incompatibility
* compile SDK incompatibility
* namespace errors
* manifest errors
* plugin incompatibility
* NDK/CMake incompatibility

Do not blindly upgrade dependencies.

Choose versions that are mutually compatible.

Document the final working versions in:

```text
BUILD_ENVIRONMENT.md
```

---

# 7. REAL ON-DEVICE AI PIPELINE

The application MUST include a real on-device inference engine.

Preferred options:

### Option A — TensorFlow Lite

Use TensorFlow Lite if the existing model can be converted and deployed correctly.

Pipeline:

```text
Existing Model
      ↓
TensorFlow/SavedModel
      ↓
TensorFlow Lite
      ↓
Android Native Runtime
      ↓
Flutter Bridge
```

### Option B — ONNX Runtime Mobile

If TensorFlow Lite is not technically suitable:

```text
Existing Model
      ↓
ONNX
      ↓
ONNX Runtime Mobile
      ↓
Android
      ↓
Flutter
```

### Option C — Other mobile-compatible runtime

Use another inference engine only if technically justified.

Document the decision.

---

# 8. MASK R-CNN

The original implementation uses Mask R-CNN.

Investigate the actual model and weights.

Determine:

* framework
* model format
* input size
* output tensors
* classes
* weights
* preprocessing
* postprocessing
* license

Attempt actual model conversion.

Do not simply replace Mask R-CNN without investigation.

If Mask R-CNN cannot provide practical real-time performance on generic phones:

1. Benchmark it.
2. Document the limitation.
3. Select a mobile-compatible segmentation/detection model.
4. Maintain equivalent functionality as closely as possible.
5. Clearly document the change.

The application must still perform **real on-device object detection**.

---

# 9. MODEL FILES

Do not invent model weights.

Do not generate fake `.tflite` or `.onnx` files.

Use real model files.

If conversion is required, actually perform the conversion where possible.

Verify that the resulting model can:

* load
* initialize
* run inference
* return tensors
* produce detections
* produce confidence values
* produce bounding boxes
* produce masks if segmentation is supported

---

# 10. FLUTTER ↔ NATIVE VISION BRIDGE

The Flutter application should use a clean interface between Dart and native inference.

Preferred architecture:

```text
Flutter/Dart
     ↓
Platform Channel / FFI
     ↓
Kotlin / Java / C++
     ↓
TensorFlow Lite / ONNX Runtime
     ↓
AI Model
```

Do not send unnecessary full-resolution frames repeatedly through platform channels.

Use efficient native processing where possible.

Return structured detection results such as:

```text
objectId
className
confidence
boundingBox
mask
motionState
obstacleState
relativePosition
```

---

# 11. CAMERA PIPELINE

Use the Android phone camera.

The application must work with a normal generic Android phone.

Support:

* rear camera
* front camera
* camera switching
* autofocus
* rotation
* portrait
* landscape
* different resolutions
* different aspect ratios

The camera must provide frames to the inference pipeline.

Do not create a fake camera preview.

---

# 12. REAL-TIME DETECTION

The application must process actual camera frames.

For each frame:

```text
Camera
 ↓
Frame
 ↓
Resize
 ↓
Normalize
 ↓
Inference
 ↓
Post-processing
 ↓
Detection
 ↓
Tracking
 ↓
Motion
 ↓
Obstacle analysis
 ↓
Display
```

Use asynchronous processing.

Never run heavy inference on the Flutter UI thread.

---

# 13. OBJECT DETECTION

Display actual model results.

For each detected object:

```text
CLASS
CONFIDENCE
BOUNDING BOX
TRACK ID
MOTION STATE
```

Example:

```text
PERSON 94%
ID: 03
MOVING
```

The numbers must come from actual inference.

---

# 14. SEGMENTATION

Where the selected model supports segmentation, display actual segmentation masks.

Do not display fake masks.

If the final mobile model does not support segmentation:

clearly document the limitation and explain the alternative model/architecture.

---

# 15. OBJECT TRACKING

Implement real tracking.

Preserve the original project's tracking concept.

Support:

* object ID persistence
* object association
* feature matching
* lost-object handling
* re-identification where practical
* tracking confidence

---

# 16. ORB FEATURE MATCHING

Implement ORB as the default mobile feature matcher.

Where technically practical, support:

* ORB
* SIFT
* SURF

Do not include components that are incompatible with the target license or Android environment.

Document any excluded algorithm and why.

---

# 17. KALMAN FILTER

Implement the Kalman-filter logic.

Track:

```text
position
velocity
prediction
uncertainty
timestamp
```

Use it for actual object-state prediction.

Do not fabricate trajectories.

---

# 18. MOTION DETECTION

Implement actual motion analysis.

Possible states:

```text
STATIC
MOVING
APPROACHING
RECEDING
UNKNOWN
```

Account for camera movement where practical.

---

# 19. OBSTACLE ANALYSIS

Implement an actual obstacle-analysis layer.

Use available:

* object class
* object position
* bounding box
* apparent size
* motion
* trajectory
* relative depth
* tracking confidence

Output:

```text
SAFE
CAUTION
WARNING
DANGER
```

Do not claim exact physical distance unless the algorithm is properly calibrated.

Use:

**Relative Distance**

when only relative depth is available.

---

# 20. PERFORMANCE OPTIMIZATION

The application must be designed for generic Android hardware.

Implement:

* frame skipping
* adaptive resolution
* asynchronous inference
* background workers
* memory reuse
* reduced image copies
* native processing
* hardware acceleration where available
* NNAPI where appropriate
* quantization where appropriate

Target:

**15–30 FPS depending on device capability.**

Do not fabricate benchmark numbers.

Measure actual performance.

---

# 21. DEVICE PERFORMANCE MODES

Implement:

### PERFORMANCE

Maximum responsiveness.

### BALANCED

Default.

### QUALITY

Maximum detection quality.

Allow adaptive inference resolution.

Example:

```text
Low-end phone:
320 × 320

Mid-range:
416 × 416

High-end:
640 × 640
```

Use actual model-supported input sizes.

Do not use unsupported dimensions.

---

# 22. OFFLINE OPERATION

Core AI functionality must work without internet.

The following must work offline:

```text
Camera
AI inference
Object detection
Tracking
Motion analysis
Obstacle analysis
```

No cloud API should be required.

---

# 23. PRIVACY

Default:

```text
ON-DEVICE AI: ON
CLOUD AI: OFF
FRAME UPLOAD: OFF
```

Do not upload camera frames.

Do not require user login.

Do not collect unnecessary personal data.

---

# 24. SESLAA BRANDING

Use:

**SESLAA Motion Stack**

Company:

**Narga Engineering Private Limited**

Package:

```text
com.seslaa.motionstack
```

Use SESLAA branding throughout the application.

---

# 25. APP ICON

Use the supplied:

```text
appicon.png
```

as the official launcher icon.

Generate appropriate Android icon resources.

Do not replace it with a generated icon.

---

# 26. COPYRIGHT

Narga Engineering-owned application code should use:

```text
© 2026 Narga Engineering Private Limited.
All rights reserved.
```

Use the appropriate SESLAA trademark designation.

Do not falsely claim third-party code or models as Narga Engineering property.

---

# 27. THIRD-PARTY LICENSES

Create:

```text
LICENSE
NOTICE
THIRD_PARTY_LICENSES.md
```

Include applicable licenses for:

* Flutter
* Dart
* Android libraries
* Camera packages
* TensorFlow Lite
* ONNX Runtime
* OpenCV
* Mask R-CNN
* third-party models
* third-party datasets
* other dependencies

Also create an in-app:

**Open Source Licenses**

screen.

---

# 28. MODEL LICENSE VERIFICATION

Before packaging any model:

verify:

* source
* owner
* license
* commercial-use rights
* redistribution rights
* attribution requirements

Do not package a model if its license does not permit the intended use.

Report any unresolved model-license issue.

---

# 29. FLUTTER UI

Create a professional SESLAA AI/robotics interface.

Main screen should show:

```text
SESLAA MOTION STACK

Camera: REAR
FPS: XX
Objects: XX
AI: ON-DEVICE

[ LIVE CAMERA ]

PERSON 94%
ID: 03
MOVING

CAR 88%
ID: 07
APPROACHING

Motion: ACTIVE
Obstacle: CAUTION
```

Controls:

```text
START
STOP
CAMERA
SETTINGS
```

---

# 30. SETTINGS

Include:

* confidence threshold
* motion sensitivity
* performance mode
* inference resolution
* camera
* tracking ON/OFF
* segmentation ON/OFF
* FPS
* snapshot
* video recording
* privacy
* licenses
* about

Default confidence:

**50%**

---

# 31. TEST VIDEO MODE

Implement a developer mode that can process a local video.

This allows comparison:

```text
Python Reference
        VS
Android Flutter
```

Compare:

* object detection
* segmentation
* tracking
* motion
* obstacle state
* FPS

---

# 32. TEST ON ACTUAL ANDROID DEVICE

If an Android device is connected to the development environment:

detect it using:

```bash
flutter devices
```

Install the application:

```bash
flutter install
```

or:

```bash
adb install <apk>
```

Run the application.

Test:

* camera permission
* camera preview
* AI model loading
* real-time detection
* tracking
* motion
* obstacle analysis
* orientation
* camera switching
* app lifecycle

If no physical phone is connected, complete all possible build/emulator tests and clearly report that physical-device validation remains pending.

Do not claim physical-phone testing if it was not performed.

---

# 33. BUILD VALIDATION

Run:

```bash
flutter clean
flutter pub get
flutter analyze
flutter test
```

Then:

```bash
flutter build apk --debug
```

Then:

```bash
flutter build apk --release
```

Fix every build error that can reasonably be fixed.

Do not stop because a dependency is inconvenient.

---

# 34. APK

Generate:

```text
SESLAA-Motion-Stack-debug.apk
```

and:

```text
SESLAA-Motion-Stack-release.apk
```

Use the actual generated APK.

Do not fabricate APK files.

Do not claim production signing without a real Narga Engineering release keystore.

---

# 35. DOCUMENTATION

Create/update:

```text
README.md
ANDROID_MIGRATION_PLAN.md
ARCHITECTURE.md
BUILD_ENVIRONMENT.md
VALIDATION_REPORT.md
THIRD_PARTY_LICENSES.md
```

Document:

* Flutter version
* Dart version
* Java version
* Gradle version
* Android Gradle Plugin
* compile SDK
* target SDK
* minimum SDK
* NDK
* inference runtime
* AI model
* model conversion
* licenses
* device testing
* performance
* limitations

---

# 36. DO NOT ACCEPT THESE AS FINAL SOLUTIONS

Do NOT finish the project with:

```text
"Native plugin incompatible."
```

without attempting to resolve it.

Do NOT finish with:

```text
"TensorFlow pipeline not implemented."
```

if a compatible runtime can be installed or integrated.

Do NOT finish with:

```text
"Object detection placeholder."
```

Do NOT finish with:

```text
"Mock camera."
```

Do NOT finish with:

```text
"Demo UI only."
```

Do NOT finish with:

```text
"Model integration can be added later."
```

The goal is a **working implementation now**.

---

# 37. IF THE ORIGINAL MODEL CANNOT RUN ON PHONE

If the original Mask R-CNN implementation is technically too heavy or incompatible:

Do not abandon the project.

Instead:

1. Measure the original model.
2. Determine the exact limitation.
3. Select an Android-compatible model.
4. Convert/deploy it.
5. Implement actual inference.
6. Preserve object detection functionality.
7. Preserve tracking.
8. Preserve motion analysis.
9. Preserve obstacle analysis.
10. Document the model substitution.

The application must still provide real on-device AI.

---

# 38. FINAL COMPLETION CRITERIA

The project is complete only when:

```text
[✓] instructions.md followed
[✓] Existing Python code inspected
[✓] Flutter project implemented
[✓] Android build environment resolved
[✓] Missing SDK/build dependencies installed where possible
[✓] Gradle compatibility resolved
[✓] Camera working
[✓] Generic Android phone supported
[✓] Real AI model integrated
[✓] Real on-device inference working
[✓] Object detection working
[✓] Segmentation working/equivalent
[✓] ORB/feature matching implemented
[✓] Object tracking working
[✓] Kalman filtering working
[✓] Motion detection working
[✓] Obstacle analysis working
[✓] Confidence values real
[✓] Tracking IDs real
[✓] Offline processing working
[✓] Privacy implemented
[✓] SESLAA branding applied
[✓] appicon.png integrated
[✓] Narga Engineering copyright applied
[✓] Third-party licenses preserved
[✓] Model licenses verified
[✓] In-app license screen implemented
[✓] flutter analyze completed
[✓] flutter tests completed
[✓] Debug APK generated
[✓] Release APK generated
[✓] Physical device tested if available
[✓] Validation report created
```

---

# 39. FINAL REPORT

At the end, provide a concise but complete report:

## Application

**SESLAA Motion Stack**

## Company

**Narga Engineering Private Limited**

## Framework

**Flutter**

## Package

`com.seslaa.motionstack`

## AI Pipeline

State exactly:

* model used
* model format
* inference runtime
* model conversion method
* input resolution
* quantization
* CPU/GPU/NNAPI usage

## Computer Vision

State exactly which are implemented:

* object detection
* segmentation
* ORB
* SIFT
* SURF
* feature matching
* tracking
* Kalman filter
* motion detection
* obstacle analysis

## Build Environment

Report actual versions.

## Device Test

Report:

* device model
* Android version
* APK version
* measured FPS
* inference latency
* memory usage if measured
* issues

## APK

Report the exact generated paths:

```text
Debug APK:
<actual path>

Release APK:
<actual path>
```

## Remaining Issues

Only list genuine remaining issues.

Do not hide limitations.

---

# 40. FINAL INSTRUCTION

**DO THE WORK, DO NOT JUST DESCRIBE THE WORK.**

Read `instructions.md`.

Inspect the existing Python repository.

Resolve the Flutter/Android/Gradle/SDK incompatibilities.

Install required components when possible.

Implement the actual on-device AI/vision pipeline.

Build the Flutter Android application.

Test it.

Generate the APK.

Use `appicon.png`.

Apply Narga Engineering ownership correctly.

Preserve all third-party licenses.

The final result must be a **real, installable SESLAA Motion Stack Android application capable of running the computer-vision pipeline on a generic Android smartphone.**
