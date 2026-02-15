# RelativeSource, StaticResource, and Name Resolution Markup

## Table of Contents
1. Scope and APIs
2. `RelativeSource` Core Model
3. `RelativeSourceExtension` in XAML
4. Wiring `RelativeSource` in `Binding` and `ReflectionBindingExtension`
5. `FindAncestor` Patterns (Visual vs Logical Tree)
6. `StaticResourceExtension` Semantics
7. `ResolveByNameExtension` Semantics
8. `Binding.TypeResolver` and Type Name Resolution
9. Best Practices
10. Troubleshooting

## Scope and APIs

Primary APIs:

- `RelativeSource`
- `RelativeSourceMode`
- `TreeType`
- `RelativeSourceExtension`
- `Binding.RelativeSource`
- `ReflectionBindingExtension.RelativeSource`
- `ReflectionBindingExtension.ConverterCulture`
- `StaticResourceExtension`
- `ResolveByNameExtension`
- `Binding.TypeResolver`

Key members:

- `RelativeSourceExtension()`
- `RelativeSourceExtension(RelativeSourceMode mode)`
- `RelativeSourceExtension.Mode`
- `RelativeSourceExtension.AncestorType`
- `RelativeSourceExtension.Tree`
- `RelativeSourceExtension.AncestorLevel`
- `StaticResourceExtension()`
- `StaticResourceExtension(object resourceKey)`
- `StaticResourceExtension.ResourceKey`
- `ResolveByNameExtension(string name)`
- `ResolveByNameExtension.Name`

Reference source files:

- `src/Avalonia.Base/Data/RelativeSource.cs`
- `src/Avalonia.Base/Data/ReflectionBinding.cs`
- `src/Markup/Avalonia.Markup/Data/Binding.cs`
- `src/Markup/Avalonia.Markup.Xaml/MarkupExtensions/ReflectionBindingExtension.cs`
- `src/Markup/Avalonia.Markup.Xaml/MarkupExtensions/RelativeSourceExtension.cs`
- `src/Markup/Avalonia.Markup.Xaml/MarkupExtensions/StaticResourceExtension.cs`
- `src/Markup/Avalonia.Markup.Xaml/MarkupExtensions/ResolveByNameExtension.cs`

## `RelativeSource` Core Model

`RelativeSource` describes where binding source values come from relative to the target.

Important options:

- `RelativeSourceMode.DataContext`
- `RelativeSourceMode.TemplatedParent`
- `RelativeSourceMode.Self`
- `RelativeSourceMode.FindAncestor`

Ancestor search controls:

- `AncestorType`
- `AncestorLevel` (1-based)
- `Tree` (`TreeType.Visual` or `TreeType.Logical`)

Notes:

- Default `Mode` is `RelativeSourceMode.FindAncestor`.
- Default `AncestorLevel` is `1`.
- Default `Tree` is visual-tree lookup unless set to logical.

## `RelativeSourceExtension` in XAML

Use `RelativeSourceExtension` for inline relative-source markup. This is the canonical style used by Avalonia themes and samples.

Core members:

- `RelativeSourceExtension()`
- `RelativeSourceExtension(RelativeSourceMode mode)`
- `Mode`
- `AncestorType`
- `Tree`
- `AncestorLevel`
- `ProvideValue(IServiceProvider)`

Inline example:

```xml
<TextBlock xmlns="https://github.com/avaloniaui"
           xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
           Text="{Binding RelativeSource={RelativeSource Mode=Self}, Path=Tag}" />
```

Ancestor example (canonical inline syntax):

```xml
<TextBlock xmlns="https://github.com/avaloniaui"
           xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
           xmlns:controls="using:MyApp.Controls">
  <TextBlock.Text>
    <Binding Path="Header"
             RelativeSource="{RelativeSource Mode=FindAncestor, AncestorType=controls:CardHost, AncestorLevel=1, Tree=Visual}" />
  </TextBlock.Text>
</TextBlock>
```

## Wiring `RelativeSource` in `Binding` and `ReflectionBindingExtension`

Two common surfaces:

1. `Binding.RelativeSource` (`Avalonia.Markup.Data.Binding`)
2. `ReflectionBindingExtension.RelativeSource`

`ReflectionBindingExtension` usage is explicit in XAML:

```xml
<TextBlock xmlns="https://github.com/avaloniaui"
           xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
           Text="{ReflectionBinding RelativeSource={RelativeSource Self}, Path=Tag}" />
```

Equivalent C# pattern with `Binding.RelativeSource`:

