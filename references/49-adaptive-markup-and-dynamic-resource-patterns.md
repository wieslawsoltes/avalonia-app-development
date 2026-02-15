# Adaptive Markup and Dynamic Resource Patterns

## Table of Contents
1. Scope and APIs
2. `OnPlatform` Markup Extension
3. `OnFormFactor` Markup Extension
4. `On` Option Nodes
5. Dynamic Resource Wiring
6. Combining Adaptive Markup with Dynamic Resources
7. Practical Patterns
8. Troubleshooting

## Scope and APIs

Primary APIs:

- `OnPlatformExtension`
- `OnPlatformExtension<TReturn>`
- `OnPlatformExtensionBase<TReturn, TOn>`
- `OnFormFactorExtension`
- `OnFormFactorExtension<TReturn>`
- `OnFormFactorExtensionBase<TReturn, TOn>`
- `On<TReturn>`
- `On`
- `DynamicResourceExtension`

Key members used in adaptive markup:

- `ShouldProvideOption(...)`
- `Default`, `Windows`, `macOS`, `Linux`, `Android`, `iOS`, `Browser`
- `Desktop`, `Mobile`, `TV`
- `Options`, `Content`
- `ResourceKey`

## `OnPlatform` Markup Extension

Use `OnPlatform` when a value depends on runtime platform.

Important APIs:

- `OnPlatformExtension()`
- `OnPlatformExtension(object defaultValue)`
- `OnPlatformExtension<TReturn>()`
- `OnPlatformExtension<TReturn>(TReturn defaultValue)`
- `ShouldProvideOption(string option)`
- `OnPlatformExtensionBase<TReturn, TOn> : IAddChild<TOn>`

Platform-specific properties:

- `Default`
- `Windows`
- `macOS`
- `Linux`
- `Android`
- `iOS`
- `Browser`

Example:

```xml
<StackPanel xmlns="https://github.com/avaloniaui"
            xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml">
  <Border Padding="{OnPlatform Default=8, Windows=10, macOS=12, Linux=10, Browser=6}" />
</StackPanel>
```

Use `Default` as a safe baseline. Override only where behavior or UX genuinely differs.

## `OnFormFactor` Markup Extension

Use `OnFormFactor` when values differ between desktop, mobile, and TV.

Important APIs:

- `OnFormFactorExtension()`
- `OnFormFactorExtension(object defaultValue)`
- `OnFormFactorExtension<TReturn>()`
- `OnFormFactorExtension<TReturn>(TReturn defaultValue)`
- `ShouldProvideOption(IServiceProvider serviceProvider, FormFactorType option)`
- `OnFormFactorExtensionBase<TReturn, TOn> : IAddChild<TOn>`

Form-factor properties:

- `Default`
- `Desktop`
- `Mobile`
- `TV`

Example:

```xml
<StackPanel xmlns="https://github.com/avaloniaui"
            xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml">
  <ItemsRepeater ItemTemplate="{OnFormFactor Default={StaticResource CompactTemplate}, Desktop={StaticResource RichTemplate}, Mobile={StaticResource CompactTemplate}}" />
</StackPanel>
```

## `On` Option Nodes

`OnPlatform` and `OnFormFactor` support child option nodes represented by `On<TReturn>` / `On`.

Key members:

- `Options`
- `Content`

Object-element syntax pattern:

```xml
<TextBlock xmlns="https://github.com/avaloniaui"
           xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml">
  <TextBlock.Text>
    <OnPlatform x:TypeArguments="x:String" Default="General profile">
      <On Options="WINDOWS, LINUX, OSX" Content="Desktop profile" />
      <On Options="ANDROID, IOS" Content="Mobile profile" />
      <On Options="BROWSER" Content="Web profile" />
    </OnPlatform>
  </TextBlock.Text>
</TextBlock>
```

For `OnPlatform`, `Options` commonly uses `WINDOWS`, `OSX`, `LINUX`, `ANDROID`, `IOS`, `BROWSER`.
For `OnFormFactor`, use form-factor option names matching `FormFactorType` values (`Desktop`, `Mobile`, `TV`).
Use child option nodes when inline property syntax becomes hard to read.

## Dynamic Resource Wiring

`DynamicResourceExtension` is the runtime-binding markup extension for resource key lookup.

Important APIs:

- `DynamicResourceExtension()`
- `DynamicResourceExtension(object resourceKey)`
- `ResourceKey`
- `ProvideValue(IServiceProvider serviceProvider)`

Example:

```xml
<Application xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             x:Class="MyApp.App">
  <Application.Resources>
    <Color x:Key="BrandColor">#0A84FF</Color>
    <SolidColorBrush x:Key="BrandBrush" Color="{DynamicResource BrandColor}" />
  </Application.Resources>
</Application>
```

Use `DynamicResource` for keys expected to change at runtime (theme/variant/plugin packs).

## Combining Adaptive Markup with Dynamic Resources

Common pattern:

1. choose a platform/form-factor-specific resource key with `OnPlatform`/`OnFormFactor`,
2. keep actual color/spacing values in dictionaries,
3. consume values via `DynamicResource`.

```xml
<TextBlock FontSize="{OnFormFactor Default=14, Desktop=15, Mobile=13}"
           Foreground="{DynamicResource BrandBrush}" />
```

This keeps adaptation decisions separate from actual resource values.

## Practical Patterns

1. Keep adaptive overrides small.
- Prefer one shared default (`Default`) plus minimal platform/form-factor deltas.

2. Use adaptive markup for UX differences, not business behavior.
- Keep behavior branching in viewmodel/services.

3. Centralize adaptive values in styles/templates.
- Avoid duplicating `OnPlatform` and `OnFormFactor` in many view files.

4. Pair with `ThemeDictionaries` for light/dark concerns.
- Platform/form-factor and theme are separate dimensions.

## Troubleshooting

1. Expected platform-specific value not applied.
- Verify option name and evaluate whether `ShouldProvideOption(...)` will match that option.

2. Form-factor value not switching.
- Check host form-factor detection and `OnFormFactor` option keys (`Desktop`, `Mobile`, `TV`).

3. Dynamic resource does not update.
- Ensure the consuming property uses `DynamicResource` and the resource key remains stable.

4. Markup becomes unreadable.
- Move adaptive expressions into shared styles/templates and keep view markup thin.
