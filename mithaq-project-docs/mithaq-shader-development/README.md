# Mithaq Shader Development

Ticket: P5.06 — Shader Development

Status: PASS WITH CONDITIONS

## Purpose

This package creates an isolated React/Vite/R3F shader sandbox for Mithaq's opening FX research. It includes reusable shader files and demo components for:

1. Desk ripple shader
2. Controlled fracture-lines shader
3. Seal emergence / reveal shader
4. Atmospheric gold dust particles shader

This is not the full opening sequence, not production Scene 01, and not a frontend architecture implementation.

## Setup Commands

```bash
cd mithaq-project-docs/mithaq-shader-development/sandbox
npm install
```

## Run Commands

```bash
npm run dev
```

## Build Commands

```bash
npm run build
```

## Shader List

| Shader | Files |
| --- | --- |
| Desk ripple | `sandbox/src/shaders/ripple.vert`, `sandbox/src/shaders/ripple.frag` |
| Fracture lines | `sandbox/src/shaders/fracture-lines.vert`, `sandbox/src/shaders/fracture-lines.frag` |
| Seal emergence | `sandbox/src/shaders/seal-emergence.vert`, `sandbox/src/shaders/seal-emergence.frag` |
| Atmospheric particles | `sandbox/src/shaders/atmospheric-particles.vert`, `sandbox/src/shaders/atmospheric-particles.frag` |

## Output Summary

| Output | Path |
| --- | --- |
| Sandbox app | `sandbox/` |
| Shader captures | `captures/` |
| Reports | `reports/` |

## Known Conditions

- `npm install` succeeded, but required network/elevated execution in this environment.
- `npm run build` succeeded; elevated filesystem access was required because this sandbox blocks some Vite/Rollup generated output writes.
- `npm run dev` reached Vite ready state, but this sandbox environment blocked Vite dependency-cache writes in normal execution; final dev validation remains conditional.
- Screenshots were captured from the built sandbox using bundled Playwright and a local static server.
- Final P5.07 R3F architecture integration, P5.08 mobile performance testing, and full asset integration remain pending.
