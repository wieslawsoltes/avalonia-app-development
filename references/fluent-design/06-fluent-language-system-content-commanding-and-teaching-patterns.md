# Fluent Language System, Content, Commanding, and Teaching Patterns

## Table of Contents
1. Scope and Primary APIs
2. Fluent Language-System Rules
3. Commanding and Label Patterns
4. Teaching, Empty, and Wait Content
5. Localization and Review Rules
6. AOT and Runtime Notes
7. Do and Don't Guidance
8. Troubleshooting
9. Official Resources

## Scope and Primary APIs

Use this reference to extend Fluent beyond color, shape, and motion into content and command language.

Primary APIs:
- `TextBlock`, `SelectableTextBlock`
- `Button`, `ToggleButton`, `MenuFlyout`, `MenuItem`
- `ToolTip`, `Expander`, `TransitioningContentControl`
- `AutomationProperties`
- `ControlTheme`, `Style`

This file covers:
- Fluent content tone,
- command labeling and hierarchy,
- teaching and onboarding surfaces,
- wait, empty, and recovery language,
- localization-safe UI writing.

## Fluent Language-System Rules

Fluent content should feel:
- clear,
- calm,
- direct,
- respectful of user effort.

Practical rules:
- use sentence case,
- prefer short verb-first commands,
- keep status copy specific and actionable,
- explain recovery paths without blame,
- make the UI sound like one product, not many teams.

Good command patterns:
- `Deploy now`
- `Schedule rollout`
- `Open report`
- `Retry sync`

Weak command patterns:
- `Submit`
- `Proceed`
- `Continue`
- `OK`

## Commanding and Label Patterns

```xml
<StackPanel xmlns="https://github.com/avaloniaui"
            xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
            Spacing="8">
  <TextBlock FontSize="28"
             FontWeight="SemiBold"
             Text="Release pipeline" />
  <TextBlock Foreground="{DynamicResource Brush.Text.Secondary}"
             Text="Choose what should happen next." />

  <StackPanel Orientation="Horizontal" Spacing="8">
    <Button Theme="{StaticResource FluentPrimaryButtonTheme}" Content="Deploy now" />
    <Button Content="Schedule rollout" />
    <Button Content="View history" />
  </StackPanel>

  <Button Content="Delete environment"
          AutomationProperties.Name="Delete environment" />
</StackPanel>
```

Guidance:
- allow only one primary action in a region,
- keep secondary actions useful but quieter,
- keep destructive labels explicit,
- make icon-only actions carry automation names or visible labels,
- use helper text to reduce ambiguity before the action, not after a failure.

## Teaching, Empty, and Wait Content

```xml
<Border xmlns="https://github.com/avaloniaui"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        Padding="16"
        CornerRadius="12"
        Background="{DynamicResource Brush.Surface.Card}">
  <StackPanel Spacing="8">
    <TextBlock FontWeight="SemiBold" Text="Set up your first rollout" />
    <TextBlock Foreground="{DynamicResource Brush.Text.Secondary}"
               Text="Choose an environment, review checks, and then deploy when you are ready." />
    <Button Theme="{StaticResource FluentPrimaryButtonTheme}"
            Content="Start setup" />
  </StackPanel>
</Border>
```

Wait and recovery rules:
- explain what is happening,
- say whether the user can keep working,
- offer one clear recovery path,
- avoid vague apology-only error text,
- keep empty states constructive and forward-looking.

## Localization and Review Rules

- assume labels will grow after localization,
- keep button text concise enough to wrap gracefully,
- keep related labels parallel,
- review capitalization, punctuation, and line breaks together,
- audit teaching surfaces for tone drift after product reviews.

## AOT and Runtime Notes

- Keep language-system styling in shared themes and helpers, not in page-local ad hoc markup.
- Prefer stable control themes and text-role styles over runtime content-specific styling branches.

## Do and Don't Guidance

Do:
- use precise verbs,
- align primary/secondary/danger labels with visual priority,
- treat onboarding, empty, wait, and error content as part of the design system.

Do not:
- ship Fluent visuals with generic or inconsistent copy,
- use button text as the only place where workflow meaning is explained,
- rely on placeholder text to carry important instructions.

## Troubleshooting

1. Fluent UI still feels generic.
- The visual language may be fine, but the command and status language is not specific enough.

2. Primary actions feel unclear.
- Rewrite labels around user intent and make supporting text reduce uncertainty.

3. Onboarding feels separate from the product.
- Reuse the same typography, spacing, tone, and action hierarchy used in the main shell.

## Official Resources

- Fluent 2 content design: [fluent2.microsoft.design/content-design](https://fluent2.microsoft.design/content-design)
- Fluent 2 design principles: [fluent2.microsoft.design/design-principles](https://fluent2.microsoft.design/design-principles)
- Fluent 2 onboarding: [fluent2.microsoft.design/onboarding](https://fluent2.microsoft.design/onboarding/)
- Fluent 2 wait UX: [fluent2.microsoft.design/wait-ux](https://fluent2.microsoft.design/wait-ux)
- Content design basics for Windows apps: [learn.microsoft.com/en-us/windows/apps/design/basics/content-basics](https://learn.microsoft.com/en-us/windows/apps/design/basics/content-basics)
- Buttons for Windows apps: [learn.microsoft.com/en-us/windows/apps/design/controls/buttons](https://learn.microsoft.com/en-us/windows/apps/design/controls/buttons)
- Microsoft Style Guide capitalization: [learn.microsoft.com/en-us/style-guide/capitalization](https://learn.microsoft.com/en-us/style-guide/capitalization)
- Microsoft Style Guide command button: [learn.microsoft.com/en-us/style-guide/a-z-word-list-term-collections/c/command-button](https://learn.microsoft.com/en-us/style-guide/a-z-word-list-term-collections/c/command-button)
