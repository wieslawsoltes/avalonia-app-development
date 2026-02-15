# Value Converters

## Table of Contents
1. Scope and APIs
2. Converter Shapes at a Glance
3. Class-Based `IValueConverter` in XAML Resources
4. Function-Based Single-Value Converters (`FuncValueConverter`)
5. Built-in Converter Helpers (`BoolConverters`, `StringConverters`, `ObjectConverters`)
6. Multi-Value Conversion with `MultiBinding` and `IMultiValueConverter`
7. Function-Based Multi-Value Converters (`FuncMultiValueConverter`)
8. Wiring Converters into Reflection/Compiled/Template Bindings
9. Return Semantics and Error Handling
10. Best Practices
11. Troubleshooting

## Scope and APIs

Primary APIs:
- `IValueConverter`
- `IMultiValueConverter`
- `FuncValueConverter<TIn, TOut>`
- `FuncValueConverter<TIn, TParam, TOut>`
- `FuncMultiValueConverter<TIn, TOut>`
- `ReflectionBinding` / `Binding`
- `CompiledBinding`
- `TemplateBinding`
- `MultiBinding`
- `BindingOperations.DoNothing`

Built-in converter helpers:
- `BoolConverters`
- `StringConverters`
- `ObjectConverters`

Reference source files:
- `src/Avalonia.Base/Data/Converters/IValueConverter.cs`
- `src/Avalonia.Base/Data/Converters/IMultiValueConverter.cs`
- `src/Avalonia.Base/Data/Converters/FuncValueConverter.cs`
- `src/Avalonia.Base/Data/Converters/FuncMultiValueConverter.cs`
- `src/Avalonia.Base/Data/Converters/BoolConverters.cs`
- `src/Avalonia.Base/Data/Converters/StringConverters.cs`
- `src/Avalonia.Base/Data/Converters/ObjectConverters.cs`
- `src/Avalonia.Base/Data/MultiBinding.cs`
- `src/Avalonia.Base/Data/ReflectionBinding.cs`
- `src/Avalonia.Base/Data/CompiledBinding.cs`
- `src/Avalonia.Base/Data/TemplateBinding.cs`
- `src/Markup/Avalonia.Markup.Xaml/MarkupExtensions/ReflectionBindingExtension.cs`
- `src/Markup/Avalonia.Markup.Xaml/MarkupExtensions/CompiledBindingExtension.cs`

## Converter Shapes at a Glance

Single-value conversion:
- implement `IValueConverter` for `Binding`, `ReflectionBinding`, `CompiledBinding`, `TemplateBinding`.

Multi-value conversion:
- implement `IMultiValueConverter` and use with `MultiBinding`.

Authoring styles:
- class-based converter (best for reusable shared logic),
- function-based converter (`FuncValueConverter`, `FuncMultiValueConverter`) for concise code wiring.

## Class-Based `IValueConverter` in XAML Resources

Converter class:

```csharp
using System;
using System.Globalization;
using Avalonia;
using Avalonia.Data.Converters;

public sealed class StatusToTextConverter : IValueConverter
{
    public object? Convert(object? value, Type targetType, object? parameter, CultureInfo culture)
        => value switch
        {
            true => "Online",
            false => "Offline",
            _ => AvaloniaProperty.UnsetValue
        };

    public object? ConvertBack(object? value, Type targetType, object? parameter, CultureInfo culture)
        => value switch
        {
            "Online" => true,
            "Offline" => false,
            _ => AvaloniaProperty.UnsetValue
        };
}
```

Register and use in XAML resources:

```xml
<Window xmlns="https://github.com/avaloniaui"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        xmlns:conv="using:MyApp.Converters">
  <Window.Resources>
    <conv:StatusToTextConverter x:Key="StatusToText" />
  </Window.Resources>

  <TextBlock Text="{Binding IsOnline, Converter={StaticResource StatusToText}}" />
</Window>
```

Resource scope can be:
- `Application.Resources` (global),
- `Window.Resources` / `UserControl.Resources` (local),
- style or template resource dictionaries.

## Function-Based Single-Value Converters (`FuncValueConverter`)

C# wiring example:

```csharp
using Avalonia.Data;
using Avalonia.Data.Converters;

var textConverter = new FuncValueConverter<decimal, string>(v => v.ToString("0.00"));

textBlock.Bind(TextBlock.TextProperty, new ReflectionBinding(nameof(ViewModel.Total))
{
    Converter = textConverter
});
```

With converter parameter:

```csharp
var suffixConverter = new FuncValueConverter<string, string, string>((value, suffix) =>
    $"{value}{suffix}");

textBlock.Bind(TextBlock.TextProperty, new ReflectionBinding(nameof(ViewModel.Name))
{
    Converter = suffixConverter,
    ConverterParameter = " (active)"
});
```

Tip:
- function-based converters are easiest from C#.
- for XAML usage, expose them as static properties and consume via `x:Static`.

## Built-in Converter Helpers (`BoolConverters`, `StringConverters`, `ObjectConverters`)

Avalonia ships reusable static converters.

XAML usage with `x:Static`:

```xml
<TextBlock IsVisible="{Binding Item, Converter={x:Static ObjectConverters.IsNotNull}}" />
<ToggleButton IsChecked="{Binding IsEnabled, Converter={x:Static BoolConverters.Not}}" />
<TextBlock IsVisible="{Binding Query, Converter={x:Static StringConverters.IsNotNullOrEmpty}}" />
```

