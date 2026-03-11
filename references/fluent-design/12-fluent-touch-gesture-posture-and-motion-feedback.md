# Fluent Touch, Gesture Posture, and Motion Feedback

## Table of Contents
1. Scope and Primary APIs
2. Fluent Posture Rules
3. Gesture and Kinetic Feedback Patterns
4. Scroll, Pull, and Refresh Guidance
5. AOT and Runtime Notes
6. Do and Don't Guidance
7. Troubleshooting
8. Official Resources

## Scope and Primary APIs

Use this reference to make Fluent experiences feel correct under touch, touchpad, pen, and mixed-input desktop workflows.

Primary APIs:
- `Gestures`
- `ScrollGestureRecognizer`, `PullGestureRecognizer`, `PinchGestureRecognizer`
- `RefreshContainer`
- `ScrollViewer`
- `Transitions`, `TransformOperationsTransition`, `DoubleTransition`
- `PointerPressedEventArgs`, `HoldingRoutedEventArgs`

This file covers:
- posture-aware Fluent spacing and command placement,
- gesture feedback and motion confirmation,
- pull and refresh patterns,
- kinetic scrolling and snap behavior.

## Fluent Posture Rules

Fluent motion and spacing should adapt to posture:

- mouse and keyboard allow higher density,
- touch needs clearer separation and faster visible feedback,
- touchpad and pen need smooth but restrained motion,
- mixed-input productivity tools should not privilege only one posture.

Rules:
- make primary actions easy to hit without crowding them,
- avoid hover-only essential affordances,
- keep gesture-triggered outcomes visible and reversible where possible,
- preserve the same command hierarchy across input modes.

## Gesture and Kinetic Feedback Patterns

```csharp
using Avalonia.Input;

Gestures.AddTappedHandler(CommandCard, (_, _) =>
{
    CommandCard.Classes.Add("pressed");
});

Gestures.AddHoldingHandler(CommandCard, (_, e) =>
{
    if (e is HoldingRoutedEventArgs args && args.HoldingState == HoldingState.Started)
    {
        CommandCard.Classes.Add("holding");
    }
});
```

```xml
<Style Selector="Border.fluent-command-card.pressed">
  <Setter Property="RenderTransform" Value="translateY(1px)" />
  <Setter Property="Opacity" Value="0.96" />
</Style>
```

Guidance:
- keep touch feedback immediate,
- use motion to confirm the gesture, not to celebrate it,
- avoid stacking hold, swipe, pinch, and pull on the same core command surface,
- ensure the visual recovery is as clear as the activation.

## Scroll, Pull, and Refresh Guidance

```xml
<RefreshContainer xmlns="https://github.com/avaloniaui"
                  xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
                  PullDirection="TopToBottom">
  <ListBox ScrollViewer.IsScrollInertiaEnabled="True"
           ScrollViewer.VerticalSnapPointsType="MandatorySingle"
           ScrollViewer.VerticalSnapPointsAlignment="Near" />
</RefreshContainer>
```

Rules:
- use pull-to-refresh only where refresh is a natural user model,
- keep snap points meaningful rather than ornamental,
- let kinetic feedback support orientation in dense lists,
- keep Fluent touch motion short and calm.

## AOT and Runtime Notes

- Keep most posture-specific feedback in styles and shared behavior patterns.
- Reuse the same Fluent motion grammar across pointer and touch states.
- Keep gesture logic thin and testable; the design system should define how feedback looks.

## Do and Don't Guidance

Do:
- design Fluent shells for mixed-input reality,
- keep gesture feedback visible and restrained,
- use pull, snap, and inertia only when they reinforce the content model.

Do not:
- make critical actions hover-dependent,
- overload one surface with many gesture types,
- let touch feedback feel heavier than the actual task.

## Troubleshooting

1. Fluent UI feels desktop-only on touch screens.
- Spacing, feedback speed, and gesture discoverability usually need work.

2. Gesture feedback feels flashy.
- Reduce distance and duration, then simplify the number of moving properties.

3. Pull-to-refresh feels bolted on.
- It likely does not match the mental model of the screen or list.

## Official Resources

- Touch interactions for Windows apps: [learn.microsoft.com/en-us/windows/apps/design/input/touch-interactions](https://learn.microsoft.com/en-us/windows/apps/design/input/touch-interactions)
- Fluent 2 accessibility: [fluent2.microsoft.design/accessibility](https://fluent2.microsoft.design/accessibility)
- Fluent 2 motion: [fluent2.microsoft.design/motion](https://fluent2.microsoft.design/motion)
