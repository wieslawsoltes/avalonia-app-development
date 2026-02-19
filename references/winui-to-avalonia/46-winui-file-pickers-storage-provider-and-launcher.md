# WinUI File Pickers, Storage, and Launcher to Avalonia

## Table of Contents
1. Scope and APIs
2. Concept Mapping
3. Conversion Example
4. Migration Notes

## Scope and APIs

Primary WinUI APIs:

- FileOpenPicker, FileSavePicker, FolderPicker, Launcher, LaunchUriAsync, LaunchFileAsync

Primary Avalonia APIs:

- TopLevel.StorageProvider, IStorageProvider, FilePickerOpenOptions, FilePickerSaveOptions, TopLevel.Launcher, ILauncher

## Concept Mapping

| WinUI idiom | Avalonia idiom |
|---|---|
| FileOpenPicker/PickSingleFileAsync | StorageProvider.OpenFilePickerAsync |
| FileSavePicker/PickSaveFileAsync | StorageProvider.SaveFilePickerAsync |
| FolderPicker/PickSingleFolderAsync | StorageProvider.OpenFolderPickerAsync |
| Launcher.LaunchUriAsync | Launcher.LaunchUriAsync |
| Launcher.LaunchFileAsync(StorageFile) | Launcher.LaunchFileAsync(IStorageItem) |

## Conversion Example

WinUI XAML:

```xaml
<StackPanel Spacing="8">
  <Button Content="Open JSON" Click="OpenJson_Click" />
  <Button Content="Open Docs" Click="OpenDocs_Click" />
</StackPanel>
```

WinUI C#:

```csharp
var picker = new FileOpenPicker();
picker.FileTypeFilter.Add(".json");
StorageFile? file = await picker.PickSingleFileAsync();
if (file is not null)
    await Launcher.LaunchFileAsync(file);

await Launcher.LaunchUriAsync(new Uri("https://docs.avaloniaui.net"));
```

Avalonia XAML:

```xaml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:DataType="vm:FilesViewModel">
  <StackPanel Spacing="8">
    <Button Content="Open JSON" Command="{CompiledBinding OpenJsonCommand}" />
    <Button Content="Open Docs" Command="{CompiledBinding OpenDocsCommand}" />
  </StackPanel>
</UserControl>
```

Avalonia C#:

```csharp
TopLevel? top = TopLevel.GetTopLevel(this);
if (top is null)
    return;

var files = await top.StorageProvider.OpenFilePickerAsync(new FilePickerOpenOptions
{
    AllowMultiple = false,
    FileTypeFilter = new[]
    {
        new FilePickerFileType("JSON") { Patterns = new[] { "*.json" } }
    }
});

if (files.Count > 0)
    await top.Launcher.LaunchFileAsync(files[0]);

await top.Launcher.LaunchUriAsync(new Uri("https://docs.avaloniaui.net"));
```

## Migration Notes

1. Resolve `TopLevel` at interaction time and use its `StorageProvider`/`Launcher`.
2. Guard picker/launcher flows with capability checks for cross-platform parity.
3. Prefer storage streams and bookmarks over raw path assumptions.