Useful built-ins:
- `BoolConverters.Not` (single value),
- `BoolConverters.And` / `BoolConverters.Or` (multi-value),
- `ObjectConverters.IsNull`, `IsNotNull`, `Equal`, `NotEqual`,
- `StringConverters.IsNullOrEmpty`, `IsNotNullOrEmpty`.

Built-in multi-converter with `MultiBinding`:

```xml
<TextBlock.IsVisible>
  <MultiBinding Converter="{x:Static BoolConverters.And}">
    <Binding Path="IsEnabled" />
    <Binding Path="HasSelection" />
  </MultiBinding>
</TextBlock.IsVisible>
```

## Multi-Value Conversion with `MultiBinding` and `IMultiValueConverter`

`IMultiValueConverter`:
- has only `Convert(...)` (no `ConvertBack`).

Class-based multi converter:

```csharp
using System;
using System.Collections.Generic;
using System.Globalization;
using Avalonia;
using Avalonia.Data.Converters;

public sealed class FullNameConverter : IMultiValueConverter
{
    public object? Convert(IList<object?> values, Type targetType, object? parameter, CultureInfo culture)
    {
        var first = values.Count > 0 ? values[0]?.ToString() : null;
        var last = values.Count > 1 ? values[1]?.ToString() : null;

        if (string.IsNullOrWhiteSpace(first) && string.IsNullOrWhiteSpace(last))
            return AvaloniaProperty.UnsetValue;

        return $"{first} {last}".Trim();
    }
}
```

XAML wiring:

```xml
<Window xmlns="https://github.com/avaloniaui"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        xmlns:conv="using:MyApp.Converters">
  <Window.Resources>
    <conv:FullNameConverter x:Key="FullNameConverter" />
  </Window.Resources>

  <TextBlock>
    <TextBlock.Text>
      <MultiBinding Converter="{StaticResource FullNameConverter}" FallbackValue="(unknown)">
        <Binding Path="FirstName" />
        <Binding Path="LastName" />
      </MultiBinding>
    </TextBlock.Text>
  </TextBlock>
</Window>
```

Notes:
- `MultiBinding` supports nested bindings, including nested `MultiBinding`.
- `StringFormat` can be used with or without a converter.
- if no converter and no string format is set, the target receives the collected values list.

## Function-Based Multi-Value Converters (`FuncMultiValueConverter`)

C# example:

```csharp
using Avalonia.Data;
using Avalonia.Data.Converters;

var join = new FuncMultiValueConverter<string, string>(values => string.Join(" / ", values));

var binding = new MultiBinding
{
    Converter = join,
    Bindings =
    {
        new ReflectionBinding(nameof(ViewModel.LeftText)),
        new ReflectionBinding(nameof(ViewModel.RightText)),
    }
};

textBlock.Bind(TextBlock.TextProperty, binding);
```

For XAML reuse, expose converter instances via static properties and reference them with `x:Static`.

## Wiring Converters into Reflection/Compiled/Template Bindings

Reflection binding (XAML):

```xml
<TextBlock Text="{Binding Name, Converter={StaticResource NameConverter}}" />
```

Compiled binding (XAML):

```xml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:local="using:MyApp"
             x:DataType="local:MyVm"
             x:CompileBindings="True">
  <TextBlock Text="{CompiledBinding Name, Converter={StaticResource NameConverter}, ConverterParameter=VIP}" />
</UserControl>
```

Compiled binding (C# API):

```csharp
var binding = CompiledBinding.Create<MyVm, decimal>(
    vm => vm.Total,
    converter: new FuncValueConverter<decimal, string>(v => v.ToString("C2")));

textBlock.Bind(TextBlock.TextProperty, binding);
```

Template binding:

```xml
<Border Background="{TemplateBinding Background, Converter={StaticResource BrushConverter}}" />
```

MultiBinding + compile bindings:
- `x:CompileBindings="True"` also affects `<Binding .../>` items inside `<MultiBinding>`.

## Return Semantics and Error Handling

`IValueConverter` guidance:
- avoid throwing exceptions for normal invalid input,
- return `BindingNotification` for binding error states when needed,
- return `AvaloniaProperty.UnsetValue` when value cannot be converted.

`IMultiValueConverter` guidance:
- return `AvaloniaProperty.UnsetValue` to trigger `FallbackValue`,
- return `null` to trigger `TargetNullValue`,
- `BindingOperations.DoNothing` keeps current target value unchanged.

## Best Practices

- Keep converter logic deterministic and side-effect-free.
- Use explicit converter classes for shared domain rules.
- Use `FuncValueConverter` / `FuncMultiValueConverter` for local concise wiring.
- Prefer converter resources for XAML readability and reuse.
- Keep `ConverterParameter` types explicit (resource/static objects if non-string needed).
- In hot paths, avoid heavy allocation or expensive formatting inside converters.
- For multi-value composition, use `MultiBinding` only when the value truly depends on multiple sources.

## Troubleshooting

1. Converter not found in XAML
- Resource key missing or wrong scope.
- Incorrect XML namespace for converter class.

2. Converter called but value not updated
- Converter returns `BindingOperations.DoNothing`.
- `UnsetValue` hits fallback path unexpectedly.

3. MultiBinding never produces output
- One or more child bindings never initialize.
- Converter rejects value types and returns `UnsetValue`.

4. Compiled-binding view still behaves like reflection binding
- Missing `x:CompileBindings="True"` and/or `x:DataType`.

5. Two-way conversion fails
- `ConvertBack` is missing/invalid for single-value converters.
- MultiBinding does not provide `ConvertBack` semantics.
