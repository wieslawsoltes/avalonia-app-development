# End-to-End Examples

## Example 1: Desktop App with Compiled Bindings

### `Program.cs`

```csharp
using System;
using Avalonia;

internal static class Program
{
    [STAThread]
    public static int Main(string[] args)
        => BuildAvaloniaApp().StartWithClassicDesktopLifetime(args);

    public static AppBuilder BuildAvaloniaApp()
        => AppBuilder.Configure<App>()
            .UsePlatformDetect();
}
```

### `App.axaml`

```xml
<Application xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             x:Class="MyApp.App"
             RequestedThemeVariant="Default">
  <Application.Styles>
    <FluentTheme />
  </Application.Styles>
</Application>
```

### `App.axaml.cs`

```csharp
using Avalonia;
using Avalonia.Controls.ApplicationLifetimes;
using Avalonia.Markup.Xaml;

public class App : Application
{
    public override void Initialize() => AvaloniaXamlLoader.Load(this);

    public override void OnFrameworkInitializationCompleted()
    {
        if (ApplicationLifetime is IClassicDesktopStyleApplicationLifetime desktop)
            desktop.MainWindow = new MainWindow { DataContext = new MainWindowViewModel() };

        base.OnFrameworkInitializationCompleted();
    }
}
```

### `MainWindow.axaml`

```xml
<Window xmlns="https://github.com/avaloniaui"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        xmlns:vm="using:MyApp"
        x:Class="MyApp.MainWindow"
        x:DataType="vm:MainWindowViewModel"
        Width="600" Height="320">
  <StackPanel Margin="16" Spacing="8">
    <TextBox Text="{CompiledBinding Query, Mode=TwoWay}" />
    <Button Content="Run" Command="{CompiledBinding RunCommand}" />
    <TextBlock Text="{CompiledBinding Status}" />
  </StackPanel>
</Window>
```

## Example 2: Browser App Startup

```csharp
using System.Threading.Tasks;
using Avalonia.Browser;

internal static class Program
{
    public static async Task Main(string[] args)
    {
        await App.BuildAvaloniaApp()
            .StartBrowserAppAsync("out", new BrowserPlatformOptions
            {
                RenderingMode = new[]
                {
                    BrowserRenderingMode.WebGL2,
                    BrowserRenderingMode.WebGL1,
                    BrowserRenderingMode.Software2D
                }
            });
    }
}
```

## Example 3: UI-Thread Safe Async Update

```csharp
using Avalonia.Threading;

public async Task LoadAsync()
{
    var rows = await _service.FetchRowsAsync();

    await Dispatcher.UIThread.InvokeAsync(() =>
    {
        Items.Clear();
        foreach (var row in rows)
            Items.Add(row);
    });
}
```

## Example 4: Theme Variant Scope

```xml
<ThemeVariantScope RequestedThemeVariant="Dark">
  <Border Padding="12">
    <TextBlock Text="This subtree forces dark theme." />
  </Border>
</ThemeVariantScope>
```

## Example 5: C# Observable Binding

```csharp
IDisposable sub = textBlock.Bind(
    TextBlock.TextProperty,
    viewModel.ClockTextObservable);
```

## Example 6: Platform Options via `With<TOptions>`

```csharp
public static AppBuilder BuildAvaloniaApp()
    => AppBuilder.Configure<App>()
        .UsePlatformDetect()
        .With(new Win32PlatformOptions
        {
            RenderingMode = new[]
            {
                Win32RenderingMode.AngleEgl,
                Win32RenderingMode.Software
            }
        });
```

## XAML-First and Code-Only Usage

Default mode:
- Build screens and themes in XAML first.
- Use code-only UI only when explicitly requested.

XAML-first complete baseline:

```xml
<Window xmlns="https://github.com/avaloniaui"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        xmlns:vm="using:MyApp"
        x:Class="MyApp.MainWindow"
        x:DataType="vm:MainWindowViewModel"
        Width="640" Height="360">
  <Grid RowDefinitions="Auto,*" Margin="16">
    <Button Content="Refresh" Command="{CompiledBinding RefreshCommand}" />
    <ListBox Grid.Row="1" ItemsSource="{CompiledBinding Items}" />
  </Grid>
</Window>
```

Code-only complete alternative (on request):

```csharp
using Avalonia;
using Avalonia.Controls;

public static class CodeOnlyShell
{
    public static Window Build(MainWindowViewModel vm)
    {
        var refresh = new Button { Content = "Refresh" };
        refresh.Command = vm.RefreshCommand;

        var list = new ListBox();
        list.ItemsSource = vm.Items;

        var grid = new Grid
        {
            RowDefinitions = new RowDefinitions("Auto,*"),
            Margin = new Thickness(16)
        };

        Grid.SetRow(list, 1);
        grid.Children.Add(refresh);
        grid.Children.Add(list);

        return new Window { Width = 640, Height = 360, Content = grid, DataContext = vm };
    }
}
```
