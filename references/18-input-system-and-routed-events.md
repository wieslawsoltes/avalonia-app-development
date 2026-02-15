# Input System and Routed Events

## Table of Contents
1. Scope and APIs
2. Input and Routing Flow
3. Authoring Patterns
4. Best Practices
5. Troubleshooting

## Scope and APIs

Primary APIs:
- `Interactive`
- `RoutedEvent` and `RoutedEvent<TEventArgs>`
- `RoutingStrategies`
- `RoutedEventArgs`
- `EventRoute`
- `RoutedEventRegistry`
- `InputElement`
- `PointerEventArgs`, `PointerPressedEventArgs`, `PointerReleasedEventArgs`
- `KeyEventArgs`
- `Gestures`
- `InteractiveExtensions`

Important members:
- `Interactive.AddHandler(...)`, `RemoveHandler(...)`, `RaiseEvent(...)`
- `RoutedEvent.Register<TOwner, TEventArgs>(...)`
- `RoutedEvent.AddClassHandler(...)`
- `RoutedEvent.Raised`, `RoutedEvent.RouteFinished`
- `RoutedEventArgs.Handled`, `Route`, `Source`, `RoutedEvent`
- `InputElement.KeyDownEvent`, `KeyUpEvent`, `TextInputEvent`
- `InputElement.PointerPressedEvent`, `PointerMovedEvent`, `PointerReleasedEvent`, `PointerWheelChangedEvent`
- `PointerEventArgs.GetPosition(...)`, `GetCurrentPoint(...)`, `PreventGestureRecognition()`
- `Gestures.TappedEvent`, `DoubleTappedEvent`, `HoldingEvent`, `PinchEvent`, `ScrollGestureEvent`
- `InteractiveExtensions.GetObservable(...)`, `AddDisposableHandler(...)`

Reference source files:
- `src/Avalonia.Base/Interactivity/Interactive.cs`
- `src/Avalonia.Base/Interactivity/RoutedEvent.cs`
- `src/Avalonia.Base/Interactivity/RoutedEventArgs.cs`
- `src/Avalonia.Base/Interactivity/EventRoute.cs`
- `src/Avalonia.Base/Interactivity/RoutedEventRegistry.cs`
- `src/Avalonia.Base/Interactivity/InteractiveExtensions.cs`
- `src/Avalonia.Base/Input/InputElement.cs`
- `src/Avalonia.Base/Input/PointerEventArgs.cs`
- `src/Avalonia.Base/Input/KeyEventArgs.cs`
- `src/Avalonia.Base/Input/Gestures.cs`

## Input and Routing Flow

Runtime flow in app code:
1. Platform sends raw input.
2. Input is translated to Avalonia routed input events.
3. Event route is built (`Direct`, `Tunnel`, `Bubble`).
4. Class handlers run first, then instance handlers.
5. `Handled` controls downstream processing.

Routing strategy quick guide:
- `Direct`: source only.
- `Tunnel`: root to source.
- `Bubble`: source to root.

Use `Tunnel` for interception, `Bubble` for normal control-level handling.

## Authoring Patterns

### Custom routed event

```csharp
using Avalonia.Interactivity;

public class CommitPanel : Avalonia.Controls.Control
{
    public static readonly RoutedEvent<RoutedEventArgs> CommitRequestedEvent =
        RoutedEvent.Register<CommitPanel, RoutedEventArgs>(
            nameof(CommitRequested),
            RoutingStrategies.Bubble);

    public event EventHandler<RoutedEventArgs>? CommitRequested
    {
        add => AddHandler(CommitRequestedEvent, value);
        remove => RemoveHandler(CommitRequestedEvent, value);
    }

    protected void RaiseCommitRequested()
    {
        RaiseEvent(new RoutedEventArgs(CommitRequestedEvent));
    }
}
```

### Intercept in tunnel and keep bubbling intact when needed

```csharp
root.AddHandler(
    Avalonia.Input.InputElement.PointerPressedEvent,
    (sender, e) =>
    {
        if (ShouldBlockPointer(e))
            e.Handled = true;
    },
    RoutingStrategies.Tunnel,
    handledEventsToo: false);
```

### Reactive subscription to routed events

```csharp
using Avalonia.Interactivity;

IDisposable sub = myControl
    .GetObservable(Avalonia.Input.InputElement.KeyDownEvent)
    .Subscribe(e => HandleKey(e));
```

### Pointer details

```csharp
void OnPointerPressed(object? sender, Avalonia.Input.PointerPressedEventArgs e)
{
    var point = e.GetCurrentPoint((Avalonia.Visual)e.Source!);
    if (point.Properties.IsLeftButtonPressed)
    {
        // Use point.Position and modifiers for deterministic handling.
    }
}
```

## Best Practices

- Register custom routed events once as `static readonly`.
- Keep input handlers small; dispatch to command or state methods.
- Use `Tunnel` only for pre-filtering and guard logic.
- Avoid global handlers with `handledEventsToo: true` unless truly required.
- Prefer typed `AddHandler<TEventArgs>` overloads for maintainability.
- For gesture-heavy controls, use `Gestures` events instead of reimplementing recognizers.
- In tests, prefer headless input simulation APIs over directly constructing pointer/key event args.

## Troubleshooting

1. Event never fires:
- Wrong routing strategy or wrong routed event instance.
- Control is not hit-testable (`IsHitTestVisible = false`) or disabled.

2. Event fires but handler never runs:
- Upstream handler set `Handled = true`.
- Your handler was added without `handledEventsToo` where needed.

3. Gesture events not appearing:
- Gesture recognition may be skipped (`PreventGestureRecognition`).
- Pointer lifecycle is incomplete (press without move/release path).

4. Duplicate handling:
- Same handler attached both as class handler and instance handler.
- Both `Tunnel` and `Bubble` are subscribed without guards.

## XAML-First and Code-Only Usage

Default mode:
- Declare interaction wiring in XAML first (events, gestures, key bindings).
- Use pure code-only handler wiring only when requested.

XAML-first references:
- Routed event handlers in XAML attributes
- `KeyBinding` collections in XAML

XAML-first usage example:

```xml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             x:Class="MyApp.Views.EditorView"
             PointerPressed="OnPointerPressed"
             KeyDown="OnKeyDown">
  <UserControl.KeyBindings>
    <KeyBinding Gesture="Ctrl+Enter" Command="{Binding CommitCommand}" />
  </UserControl.KeyBindings>
</UserControl>
```

Code-only alternative (on request):

```csharp
AddHandler(InputElement.PointerPressedEvent, OnPointerPressed, RoutingStrategies.Bubble);
AddHandler(InputElement.KeyDownEvent, OnKeyDown, RoutingStrategies.Bubble);
```
