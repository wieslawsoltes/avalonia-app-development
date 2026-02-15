# Architecture and Lifetime Patterns

## Goals

- Keep startup deterministic and debuggable.
- Keep lifetime transitions explicit (`Startup`, activation, shutdown, exit).
- Keep platform-specific bootstrapping isolated from app composition.

## Recommended Project Shape

- `Program.cs`: `BuildAvaloniaApp`, platform bootstrap, and app start method.
- `App.axaml` + `App.axaml.cs`: global resources/themes and root assignment.
- `Views/`: `Window` / `UserControl` definitions.
- `ViewModels/`: app state, commands, async workflows.
- `Services/`: I/O, storage, launcher, domain services.

## Startup Baseline

```csharp
using System;
using Avalonia;
using Avalonia.Controls.ApplicationLifetimes;

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

## `AppBuilder` Orchestration Surface

High-value app startup APIs:

- `Configure<TApp>()`, `Configure<TApp>(Func<TApp> appFactory)`
- `UseWindowingSubsystem(...)`, `UseRenderingSubsystem(...)`, `UseRuntimePlatformSubsystem(...)`, `UseStandardRuntimePlatformSubsystem()`
- `With<T>(T options)`, `With<T>(Func<T> options)`
- `ConfigureFonts(...)`
- `AfterSetup(...)`, `AfterApplicationSetup(...)`, `AfterPlatformServicesSetup(...)`
- `SetupWithoutStarting()`, `SetupWithLifetime(...)`, `Start(AppMainDelegate, args)`
- `AppMainDelegate`

Useful diagnostics/introspection properties while composing startup:

- `Instance`, `ApplicationType`
- `WindowingSubsystemInitializer`, `WindowingSubsystemName`
- `RenderingSubsystemInitializer`, `RenderingSubsystemName`
- `RuntimePlatformServicesInitializer`, `RuntimePlatformServicesName`
- `AfterSetupCallback`, `AfterPlatformServicesSetupCallback`
- `LifetimeOverride`

Example:

```csharp
public static AppBuilder BuildAvaloniaApp()
    => AppBuilder.Configure<App>(() => new App())
        .UsePlatformDetect()
        .AfterPlatformServicesSetup(builder =>
        {
            // Platform services are registered here.
            _ = builder.RuntimePlatformServicesName;
        })
        .AfterSetup(builder =>
        {
            // Application instance exists here.
            _ = builder.Instance;
        });
```

## `Application` Lifecycle Surface

App-level events and collections often needed in production apps:

- `Application.ResourcesChanged`
- `Application.ActualThemeVariantChanged`
- `Application.UrlsOpened` (obsolete compatibility event for URL activation flows)
- `Application.DataTemplates`
- `Application.DataContextProperty`
- `Application.NameProperty`
- `Application.Name`

Pattern:

```csharp
public override void OnFrameworkInitializationCompleted()
{
    ResourcesChanged += (_, _) => { };
    ActualThemeVariantChanged += (_, _) => { };
    UrlsOpened += (_, e) =>
    {
        // Compatibility path; prefer IActivatableLifetime for new code.
        _navigation.OpenUrls(e.Urls);
    };

    _ = DataTemplates;
    base.OnFrameworkInitializationCompleted();
}
```

`Application` identity and root data context are explicit property-system entries:

- `DataContextProperty` (styled property owner on `Application`)
- `NameProperty` (direct property)
- `Name` (CLR wrapper)

Example:

```csharp
public override void Initialize()
{
    // Set root application identity and default binding context intentionally.
    Name = "MyApp";
    DataContext = _rootShellState;
}
```

## Lifetime Selection and Activation

Main lifetime choices:

- `IClassicDesktopStyleApplicationLifetime` for multi-window desktop apps.
- `ISingleViewApplicationLifetime` for single-root hosts.
- `IActivatableLifetime` for activation/deactivation flow.
- `ISingleTopLevelApplicationLifetime` when the host has exactly one `TopLevel`.

Compatibility note:
- `IActivatableApplicationLifetime` exists as an obsolete compatibility interface and has no effect in `11.3.12`; use `Application.Current.TryGetFeature<IActivatableLifetime>()`.

Related public activation types:

- `ActivatableLifetimeBase`
- `ActivatedEventArgs` (`Kind` as `ActivationKind`)
- `ProtocolActivatedEventArgs` (`Uri`)
- `FileActivatedEventArgs` (`Files`)

Pattern:

```csharp
if (ApplicationLifetime is IActivatableLifetime activatable)
{
    activatable.Activated += (_, e) =>
    {
        if (e is ProtocolActivatedEventArgs p)
            _navigation.OpenUri(p.Uri);
        else if (e is FileActivatedEventArgs f)
            _navigation.OpenFiles(f.Files);
    };
}
```

## Desktop Lifetime Operational APIs

Desktop-specific useful APIs:

- `ClassicDesktopStyleApplicationLifetime.Args`
- `ClassicDesktopStyleApplicationLifetime.ShutdownMode`
- `ClassicDesktopStyleApplicationLifetime.ShutdownRequested`
- `ClassicDesktopStyleApplicationLifetime.Startup`
- `ClassicDesktopStyleApplicationLifetime.Exit`
- `ClassicDesktopStyleApplicationLifetimeOptions.ProcessUrlActivationCommandLine`
- `ClassicDesktopStyleApplicationLifetimeExtensions`

Event arg types used by controlled lifetime:

- `ControlledApplicationLifetimeStartupEventArgs` (`Args`)
- `ShutdownRequestedEventArgs` (`Cancel`)
- `ControlledApplicationLifetimeExitEventArgs` (`ApplicationExitCode`)

Pattern:

```csharp
if (ApplicationLifetime is IClassicDesktopStyleApplicationLifetime desktop)
{
    desktop.Startup += (_, e) =>
    {
        string[] args = e.Args;
        _ = args.Length;
    };

    desktop.ShutdownRequested += (_, e) =>
    {
        e.Cancel = !CanCloseSafely();
    };

    desktop.Exit += (_, e) =>
    {
        e.ApplicationExitCode = 0;
    };
}
```

Additional desktop startup helpers:

- `DesktopApplicationExtensions.RunWithMainWindow<TWindow>()`
- `AppBuilderDesktopExtensions`

## Root Assignment Baseline

```csharp
using Avalonia.Controls;
using Avalonia.Controls.ApplicationLifetimes;
using Avalonia.Markup.Xaml;

public class App : Application
{
    public override void Initialize() => AvaloniaXamlLoader.Load(this);

    public override void OnFrameworkInitializationCompleted()
    {
        if (ApplicationLifetime is IClassicDesktopStyleApplicationLifetime desktop)
        {
            desktop.MainWindow = new MainWindow
            {
                DataContext = new MainWindowViewModel()
            };
        }
        else if (ApplicationLifetime is ISingleViewApplicationLifetime singleView)
        {
            singleView.MainView = new MainView
            {
                DataContext = new MainViewModel()
            };
        }

        base.OnFrameworkInitializationCompleted();
    }
}
```

## Common Architecture Mistakes

1. Mixing business logic into `Program.cs`.
- Fix: keep `Program.cs` focused on `AppBuilder` composition.

2. Assigning `MainWindow`/`MainView` outside `OnFrameworkInitializationCompleted()`.
- Fix: assign roots only after lifetime is established.

3. Shutdown logic spread across views/viewmodels.
- Fix: route lifecycle shutdown through one app-level service/lifetime adapter.

4. Using startup callback hooks without clear ownership.
- Fix: keep `AfterSetup`/`AfterPlatformServicesSetup` callbacks minimal and deterministic.
