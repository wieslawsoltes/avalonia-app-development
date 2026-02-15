# Platform Services: Storage, Clipboard, Launcher, Screens, and DragDrop

## Table of Contents
1. Scope and APIs
2. Service Access Model
3. Storage Provider Patterns
4. Clipboard and DataTransfer Patterns
5. Launcher, Screens, and Insets Patterns
6. DragDrop Patterns
7. XAML-First and Code-Only Usage
8. Best Practices
9. Troubleshooting

## Scope and APIs

Primary APIs:
- `TopLevel.GetTopLevel(...)`
- `TopLevel.StorageProvider`
- `TopLevel.Clipboard`
- `TopLevel.Launcher`
- `TopLevel.Screens`
- `TopLevel.InsetsManager`
- `IStorageProvider`
- `IStorageFile`, `IStorageFolder`, `IStorageItem`
- `FilePickerOpenOptions`, `FilePickerSaveOptions`
- `StorageProviderExtensions.TryGetFileFromPathAsync(...)`
- `StorageProviderExtensions.TryGetFolderFromPathAsync(...)`
- `StorageProviderExtensions.TryGetLocalPath(...)`
- `IClipboard`, `ClipboardExtensions`
- `ILauncher`, `LauncherExtensions`
- `DragDrop` and `DragEventArgs`
- `DataTransfer`, `DataTransferItem`

Reference source files:
- `src/Avalonia.Controls/TopLevel.cs`
- `src/Avalonia.Controls/Screens.cs`
- `src/Avalonia.Controls/Platform/IInsetsManager.cs`
- `src/Avalonia.Base/Platform/Storage/IStorageProvider.cs`
- `src/Avalonia.Base/Platform/Storage/IStorageItem.cs`
- `src/Avalonia.Base/Platform/Storage/IStorageFile.cs`
- `src/Avalonia.Base/Platform/Storage/IStorageFolder.cs`
- `src/Avalonia.Base/Platform/Storage/FilePickerOpenOptions.cs`
- `src/Avalonia.Base/Platform/Storage/FilePickerSaveOptions.cs`
- `src/Avalonia.Base/Platform/Storage/StorageProviderExtensions.cs`
- `src/Avalonia.Base/Input/Platform/IClipboard.cs`
- `src/Avalonia.Base/Input/Platform/ClipboardExtensions.cs`
- `src/Avalonia.Base/Platform/Storage/ILauncher.cs`
- `src/Avalonia.Base/Input/DragDrop.cs`
- `src/Avalonia.Base/Input/DragEventArgs.cs`
- `src/Avalonia.Base/Input/DataTransfer.cs`
- `src/Avalonia.Base/Input/DataTransferItem.cs`

## Service Access Model

Use `TopLevel` as the platform-service boundary for a view scope:
1. Resolve current root with `TopLevel.GetTopLevel(control)`.
2. Access `StorageProvider`, `Clipboard`, `Launcher`, `Screens`, `InsetsManager`.
3. Keep actual app logic in viewmodel/service code and pass only required abstractions/state.

Practical notes:
- `StorageProvider` can fallback to `NoopStorageProvider` when unsupported.
- `Clipboard` can be null on platforms where no clipboard feature is exposed.
- `Launcher` always resolves (`NoopLauncher` fallback returns `false`).

## Storage Provider Patterns

Typical open flow:
1. Check `CanOpen` / `CanSave` / `CanPickFolder`.
2. Create picker options with title, start location, and file types.
3. Process `IStorageFile` / `IStorageFolder`.
4. Dispose storage items when no longer needed.

```csharp
using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using Avalonia.Controls;
using Avalonia.Platform.Storage;

public static class StorageWorkflows
{
    public static async Task<IReadOnlyList<IStorageFile>> PickJsonFilesAsync(Control anchor)
    {
        TopLevel? topLevel = TopLevel.GetTopLevel(anchor);
        if (topLevel is null || !topLevel.StorageProvider.CanOpen)
            return Array.Empty<IStorageFile>();

        FilePickerFileType jsonType = new("JSON")
        {
            Patterns = new[] { "*.json" },
            MimeTypes = new[] { "application/json" }
        };

        return await topLevel.StorageProvider.OpenFilePickerAsync(new FilePickerOpenOptions
        {
            Title = "Open JSON files",
            AllowMultiple = true,
            FileTypeFilter = new[] { jsonType }
        });
    }
}
```

## Clipboard and DataTransfer Patterns

Clipboard APIs are async and support typed formats through `DataFormat`.

```csharp
using System.Threading.Tasks;
using Avalonia.Controls;
using Avalonia.Input.Platform;

public static class ClipboardWorkflows
{
    public static async Task CopyTextAsync(Control anchor, string value)
    {
        TopLevel? topLevel = TopLevel.GetTopLevel(anchor);
        if (topLevel?.Clipboard is { } clipboard)
            await clipboard.SetTextAsync(value);
    }

    public static async Task<string?> PasteTextAsync(Control anchor)
    {
        TopLevel? topLevel = TopLevel.GetTopLevel(anchor);
        if (topLevel?.Clipboard is not { } clipboard)
            return null;

        return await clipboard.TryGetTextAsync();
    }
}
```

