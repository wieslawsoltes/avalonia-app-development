# WinUI Activation (Protocol/File) and Lifecycle to Avalonia

## Table of Contents
1. Scope and APIs
2. Concept Mapping
3. Conversion Example
4. Migration Notes

## Scope and APIs

Primary WinUI APIs:

- AppInstance, AppActivationArguments, ExtendedActivationKind, protocol/file activation events

Primary Avalonia APIs:

- IClassicDesktopStyleApplicationLifetime, ControlledApplicationLifetimeStartupEventArgs, IActivatableLifetime, ProtocolActivatedEventArgs, FileActivatedEventArgs

## Concept Mapping

| WinUI idiom | Avalonia idiom |
|---|---|
| AppInstance activation event | IActivatableLifetime.Activated |
| ExtendedActivationKind.Protocol | ProtocolActivatedEventArgs |
| ExtendedActivationKind.File | FileActivatedEventArgs |
| Launch arguments at startup | Startup event + `Args` |
| App lifecycle hooks | desktop lifetime Startup/Exit/ShutdownRequested |

## Conversion Example

WinUI XAML:

```xaml
<StackPanel Spacing="6">
  <TextBlock Text="Last activation:" />
  <TextBlock Text="{x:Bind ViewModel.LastActivation, Mode=OneWay}" />
</StackPanel>
```

WinUI C#:

```csharp
AppInstance.GetCurrent().Activated += (_, e) =>
{
    switch (e.Kind)
    {
        case ExtendedActivationKind.Protocol:
            var protocol = (ProtocolActivatedEventArgs)e.Data;
            ViewModel.HandleUri(protocol.Uri);
            break;
        case ExtendedActivationKind.File:
            var files = (FileActivatedEventArgs)e.Data;
            ViewModel.HandleFiles(files.Files);
            break;
    }
};
```

Avalonia XAML:

```xaml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:DataType="vm:ActivationViewModel">
  <StackPanel Spacing="6">
    <TextBlock Text="Last activation:" />
    <TextBlock Text="{CompiledBinding LastActivation}" />
  </StackPanel>
</UserControl>
```

Avalonia C#:

```csharp
if (ApplicationLifetime is IClassicDesktopStyleApplicationLifetime desktop)
{
    desktop.Startup += (_, e) => ViewModel.HandleStartupArgs(e.Args);
}

if (Application.Current?.TryGetFeature<IActivatableLifetime>() is { } activatable)
{
    activatable.Activated += (_, e) =>
    {
        if (e is ProtocolActivatedEventArgs protocol)
            ViewModel.HandleUri(protocol.Uri);
        else if (e is FileActivatedEventArgs file)
            ViewModel.HandleFiles(file.Files);
    };
}
```

## Migration Notes

1. Keep activation parsing centralized so startup and re-activation share one code path.
2. Use typed activation event args in Avalonia instead of string-only command-line branching.
3. For desktop apps, combine startup args handling with optional `IActivatableLifetime` hooks.
