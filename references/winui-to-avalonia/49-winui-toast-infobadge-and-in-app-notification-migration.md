# WinUI Toast, InfoBadge, and In-App Notifications to Avalonia

## Table of Contents
1. Scope and APIs
2. Concept Mapping
3. Conversion Example
4. Migration Notes

## Scope and APIs

Primary WinUI APIs:

- AppNotificationManager, AppNotification, InfoBadge, InfoBar

Primary Avalonia APIs:

- WindowNotificationManager, Notification, NotificationType, in-view badge composition

## Concept Mapping

| WinUI idiom | Avalonia idiom |
|---|---|
| OS toast via AppNotificationManager | platform integration or app-level notification service |
| InfoBar inline surface | banner-like Border + styles or notification card |
| InfoBadge control | lightweight badge composition in XAML |
| notification severity | NotificationType (`Information`, `Success`, `Warning`, `Error`) |

## Conversion Example

WinUI XAML:

```xaml
<StackPanel Spacing="8">
  <InfoBadge Value="3" />
  <InfoBar IsOpen="True" Severity="Warning" Title="Unsaved changes" />
</StackPanel>
```

WinUI C#:

```csharp
var appNotification = new AppNotification("<toast><visual><binding template='ToastGeneric'><text>Build complete</text></binding></visual></toast>");
AppNotificationManager.Default.Show(appNotification);
```

Avalonia XAML:

```xaml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:DataType="vm:NotificationsViewModel">
  <StackPanel Spacing="8">
    <Border Classes="badge" MinWidth="20" Padding="6,2">
      <TextBlock Text="{CompiledBinding UnreadCount}" HorizontalAlignment="Center" />
    </Border>

    <Border Classes="warning-banner" IsVisible="{CompiledBinding HasWarning}" Padding="8">
      <TextBlock Text="Unsaved changes" />
    </Border>
  </StackPanel>
</UserControl>
```

Avalonia C#:

```csharp
var manager = new WindowNotificationManager(topLevel)
{
    Position = NotificationPosition.BottomRight,
    MaxItems = 4
};

manager.Show(new Notification("Build complete", "Artifacts were published.", NotificationType.Success));
```

## Migration Notes

1. Model toast and in-app notifications as separate concerns in cross-platform apps.
2. Use `WindowNotificationManager` for deterministic in-app messaging across platforms.
3. Replace InfoBadge with a styled badge component bound to count/state.