For drag source payloads, use `DataTransfer` + `DataTransferItem` and `DragDrop.DoDragDropAsync(...)`.

## Launcher, Screens, and Insets Patterns

Launch external targets via platform default apps:

```csharp
using System;
using System.Threading.Tasks;
using Avalonia.Controls;

public static class LaunchWorkflows
{
    public static async Task<bool> OpenProjectSiteAsync(Control anchor)
    {
        TopLevel? topLevel = TopLevel.GetTopLevel(anchor);
        if (topLevel is null)
            return false;

        return await topLevel.Launcher.LaunchUriAsync(new Uri("https://avaloniaui.net"));
    }
}
```

Use `Screens` for monitor-aware placement and diagnostics. Use `InsetsManager` for safe-area and system-bar integration on mobile/edge-to-edge platforms.

## DragDrop Patterns

Drop target strategy:
1. Set `DragDrop.AllowDrop="True"` on target.
2. Handle `DragOver` to set `e.DragEffects`.
3. Handle `Drop` and extract data from `e.DataTransfer`.

```csharp
using System;
using Avalonia.Controls;
using Avalonia.Input;
using Avalonia.Platform.Storage;

public sealed class DropTargetBehavior
{
    public static void Attach(Control target, Action<IStorageItem[]> onFilesDropped)
    {
        DragDrop.SetAllowDrop(target, true);

        target.AddHandler(DragDrop.DragOverEvent, (_, e) =>
        {
            IStorageItem[]? files = e.DataTransfer.TryGetFiles();
            e.DragEffects = files is { Length: > 0 } ? DragDropEffects.Copy : DragDropEffects.None;
            e.Handled = true;
        });

        target.AddHandler(DragDrop.DropEvent, (_, e) =>
        {
            IStorageItem[]? files = e.DataTransfer.TryGetFiles();
            if (files is { Length: > 0 })
                onFilesDropped(files);

            e.Handled = true;
        });
    }
}
```

## XAML-First and Code-Only Usage

Default mode:
- Declare platform interaction surfaces in XAML first.
- Keep platform API calls in services/viewmodels.
- Use code-only UI trees only when explicitly requested.

XAML-first complete example:

```xml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:DataType="vm:PlatformToolsViewModel">
  <Grid RowDefinitions="Auto,*" Margin="12" RowSpacing="8">
    <StackPanel Orientation="Horizontal" Spacing="8">
      <Button Content="Open Files" Command="{CompiledBinding OpenFilesCommand}" />
      <Button Content="Save As" Command="{CompiledBinding SaveFileCommand}" />
      <Button Content="Copy Path" Command="{CompiledBinding CopyPathCommand}" />
      <Button Content="Open Website" Command="{CompiledBinding OpenWebsiteCommand}" />
    </StackPanel>

    <Border Grid.Row="1"
            Padding="12"
            BorderBrush="Gray"
            BorderThickness="1"
            DragDrop.AllowDrop="True">
      <TextBlock Text="{CompiledBinding DropHint}" />
    </Border>
  </Grid>
</UserControl>
```

Code-only alternative (on request):

```csharp
using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using Avalonia;
using Avalonia.Controls;
using Avalonia.Input.Platform;
using Avalonia.Platform.Storage;

public static class CodeOnlyPlatformSample
{
    public static async Task ExecuteAsync(Control anchor)
    {
        TopLevel? top = TopLevel.GetTopLevel(anchor);
        if (top is null)
            return;

        if (top.StorageProvider.CanOpen)
        {
            IReadOnlyList<IStorageFile> files = await top.StorageProvider.OpenFilePickerAsync(
                new FilePickerOpenOptions { Title = "Open file", AllowMultiple = false });

            IStorageFile? file = files.Count > 0 ? files[0] : null;
            if (file is not null && top.Clipboard is { } clipboard)
                await clipboard.SetTextAsync(file.TryGetLocalPath() ?? file.Path.ToString());
        }

        _ = await top.Launcher.LaunchUriAsync(new Uri("https://avaloniaui.net"));
    }
}
```

## Best Practices

- Resolve `TopLevel` at interaction time; do not cache platform objects globally.
- Guard for capability flags (`CanOpen`, `CanSave`, `CanPickFolder`) before picker calls.
- Use typed `DataFormat`/clipboard helpers, not ad-hoc format strings.
- Keep drag/drop handlers lightweight and deterministic.
- Keep platform service calls in dedicated services to preserve MVVM boundaries.

## Troubleshooting

1. Picker methods return empty results:
- User canceled dialog.
- Capability (`CanOpen`/`CanSave`) is false on current platform.

2. Clipboard returns null/empty unexpectedly:
- Clipboard feature unavailable on current platform.
- Wrong format requested; verify with `GetDataFormatsAsync()`.

3. Drag/drop never triggers:
- `DragDrop.AllowDrop` not enabled on target.
- Target is covered by another control intercepting pointer/input.

4. `LaunchUriAsync` returns false:
- Scheme unsupported or blocked by platform policy.
- No default handler installed for the target URI/file type.
