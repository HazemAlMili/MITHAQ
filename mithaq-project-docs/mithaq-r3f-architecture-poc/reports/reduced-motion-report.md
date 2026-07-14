# P5.07 Reduced Motion Report

## OS Preference Detection

`useReducedMotion` reads:

```ts
window.matchMedia('(prefers-reduced-motion: reduce)')
```

The result is stored in Zustand as `reducedMotion`.

## Manual Override

`ReducedMotionToggle` writes a local override to:

```txt
mithaq-reduced-motion-override
```

The toggle is visible in the debug panel and updates the shared store immediately. The validation-only query `?reduced=true` also forces the reduced-motion state for screenshots.

## Scene Behavior

Scene proxy motion uses `AnimatedGroup`. When `reducedMotion` is true, the group stops applying per-frame rotation. Geometry remains visible and readable.

## Animations Disabled

- Proxy object idle rotation
- Any implied camera/object motion inside proxy groups
- Postprocessing availability through `PostProcessingGate`

## Fallback Limitations

This ticket proves architecture-level reduced-motion handling only. Final reduced-motion static posters and page-level content equivalents remain later implementation work.
