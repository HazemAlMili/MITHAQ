# Mithaq R3F Architecture Proof of Concept

Ticket: P5.07 — R3F Architecture Proof of Concept

Status: PASS WITH CONDITIONS

## Purpose

This package validates Mithaq's core R3F architecture before production implementation. It proves a persistent canvas, scene manager, Zustand store, scroll progress mapping, scene-local progress mapping, reduced-motion handling, WebGL fallback detection, device-tier detection, and lightweight 10-scene proxy switching.

This is not the production Mithaq website. It does not implement final UI, production routes, the full opening sequence, final assets, Lenis, ScrollTrigger, or Phase 8 frontend work.

## Setup

```bash
cd D:/Clinets/MITHAQ/MITHAQ/mithaq-project-docs/mithaq-r3f-architecture-poc/poc
npm install
npm run dev
npm run build
```

## Output Summary

- Standalone Vite/R3F PoC: `poc/`
- Required captures: `captures/`
- Architecture reports: `reports/`

## Architecture Summary

- `MithaqCanvas` creates one fixed, persistent R3F canvas.
- `SceneManager` switches lightweight scene proxy components from the Zustand store.
- `mithaqStore` exposes the requested shared DOM/R3F state skeleton.
- `useScrollProgress` maps page scroll to global progress, active scene, and scene-local progress.
- `useReducedMotion`, `useWebGLSupport`, and `useDeviceTier` prove baseline accessibility and capability gates.
- `PostProcessingGate` is intentionally placeholder-only and documents conditional enablement.

## Known Conditions

- Browser testing was performed in local headless Chromium, not Safari, Samsung Internet, or physical mobile devices.
- Performance was visually inspected and architecture-level only; formal FPS/mobile profiling remains for P5.08.
- Vite production build emits a large single-chunk warning because this isolated PoC bundles Three/R3F/Drei without production code splitting.
- The validation harness supports `?scene=1..10`, `?reduced=true`, and `?webgl=false` for deterministic testing only.
