# Mithaq Shader Known Conditions

Ticket: P5.06 — Shader Development

Status: PASS WITH CONDITIONS

## Not Tested

- Real mobile devices
- Safari/iOS WebGL behavior
- Samsung Internet
- Integrated P5.02/P5.03/P5.04/P5.05 asset scene
- Real Scene 01 opening timeline
- GSAP, Lenis, ScrollTrigger, Zustand, or production routing
- Long-running thermal/GPU stability
- Full accessibility QA in final page context

## Dependency / Build Conditions

- `npm install` succeeded with elevated/network access.
- `npm run build` passed, but elevated filesystem access was required in this environment for generated `dist` writes.
- `npm run dev` reached Vite ready state, but the sandboxed shell blocked Vite dependency-cache temp directory writes during normal execution.
- Vite uses `--configLoader runner` and `cacheDir: 'vite-cache'` to avoid `.vite-temp` config writes under `node_modules`.

## Browser / GPU Conditions

- Captures were generated through bundled Playwright using an installed Chromium headless shell executable.
- Console output included screenshot-related `ReadPixels` warnings only.
- No shader compile/page errors were captured.

## Asset Integration Conditions

- No existing P5.02-P5.05 production GLB assets were modified.
- P5.03 Seal adaptation remains conceptual; shader is currently demonstrated on a circular proxy.
- P5.04 desk ripple integration remains pending.
- Scene 03 document shader integration is not part of this ticket.

## Roadmap Conditions

- P5.07 R3F Architecture Proof of Concept remains pending.
- P5.08 Mobile Performance Audit remains pending.
- Full opening sequence implementation remains pending.
