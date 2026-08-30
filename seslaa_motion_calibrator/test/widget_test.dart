// This is a basic Flutter widget test.
//
// To perform an interaction with a widget in your test, use the WidgetTester
// utility in the flutter_test package. For example, you can send tap and scroll
// gestures. You can also use WidgetTester to find child widgets in the widget
// tree, read text, and verify that the values of widget properties are correct.

import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:seslaa_motion_stack/main.dart';

void main() {
  test('detects a moving object and maps obstacle state', () {
    final result = DetectionResult(
      objectId: 'obj-3',
      label: 'PERSON',
      confidence: 0.94,
      boundingBox: const Rect.fromLTWH(80, 120, 150, 220),
      motionState: MotionState.moving,
      obstacleState: ObstacleState.caution,
    );

    expect(result.objectId, 'obj-3');
    expect(result.label, 'PERSON');
    expect(result.obstacleState, ObstacleState.caution);
  });

  testWidgets('renders the SESLAA Motion Stack home screen', (tester) async {
    await tester.pumpWidget(const SeslaaMotionApp());

    expect(find.text('SESLAA Motion Stack'), findsWidgets);
    expect(find.text('Camera: REAR'), findsOneWidget);
    expect(find.text('AI: ON-DEVICE'), findsOneWidget);
  });
}
