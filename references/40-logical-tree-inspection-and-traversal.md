# Logical Tree Inspection and Traversal

## Table of Contents
1. Scope and APIs
2. Logical Tree Fundamentals
3. Traversal and Query Patterns
4. Logical Lifecycle and Root Awareness
5. Resource/DataContext/Template Lookup Implications
6. Debug Inspection Patterns
7. Best Practices
8. Troubleshooting

## Scope and APIs

Primary APIs:
- `ILogical.LogicalParent`
- `ILogical.LogicalChildren`
- `ILogical.IsAttachedToLogicalTree`
- `ILogical.AttachedToLogicalTree`
- `ILogical.DetachedFromLogicalTree`
- `LogicalExtensions.GetLogicalAncestors(...)`
- `LogicalExtensions.GetSelfAndLogicalAncestors(...)`
- `LogicalExtensions.FindLogicalAncestorOfType<T>(...)`
- `LogicalExtensions.GetLogicalChildren(...)`
- `LogicalExtensions.GetLogicalDescendants(...)`
- `LogicalExtensions.GetSelfAndLogicalDescendants(...)`
- `LogicalExtensions.FindLogicalDescendantOfType<T>(...)`
- `LogicalExtensions.GetLogicalParent(...)`
- `LogicalExtensions.GetLogicalSiblings(...)`
- `LogicalExtensions.IsLogicalAncestorOf(...)`
- `LogicalTreeAttachmentEventArgs`
- `StyledElement.OnAttachedToLogicalTree(...)`
- `StyledElement.OnDetachedFromLogicalTree(...)`

Reference source files:
- `src/Avalonia.Base/LogicalTree/ILogical.cs`
- `src/Avalonia.Base/LogicalTree/LogicalExtensions.cs`
- `src/Avalonia.Base/LogicalTree/LogicalTreeAttachmentEventArgs.cs`
- `src/Avalonia.Base/StyledElement.cs`
- `src/Avalonia.Controls/Templates/DataTemplateExtensions.cs`

## Logical Tree Fundamentals

The logical tree models ownership/composition semantics and is used heavily for:
- resource lookup,
- inherited properties like `DataContext`,
- data template resolution scopes,
- containment semantics that may differ from rendered visuals.

Logical relationships can differ from visual relationships (for example popups, presenters, overlays).

## Traversal and Query Patterns

### Find logical ancestor/descendant

```csharp
using Avalonia.Controls;
using Avalonia.LogicalTree;

var ownerItemsControl = this.FindLogicalAncestorOfType<ItemsControl>();
var firstPopup = this.FindLogicalDescendantOfType<Popup>();
```

### Enumerate logical ancestors

```csharp
using Avalonia.LogicalTree;

foreach (var node in myElement.GetSelfAndLogicalAncestors())
{
    Console.WriteLine(node.GetType().Name);
}
```

### Parent/sibling inspection

```csharp
using Avalonia.LogicalTree;

var parent = myElement.GetLogicalParent();
var siblings = myElement.GetLogicalSiblings();
bool isAncestor = parent.IsLogicalAncestorOf(myElement);
```

Use these patterns when diagnosing ownership and scoping issues rather than rendering issues.

## Logical Lifecycle and Root Awareness

Attachment hooks for logical-root-dependent setup:

```csharp
using Avalonia.LogicalTree;

protected override void OnAttachedToLogicalTree(LogicalTreeAttachmentEventArgs e)
{
    base.OnAttachedToLogicalTree(e);
    // e.Root, e.Source, e.Parent available
}

protected override void OnDetachedFromLogicalTree(LogicalTreeAttachmentEventArgs e)
{
    base.OnDetachedFromLogicalTree(e);
    // cleanup logical-scope subscriptions/resources
}
```

Guidance:
- Check `IsAttachedToLogicalTree` before relying on logical ancestor scopes.
- Prefer logical attach/detach hooks for resource/data scope initialization.

## Resource/DataContext/Template Lookup Implications

Logical ancestry directly affects common framework behavior:
- Data template resolution traverses logical `IDataTemplateHost` ancestors.
- Resource lookup often relies on logical ownership chain.
- `DataContext` propagation is logical-tree-driven.

Practical implication:
- If template/resource resolution differs from expectation, inspect logical ancestors first.

## Debug Inspection Patterns

Quick logical tree dump helper:

```csharp
using Avalonia.LogicalTree;

static void DumpLogical(ILogical logical, int depth = 0)
{
    Console.WriteLine($"{new string(' ', depth * 2)}{logical.GetType().Name}");
    foreach (var child in logical.GetLogicalChildren())
    {
        DumpLogical(child, depth + 1);
    }
}
```

Use this to verify containment and scope boundaries in composite controls.

## Best Practices

- Use logical tree APIs for ownership/scope concerns, not rendering geometry.
- Keep logical traversal deterministic and side-effect free.
- Avoid expensive full-tree scans on every property/input event.
- Pair logical attach setup with logical detach cleanup.
- Validate assumptions in controls that use presenters/popups.

## Troubleshooting

1. Resource or `DataContext` not found:
- Expected logical parent chain is different than assumed.
- Control not attached to rooted logical tree.

2. Template lookup chooses unexpected template:
- A closer logical `IDataTemplateHost` overrides app-level templates.

3. Logical ancestor query returns `null`:
- Query runs before attachment.
- Element is hosted under a different logical branch.

4. Visual behavior differs from logical expectations:
- Control composition splits logical and visual trees (presenters/popups/overlays).
