# Focus and Keyboard Navigation

## Table of Contents
1. Scope and APIs
2. Focus and Navigation Model
3. Authoring Patterns
4. Best Practices
5. Troubleshooting

## Scope and APIs

Primary APIs:
- `TopLevel.FocusManager`
- `FocusManager`
- `IFocusManager`
- `InputElement.Focus(...)`
- `KeyboardNavigation`
- `KeyboardNavigationMode`
- `NavigationDirection`
- `NavigationMethod`
- `FindNextElementOptions`
- `XYFocus`
- `AccessText`

Important members:
- `FocusManager.Focus(...)`
- `FocusManager.TryMoveFocus(...)`
- `IFocusManager.GetFocusedElement()`
- `InputElement.IsTabStop`, `TabIndex`, `Focusable`
- `KeyboardNavigation.TabNavigationProperty`
- `KeyboardNavigation.TabOnceActiveElementProperty`
- `KeyboardNavigation.IsTabStopProperty`
- `KeyboardNavigation.SetTabNavigation(...)`, `SetTabIndex(...)`
- `XYFocus.LeftProperty`, `RightProperty`, `UpProperty`, `DownProperty`
- `XYFocus.NavigationModesProperty`
- `AccessText.ShowAccessKeyProperty`

Reference source files:
- `src/Avalonia.Controls/TopLevel.cs`
- `src/Avalonia.Base/Input/FocusManager.cs`
- `src/Avalonia.Base/Input/IFocusManager.cs`
- `src/Avalonia.Base/Input/InputElement.cs`
- `src/Avalonia.Base/Input/KeyboardNavigation.cs`
- `src/Avalonia.Base/Input/KeyboardNavigationMode.cs`
- `src/Avalonia.Base/Input/NavigationDirection.cs`
- `src/Avalonia.Base/Input/NavigationMethod.cs`
- `src/Avalonia.Base/Input/FindNextElementOptions.cs`
- `src/Avalonia.Base/Input/Navigation/XYFocus.Properties.cs`
- `src/Avalonia.Controls/Primitives/AccessText.cs`

## Focus and Navigation Model

Focus is owned by the current `TopLevel`.

Practical model:
- Use `InputElement.Focus(...)` for direct focus targeting.
- Use `KeyboardNavigation` attached properties to shape tab order.
- Use `FocusManager.TryMoveFocus(...)` for directional or tab traversal.
- Use `XYFocus` overrides when TV/gamepad-like directional behavior is needed.

## Authoring Patterns

### Basic tab order

```xml
<StackPanel>
  <TextBox Name="First" KeyboardNavigation.TabIndex="0" />
  <TextBox Name="Second" KeyboardNavigation.TabIndex="1" />
  <Button Content="Submit" KeyboardNavigation.TabIndex="2" />
</StackPanel>
```

### Container navigation mode

```xml
<StackPanel KeyboardNavigation.TabNavigation="Cycle">
  <TextBox />
  <TextBox />
</StackPanel>
```

### Programmatic traversal

```csharp
using Avalonia.Controls;
using Avalonia.Input;

if (TopLevel.GetTopLevel(this)?.FocusManager is FocusManager fm)
{
    fm.TryMoveFocus(NavigationDirection.Next);
}
```

### Directional override with `XYFocus`

```xml
<Button x:Name="LeftButton" XYFocus.Right="{Binding #RightButton}" />
<Button x:Name="RightButton" XYFocus.Left="{Binding #LeftButton}" />
```

### Access key visibility and labels

```xml
<StackPanel>
  <Label Content="_Name" Target="{Binding #NameBox}" />
  <TextBox x:Name="NameBox" />
</StackPanel>
```

## Best Practices

- Keep `TabIndex` usage minimal and local; rely on visual order where possible.
- Explicitly set `KeyboardNavigation.TabNavigation` on complex popups/dialog roots.
- Keep keyboard and pointer focus behavior consistent.
- Use `NavigationMethod.Tab` semantics for access-key focus feedback.
- For remote/gamepad UIs, define critical `XYFocus` directional edges explicitly.
- Avoid calling `ClearFocus()` as a normal UX pattern; move focus to a valid target.

## Troubleshooting

1. Focus cannot move into a control:
- `Focusable` is false.
- `IsEffectivelyEnabled` is false.
- Control is not visible.

2. Tab key skips expected elements:
- `KeyboardNavigation.IsTabStop` disabled.
- `KeyboardNavigation.TabNavigation` on ancestor is `None` or restrictive.

3. Directional keys move unpredictably:
- Missing `XYFocus` overrides in sparse layouts.
- Flow direction (RTL) changes effective left/right behavior.

4. Access keys do not appear or act:
- Missing `_` marker in `AccessText`/label content.
- Focus is not inside the active input root.

## XAML-First and Code-Only Usage

Default mode:
- Configure focus order/navigation in XAML first.
- Use code-only focus orchestration only when requested.

XAML-first complete example:

```xml
<StackPanel xmlns="https://github.com/avaloniaui"
            xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
            KeyboardNavigation.TabNavigation="Cycle"
            Spacing="6">
  <TextBox x:Name="FirstNameBox" KeyboardNavigation.TabIndex="0" />
  <TextBox x:Name="LastNameBox" KeyboardNavigation.TabIndex="1" />
  <Button x:Name="SaveButton" KeyboardNavigation.TabIndex="2" Content="Save" />
</StackPanel>
```

Code-only alternative (on request):

```csharp
using Avalonia.Controls;
using Avalonia.Input;

KeyboardNavigation.SetTabNavigation(formPanel, KeyboardNavigationMode.Cycle);
KeyboardNavigation.SetTabIndex(firstNameBox, 0);
KeyboardNavigation.SetTabIndex(lastNameBox, 1);
KeyboardNavigation.SetTabIndex(saveButton, 2);

TopLevel.GetTopLevel(saveButton)?.FocusManager?.Focus(firstNameBox, NavigationMethod.Tab);
```
