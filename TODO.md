## Task: Improve Motion Detection and Monocular Event-Based Vision

Improve the existing vision system to provide **robust motion detection and monocular event-based vision**, with all detected objects/events clearly identified using **rectangular bounding boxes** on the camera preview.

### Requirements

1. **Improve Motion Detection**

   * Detect meaningful movement reliably from the monocular camera feed.
   * Reduce false positives caused by:

     * Camera vibration/shake
     * Lighting changes
     * Shadows
     * Reflections
     * Noise
   * Distinguish between actual object movement and background/environment changes.
   * Provide configurable motion sensitivity and detection thresholds.
   * Maintain real-time performance on the Android device.

2. **Monocular Event-Based Vision**

   * Use the single RGB/monocular camera as the primary vision sensor.
   * Detect and classify important visual events from consecutive camera frames.
   * Track objects across frames rather than treating every frame as a new detection.
   * Generate events such as:

     * Object detected
     * Object entering the scene
     * Object leaving the scene
     * Object approaching
     * Object moving away
     * Object stopped
     * Significant motion detected
     * Sudden movement
   * Where technically feasible, estimate relative motion/approach using monocular vision without claiming absolute distance accuracy unless calibrated.

3. **Object Detection and Bounding Boxes**

   * Every detected object must be displayed with a **rectangular bounding box**.
   * Show the detected object's class/name above or inside the bounding box.
   * Example:

     * `PERSON`
     * `CAR`
     * `TRUCK`
     * `BIKE`
     * `MOTORCYCLE`
     * `ANIMAL`
     * `UNKNOWN`
   * Display a confidence score where available.
   * Use stable bounding boxes that do not excessively jump between frames.
   * Assign a persistent tracking ID when the same object remains visible, e.g. `Person #1`, `Car #2`.

4. **Event Visualization**

   * Highlight the bounding box when an important event occurs.
   * Display a clear event label such as:

     * `MOTION`
     * `APPROACHING`
     * `DEPARTING`
     * `ENTERED`
     * `EXITED`
     * `STOPPED`
   * Include event timestamp and object ID in the event log.
   * Avoid generating duplicate events continuously for the same object.

5. **Tracking**

   * Implement object tracking between frames.
   * Preserve object identity when the object temporarily moves or changes position.
   * Use an appropriate lightweight tracker suitable for Android real-time processing.
   * Handle multiple objects simultaneously.

6. **Performance**

   * Prioritize real-time inference on the physical Android phone.
   * Optimize camera frame processing, inference frequency, memory usage, and CPU/GPU/NPU utilization.
   * Do not unnecessarily process every camera frame if frame skipping or adaptive inference can improve performance.
   * The system must fail gracefully if the device cannot maintain the target FPS.

7. **Calibration / Monocular Geometry**

   * Support camera calibration parameters where available:

     * Camera matrix
     * Focal length
     * Principal point
     * Distortion coefficients
   * Use OpenCV or another suitable open-source computer-vision implementation where appropriate.
   * Do not assume that monocular vision can provide accurate absolute depth without calibration/additional information.
   * Clearly separate **relative motion/depth estimation** from true metric distance measurement.

8. **Architecture**

   * Keep the vision pipeline modular:
     `Camera → Preprocessing → Motion Detection → Object Detection → Tracking → Event Detection → Bounding Box/Event Overlay → Event Log`
   * Avoid hard-coded device-specific assumptions.
   * Keep model inference and camera processing asynchronous so the UI remains responsive.

9. **Model Integration**

   * Use a lightweight, Android-compatible open-source object detection model if the current project does not already have one.
   * Prefer TensorFlow Lite, ONNX Runtime, MediaPipe, OpenCV DNN, or another proven on-device framework compatible with the existing Android/Gradle/SDK environment.
   * If the current environment prevents the required vision pipeline from working, resolve the dependency/version incompatibility rather than leaving the feature as a placeholder.
   * Do not replace the existing working functionality unnecessarily.

10. **Testing**
    Test using the **actual Android phone camera**, not only an emulator.

Verify:

* Stationary scene → no continuous false motion events.
* Person walking → person detected, tracked, and boxed.
* Vehicle moving → vehicle detected, tracked, and boxed.
* Multiple objects → separate bounding boxes and tracking IDs.
* Object entering → `ENTERED` event.
* Object leaving → `EXITED` event.
* Object approaching → `APPROACHING` event when reliably measurable.
* Camera shake → minimize false detections.
* Lighting changes → minimize false events.
* Low-light conditions → graceful degradation.
* App restart → camera and vision pipeline recover correctly.

### Acceptance Criteria

The implementation is considered complete only when:

* The **physical Android camera works correctly**.
* Real objects are detected in real time.
* Detected objects are displayed using **rectangular bounding boxes**.
* Object labels and confidence scores are visible.
* Objects can be tracked across frames.
* Motion/events are generated based on actual visual changes.
* False motion events are significantly reduced.
* Event labels are displayed together with the relevant bounding box.
* The pipeline runs reliably without crashes.
* No major vision component is left as a mock, placeholder, or TODO.
* Build dependencies and Android/Gradle/SDK compatibility are resolved.
* The final implementation is tested on the actual phone and the results are documented.

**Important:** First inspect the existing project architecture and `instructions.md` and follow its requirements. Do not rewrite unrelated parts of the application. Preserve existing functionality while implementing and integrating the improved monocular motion/event-based vision pipeline.
