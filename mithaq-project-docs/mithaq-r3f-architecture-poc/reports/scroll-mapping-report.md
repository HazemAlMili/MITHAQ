# P5.07 Scroll Mapping Report

## Scene Map

| Scene | Label | Start | End |
| ---: | --- | ---: | ---: |
| 1 | Gavel Seal Opening | 0.00 | 0.10 |
| 2 | Hero / Mithaq Reveal | 0.10 | 0.22 |
| 3 | The Gap | 0.22 | 0.37 |
| 4 | The Mithaq Method | 0.37 | 0.50 |
| 5 | Training Pillars | 0.50 | 0.62 |
| 6 | Workshops Preview | 0.62 | 0.72 |
| 7 | Hall of Mentors | 0.72 | 0.82 |
| 8 | Trust & Credibility | 0.82 | 0.88 |
| 9 | FAQ | 0.88 | 0.94 |
| 10 | Final CTA | 0.94 | 1.00 |

## Active Scene Calculation

`getSceneByProgress(progress)` selects the scene where:

```ts
progress >= scene.start && progress < scene.end
```

If progress reaches the final boundary, Scene 10 is returned.

## Scene Progress Calculation

Scene-local progress uses:

```ts
mapRange(globalProgress, activeScene.start, activeScene.end)
```

The value is clamped from 0 to 1 and exposed through Zustand as `sceneProgress`.

## Validation Notes

All 10 scene query states were tested in Chromium against the built app. Each state mounted a canvas and showed the expected active scene in the debug panel.

## Edge Cases

- The final `progress = 1` boundary falls back to Scene 10.
- Scene-local progress is clamped to avoid negative or above-one values.
- Query navigation is validation-only and should not be carried into final routing without explicit production review.

## Limitations

- The scroll container uses simple section blocks rather than final content.
- Pinning, Lenis, ScrollTrigger, and production scroll smoothing remain out of scope.
