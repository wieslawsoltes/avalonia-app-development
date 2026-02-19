# WinUI TitleBar/SystemBackdrop and Custom Chrome to Avalonia

## Table of Contents
1. Scope and APIs
2. Concept Mapping
3. Conversion Example
4. Migration Notes

## Scope and APIs

Primary WinUI APIs:

- AppWindow, AppWindowTitleBar, ExtendsContentIntoTitleBar, SetTitleBar, MicaBackdrop/DesktopAcrylicBackdrop

Primary Avalonia APIs:

- Window ExtendClientArea* properties, SystemDecorations, WindowTransparencyLevel, WindowTransparencyLevelCollection, BeginMoveDrag

## Concept Mapping

| WinUI idiom | Avalonia idiom |
|---|---|
| ExtendsContentIntoTitleBar + SetTitleBar | ExtendClientAreaToDecorationsHint + custom title region |
| AppWindow.TitleBar color tuning | style/theme resources for title surface |
| SystemBackdrop (Mica/Acrylic) | TransparencyLevelHint (`Mica`, `AcrylicBlur`, `Blur`) |
| non-client drag handling | BeginMoveDrag / BeginResizeDrag |

## Conversion Example

WinUI XAML:

```xaml
<Grid>
  <Grid x:Name="AppTitleBar" Height="36">
    <TextBlock Text="MyApp" VerticalAlignment="Center" Margin="12,0" />
  </Grid>
  <ContentPresenter Margin="0,36,0,0" />
</Grid>
```

WinUI C#:

```csharp
ExtendsContentIntoTitleBar = true;
SetTitleBar(AppTitleBar);
SystemBackdrop = new MicaBackdrop();
AppWindow.Title = "MyApp";
```

Avalonia XAML:

```xaml
<Window xmlns="https://github.com/avaloniaui"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        ExtendClientAreaToDecorationsHint="True"
        ExtendClientAreaChromeHints="PreferSystemChrome"
        ExtendClientAreaTitleBarHeightHint="36"
        SystemDecorations="Full">
  <Grid RowDefinitions="36,*">
    <Border Grid.Row="0" Background="{DynamicResource ThemeControlMidBrush}" PointerPressed="OnTitleBarPressed">
      <TextBlock Text="MyApp" VerticalAlignment="Center" Margin="12,0" />
    </Border>
    <ContentPresenter Grid.Row="1" />
  </Grid>
</Window>
```

Avalonia C#:

```csharp
TransparencyLevelHint = new WindowTransparencyLevelCollection(new[]
{
    WindowTransparencyLevel.Mica,
    WindowTransparencyLevel.AcrylicBlur,
    WindowTransparencyLevel.Blur,
    WindowTransparencyLevel.None
});

private void OnTitleBarPressed(object? sender, PointerPressedEventArgs e)
{
    if (e.GetCurrentPoint(this).Properties.IsLeftButtonPressed)
        BeginMoveDrag(e);
}
```

## Migration Notes

1. Keep title bar hit-testing and drag behavior explicit in custom chrome.
2. Provide fallback transparency levels for platforms without Mica/Acrylic support.
3. Separate visual chrome composition from window lifecycle/service logic.
