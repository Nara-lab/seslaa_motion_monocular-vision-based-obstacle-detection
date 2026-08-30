# Third-Party Licenses

This document covers the major third-party components referenced by the SESLAA Motion Stack project and the Python reference implementation.

## Flutter and Dart

- Flutter SDK: BSD-style license governing the Flutter framework and engine
- Dart SDK: BSD 3-Clause style license
- Material and Cupertino UI components: Apache 2.0 / Flutter framework license terms

## Android and Java tooling

- Android SDK / platform builds: Apache 2.0 license terms
- Android Gradle Plugin and Kotlin tooling: Apache 2.0 license terms
- AndroidX libraries: Apache 2.0 license terms

## Camera and vision tooling

- camera package: Flutter plugin license terms as published by the package maintainer
- OpenCV: Apache 2.0 license with additional patent and third-party notices depending on the build configuration
- TFLite / TensorFlow Lite: Apache 2.0 license

## Python reference project

The repository uses a Python monocular-vision codebase as a technical reference. That codebase includes Mask R-CNN, feature matching algorithms, and calibration logic that may carry additional licensing and redistribution obligations depending on model and dataset origin.

Relevant reference components include:

- Mask R-CNN
- ORB matcher
- SIFT matcher
- SURF matcher
- Kalman-based tracking logic
- model weights and calibration assets

The project does not redistribute model weights or third-party model packages unless they have been reviewed for license compatibility and provenance.

## Model and dataset caveat

Mask R-CNN model weights, datasets, and derived assets may require separate review for:

- source ownership
- commercial-use permission
- redistribution permission
- attribution requirements
- model license compatibility

The current project ships the app shell and APK artifacts but does not bundle a production AI model for distribution without a verified license check.
