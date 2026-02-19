# WinUI MenuBar and Tray Patterns to Avalonia NativeMenu/TrayIcon

## Table of Contents
1. Scope and APIs
2. Concept Mapping
3. Conversion Example
4. Migration Notes

## Scope and APIs

Primary WinUI APIs:

- MenuBar, MenuBarItem, MenuFlyoutItem, keyboard accelerators, tray via Win32 interop patterns

Primary Avalonia APIs:

- NativeMenu, NativeMenuItem, NativeMenuBar, TrayIcon, TrayIcons

## Concept Mapping

| WinUI idiom | Avalonia idiom |
|---|---|
| MenuBar in visual tree | NativeMenuBar fallback surface |
| Command MenuFlyoutItem | NativeMenuItem with Command |
| Top-level native menu export | NativeMenu attached to Window |
| App tray integration via native interop | TrayIcon/TrayIcons on Application |

## Conversion Example

WinUI XAML:

```xaml
<MenuBar>
  <MenuBarItem Title="File">
    <MenuFlyoutItem Text="Open" Command="{x:Bind ViewModel.OpenCommand}" />
    <MenuFlyoutItem Text="Exit" Command="{x:Bind ViewModel.ExitCommand}" />
  </MenuBarItem>
</MenuBar>
```

WinUI C#:

```csharp
var bar = new MenuBar();
var file = new MenuBarItem { Title = "File" };
file.Items.Add(new MenuFlyoutItem { Text = "Open", Command = ViewModel.OpenCommand });
bar.Items.Add(file);
```

Avalonia XAML:

```xaml
<Window xmlns="https://github.com/avaloniaui"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml">
  <NativeMenu.Menu>
    <NativeMenu>
      <NativeMenuItem Header="_File">
        <NativeMenuItem.Menu>
          <NativeMenu>
            <NativeMenuItem Header="_Open" Command="{Binding OpenCommand}" />
            <NativeMenuItem Header="E_xit" Command="{Binding ExitCommand}" />
          </NativeMenu>
        </NativeMenuItem.Menu>
      </NativeMenuItem>
    </NativeMenu>
  </NativeMenu.Menu>

  <DockPanel>
    <NativeMenuBar DockPanel.Dock="Top" />
    <ContentPresenter />
  </DockPanel>
</Window>
```

Avalonia C#:

```csharp
NativeMenu.SetMenu(window, new NativeMenu
{
    new NativeMenuItem("_File")
    {
        Menu = new NativeMenu
        {
            new NativeMenuItem("_Open") { Command = viewModel.OpenCommand },
            new NativeMenuItem("E_xit") { Command = viewModel.ExitCommand }
        }
    }
});

TrayIcon.SetIcons(Application.Current!, new TrayIcons
{
    new TrayIcon
    {
        Icon = new WindowIcon("Assets/app.ico"),
        ToolTipText = "MyApp",
        Menu = new NativeMenu { new NativeMenuItem("E_xit") { Command = viewModel.ExitCommand } }
    }
});
```

## Migration Notes

1. Use one `NativeMenu` model and let `NativeMenuBar` be fallback when native export is unavailable.
2. Keep menu state/visibility command-driven instead of imperative click-only handlers.
3. Use `TrayIcon` APIs for cross-platform tray behavior; avoid ad-hoc per-OS glue in app logic.
