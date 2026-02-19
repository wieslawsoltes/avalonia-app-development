# WinUI Style Resolution (BasedOn/Implicit) to Avalonia Selectors

## Table of Contents
1. Scope and APIs
2. Concept Mapping
3. Conversion Example
4. Migration Notes

## Scope and APIs

Primary WinUI APIs:

- Style, Setter, BasedOn, TargetType
- implicit style by `TargetType`, explicit style by `x:Key`

Primary Avalonia APIs:

- Style + selector syntax
- classes and pseudo-classes
- ControlTheme, StyledElement.Theme, StyleKeyOverride

## Concept Mapping

| WinUI idiom | Avalonia idiom |
|---|---|
| implicit style by control type | type selector (`Button`) |
| explicit style key usage | style/class/theme indirection |
| stateful style in visual states | selector + pseudo-class (`:pointerover`, `:pressed`) |
| `BasedOn` style chains | selector layering and `ControlTheme.BasedOn` |

## Conversion Example

WinUI XAML:

```xaml
<Page.Resources>
  <Style x:Key="AccentButtonStyle"
         TargetType="Button"
         BasedOn="{StaticResource DefaultButtonStyle}">
    <Setter Property="Background" Value="{ThemeResource AccentFillColorDefaultBrush}" />
  </Style>
</Page.Resources>

<Button Style="{StaticResource AccentButtonStyle}" Content="Save" />
```

WinUI C#:

```csharp
SaveButton.Style = (Style)Application.Current.Resources["AccentButtonStyle"];
```

Avalonia XAML:

```xaml
<Styles xmlns="https://github.com/avaloniaui"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml">
  <Style Selector="Button.accent">
    <Setter Property="Background" Value="{DynamicResource AccentBrush}" />
  </Style>

  <Style Selector="Button.accent:pointerover">
    <Setter Property="Opacity" Value="0.92" />
  </Style>
</Styles>

<Button Classes="accent" Content="Save" />
```

Avalonia C#:

```csharp
SaveButton.Classes.Add("accent");
```

## Migration Notes

1. Convert key-based style selection to selector/class-driven selection where possible.
2. Keep selector specificity shallow; prefer explicit classes over deeply nested selectors.
3. Use `ControlTheme` when template-level reuse is required, not only simple property overrides.
