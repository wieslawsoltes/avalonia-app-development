# Popups, Flyouts, ToolTips, and Overlay Layering

## Table of Contents
1. Scope and APIs
2. Placement and Layering Model
3. Authoring Patterns
4. Best Practices
5. Troubleshooting

## Scope and APIs

Primary APIs:
- `Popup`
- `FlyoutBase` and `PopupFlyoutBase`
- `ContextMenu`
- `ToolTip`
- `OverlayPopupHost`
- `PlacementMode`
- `PopupAnchor`, `PopupGravity`, `PopupPositionerConstraintAdjustment`
- `CustomPopupPlacementCallback`

Important members:
- `Popup.IsOpen`, `Child`, `PlacementTarget`, `Placement`, `PlacementRect`
- `Popup.IsLightDismissEnabled`, `Topmost`, `ShouldUseOverlayLayer`, `IsUsingOverlayLayer`
- `Popup.OverlayDismissEventPassThrough`, `OverlayInputPassThroughElement`
- `Popup.Opened`, `Closed`, `Closing`
- `FlyoutBase.ShowAt(...)`, `Hide()`, `IsOpen`, `Target`
- `FlyoutBase.AttachedFlyoutProperty`, `ShowAttachedFlyout(...)`
- `PopupFlyoutBase.ShowMode`
- `ToolTip.TipProperty`, `IsOpenProperty`, `PlacementProperty`, `ShowDelayProperty`
- `ToolTip.ToolTipOpeningEvent`, `ToolTip.ToolTipClosingEvent`
- `Control.ContextMenuProperty`, `Control.ContextFlyoutProperty`

Reference source files:
- `src/Avalonia.Controls/Primitives/Popup.cs`
- `src/Avalonia.Controls/Flyouts/FlyoutBase.cs`
- `src/Avalonia.Controls/Flyouts/PopupFlyoutBase.cs`
- `src/Avalonia.Controls/ContextMenu.cs`
- `src/Avalonia.Controls/ToolTip.cs`
- `src/Avalonia.Controls/Primitives/OverlayPopupHost.cs`
- `src/Avalonia.Controls/PlacementMode.cs`
- `src/Avalonia.Controls/Primitives/PopupPositioning/IPopupPositioner.cs`
- `src/Avalonia.Controls/Primitives/PopupPositioning/CustomPopupPlacementCallback.cs`
- `src/Avalonia.Controls/Control.cs`

## Placement and Layering Model

Core decisions:
- Surface: native popup host vs overlay host.
- Placement: simple (`Bottom`, `Pointer`) vs anchor/gravity mode.
- Dismissal: explicit close vs light dismiss.
- Focus: whether popup/flyout takes focus and how it closes on key/pointer.

Constraint adjustment flags (`Slide`, `Flip`, `Resize`) control fallback behavior when popup would be out of bounds.

## Authoring Patterns

### Context flyout on control

```xml
<Button Content="Actions">
  <Button.ContextFlyout>
    <Flyout Placement="Bottom">
      <StackPanel Spacing="8" Margin="8">
        <Button Content="Rename" Command="{Binding RenameCommand}" />
        <Button Content="Delete" Command="{Binding DeleteCommand}" />
      </StackPanel>
    </Flyout>
  </Button.ContextFlyout>
</Button>
```

### Popup with explicit positioning and light dismiss

```xml
<Popup x:Name="InspectorPopup"
       IsOpen="{Binding IsInspectorOpen}"
       PlacementTarget="{Binding #AnchorButton}"
       Placement="AnchorAndGravity"
       PlacementAnchor="BottomLeft"
       PlacementGravity="BottomLeft"
       IsLightDismissEnabled="True"
       PlacementConstraintAdjustment="FlipX,FlipY,SlideX,SlideY" />
```

### ToolTip attached properties

```xml
<TextBox ToolTip.Tip="Enter API token"
         ToolTip.Placement="Top"
         ToolTip.ShowDelay="250"
         ToolTip.BetweenShowDelay="100" />
```

### Custom placement callback

```csharp
using Avalonia.Controls.Primitives.PopupPositioning;

popup.CustomPopupPlacementCallback = (popupSize, targetSize, offset) =>
{
    return new[]
    {
        new CustomPopupPlacement(new Point(0, targetSize.Height + 4), PopupPrimaryAxis.Vertical)
    };
};
```

## Best Practices

- Prefer `ContextFlyout`/`ContextMenu` for menu semantics over ad-hoc popups.
- Use `PlacementMode.AnchorAndGravity` when you need predictable cross-platform edge behavior.
- Keep light-dismiss behavior consistent across dialog-like surfaces.
- For overlays above complex UI, set pass-through properties deliberately.
- Always define keyboard-close semantics (Escape) for non-trivial popups/flyouts.

## Troubleshooting

1. Popup opens in wrong location:
- Missing `PlacementTarget` or incorrect `PlacementRect`.
- Constraint adjustments flipping unexpectedly.

2. Click-through or blocked input issues:
- Misconfigured `OverlayDismissEventPassThrough` or `OverlayInputPassThroughElement`.

3. Popup closes immediately:
- Light dismiss enabled with focus/pointer move path hitting outside bounds.

4. ToolTip does not show:
- `ToolTip.ServiceEnabled` disabled or `Tip` unset.
- Opening canceled by `ToolTipOpeningEvent` handler.

## XAML-First and Code-Only Usage

Default mode:
- Define popup/flyout surfaces in XAML first.
- Use code-only popup construction when requested.

XAML-first complete example:

```xml
<StackPanel xmlns="https://github.com/avaloniaui"
            xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
            Spacing="8">
  <Button x:Name="AnchorButton" Content="Show Popup" Click="ShowPopupClick" />

  <Popup x:Name="InspectorPopup"
         PlacementTarget="{Binding #AnchorButton}"
         Placement="Bottom"
         IsLightDismissEnabled="True">
    <Border Padding="8" Background="#2B2F36">
      <TextBlock Text="Inspector" />
    </Border>
  </Popup>
</StackPanel>
```

Code-only alternative (on request):

```csharp
using Avalonia;
using Avalonia.Controls;
using Avalonia.Media;

var popup = new Popup
{
    PlacementTarget = anchorButton,
    Placement = PlacementMode.Bottom,
    IsLightDismissEnabled = true,
    Child = new Border
    {
        Padding = new Thickness(8),
        Background = Brushes.DimGray,
        Child = new TextBlock { Text = "Inspector" }
    }
};

anchorButton.Click += (_, _) => popup.IsOpen = true;
```
