# WinUI RefreshContainer and Pull-to-Refresh to Avalonia

## Table of Contents
1. Scope and APIs
2. Concept Mapping
3. Conversion Example
4. Migration Notes

## Scope and APIs

Primary WinUI APIs:

- RefreshContainer, RefreshVisualizer, RefreshRequested, deferral completion

Primary Avalonia APIs:

- RefreshContainer, RefreshVisualizer, RefreshRequested, RefreshRequestedEventArgs.GetDeferral

## Concept Mapping

| WinUI idiom | Avalonia idiom |
|---|---|
| RefreshContainer + RefreshVisualizer | RefreshContainer + RefreshVisualizer |
| RefreshRequested event | RefreshRequested event |
| GetDeferral/Complete async refresh | GetDeferral/Complete async refresh |
| request refresh programmatically | RequestRefresh() |

## Conversion Example

WinUI XAML:

```xaml
<RefreshContainer RefreshRequested="OnRefreshRequested">
  <ListView ItemsSource="{x:Bind ViewModel.Items}" />
</RefreshContainer>
```

WinUI C#:

```csharp
private async void OnRefreshRequested(RefreshContainer sender, RefreshRequestedEventArgs args)
{
    var deferral = args.GetDeferral();
    try
    {
        await ViewModel.ReloadAsync();
    }
    finally
    {
        deferral.Complete();
    }
}
```

Avalonia XAML:

```xaml
<RefreshContainer xmlns="https://github.com/avaloniaui"
                  xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
                  RefreshRequested="OnRefreshRequested">
  <ListBox ItemsSource="{Binding Items}" />
</RefreshContainer>
```

Avalonia C#:

```csharp
private async void OnRefreshRequested(object? sender, RefreshRequestedEventArgs e)
{
    var deferral = e.GetDeferral();
    try
    {
        await ViewModel.ReloadAsync();
    }
    finally
    {
        deferral.Complete();
    }
}
```

## Migration Notes

1. Keep refresh handlers async and always complete the deferral.
2. Prefer one refresh pipeline shared by gesture and explicit reload commands.
3. Use `RequestRefresh()` for deterministic test or retry flows.
