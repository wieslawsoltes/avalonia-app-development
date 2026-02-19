# WinUI InfoBar, TeachingTip, and Inline Guidance Surfaces to Avalonia

## Table of Contents
1. Scope and APIs
2. Concept Mapping
3. Conversion Example
4. Migration Notes

## Scope and APIs

Primary WinUI APIs:

- InfoBar, TeachingTip, IsOpen, Severity, ActionButton

Primary Avalonia APIs:

- WindowNotificationManager, Flyout, ToolTip, inline banners

## Concept Mapping

| WinUI idiom | Avalonia idiom |
|---|---|
| WinUI control and state pipeline | Avalonia control themes, selectors, and transitions |
| WinUI command/input surfaces | Avalonia commands + `KeyBinding`/routed input |
| WinUI resource/theme flow | Avalonia resource dictionaries + `ThemeVariant` |

## Conversion Example

WinUI XAML:

```xaml
<InfoBar IsOpen="{x:Bind ViewModel.IsInfoOpen, Mode=TwoWay}" Severity="Warning" Title="Unsaved changes" />
```

WinUI C#:

```csharp
var info = new InfoBar { IsOpen = true };
```

Avalonia XAML:

```xaml
<Border IsVisible="{Binding IsInfoOpen}" Classes="warning-banner"><TextBlock Text="Unsaved changes" /></Border>
```

Avalonia C#:

```csharp
var manager = new WindowNotificationManager(topLevel); manager.Show(new Notification("Warning", "Unsaved changes", NotificationType.Warning));
```

## Migration Notes

1. Preserve behavior and interaction contracts before visual refinements.
2. Port hot paths with explicit UI-thread and invalidation discipline.
3. Prefer typed compiled bindings and deterministic state flow in migrated views.
