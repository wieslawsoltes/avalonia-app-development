# Tray Icons and System Tray Integration

## Table of Contents
1. Scope and APIs
2. Platform and Lifecycle Model
3. XAML Pattern in `Application`
4. C# Pattern for Runtime Control
5. Native Menu Integration for Tray Icons
6. Platform-Specific Notes
7. Best Practices
8. Troubleshooting

## Scope and APIs

Primary APIs:
- `TrayIcon`
- `TrayIcons`
- `TrayIcon.IconsProperty` (attached on `Application`)
- `TrayIcon.ToolTipTextProperty`
- `TrayIcon.IsVisibleProperty`
- `TrayIcon.Icon`
- `TrayIcon.ToolTipText`
- `TrayIcon.IsVisible`
- `TrayIcon.Menu`
- `TrayIcon.Command`, `TrayIcon.CommandParameter`, `TrayIcon.Clicked`
- `TrayIcon.NativeMenuExporter`
- `MacOSProperties.IsTemplateIcon`
- `MacOSProperties.IsTemplateIconProperty`
- `MacOSProperties.SetIsTemplateIcon(...)`, `MacOSProperties.GetIsTemplateIcon(...)`
- `INativeMenuExporter`
- `ITrayIconWithIsTemplateImpl`

Related menu/platform APIs:
- `NativeMenu`
- `NativeMenuItem`
- `NativeMenuItemSeparator`
- `INativeMenuExporterProvider`
- `PlatformManager.CreateTrayIcon()` (platform factory; do not call from normal app code)

Reference source files:
- `src/Avalonia.Controls/TrayIcon.cs`
- `src/Avalonia.Controls/Platform/MacOSProperties.cs`
- `src/Avalonia.Controls/Platform/ITopLevelNativeMenuExporter.cs`
- `src/Avalonia.Controls/Platform/ITrayIconImpl.cs`

## Platform and Lifecycle Model

Key behavior:
- tray icons are declared on the `Application` via attached property `TrayIcon.Icons`.
- each `TrayIcon` binds to a platform tray implementation.
- on app shutdown, Avalonia disposes tray icons so they are removed from the system tray.

Important detail:
- `TrayIcon.Clicked` is platform-dependent; the source comment notes this event is not raised on macOS.
- menu support is provided through `NativeMenu` attached to `TrayIcon.Menu`.

## XAML Pattern in `Application`

Declare tray icons directly in `App.axaml`:

```xml
<Application xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp"
             x:Class="MyApp.App"
             x:DataType="vm:App">
  <Application.Styles>
    <FluentTheme />
  </Application.Styles>

  <TrayIcon.Icons>
    <TrayIcons>
      <TrayIcon Icon="/Assets/app.ico"
                ToolTipText="MyApp"
                Command="{Binding ActivateFromTrayCommand}"
                CommandParameter="open-main-window"
                MacOSProperties.IsTemplateIcon="True">
        <TrayIcon.Menu>
          <NativeMenu>
            <NativeMenuItem Header="Open" Command="{Binding OpenCommand}" />
            <NativeMenuItem Header="Pause Sync"
                            ToggleType="CheckBox"
                            IsChecked="{Binding IsSyncPaused}" />
            <NativeMenuItemSeparator />
            <NativeMenuItem Header="Exit" Command="{Binding ExitCommand}" />
          </NativeMenu>
        </TrayIcon.Menu>
      </TrayIcon>
    </TrayIcons>
  </TrayIcon.Icons>
</Application>
```

Notes:
- `Icon` uses `WindowIcon` conversion from resource URI/file.
- `MacOSProperties.IsTemplateIcon` is useful for monochrome template icons in macOS menu bar.

## C# Pattern for Runtime Control

```csharp
using System.Linq;
using Avalonia;
using Avalonia.Controls;

public static class TrayIconHelpers
{
    public static TrayIcon? GetPrimaryTrayIcon()
    {
        var app = Application.Current;
        if (app is null)
            return null;

        return TrayIcon.GetIcons(app)?.FirstOrDefault();
    }

    public static void ToggleTrayIconVisibility()
    {
        var icon = GetPrimaryTrayIcon();
        if (icon is null)
            return;

        icon.IsVisible = !icon.IsVisible;
    }

    public static void UpdateTooltip(string text)
    {
        var icon = GetPrimaryTrayIcon();
        if (icon is null)
            return;

        icon.ToolTipText = text;
    }
}
```

Manual creation (code-only):

```csharp
using Avalonia;
using Avalonia.Controls;

var tray = new TrayIcon
{
    Icon = new WindowIcon("Assets/app.ico"),
    ToolTipText = "MyApp",
    IsVisible = true,
    Menu = new NativeMenu
    {
        new NativeMenuItem("Open") { Command = viewModel.OpenCommand },
        new NativeMenuItemSeparator(),
        new NativeMenuItem("Exit") { Command = viewModel.ExitCommand }
    }
};

var icons = new TrayIcons { tray };
TrayIcon.SetIcons(Application.Current!, icons);
```

## Native Menu Integration for Tray Icons

`TrayIcon.Menu` uses `NativeMenu` APIs:
- checkbox/radio menu items (`ToggleType`, `IsChecked`),
- command-based actions (`Command`, `CommandParameter`),
- visibility/enabled state (`IsVisible`, `IsEnabled`).

For dynamic tray menus, update menu items in response to state changes before user interaction, similar to native menu guidance in:
- [`54-native-menu-and-native-menubar-integration.md`](54-native-menu-and-native-menubar-integration)

## Platform-Specific Notes

- macOS:
  - prefer template/monochrome icon assets and set `MacOSProperties.IsTemplateIcon="True"` when needed.
  - `Clicked` event may not be raised; rely on menu commands.
- Linux:
  - tray behavior depends on desktop environment and status notifier support.
- Windows:
  - click and context menu behavior is generally available.

## Best Practices

- Declare tray icons at `Application` scope, not per-window.
- Keep tray commands idempotent (open window, toggle feature, exit).
- Use `NativeMenu` for predictable cross-platform tray menus.
- Prefer command binding over direct click handlers for testability.
- Keep tooltip text short; long text truncation is platform-specific.

## Troubleshooting

1. Tray icon does not appear.
- Ensure `TrayIcon.Icons` is set on `Application` (not `Window`).
- Verify the icon asset path is valid and loadable.

2. Tray click does nothing on macOS.
- Expected on macOS for `Clicked`; use tray menu commands instead.

3. Tray menu not shown.
- Ensure `TrayIcon.Menu` is a `NativeMenu` with items.

4. Icon remains in tray after app closes.
- Verify app shutdown is graceful and no external process holds the tray icon.

5. Runtime icon update has no visible effect.
- Replace `Icon` with a valid `WindowIcon` and confirm platform icon format support.
