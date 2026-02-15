# Native Menu and NativeMenuBar Integration

## Table of Contents
1. Scope and APIs
2. Export Model and Platform Behavior
3. XAML Pattern: Shared Menu + Native Fallback Bar
4. C# Pattern: Build and Attach Native Menus
5. Dynamic Updates (`NeedsUpdate`) and Command State
6. `NativeMenuBar` Behavior and Visibility
7. Best Practices
8. Troubleshooting

## Scope and APIs

Primary APIs:
- `NativeMenu`
- `NativeMenuItemBase`
- `NativeMenuItem`
- `NativeMenuItemSeparator`
- `NativeMenuBar`
- `INativeMenuExporter`

Attached properties and helpers:
- `NativeMenu.MenuProperty`
- `NativeMenu.SetMenu(...)`
- `NativeMenu.GetMenu(...)`
- `NativeMenu.IsNativeMenuExportedProperty`
- `NativeMenu.GetIsNativeMenuExported(...)`

Important members:
- `NativeMenu.Items`, `NeedsUpdate`, `Opening`, `Closed`
- `NativeMenuItem.Header`, `Menu`, `Command`, `CommandParameter`
- `NativeMenuItem.Gesture`, `ToggleType`, `IsChecked`, `IsEnabled`, `IsVisible`
- `NativeMenuItem.Icon`, `ToolTip`, `Click`

Reference source files:
- `src/Avalonia.Controls/NativeMenu.cs`
- `src/Avalonia.Controls/NativeMenu.Export.cs`
- `src/Avalonia.Controls/NativeMenuItemBase.cs`
- `src/Avalonia.Controls/NativeMenuItem.cs`
- `src/Avalonia.Controls/NativeMenuItemSeparator.cs`
- `src/Avalonia.Controls/NativeMenuBar.cs`

## Export Model and Platform Behavior

Avalonia native menu integration works through `NativeMenu.MenuProperty` attached to a `TopLevel` (`Window` and other top-level hosts).

High-level flow:
1. You attach a `NativeMenu` to a top-level.
2. Platform exporter decides whether to export to real OS-native menu.
3. `NativeMenu.IsNativeMenuExportedProperty` reflects exporter state.

Important constraint:
- `IsNativeMenuExportedProperty` is effectively read-only for app code. Do not set it directly.

## XAML Pattern: Shared Menu + Native Fallback Bar

Use one `NativeMenu` model and show `NativeMenuBar` for platforms where native export is unavailable.

```xml
<Window xmlns="https://github.com/avaloniaui"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        xmlns:vm="using:MyApp.ViewModels"
        x:DataType="vm:MainWindowViewModel">
  <NativeMenu.Menu>
    <NativeMenu>
      <NativeMenuItem Header="_File">
        <NativeMenuItem.Menu>
          <NativeMenu>
            <NativeMenuItem Header="_Open" Command="{Binding OpenCommand}" Gesture="Ctrl+O" />
            <NativeMenuItem Header="_Save" Command="{Binding SaveCommand}" Gesture="Ctrl+S" />
            <NativeMenuItemSeparator />
            <NativeMenuItem Header="E_xit" Command="{Binding ExitCommand}" />
          </NativeMenu>
        </NativeMenuItem.Menu>
      </NativeMenuItem>

      <NativeMenuItem Header="_View">
        <NativeMenuItem.Menu>
          <NativeMenu>
            <NativeMenuItem Header="Show _Grid"
                            ToggleType="CheckBox"
                            IsChecked="{Binding ShowGrid}" />
          </NativeMenu>
        </NativeMenuItem.Menu>
      </NativeMenuItem>
    </NativeMenu>
  </NativeMenu.Menu>

  <DockPanel>
    <NativeMenuBar DockPanel.Dock="Top" />
    <ContentPresenter Content="{Binding MainContent}" />
  </DockPanel>
</Window>
```

`NativeMenuBar` binds itself to `NativeMenu.Menu` and hides automatically when native export is active.

## C# Pattern: Build and Attach Native Menus

```csharp
using Avalonia.Controls;
using Avalonia.Input;

static NativeMenu BuildNativeMenu(MainWindowViewModel vm)
{
    var fileMenu = new NativeMenuItem("_File") { Menu = new NativeMenu() };

    fileMenu.Menu!.Add(new NativeMenuItem("_Open")
    {
        Command = vm.OpenCommand,
        Gesture = KeyGesture.Parse("Ctrl+O")
    });

    fileMenu.Menu.Add(new NativeMenuItem("_Save")
    {
        Command = vm.SaveCommand,
        Gesture = KeyGesture.Parse("Ctrl+S")
    });

    fileMenu.Menu.Add(new NativeMenuItemSeparator());
    fileMenu.Menu.Add(new NativeMenuItem("E_xit") { Command = vm.ExitCommand });

    return new NativeMenu { fileMenu };
}

static void AttachNativeMenu(Window window, MainWindowViewModel vm)
{
    var menu = BuildNativeMenu(vm);
    NativeMenu.SetMenu(window, menu);
}
```

## Dynamic Updates (`NeedsUpdate`) and Command State

`NeedsUpdate` is the preferred hook for changing menu structure/state before display or hotkey dispatch.

```csharp
void WireDynamicState(NativeMenu menu, MainWindowViewModel vm)
{
    menu.NeedsUpdate += (_, _) =>
    {
        // Keep updates here instead of Opening/Closed.
        vm.RefreshRecentFilesMenu();
    };
}
```

`NativeMenuItem` command-state behavior:
- subscribes to `ICommand.CanExecuteChanged`,
- updates `IsEnabled` on UI thread,
- executes `Command` when clicked (if `CanExecute` is true).

## `NativeMenuBar` Behavior and Visibility

`NativeMenuBar` is a `TemplatedControl` that:
- reads the current top-level `NativeMenu.Menu`,
- presents it through an internal `MenuBase` presenter,
- binds presenter visibility to `!NativeMenu.IsNativeMenuExported`.

Practical meaning:
- exported native menu available: OS-native surface is used, in-window bar hides,
- no exporter/support: in-window bar shows with same menu model.

## Best Practices

- Treat `NativeMenu` as the single source of truth for app menu structure.
- Include a `NativeMenuBar` in desktop shells for non-exported fallback behavior.
- Use `NeedsUpdate` for dynamic menu population; avoid structure mutation in `Opening`/`Closed`.
- Prefer `Command` on `NativeMenuItem`; use `Click` only for small glue logic.
- Expect platform variation for icon, tooltip, and gesture rendering.

## Troubleshooting

1. Native menu does not appear on a platform.
- Check `NativeMenu.GetIsNativeMenuExported(topLevel)` at runtime.
- Confirm the platform backend exposes an `ITopLevelNativeMenuExporter`.

2. `NativeMenuBar` never shows.
- Verify it is part of visual tree for the same `TopLevel` where `NativeMenu.Menu` is set.

3. Dynamic entries are stale.
- Move update logic from `Opening`/`Closed` into `NeedsUpdate`.

4. Shortcut text or behavior differs per OS.
- Native exporters map gestures to platform conventions; rendering is backend-dependent.

5. Parenting exceptions when reusing menu nodes.
- A `NativeMenu` and its `NativeMenuItemBase` children can have only one parent at a time.
