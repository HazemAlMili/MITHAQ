# P5.07 R3F Architecture Report

## Architecture Overview

The PoC creates a standalone Vite + React + TypeScript + Three.js + React Three Fiber + Drei + Zustand sandbox. It validates the architecture that Mithaq can later use for a persistent 3D scene layer across the 10-scene landing experience.

The system uses placeholder scene proxies only. No production GLB files, shaders, routing, final UI, or full opening sequence implementation were added.

## Canvas Strategy

`poc/src/canvas/MithaqCanvas.tsx` mounts a fixed full-viewport `<Canvas>` and keeps it persistent while the active scene changes. The canvas uses a Mithaq-style camera, dark background, local warm lights, and DPR caps based on the detected device tier.

The PoC intentionally removed Drei's external HDR environment preset after validation revealed it created blocked network fetch errors in headless Chromium. The architecture now uses local lights only.

## Scene Manager Strategy

`poc/src/canvas/SceneManager.tsx` reads `activeScene` from Zustand and renders one of 10 scene proxy components:

1. Gavel Seal Opening
2. Hero / Mithaq Reveal
3. The Gap
4. The Mithaq Method
5. Training Pillars
6. Workshops Preview
7. Hall of Mentors
8. Trust & Credibility
9. FAQ
10. Final CTA

Each proxy uses distinct, lightweight placeholder geometry and a canvas label. This proves scene routing inside the persistent canvas without claiming final visuals.

## Store Strategy

`poc/src/store/mithaqStore.ts` implements the requested Zustand skeleton, including:

- scroll state
- opening state
- asset-loading placeholders
- reduced-motion state
- WebGL availability
- device tier
- nav/modal/language placeholders
- CTA source placeholder

Both DOM controls and R3F scene components read from the same store.

## Scroll Mapping Strategy

`useScrollProgress` calculates:

- global scroll progress from `window.scrollY`
- active scene from `MITHAQ_SCENE_MAP`
- scene-local progress from 0 to 1

The debug panel shows these values live. Query parameters were added for validation only: `?scene=1..10` scrolls to the mapped scene start.

## Reduced-Motion Strategy

`useReducedMotion` detects `prefers-reduced-motion` and allows a manual override through `ReducedMotionToggle`. Scene proxy rotation is disabled when reduced motion is active, while the visual state remains readable.

## WebGL Fallback Strategy

`useWebGLSupport` detects WebGL/WebGL2 availability. `WebGLFallback` displays the required fallback text and CTA placeholder when unavailable. A validation-only `?webgl=false` query forces this path for QA.

## Device-Tier Strategy

`useDeviceTier` estimates `high`, `mid`, or `low` from WebGL support, hardware concurrency, optional device memory, and mobile user agent. The tier influences DPR and postprocessing availability.

## What Was Intentionally Not Implemented

- No Next.js production app
- No final routing
- No Lenis or ScrollTrigger integration
- No production opening animation
- No production GLB imports
- No final shaders
- No real content, testimonials, workshop details, or fake data
- No Phase 8 frontend work
