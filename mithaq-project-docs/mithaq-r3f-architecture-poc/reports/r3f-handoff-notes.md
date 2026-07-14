# P5.07 R3F Handoff Notes

## Phase 8 Architecture Implications

This PoC supports a persistent canvas approach for Mithaq. The production implementation should preserve the separation between:

- DOM-first content and CTAs
- persistent R3F canvas
- scene manager
- global store
- scroll progress mapping
- reduced-motion and device-tier gates

## Recommended Component Names

- `MithaqCanvas`
- `SceneManager`
- `SharedEnvironment`
- `PostProcessingGate`
- `WebGLFallback`
- `useMithaqStore`
- `useScrollProgress`
- `useSceneProgress`
- `useReducedMotion`
- `useWebGLSupport`
- `useDeviceTier`

## Recommended Store Fields

The store in `poc/src/store/mithaqStore.ts` should be the starting contract for production. It already includes opening state, asset-loading placeholders, reduced motion, device tier, language, modal, nav, and CTA source fields.

## Scroll Integration Notes

The current scroll mapping is direct `window.scrollY` mapping. Production may replace the scroll source with Lenis or ScrollTrigger, but the output contract should remain:

- `scrollProgress`
- `activeScene`
- `sceneProgress`

## Scene Integration Notes

Production scene modules should replace proxy scene components gradually. Scene switching should continue through `SceneManager` rather than remounting the whole canvas.

## Shader Integration Notes From P5.06

The P5.06 shaders should be integrated as scene-level materials or overlays, not as global mandatory effects. Reduced-motion and low-tier device gates should disable or simplify:

- ripple shader
- fracture lines
- seal emergence shimmer
- atmospheric particles

## Asset Integration Notes From P5.02-P5.05

Future integration should import optimized GLBs only:

- gavel: P5.02 `gavel.opt.glb`
- seal: P5.03 `seal.opt.glb`
- desk: P5.04 `desk.opt.glb`
- documents: P5.05 `documents.opt.glb`

Assets should remain independently addressable, especially the floating documents.

## Reduced-Motion Notes

Reduced motion should not remove meaning. It should switch opening motion to static/fade states and keep DOM content and CTA access visible.

## Production Risks Before Full Implementation

- Final Next.js architecture still needs confirmation.
- GLB and shader integration may shift bundle and GPU budgets.
- Real mobile performance remains unvalidated.
- Safari and Samsung Internet need dedicated browser checks.
- Production code splitting should be planned before Phase 8 build-out.
