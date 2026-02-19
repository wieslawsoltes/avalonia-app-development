# WinUI Visual Tree / Logical Tree / NameScope to Avalonia

## Table of Contents
1. Scope and APIs
2. Concept Mapping
3. Conversion Example
4. Migration Notes

## Scope and APIs

Primary WinUI APIs:

- VisualTreeHelper.GetParent, GetChildrenCount, GetChild
- FrameworkElement.Parent, FindName, GetTemplateChild

Primary Avalonia APIs:

- VisualTree.VisualExtensions (`GetVisualParent`, `GetVisualChildren`, `FindDescendantOfType`)
- LogicalTree.LogicalExtensions (`GetLogicalParent`, `GetLogicalChildren`, `GetLogicalAncestors`)
- NameScope, NameScopeExtensions.Find / FindNameScope
- TemplateAppliedEventArgs.NameScope, StyledElement.TemplatedParent

## Concept Mapping

| WinUI idiom | Avalonia idiom |
|---|---|
| visual tree traversal via `VisualTreeHelper` | visual tree traversal via `VisualExtensions` |
| parent traversal from `FrameworkElement.Parent` | logical parent traversal via `GetLogicalParent` |
| `GetTemplateChild("PART_...")` | `TemplateAppliedEventArgs.NameScope.Find<T>("PART_...")` |
| template parent semantics | `TemplatedParent` |

## Conversion Example

WinUI XAML:

```xaml
<ControlTemplate TargetType="local:StatusChip">
  <Border x:Name="PART_Indicator" />
</ControlTemplate>
```

WinUI C#:

```csharp
protected override void OnApplyTemplate()
{
    base.OnApplyTemplate();
    _indicator = GetTemplateChild("PART_Indicator") as Border;

    var visualParent = VisualTreeHelper.GetParent(this);
    var logicalParent = Parent;
}
```

Avalonia XAML:

```xaml
<ControlTheme TargetType="local:StatusChip">
  <Setter Property="Template">
    <ControlTemplate>
      <Border x:Name="PART_Indicator" />
    </ControlTemplate>
  </Setter>
</ControlTheme>
```

Avalonia C#:

```csharp
protected override void OnApplyTemplate(TemplateAppliedEventArgs e)
{
    base.OnApplyTemplate(e);
    _indicator = e.NameScope.Find<Border>("PART_Indicator");

    var visualParent = this.GetVisualParent();
    var logicalParent = this.GetLogicalParent();
    var templatedParent = TemplatedParent;
}
```

## Migration Notes

1. Keep visual-tree and logical-tree concerns separate; they diverge in templated and item-generated UI.
2. Port template-part access to `NameScope`-based lookup inside `OnApplyTemplate`.
3. Avoid long-lived cached tree references when controls can be reparented or re-templated.
