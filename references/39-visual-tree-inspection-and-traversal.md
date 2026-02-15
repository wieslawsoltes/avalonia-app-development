# Visual Tree Inspection and Traversal

## Table of Contents
1. Scope and APIs
2. Visual Tree Fundamentals
3. Traversal and Query Patterns
4. Hit Testing and Bounds Inspection
5. Lifecycle and Root Awareness
6. Debug Inspection Patterns
7. Best Practices
8. Troubleshooting

## Scope and APIs

Primary APIs:
- `Visual.VisualParent`
- `Visual.VisualChildren`
- `Visual.AttachedToVisualTree`
- `Visual.DetachedFromVisualTree`
- `VisualExtensions.GetVisualAncestors(...)`
- `VisualExtensions.GetSelfAndVisualAncestors(...)`
- `VisualExtensions.FindAncestorOfType<T>(...)`
- `VisualExtensions.FindDescendantOfType<T>(...)`
- `VisualExtensions.GetVisualChildren(...)`
- `VisualExtensions.GetVisualDescendants(...)`
- `VisualExtensions.GetSelfAndVisualDescendants(...)`
- `VisualExtensions.GetVisualParent(...)`
- `VisualExtensions.GetVisualRoot(...)`
- `VisualExtensions.GetVisualAt(...)`
- `VisualExtensions.GetVisualsAt(...)`
- `VisualExtensions.GetTransformedBounds(...)`
- `VisualExtensions.IsAttachedToVisualTree(...)`
- `VisualExtensions.IsVisualAncestorOf(...)`
- `VisualTreeAttachmentEventArgs`
- `TopLevel.GetTopLevel(...)`

Reference source files:
- `src/Avalonia.Base/Visual.cs`
- `src/Avalonia.Base/VisualTree/VisualExtensions.cs`
- `src/Avalonia.Base/VisualTreeAttachmentEventArgs.cs`
- `src/Avalonia.Controls/TopLevel.cs`

## Visual Tree Fundamentals

The visual tree is the rendered structure used for:
- layout and rendering,
- transforms and clipping,
- hit testing and input routing.

Key properties:
- `VisualParent`: immediate rendered parent.
- `VisualChildren`: immediate rendered children.
- `GetVisualRoot()`: current `IRenderRoot` (often a `TopLevel`).

Use the visual tree when reasoning about on-screen behavior.

## Traversal and Query Patterns

### Ancestor/descendant queries

```csharp
using Avalonia.Controls;
using Avalonia.VisualTree;

var scroll = myControl.FindAncestorOfType<ScrollViewer>();
var button = myRoot.FindDescendantOfType<Button>();
```

### Enumerate ancestors

```csharp
using Avalonia.VisualTree;

foreach (var ancestor in myControl.GetSelfAndVisualAncestors())
{
    Console.WriteLine(ancestor.GetType().Name);
}
```

### Enumerate descendants

```csharp
using Avalonia.VisualTree;

foreach (var descendant in myRoot.GetVisualDescendants())
{
    // inspection, diagnostics, selective filtering
}
```

### Root/top-level lookup

```csharp
using Avalonia.Controls;

TopLevel? host = TopLevel.GetTopLevel(myControl);
```

## Hit Testing and Bounds Inspection

Point hit testing:

```csharp
using Avalonia;
using Avalonia.VisualTree;

Point p = new Point(120, 40); // point in myRoot coordinate space
var first = myRoot.GetVisualAt(p);
var all = myRoot.GetVisualsAt(p, v => v.IsVisible);
```

Transformed bounds inspection:

```csharp
using Avalonia.VisualTree;

var tb = myControl.GetTransformedBounds();
if (tb is { } bounds)
{
    var clip = bounds.Clip;
    var transform = bounds.Transform;
}
```

Use this when debugging clipping, transforms, or unexpected hit targets.

## Lifecycle and Root Awareness

Attach/detach events are the correct points for visual-root-dependent work:

```csharp
using Avalonia;

protected override void OnAttachedToVisualTree(VisualTreeAttachmentEventArgs e)
{
    base.OnAttachedToVisualTree(e);
    // e.Root, e.Parent available here
}

protected override void OnDetachedFromVisualTree(VisualTreeAttachmentEventArgs e)
{
    base.OnDetachedFromVisualTree(e);
    // cleanup root-dependent subscriptions/resources
}
```

Guidance:
- Avoid assuming `GetVisualRoot()` is non-null before attachment.
- Prefer attach/detach hooks over constructor-time visual traversal.

## Debug Inspection Patterns

Quick visual tree dump helper:

```csharp
using Avalonia.VisualTree;

static void DumpVisual(Visual visual, int depth = 0)
{
    Console.WriteLine($"{new string(' ', depth * 2)}{visual.GetType().Name}");
    foreach (var child in visual.GetVisualChildren())
    {
        DumpVisual(child, depth + 1);
    }
}
```

Use in diagnostics, tests, and runtime asserts for template/overlay bugs.

## Best Practices

- Use visual tree APIs for rendered/layout concerns only.
- Use `includeSelf: true` deliberately when searching from a known node.
- Keep traversal out of hot render/input loops where possible.
- Cache stable query results only when lifetimes are clear.
- Always unsubscribe visual-root-dependent handlers on detach.

## Troubleshooting

1. `FindAncestorOfType` returns `null` unexpectedly:
- Control is in another visual root (popup/overlay).
- Query runs before attachment.

2. `GetVisualRoot()` is `null`:
- Element is not attached to visual tree yet.

3. Hit testing misses expected element:
- Wrong coordinate space.
- Element filtered out by visibility/filter predicate.
- Overlay/adorner consumes topmost hit.

4. Traversal results fluctuate:
- Template reapplication or virtualization changed realized visuals.
