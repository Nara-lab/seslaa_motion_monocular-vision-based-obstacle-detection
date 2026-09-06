# Open-source model assets

The app bundles `efficientdet_lite0_detection_metadata_1.tflite`, an EfficientDet
Lite0 model with TensorFlow Lite Task Library object-detection metadata. The
metadata supplies COCO-compatible labels such as car, motorcycle, bus, truck,
airplane, bicycle, person, and animal instead of ML Kit's coarse base categories.

Recommended open-source candidates for future production integration:

- MobileNet SSD
- YOLOv8n

Before bundling a model into production APKs, verify:

- source provenance
- license compatibility
- commercial-use permission
- redistribution rights
- attribution requirements

The bundled model is downloaded from the TensorFlow model storage endpoint and
is used through ML Kit's local model API. Keep its provenance and license review
with release artifacts.

Do not redistribute model files without confirming the final legal terms.
