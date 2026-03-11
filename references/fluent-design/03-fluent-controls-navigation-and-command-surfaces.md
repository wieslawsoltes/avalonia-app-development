# Fluent Controls, Navigation, and Command Surfaces in Avalonia

## Scope and Primary APIs

Use this reference to build Fluent-aligned controls and interaction surfaces.

Primary APIs:
- `ControlTheme`, `StyledElement.Theme`
- `Button`, `TextBox`, `ToggleSwitch`, `ListBox`, `TabControl`, `AutoCompleteBox`
- `ItemsControl.ItemContainerTheme`
- `MenuFlyout`, `MenuItem`, `Flyout.FlyoutPresenterTheme`

## Fluent Control Variant Example

```xml
<ControlTheme xmlns="https://github.com/avaloniaui"
              xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
              x:Key="FluentPrimaryButtonTheme"
              TargetType="Button"
              BasedOn="{StaticResource {x:Type Button}}">
  <Setter Property="Padding" Value="14,10" />
  <Setter Property="CornerRadius" Value="8" />
  <Setter Property="Background" Value="{DynamicResource Brush.Brand.Primary}" />
  <Setter Property="Foreground" Value="White" />
  <Setter Property="BorderBrush" Value="{DynamicResource Brush.Brand.Primary}" />

  <Style Selector="^:pointerover">
    <Setter Property="Background" Value="{DynamicResource Brush.Brand.Secondary}" />
  </Style>
</ControlTheme>
```

## Navigation and Lists

```xml
<ListBox xmlns="https://github.com/avaloniaui"
         xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
         ItemContainerTheme="{StaticResource FluentNavItemTheme}" />
```

Use:
- `SplitView` plus themed list items for Fluent side navigation,
- `TabControl` for workspace switching,
- `MenuFlyout` for lightweight overflow actions.

## Command Surfaces

```xml
<Button xmlns="https://github.com/avaloniaui"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        Theme="{StaticResource FluentPrimaryButtonTheme}"
        Content="Deploy">
  <Button.ContextFlyout>
    <MenuFlyout FlyoutPresenterTheme="{StaticResource FluentFlyoutPresenterTheme}">
      <MenuItem Header="Deploy now" />
      <MenuItem Header="Schedule rollout" />
    </MenuFlyout>
  </Button.ContextFlyout>
</Button>
```

## AOT and Runtime Notes

- Prefer shared `ControlTheme` resources over repeated local styles.
- Keep command-surface state changes selector-driven rather than template-replacement-driven.

## Do and Don't Guidance

Do:
- base your variants on Fluent defaults,
- theme item containers and flyout presenters explicitly,
- keep command surfaces calm and predictable.

Do not:
- overload every action row with primary styling,
- use accent treatment for low-priority actions,
- invent many independent control families in one product.

## Troubleshooting

1. Fluent controls look disconnected from stock controls.
- Rebase your themes on the stock control type and reduce the number of overridden primitives.

2. Navigation feels heavy.
- Simplify borders and shadows before reducing action density.

3. Overflow menus look off-brand.
- Apply the same semantic surface and border treatment used by cards and dialogs.

## Official Resources

- Avalonia control themes: [docs.avaloniaui.net/docs/basics/user-interface/styling/control-themes](https://docs.avaloniaui.net/docs/basics/user-interface/styling/control-themes)
- Fluent 2 controls: [fluent2.microsoft.design/components/web/react](https://fluent2.microsoft.design/components/web/react)
