# WinUI WebView2 Navigation/Permissions and Host Interop to Avalonia

## Table of Contents
1. Scope and APIs
2. Concept Mapping
3. Conversion Example
4. Migration Notes

## Scope and APIs

Primary WinUI APIs:

- WebView2, CoreWebView2, NavigationStarting, NavigationCompleted, permission and host-object wiring

Primary Avalonia APIs:

- NativeControlHost interop boundary, optional external WebView packages, launcher fallback for external browser

## Concept Mapping

| WinUI idiom | Avalonia idiom |
|---|---|
| built-in WebView2 control | package-backed web control or native host wrapper |
| CoreWebView2 permission hooks | wrapper/service abstractions per platform engine |
| host object/script bridge | explicit interop API in host wrapper |
| in-app web view fallback | launcher external-browser fallback |

## Conversion Example

WinUI XAML:

```xaml
<WebView2 x:Name="Browser" Source="https://example.com" />
```

WinUI C#:

```csharp
Browser.NavigationStarting += (_, e) =>
{
    if (!IsAllowed(e.Uri))
        e.Cancel = true;
};

await Browser.EnsureCoreWebView2Async();
Browser.CoreWebView2.Settings.IsScriptEnabled = true;
```

Avalonia XAML:

```xaml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:local="using:MyApp.Controls">
  <local:BrowserHost Url="{Binding Url}" />
</UserControl>
```

Avalonia C#:

```csharp
public sealed class BrowserHost : NativeControlHost
{
    public Uri? Url { get; set; }

    public Task OpenExternallyAsync(Control anchor)
    {
        TopLevel? top = TopLevel.GetTopLevel(anchor);
        return top is null || Url is null
            ? Task.CompletedTask
            : top.Launcher.LaunchUriAsync(Url);
    }
}
```

## Migration Notes

1. Treat embedded web as an interop boundary, not a core cross-platform control guarantee.
2. Abstract navigation/permission policy behind an app service to avoid vendor lock-in.
3. Provide external-browser fallback when embedded engine is unavailable.
