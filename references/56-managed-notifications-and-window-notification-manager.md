# Managed Notifications and WindowNotificationManager

## Table of Contents
1. Scope and APIs
2. Notification Model
3. Host-Bound Notification Manager Pattern
4. XAML-Only Notification Manager Pattern
5. C# Usage Patterns
6. Styling and Positioning
7. Best Practices
8. Troubleshooting

## Scope and APIs

Primary APIs:
- `INotification`
- `Notification`
- `INotificationManager`
- `IManagedNotificationManager`
- `WindowNotificationManager`
- `NotificationType`
- `NotificationPosition`
- `NotificationCard`

Important members:
- `WindowNotificationManager.Position`, `MaxItems`
- `WindowNotificationManager.Show(INotification)`
- `WindowNotificationManager.Show(object)`
- `WindowNotificationManager.Show(object, NotificationType, TimeSpan?, Action?, Action?, string[]?)`
- `WindowNotificationManager.Close(INotification)`, `Close(object)`, `CloseAll()`
- `Notification.Title`, `Message`, `Type`, `Expiration`, `OnClick`, `OnClose`

Reference source files:
- `src/Avalonia.Controls/Notifications/INotification.cs`
- `src/Avalonia.Controls/Notifications/INotificationManager.cs`
- `src/Avalonia.Controls/Notifications/IManagedNotificationManager.cs`
- `src/Avalonia.Controls/Notifications/Notification.cs`
- `src/Avalonia.Controls/Notifications/NotificationType.cs`
- `src/Avalonia.Controls/Notifications/NotificationPosition.cs`
- `src/Avalonia.Controls/Notifications/WindowNotificationManager.cs`
- `src/Avalonia.Controls/Notifications/NotificationCard.cs`

## Notification Model

`Notification` is the default managed model implementing `INotification`.

Core semantics:
- `Type` controls visual severity (`Information`, `Success`, `Warning`, `Error`).
- `Expiration` controls auto-close timeout.
- `Expiration == TimeSpan.Zero` means stay open until closed.
- `OnClick` and `OnClose` provide optional callbacks.

```csharp
using System;
using Avalonia.Controls.Notifications;

var notification = new Notification(
    title: "Sync complete",
    message: "42 files uploaded.",
    type: NotificationType.Success,
    expiration: TimeSpan.FromSeconds(4),
    onClick: () => OpenSyncLog(),
    onClose: () => MarkToastSeen());
```

## Host-Bound Notification Manager Pattern

This is the common app pattern: create `WindowNotificationManager` bound to current `TopLevel`.

```csharp
using Avalonia;
using Avalonia.Controls;
using Avalonia.Controls.Notifications;

public partial class DashboardView : UserControl
{
    private WindowNotificationManager? _notifications;

    protected override void OnAttachedToVisualTree(VisualTreeAttachmentEventArgs e)
    {
        base.OnAttachedToVisualTree(e);

        var topLevel = TopLevel.GetTopLevel(this);
        if (topLevel is not null)
        {
            _notifications = new WindowNotificationManager(topLevel)
            {
                Position = NotificationPosition.BottomRight,
                MaxItems = 4
            };
        }
    }

    private void NotifySaved()
    {
        _notifications?.Show(new Notification("Saved", "Preferences updated.", NotificationType.Success));
    }
}
```

Implementation detail:
- manager installs itself into `AdornerLayer` of host top-level.
- notification operations require UI thread access.

## XAML-Only Notification Manager Pattern

For local notification regions, declare a manager in view XAML and call it via command/event wiring.

```xml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:DataType="vm:NotificationsViewModel">
  <DockPanel>
    <Button DockPanel.Dock="Top"
            Content="Show Info"
            Command="{Binding #LocalNotifications.Show}">
      <Button.CommandParameter>
        <Notification Title="Info" Message="Local notification example." Type="Information" />
      </Button.CommandParameter>
    </Button>

    <Border Padding="12">
      <WindowNotificationManager x:Name="LocalNotifications"
                                 Position="TopRight"
                                 MaxItems="3" />
    </Border>
  </DockPanel>
</UserControl>
```

## C# Usage Patterns

Show arbitrary content:

```csharp
using Avalonia.Controls.Notifications;

WindowNotificationManager manager = new();
manager.Show("Simple message");
```

Show custom content with classes and callbacks:

```csharp
using System;
using Avalonia.Controls;
using Avalonia.Controls.Notifications;

manager.Show(
    content: new TextBlock { Text = "Deployment started." },
    type: NotificationType.Information,
    expiration: TimeSpan.FromSeconds(6),
    onClick: () => OpenDeployPage(),
    onClose: () => LogClosed(),
    classes: new[] { "deployment", "sticky" });
```

Close specific or all notifications:

```csharp
var n = new Notification("Warning", "Connection unstable.", NotificationType.Warning, TimeSpan.Zero);
manager.Show(n);

manager.Close(n);
manager.CloseAll();
```

## Styling and Positioning

`WindowNotificationManager.Position` controls pseudo classes:
- `:topleft`
- `:topright`
- `:bottomleft`
- `:bottomright`
- `:topcenter`
- `:bottomcenter`

`NotificationCard` provides type pseudo classes:
- `:information`
- `:success`
- `:warning`
- `:error`

Use these in custom styles/themes to align visuals with app branding.

## Best Practices

- Create one manager per top-level host/surface.
- Keep `MaxItems` conservative to avoid notification overload.
- Use `TimeSpan.Zero` only for truly actionable notifications.
- Keep notification callbacks fast; dispatch long work asynchronously.
- Prefer structured `Notification` objects for user-facing toasts.

## Troubleshooting

1. Notifications do not appear.
- Ensure manager is attached to a live `TopLevel` or present in visual tree.

2. Exception about thread access.
- Call manager APIs on UI thread.

3. Notifications vanish too quickly.
- Increase `Expiration` or set `TimeSpan.Zero` for sticky notifications.

4. Too many stacked notifications.
- Reduce produce rate and set lower `MaxItems`.

5. `Close(notification)` does not find card.
- Pass the same notification instance or close by matching content object.
