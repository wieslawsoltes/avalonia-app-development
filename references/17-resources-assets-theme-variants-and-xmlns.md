# Resources, Assets, Theme Variants, and XmlnsDefinition

## Table of Contents
1. Scope and APIs
2. Resource Authoring and Lookup
3. Runtime ResourceDictionary Mutation
4. Deferred and Not-Shared Resource Entries
5. Theme Variant Authoring and Runtime Behavior
6. Dynamic Resources and Includes
7. Asset Authoring and Access
8. XmlnsDefinition Usage
9. Best Practices
10. Troubleshooting

## Scope and APIs

Primary APIs:

- `ResourceDictionary`, `IResourceDictionary`
- `ResourceDictionary.MergedDictionaries`, `ResourceDictionary.ThemeDictionaries`
- `TryGetResource(key, theme, out value)`
- `ThemeVariant` (`Default`, `Light`, `Dark`)
- `ThemeVariantScope`
- `Application.RequestedThemeVariant`
- `AssetLoader`, `IAssetLoader`
- `XmlnsDefinitionAttribute`

Related XAML runtime resource APIs:

- `DynamicResourceExtension`
- `ResourceInclude`
- `StyleInclude`

Related markup type-converter contracts (framework parsing layer):

- `CultureInfoIetfLanguageTagConverter`
- `CultureInfoIetfLanguageTagConverter.CanConvertFrom(...)`
- `CultureInfoIetfLanguageTagConverter.ConvertFrom(...)`

Note:
- This converter is part of framework parsing internals; app code should usually pass `CultureInfo` directly instead of calling it explicitly.

## Resource Authoring and Lookup

Layered strategy:

1. Global resources (`Application.Resources`, `Application.Styles`).
2. Feature/module dictionaries (`MergedDictionaries`).
3. Control-local dictionaries only when scoping is intentional.

`ResourceDictionary` lookup behavior:

- local dictionary entries first,
- theme dictionaries (`ThemeDictionaries`) including `ThemeVariant.InheritVariant` chain,
- merged dictionaries in reverse registration order.

Example:

```xml
<ResourceDictionary>
  <Color x:Key="BrandColor">#0A84FF</Color>

  <ResourceDictionary.MergedDictionaries>
    <ResourceInclude Source="avares://MyApp/Styles/Buttons.axaml" />
  </ResourceDictionary.MergedDictionaries>
</ResourceDictionary>
```

## Runtime ResourceDictionary Mutation

`ResourceDictionary` is mutable and supports efficient runtime updates.

Useful members:

- `Count`, indexer `this[object key]`
- `Keys`, `Values`
- `HasResources`
- `SetItems(...)`
- `ContainsKey(...)`
- `EnsureCapacity(...)`
- `GetEnumerator()`

Pattern:

```csharp
var resources = Application.Current!.Resources;

if (resources is ResourceDictionary dict)
{
    dict.EnsureCapacity(64);

    dict.SetItems(new[]
    {
        new KeyValuePair<object, object?>("SpacingM", 12d),
        new KeyValuePair<object, object?>("SpacingL", 16d)
    });

    if (!dict.ContainsKey("FeatureEnabled"))
        dict["FeatureEnabled"] = true;
}
```

## Deferred and Not-Shared Resource Entries

For expensive or late materialization, use deferred APIs:

- `AddDeferred(object key, Func<IServiceProvider?, object?> factory)`
- `AddDeferred(object key, IDeferredContent deferredContent)`
- `AddNotSharedDeferred(object key, IDeferredContent deferredContent)`

Guidance:

- use `AddDeferred` for cached-on-first-use resource values,
- use `AddNotSharedDeferred` when each lookup needs a fresh instance.

## Theme Variant Authoring and Runtime Behavior

Theme variant APIs:

- `ThemeVariant.Default`, `ThemeVariant.Light`, `ThemeVariant.Dark`
- `ThemeVariant.InheritVariant`
- explicit operators between `ThemeVariant` and `PlatformThemeVariant`
- `operator ThemeVariant`
- `operator PlatformThemeVariant?`
- `RequestedThemeVariant`, `ActualThemeVariant`

Use app-wide setting:

```xml
<Application RequestedThemeVariant="Default" />
```

Use local override scope:

```xml
<ThemeVariantScope RequestedThemeVariant="Dark">
  <ContentPresenter Content="{Binding}" />
</ThemeVariantScope>
```

Theme dictionaries:

```xml
<ResourceDictionary>
  <ResourceDictionary.ThemeDictionaries>
    <ResourceDictionary x:Key="Light">
      <SolidColorBrush x:Key="AppBackground" Color="White" />
    </ResourceDictionary>
    <ResourceDictionary x:Key="Dark">
      <SolidColorBrush x:Key="AppBackground" Color="#202020" />
    </ResourceDictionary>
  </ResourceDictionary.ThemeDictionaries>
</ResourceDictionary>
```

## Dynamic Resources and Includes

Use dynamic resources when runtime theme/resource changes should propagate automatically.

Key APIs:

- `DynamicResourceExtension`
- `DynamicResourceExtension.ResourceKey`
- `ResourceInclude.Source`, `StyleInclude.Source`
- `ResourceInclude.Owner`, `StyleInclude.Owner`
- `ResourceInclude.OwnerChanged`, `StyleInclude.OwnerChanged`

Guidance:

- keep static baseline resources in compiled XAML,
- use `DynamicResource` for values expected to change,
- treat include-owner events as advanced runtime infrastructure hooks.

## Asset Authoring and Access

Project item guidance:

- mark XAML and static assets as `AvaloniaResource`.
- access with `avares://AssemblyName/path` URIs.

C# asset access:

```csharp
using Avalonia.Platform;

using var stream = AssetLoader.Open(new Uri("avares://MyApp/Assets/logo.png"));
```

Additional APIs:

- `AssetLoader.Exists(...)`
- `AssetLoader.OpenAndGetAssembly(...)`
- `AssetLoader.GetAssets(...)`

## XmlnsDefinition Usage

`XmlnsDefinitionAttribute` maps XML namespace to CLR namespace at assembly level.

Pattern:

```csharp
[assembly: XmlnsDefinition("https://github.com/avaloniaui", "MyApp.Controls")]
[assembly: XmlnsDefinition("https://github.com/avaloniaui", "MyApp.Theming")]
```

Effect:

- controls become available under mapped XML namespace,
- fewer repetitive `clr-namespace` mappings in XAML.

## Best Practices

- keep resource keys semantic and stable.
- keep variant-specific values inside `ThemeDictionaries`.
- prefer `DynamicResource` for theme-sensitive values.
- use deferred entries selectively and document ownership/shared semantics.
- keep `XmlnsDefinition` mappings explicit and non-overlapping.

## Troubleshooting

1. Resource not found.
- Key mismatch, dictionary not merged, or scope owner is wrong.

2. Theme switch does not update value.
- Missing `ThemeDictionaries` entry for active variant or missing `DynamicResource` usage.

3. Deferred resource throws/re-enters unexpectedly.
- Check `AddDeferred` factory side effects and avoid recursive same-key lookups.

4. Include-based resources appear detached.
- Verify `Source` URI and inspect `ResourceInclude.Owner` / `StyleInclude.Owner` transitions.

5. XAML cannot resolve custom controls.
- Verify assembly-level `XmlnsDefinition` mapping and public type visibility.

6. Culture-tag strings fail to parse in custom markup extensions.
- Verify the input is a valid IETF language tag expected by `CultureInfoIetfLanguageTagConverter`.
