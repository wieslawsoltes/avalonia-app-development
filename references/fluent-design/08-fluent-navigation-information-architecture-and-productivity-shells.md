# Fluent Navigation, Information Architecture, and Productivity Shells

## Table of Contents
1. Scope and Primary APIs
2. Fluent Information-Architecture Rules
3. Fluent Navigation Patterns
4. Productivity Shell Guidance
5. AOT and Runtime Notes
6. Do and Don't Guidance
7. Troubleshooting
8. Official Resources

## Scope and Primary APIs

Use this reference to shape Fluent shells that feel product-grade, not just Fluent-colored.

Primary APIs:
- `SplitView`, `TabControl`, `TreeView`
- `ListBox`, `MenuFlyout`, `TransitioningContentControl`
- `Grid`, `ScrollViewer`
- `Window`, `Flyout`

This file covers:
- selecting the right Fluent shell model,
- structuring navigation for productivity tools,
- keeping local and global navigation distinct,
- using motion and layout to communicate scope.

## Fluent Information-Architecture Rules

Fluent productivity UI should feel:
- clear about location,
- consistent in action priority,
- efficient for repeat use,
- calm under high information density.

Rules:
- keep global navigation persistent when the product area is broad,
- use local navigation only for scope inside the current area,
- let information architecture carry complexity before motion does,
- reduce mode-switching where possible.

## Fluent Navigation Patterns

Choose the primary model by product shape:

- `SplitView` for app-area navigation,
- `TabControl` for peer workspaces, editors, or views,
- `TreeView` for hierarchical exploration,
- `MenuFlyout` for contextual or overflow commands.

```xml
<SplitView xmlns="https://github.com/avaloniaui"
           xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
           DisplayMode="Inline"
           IsPaneOpen="True">
  <SplitView.Pane>
    <ListBox ItemContainerTheme="{StaticResource FluentNavItemTheme}" />
  </SplitView.Pane>

  <Grid RowDefinitions="Auto,*">
    <TabControl Grid.Row="0" />
    <TransitioningContentControl Grid.Row="1"
                                 PageTransition="{StaticResource FluentShellTransition}"
                                 Content="{CompiledBinding CurrentView}" />
  </Grid>
</SplitView>
```

Guidance:
- make the left rail stable,
- use tabs for sibling workspaces, not for every nested state,
- keep contextual actions near the content they affect,
- keep shell chrome quieter than the active workspace.

## Productivity Shell Guidance

Fluent shells should optimize for repeated professional use:
- commands are predictable,
- filters and status are discoverable,
- dense surfaces remain readable,
- advanced actions stay available without dominating the UI.

Use teaching surfaces sparingly after onboarding. Persistent productivity shells should favor stable structure over constant guidance surfaces.

## AOT and Runtime Notes

- Keep shell structure and navigation themes in compiled XAML.
- Use page transitions to support orientation, not to mask poor routing choices.
- Keep navigation state model-driven so shell motion and disclosure stay deterministic.

## Do and Don't Guidance

Do:
- use one dominant shell model,
- keep left-rail, tabs, and contextual commands in distinct roles,
- support repeat workflows over first-run spectacle.

Do not:
- use overflow menus as the real app map,
- layer several competing navigation metaphors into one workspace,
- let shell chrome overpower task content.

## Troubleshooting

1. The app looks Fluent but still feels hard to learn.
- The issue is likely shell structure and scope, not token styling.

2. Power users feel slowed down.
- Reduce navigation hops and make common actions more local to the workspace.

3. Global and local navigation feel interchangeable.
- Reassign one model to app-wide scope and the other to area-specific scope.

## Official Resources

- Fluent 2 navigation guidance: [fluent2.microsoft.design/components/web/react/core/nav/usage](https://fluent2.microsoft.design/components/web/react/core/nav/usage)
- Fluent 2 tab list guidance: [fluent2.microsoft.design/components/web/react/core/tablist/usage](https://fluent2.microsoft.design/components/web/react/core/tablist/usage)
- Navigation basics for Windows apps: [learn.microsoft.com/en-us/windows/apps/design/basics/navigation-basics](https://learn.microsoft.com/en-us/windows/apps/design/basics/navigation-basics)
- List-details view guidance: [learn.microsoft.com/en-us/windows/apps/design/controls/list-details](https://learn.microsoft.com/en-us/windows/apps/design/controls/list-details)
