# Menu Controls, ContextMenu, and MenuFlyout Patterns

## Table of Contents
1. Scope and APIs
2. Choose the Right Menu Surface
3. Top Menu Authoring (`Menu` + `MenuItem`)
4. Command, HotKey, and InputGesture Wiring
5. Stateful Menu Items (`CheckBox` and `Radio`)
6. `ContextMenu` Placement and Lifecycle
7. `MenuFlyout` and `ContextFlyout` Patterns
8. Dynamic Menu Construction in C#
9. Best Practices
10. Troubleshooting

## Scope and APIs

Primary APIs:
- `MenuBase`
- `Menu`
- `MenuItem`
- `ContextMenu`
- `MenuFlyout`
- `MenuFlyoutPresenter`
- `MenuItemToggleType`
- `HotKeyManager`
- `KeyBinding` and `KeyGesture`

Important members:
- `MenuBase.IsOpen`, `MenuBase.Open()`, `MenuBase.Close()`, `MenuBase.Opened`, `MenuBase.Closed`
- `MenuItem.Command`, `MenuItem.CommandParameter`, `MenuItem.HotKey`, `MenuItem.InputGesture`
- `MenuItem.IsSubMenuOpen`, `MenuItem.StaysOpenOnClick`
- `MenuItem.ToggleType`, `MenuItem.IsChecked`, `MenuItem.GroupName`
- `ContextMenu.Placement`, `PlacementTarget`, `PlacementRect`, `PlacementAnchor`, `PlacementGravity`
- `ContextMenu.Open(Control?)`, `ContextMenu.Opening`, `ContextMenu.Closing`
- `MenuFlyout.Items`, `ItemsSource`, `ItemTemplate`, `ItemContainerTheme`, `FlyoutPresenterTheme`

Reference source files:
- `src/Avalonia.Controls/MenuBase.cs`
- `src/Avalonia.Controls/Menu.cs`
- `src/Avalonia.Controls/MenuItem.cs`
- `src/Avalonia.Controls/ContextMenu.cs`
- `src/Avalonia.Controls/Flyouts/MenuFlyout.cs`
- `src/Avalonia.Controls/Flyouts/MenuFlyoutPresenter.cs`
- `src/Avalonia.Base/Input/KeyGesture.cs`
- `src/Avalonia.Base/Input/KeyBinding.cs`

## Choose the Right Menu Surface

Use `Menu` when:
- the app needs a persistent top menu strip,
- keyboard access keys should work against a visible main menu.

Use `ContextMenu` when:
- menu content is target-specific (item/canvas row/cell),
- open location should follow pointer or explicit placement rules.

Use `MenuFlyout` when:
- you want flyout-style attachment (`ContextFlyout`, explicit `ShowAt(...)`),
- menu content behaves like a popup flyout but uses `MenuItem` semantics.

## Top Menu Authoring (`Menu` + `MenuItem`)

XAML-first top menu with submenus:

```xml
<Menu xmlns="https://github.com/avaloniaui"
      xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml">
  <MenuItem Header="_File">
    <MenuItem Header="_Open"
              Command="{Binding OpenCommand}"
              InputGesture="Ctrl+O" />
    <MenuItem Header="_Save"
              Command="{Binding SaveCommand}"
              InputGesture="Ctrl+S" />
    <Separator />
    <MenuItem Header="E_xit"
              Command="{Binding ExitCommand}" />
  </MenuItem>

  <MenuItem Header="_Edit">
    <MenuItem Header="_Copy" Command="{Binding CopyCommand}" InputGesture="Ctrl+C" />
    <MenuItem Header="_Paste" Command="{Binding PasteCommand}" InputGesture="Ctrl+V" />
  </MenuItem>
</Menu>
```

Notes:
- `_` in `Header` defines access key text.
- `Menu` is a `MenuBase` and manages open/close state across top-level items.

## Command, HotKey, and InputGesture Wiring

`InputGesture`:
- display-only shortcut text in menu UI.

`HotKey`:
- actual key gesture handling for a command source.

Common pattern:
- set `Command` + `InputGesture` for display,
- register execution through `HotKey` or root `KeyBindings` for deterministic behavior.

```xml
<MenuItem Header="_Save"
          Command="{Binding SaveCommand}"
          HotKey="Ctrl+S"
          InputGesture="Ctrl+S" />
```

If you centralize shortcuts at view root:

```xml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml">
  <UserControl.KeyBindings>
    <KeyBinding Gesture="Ctrl+S" Command="{Binding SaveCommand}" />
  </UserControl.KeyBindings>
</UserControl>
```

