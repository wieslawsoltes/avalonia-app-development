# Windowing System and Custom Decorations

## Table of Contents
1. Scope and APIs
2. App-Level Windowing APIs
3. Custom Client Area and Decorations
4. Platform-Specific Decoration Hooks
5. Best Practices
6. Troubleshooting

## Scope and APIs

Primary app-building APIs:
- `Window`
- `TopLevel`
- `SystemDecorations`
- `ExtendClientAreaToDecorationsHint`
- `ExtendClientAreaChromeHints`
- `ExtendClientAreaTitleBarHeightHint`
- `Window.BeginMoveDrag(...)`
- `Window.BeginResizeDrag(...)`
- `TopLevel.TransparencyLevelHint`
- `TopLevel.ActualTransparencyLevel`

Related platform-facing interfaces (mostly unstable/internal implementation points):
- `ITopLevelImpl`
- `IWindowImpl`
- `IWindowingPlatform`

Reference source files:
- `src/Avalonia.Controls/Window.cs`
- `src/Avalonia.Controls/TopLevel.cs`
- `src/Avalonia.Controls/Platform/IWindowImpl.cs`
- `src/Avalonia.Controls/Platform/ITopLevelImpl.cs`
- `src/Avalonia.Controls/Platform/ExtendClientAreaChromeHints.cs`

## App-Level Windowing APIs

Use `Window` for normal desktop app UI:
- Size/state: `SizeToContent`, `WindowState`, `CanResize`, `CanMinimize`, `CanMaximize`
- Frame/chrome: `SystemDecorations`, `ExtendClientArea*`
- Taskbar and activation: `ShowInTaskbar`, `ShowActivated`

Use `TopLevel` for cross-window surface behavior:
- Transparency: `TransparencyLevelHint`, `ActualTransparencyLevel`
- Theme bridge to frame: `RequestedThemeVariant`, `ActualThemeVariant`
- Frame callback scheduling: `RequestAnimationFrame`

## Custom Client Area and Decorations

To build custom title bars/chrome:
1. Set `ExtendClientAreaToDecorationsHint="True"`.
2. Configure `ExtendClientAreaChromeHints`.
3. Set `SystemDecorations` if needed.
4. Handle dragging/resizing through window methods.

Example:

```xml
<Window x:Class="MyApp.MainWindow"
        ExtendClientAreaToDecorationsHint="True"
        ExtendClientAreaChromeHints="PreferSystemChrome"
        ExtendClientAreaTitleBarHeightHint="32"
        SystemDecorations="Full" />
```

For custom drag handles:

```csharp
private void TitlePointerPressed(object? sender, PointerPressedEventArgs e)
{
    if (e.GetCurrentPoint(this).Properties.IsLeftButtonPressed)
        BeginMoveDrag(e);
}
```

For custom resize grips:

```csharp
private void ResizeGripPressed(object? sender, PointerPressedEventArgs e)
{
    BeginResizeDrag(WindowEdge.SouthEast, e);
}
```

Built-in managed decoration controls:
- `Avalonia.Controls.Chrome.TitleBar`
- `Avalonia.Controls.Chrome.CaptionButtons`

## Platform-Specific Decoration Hooks

Platform extension APIs for deeper control:
- Win32: `Win32Properties`
  - `AddWindowStylesCallback`
  - `AddWndProcHookCallback`
  - `NonClientHitTestResultProperty`
- X11: `X11Properties`
  - `NetWmWindowTypeProperty`
  - `WmClassProperty`

Use these only when standard cross-platform APIs are insufficient.

## Best Practices

- Start with cross-platform `Window` APIs first.
- Only add platform-specific hooks behind runtime checks.
- Keep drag/resize behavior centralized in one chrome component.
- Account for `WindowDecorationMargin` and `OffScreenMargin` in custom layout.

## Troubleshooting

1. Custom title bar visible but dragging fails:
- Ensure pointer handler calls `BeginMoveDrag` on press with left button.

2. Resize handles do nothing:
- Confirm `CanResize=true` and call `BeginResizeDrag` with correct `WindowEdge`.

3. Transparency hint not honored:
- `TransparencyLevelHint` is best-effort; check `ActualTransparencyLevel`.

4. Decorated area overlaps content:
- Observe `WindowDecorationMargin`/`OffScreenMargin` and adjust layout padding.

5. Inconsistent behavior across OSes:
- This is expected for decoration internals; prefer portable APIs for baseline UX.

## XAML-First and Code-Only Usage

Default mode:
- Define custom chrome surface in XAML first.
- Use code-only window composition only when requested.

XAML-first complete example:

```xml
<Window xmlns="https://github.com/avaloniaui"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        x:Class="MyApp.MainWindow"
        ExtendClientAreaToDecorationsHint="True"
        ExtendClientAreaChromeHints="NoChrome"
        SystemDecorations="None">
  <Grid RowDefinitions="32,*">
    <Border Grid.Row="0" Background="#2A2E35" PointerPressed="TitleBarPointerPressed">
      <TextBlock Margin="10,0" VerticalAlignment="Center" Text="My App" />
    </Border>
    <ContentPresenter Grid.Row="1" />
  </Grid>
</Window>
```

Code-only alternative (on request):

```csharp
using Avalonia.Controls;
using Avalonia.Input;

var window = new Window
{
    ExtendClientAreaToDecorationsHint = true,
    ExtendClientAreaChromeHints = ExtendClientAreaChromeHints.NoChrome,
    SystemDecorations = SystemDecorations.None
};

window.PointerPressed += (_, e) =>
{
    if (e.GetCurrentPoint(window).Properties.IsLeftButtonPressed)
        window.BeginMoveDrag(e);
};
```
