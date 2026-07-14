# Mithaq Shader Performance Notes

Ticket: P5.06 — Shader Development

Status: PASS WITH CONDITIONS

## Device / Browser Used

- Browser: Chromium headless shell from Playwright cache
- Rendering path: built Vite output served through a local static server
- Viewport for captures: `1440 x 960`

## Particle Count

| Mode | Count |
| --- | ---: |
| Desktop | 220 particles |
| Low/mobile | 80 particles |
| Reduced motion | 36 particles |

## FPS Observation

No precise FPS profiler was run in this ticket. The sandbox rendered and captured successfully without browser page errors or visible instability during screenshot automation. Real FPS profiling remains pending for P5.08 Mobile Performance Audit.

## Visible Performance Issues

- No shader compile errors were captured.
- Browser console emitted `ReadPixels` GPU stall warnings during screenshot capture. These are expected from automated screenshot readback and are not considered runtime shader errors.
- Vite build emitted a large chunk warning due to Three/R3F bundle size. This is acceptable for an isolated sandbox but should be optimized during architecture work.

## Optimization Notes

- Particle count is capped at 220 desktop and 80 low/mobile.
- No post-processing or bloom dependency was added.
- No raymarching, heavy texture loops, or full-screen noise passes were used.
- All shaders are simple overlay/proxy materials intended for later targeted integration.

## Mobile Simplification Recommendation

- Use low mode by default on constrained devices.
- Disable particles first if frame time rises.
- Use static final states for reduced motion.
- Avoid long pinned mobile animation sections until P5.08 validation.