## Stateful Menu Items (`CheckBox` and `Radio`)

`MenuItem` supports toggled states:
- `ToggleType="CheckBox"` for independent flags,
- `ToggleType="Radio"` + `GroupName` for exclusive choices.

```xml
<MenuItem xmlns="https://github.com/avaloniaui"
          Header="_View">
  <MenuItem Header="Show _Grid"
            ToggleType="CheckBox"
            IsChecked="{Binding ShowGrid}" />

  <Separator />

  <MenuItem Header="Zoom _100%"
            ToggleType="Radio"
            GroupName="Zoom"
            IsChecked="{Binding Zoom100}" />
  <MenuItem Header="Zoom _200%"
            ToggleType="Radio"
            GroupName="Zoom"
            IsChecked="{Binding Zoom200}" />
</MenuItem>
```

## `ContextMenu` Placement and Lifecycle

Attached usage:

```xml
<Button xmlns="https://github.com/avaloniaui"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        Content="Item Actions">
  <Button.ContextMenu>
    <ContextMenu Placement="Pointer">
      <MenuItem Header="Rename" Command="{Binding RenameCommand}" />
      <MenuItem Header="Delete" Command="{Binding DeleteCommand}" />
    </ContextMenu>
  </Button.ContextMenu>
</Button>
```

Programmatic open with explicit target:

```csharp
using Avalonia.Controls;

void ShowMenu(Control target, ContextMenu menu)
{
    if (!menu.IsOpen)
        menu.Open(target);
}
```

Lifecycle signals:
- `Opening` allows canceling before opening,
- `Closing` allows canceling close,
- `Opened` and `Closed` come from `MenuBase` routed events.

## `MenuFlyout` and `ContextFlyout` Patterns

Use a menu flyout for context-style actions without directly attaching `ContextMenu`:

```xml
<Button xmlns="https://github.com/avaloniaui"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        Content="More">
  <Button.ContextFlyout>
    <MenuFlyout>
      <MenuItem Header="Refresh" Command="{Binding RefreshCommand}" />
      <MenuItem Header="Duplicate" Command="{Binding DuplicateCommand}" />
      <Separator />
      <MenuItem Header="Archive" Command="{Binding ArchiveCommand}" />
    </MenuFlyout>
  </Button.ContextFlyout>
</Button>
```

Key behaviors:
- `MenuFlyout` creates a `MenuFlyoutPresenter` inside popup host.
- presenter theme customization is available via `FlyoutPresenterTheme` and `FlyoutPresenterClasses`.

## Dynamic Menu Construction in C#

```csharp
using Avalonia.Controls;
using Avalonia.Input;

Menu BuildMainMenu(MainWindowViewModel vm)
{
    var file = new MenuItem { Header = "_File" };

    file.Items.Add(new MenuItem
    {
        Header = "_Open",
        Command = vm.OpenCommand,
        InputGesture = KeyGesture.Parse("Ctrl+O")
    });

    file.Items.Add(new MenuItem
    {
        Header = "_Save",
        Command = vm.SaveCommand,
        HotKey = KeyGesture.Parse("Ctrl+S"),
        InputGesture = KeyGesture.Parse("Ctrl+S")
    });

    file.Items.Add(new Separator());
    file.Items.Add(new MenuItem { Header = "E_xit", Command = vm.ExitCommand });

    return new Menu { Items = { file } };
}
```

## Best Practices

- Keep command execution in viewmodels; keep menu code declarative.
- Use `InputGesture` for visible hints, but wire real execution through `HotKey` or `KeyBindings`.
- Use `ContextMenu` for target-specific operations and `Menu` for global app actions.
- Prefer `MenuFlyout` when you need flyout lifecycle/placement behavior with menu semantics.
- Avoid duplicated shortcut registration on nested scopes to prevent double execution.

## Troubleshooting

1. Menu item shows shortcut text but pressing keys does nothing.
- `InputGesture` is display-only; register `HotKey` or a `KeyBinding`.

2. Context menu opens on wrong target.
- Ensure `Open(control)` uses an attached control and check `PlacementTarget` overrides.

3. Radio menu items are not mutually exclusive.
- Set `ToggleType="Radio"` and consistent `GroupName` values.

4. Submenu remains open unexpectedly.
- Check `StaysOpenOnClick` and command handlers that keep focus in popup.

5. Shortcuts execute twice.
- Remove duplicate `KeyBinding`/`HotKey` registrations across parent and child scopes.
