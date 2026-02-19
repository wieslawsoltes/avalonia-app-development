# WinUI Pointer Gestures, Touch/Pen, and InkCanvas to Avalonia

## Table of Contents
1. Scope and APIs
2. Concept Mapping
3. Conversion Example
4. Migration Notes

## Scope and APIs

Primary WinUI APIs:

- PointerPressed/PointerMoved/PointerReleased, GestureRecognizer, InkCanvas, InkPresenter

Primary Avalonia APIs:

- PointerPressed/PointerMoved/PointerReleased, Gestures (`Tapped`, `Holding`), GestureRecognizers, pointer type detection

## Concept Mapping

| WinUI idiom | Avalonia idiom |
|---|---|
| Pointer event handlers | Pointer event handlers |
| GestureRecognizer + taps/holds | Gestures events + recognizers |
| Pen input branching | `e.Pointer.Type` checks |
| InkCanvas strokes | custom drawing surface + pointer sampling |

## Conversion Example

WinUI XAML:

```xaml
<Grid PointerPressed="OnPressed" PointerMoved="OnMoved" PointerReleased="OnReleased">
  <InkCanvas x:Name="InkSurface" />
</Grid>
```

WinUI C#:

```csharp
void OnPressed(object sender, PointerRoutedEventArgs e)
{
    if (e.Pointer.PointerDeviceType == PointerDeviceType.Pen)
    {
        InkSurface.InkPresenter.InputDeviceTypes = CoreInputDeviceTypes.Pen;
    }
}
```

Avalonia XAML:

```xaml
<Border xmlns="https://github.com/avaloniaui"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        PointerPressed="OnPressed"
        PointerMoved="OnMoved"
        PointerReleased="OnReleased">
  <Canvas x:Name="InkSurface" Background="Transparent" />
</Border>
```

Avalonia C#:

```csharp
void OnPressed(object? sender, PointerPressedEventArgs e)
{
    if (e.Pointer.Type == PointerType.Pen)
    {
        _activeStroke = new List<Point> { e.GetPosition(InkSurface) };
    }
}

void OnMoved(object? sender, PointerEventArgs e)
{
    if (_activeStroke is not null)
        _activeStroke.Add(e.GetPosition(InkSurface));
}

void OnReleased(object? sender, PointerReleasedEventArgs e)
{
    _activeStroke = null;
}
```

## Migration Notes

1. Avalonia has no one-to-one `InkCanvas`; use custom pointer sampling + rendering.
2. Prefer routed gesture events (`Tapped`, `Holding`) for high-level interactions.
3. Keep pen/touch branching explicit via pointer type and modifiers.
