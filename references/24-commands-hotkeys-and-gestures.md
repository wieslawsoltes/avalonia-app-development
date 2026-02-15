# Commands, Hotkeys, and Gesture Architecture

## Table of Contents
1. Scope and APIs
2. Command and Gesture Model
3. Authoring Patterns
4. Best Practices
5. Troubleshooting

## Scope and APIs

Primary APIs:
- `ICommandSource`
- `Button.Command` and `MenuItem.Command`
- `Button.HotKey` and `MenuItem.HotKey`
- `HotKeyManager`
- `InputElement.KeyBindings`
- `KeyBinding`
- `KeyGesture`
- `Gestures`
- `MenuItem.InputGesture`

Important members:
- `ICommandSource.Command`, `CommandParameter`
- `HotKeyManager.HotKeyProperty`, `SetHotKey(...)`, `GetHotKey(...)`
- `InputElement.KeyBindings` list
- `KeyBinding.Gesture`, `Command`, `CommandParameter`, `TryHandle(...)`
- `KeyGesture.Parse(...)`, `Matches(...)`, `ToString(...)`
- `Gestures.AddTappedHandler(...)`, `AddHoldingHandler(...)`, `AddPinchHandler(...)`

Reference source files:
- `src/Avalonia.Base/Input/ICommandSource.cs`
- `src/Avalonia.Controls/Button.cs`
- `src/Avalonia.Controls/MenuItem.cs`
- `src/Avalonia.Controls/HotkeyManager.cs`
- `src/Avalonia.Base/Input/InputElement.cs`
- `src/Avalonia.Base/Input/KeyBinding.cs`
- `src/Avalonia.Base/Input/KeyGesture.cs`
- `src/Avalonia.Base/Input/Gestures.cs`

## Command and Gesture Model

Architecture layers:
1. Command source (`Button`, `MenuItem`, custom `ICommandSource`).
2. Trigger mechanism (`Click`, key binding, hotkey, pointer gesture).
3. Command execution with parameter and `CanExecute` semantics.

Use hotkeys for control-scoped shortcuts and `KeyBindings` for root-level or view-level shortcuts.

## Authoring Patterns

### Standard command binding

```xml
<Button Content="Save"
        Command="{Binding SaveCommand}"
        CommandParameter="{Binding CurrentDocument}" />
```

### Add key binding at view root

```csharp
using Avalonia.Input;

var binding = new KeyBinding
{
    Gesture = KeyGesture.Parse("Ctrl+S"),
    Command = viewModel.SaveCommand
};

rootControl.KeyBindings.Add(binding);
```

### Attach hotkey declaratively

```xml
<Button Content="Run"
        Command="{Binding RunCommand}"
        HotKey="Ctrl+R" />
```

### Gesture event hookup for touch/pointer interactions

```csharp
using Avalonia.Input;

Gestures.AddTappedHandler(canvas, (_, e) => HandleTap(e));
Gestures.AddHoldingHandler(canvas, (_, e) => HandleHold(e));
```

### Show keyboard gesture text in menus

```xml
<MenuItem Header="_Save"
          Command="{Binding SaveCommand}"
          InputGesture="Ctrl+S" />
```

## Best Practices

- Keep command logic in viewmodels; keep UI handlers thin.
- Use stable command parameters and avoid long-running work on UI thread.
- Prefer one authoritative binding location for a shortcut to avoid conflicts.
- Use `InputGesture` for menu display consistency, with actual command binding.
- For game-like key mapping, use `PhysicalKey` from `KeyEventArgs` instead of locale-dependent `Key` when required.

## Troubleshooting

1. Hotkey does not execute:
- Target control is neither `ICommandSource` nor `IClickableControl`.
- Control is not under active `TopLevel`.

2. Shortcut executes twice:
- Same `KeyGesture` registered in both parent and child routes.

3. Command disabled unexpectedly:
- `CanExecute` false or control not effectively enabled.

4. Gesture never fires:
- Element does not receive pointer input, or gesture recognition was skipped upstream.

## XAML-First and Code-Only Usage

Default mode:
- Define command surfaces and gestures in XAML first.
- Use code-only gesture/command wiring when requested.

XAML-first complete example:

```xml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:DataType="vm:EditorViewModel">
  <UserControl.KeyBindings>
    <KeyBinding Gesture="Ctrl+S" Command="{CompiledBinding SaveCommand}" />
  </UserControl.KeyBindings>

  <StackPanel Spacing="8">
    <Button Content="Save" Command="{CompiledBinding SaveCommand}" HotKey="Ctrl+S" />
    <Menu>
      <MenuItem Header="_File">
        <MenuItem Header="_Save"
                  InputGesture="Ctrl+S"
                  Command="{CompiledBinding SaveCommand}" />
      </MenuItem>
    </Menu>
  </StackPanel>
</UserControl>
```

Code-only alternative (on request):

```csharp
using Avalonia.Controls;
using Avalonia.Input;

var saveBinding = new KeyBinding
{
    Gesture = KeyGesture.Parse("Ctrl+S"),
    Command = viewModel.SaveCommand
};

root.KeyBindings.Add(saveBinding);
HotKeyManager.SetHotKey(saveButton, KeyGesture.Parse("Ctrl+S"));
Gestures.AddTappedHandler(canvas, (_, e) => viewModel.SelectAt(e.GetPosition(canvas)));
```
