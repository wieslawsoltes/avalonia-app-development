# WinUI Style/Resource/Tree Diagnostics to Avalonia Runtime Inspection

## Table of Contents
1. Scope and APIs
2. Concept Mapping
3. Conversion Example
4. Migration Notes

## Scope and APIs

Primary WinUI APIs:

- VisualTreeHelper, XAML Live Visual Tree tooling
- resource probing via `ResourceDictionary` / `TryGetValue`

Primary Avalonia APIs:

- VisualTree.VisualExtensions, LogicalTree.LogicalExtensions
- Avalonia.Diagnostics.StyledElementExtensions.GetStyleDiagnostics
- Avalonia.Diagnostics.AvaloniaObjectExtensions.GetDiagnostic / GetValueStoreDiagnostic

## Concept Mapping

| WinUI idiom | Avalonia idiom |
|---|---|
| inspect parent/child hierarchy | inspect visual + logical trees via extensions |
| inspect applied styles in tooling | inspect applied styles via diagnostics APIs + DevTools |
| inspect runtime resource values | inspect effective property/resource diagnostics |

## Conversion Example

WinUI XAML:

```xaml
<ListView x:Name="ResultsList" />
```

WinUI C#:

```csharp
DependencyObject? current = ResultsList;
while (current is not null)
{
    current = VisualTreeHelper.GetParent(current);
}
```

Avalonia XAML:

```xaml
<ListBox x:Name="ResultsList" />
```

Avalonia C#:

```csharp
var visualParent = ResultsList.GetVisualParent();
var logicalParent = ResultsList.GetLogicalParent();

var styleDiagnostics = ResultsList.GetStyleDiagnostics();
var valueDiagnostics = ResultsList.GetDiagnostic(Control.BackgroundProperty);
```

## Migration Notes

1. Use both logical and visual tree inspection when style/resource behavior diverges.
2. Prefer deterministic diagnostic snapshots in tests for regression safety.
3. Keep diagnostics and DevTools hooks out of performance-critical production paths.
