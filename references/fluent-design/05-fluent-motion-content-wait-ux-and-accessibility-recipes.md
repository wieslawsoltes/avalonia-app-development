# Fluent Motion, Content Tone, Wait UX, and Accessibility Recipes

## Scope and Primary APIs

Use this reference to finish Fluent experiences with restrained motion and strong usability.

Primary APIs:
- `Transitions`
- `BrushTransition`, `BoxShadowsTransition`, `TransformOperationsTransition`
- `ProgressBar`, `TransitioningContentControl`
- `AutomationProperties`
- focus and pseudo-class styling

## Motion Recipe

```xml
<Border xmlns="https://github.com/avaloniaui"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        Classes="fluent-card"
        RenderTransform="translateY(0px)">
  <Border.Transitions>
    <Transitions>
      <TransformOperationsTransition Property="RenderTransform" Duration="0:0:0.16" />
      <BoxShadowsTransition Property="BoxShadow" Duration="0:0:0.16" />
    </Transitions>
  </Border.Transitions>
</Border>
```

## Wait and Content Tone

Guidance:
- keep wait states informative and short,
- prefer calm copy over marketing tone in productivity flows,
- expose one clear recovery action for errors,
- keep empty states constructive, not apologetic.

```xml
<StackPanel xmlns="https://github.com/avaloniaui"
            xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
            Spacing="12">
  <TextBlock Text="Checking deployment readiness" />
  <ProgressBar IsIndeterminate="True" />
  <TextBlock Foreground="{DynamicResource Brush.Text.Secondary}"
             Text="This usually takes a few seconds." />
</StackPanel>
```

## Accessibility Review

- Keep focus-visible styling prominent.
- Pair icon-only actions with labels or automation metadata.
- Preserve contrast after palette overrides.
- Keep motion optional or minimal in repetitive workflows.

## AOT and Runtime Notes

- Prefer short transitions rather than heavier custom animation pipelines.
- Keep wait and empty states template-light in highly dynamic screens.

## Do and Don't Guidance

Do:
- use motion to confirm changes,
- keep wait copy calm and actionable,
- review accessibility after palette and density changes.

Do not:
- animate every shell interaction,
- hide focus under hover treatment,
- ship Fluent branding while neglecting wait UX and accessibility.

## Troubleshooting

1. Fluent UI feels flashy rather than calm.
- Reduce animation distance, accent saturation, and shadow depth together.

2. Wait states feel generic.
- Write task-specific copy and provide clear next actions for failure or empty results.

3. Accessibility regresses after brand theming.
- Re-check contrast, focus visibility, and automation names across both variants.

## Official Resources

- Fluent 2 motion: [fluent2.microsoft.design/styles/motion](https://fluent2.microsoft.design/styles/motion/)
- Fluent 2 wait UX: [fluent2.microsoft.design/wait-ux](https://fluent2.microsoft.design/wait-ux)
- Fluent 2 accessibility: [fluent2.microsoft.design/accessibility](https://fluent2.microsoft.design/accessibility)