```csharp
using Avalonia.Data;
using Avalonia.Markup.Data;

textBlock.Bind(TextBlock.TextProperty, new Binding("Tag")
{
    RelativeSource = new RelativeSource(RelativeSourceMode.Self)
});
```

Culture behavior on reflection path:

- `ReflectionBindingExtension.ConverterCulture` sets converter culture explicitly.
- If omitted, converter path falls back to current culture behavior from reflection binding.

## `FindAncestor` Patterns (Visual vs Logical Tree)

Use visual tree for template/composition ancestry:

```xml
<TextBlock Text="{Binding RelativeSource={RelativeSource Mode=FindAncestor, AncestorType={x:Type Border}, AncestorLevel=1, Tree=Visual}, Path=Name}" />
```

Use logical tree for content/ownership ancestry:

```xml
<TextBlock Text="{Binding RelativeSource={RelativeSource Mode=FindAncestor, AncestorType={x:Type Window}, AncestorLevel=1, Tree=Logical}, Path=Title}" />
```

Rule of thumb:

- prefer `Tree=Visual` for template/visual composition,
- use `Tree=Logical` when logical ownership is what matters.

## `StaticResourceExtension` Semantics

`StaticResourceExtension` resolves a resource key during markup value provisioning.

Key APIs:

- `StaticResourceExtension`
- `StaticResourceExtension()`
- `StaticResourceExtension(object resourceKey)`
- `ResourceKey`
- `ProvideValue(IServiceProvider)`

Example:

```xml
<StackPanel xmlns="https://github.com/avaloniaui"
            xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml">
  <StackPanel.Resources>
    <SolidColorBrush x:Key="AccentBrush" Color="#0A84FF" />
  </StackPanel.Resources>

  <TextBlock Foreground="{StaticResource AccentBrush}" Text="Static resource lookup" />
</StackPanel>
```

Behavior details:

- missing `ResourceKey` is an error,
- lookup walks resource-capable parents,
- when immediate value cannot be resolved in specific setter/control cases, the pipeline may return `AvaloniaProperty.UnsetValue` and complete later.

Use `StaticResource` when value is expected to be stable after load. Use `DynamicResource` for runtime-changing keys.

## `ResolveByNameExtension` Semantics

`ResolveByNameExtension` performs name-scope lookup by string name.

Key APIs:

- `ResolveByNameExtension`
- `ResolveByNameExtension(string name)`
- `Name`
- `ProvideValue(IServiceProvider)`

Example:

```xml
<Grid xmlns="https://github.com/avaloniaui"
      xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml">
  <Border x:Name="Host" />
  <TextBlock Tag="{ResolveByName Host}" />
</Grid>
```

Behavior details:

- lookup uses the active `INameScope`,
- if no name scope exists, result is `null`,
- asynchronous name resolution paths can temporarily return `AvaloniaProperty.UnsetValue` and apply value once available.

## `Binding.TypeResolver` and Type Name Resolution

`Binding.TypeResolver` is a function hook for resolving type names used by reflection binding path parsing.

API:

- `Binding.TypeResolver`

`ReflectionBindingExtension` sets type-resolution behavior from service provider context when it creates the binding instance.

Use cases:

- plugin/module type resolution,
- custom namespace or alias mapping for runtime binding paths.

Most apps should use default resolution and avoid custom `TypeResolver` unless runtime composition requires it.

## Best Practices

1. Prefer explicit relative-source intent.
- Use `Mode=Self`, `Mode=TemplatedParent`, or `Mode=FindAncestor` deliberately.

2. Set `Tree` intentionally for ancestor lookups.
- Wrong tree choice is a common reason for unresolved bindings.

3. Keep `AncestorLevel` minimal.
- `AncestorLevel=1` is the default and usually correct.

4. Use `StaticResource` for stable keys.
- Switch to `DynamicResource` only when runtime key changes are required.

5. Keep name-scope lookups local.
- Prefer direct element references in templates/views before adding generic name-resolution indirection.

6. Treat reflection binding knobs as opt-in.
- `Binding.TypeResolver` and reflection markup paths are advanced configuration points.

## Troubleshooting

1. Ancestor binding never resolves.
- Verify `AncestorType` and `Tree` (`Visual` vs `Logical`) match actual tree shape.

2. Ancestor lookup returns wrong node.
- Check `AncestorLevel`; it is 1-based and defaults to first match.

3. `StaticResource` throws not found.
- Confirm `ResourceKey` exists in local/app/theme dictionaries at lookup time.

4. Name lookup returns `null` or stays unset.
- Ensure the target is inside a valid `INameScope` and the named element is registered there.

5. Reflection binding path type segments fail.
- Validate or remove custom `Binding.TypeResolver`; fallback to default when possible.
