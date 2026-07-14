# P5.08 Mobile Audit Methodology

## Scope

This audit used P5.07 as the base architecture and added a representative Scene 01 audit workload using the Phase 5 optimized assets:

- P5.02 `gavel.opt.glb`
- P5.03 `seal.opt.glb`
- P5.04 `desk.opt.glb`

The audit did not start P5.09, did not create production frontend routes, and did not implement the final opening sequence.

## Test Environment

- Host: Windows desktop execution shell
- Browser: Headless Chromium `149.0.7827.55`
- Rendering backend reported by WebGL: ANGLE / SwiftShader
- Viewport: `390 x 844`
- Device scale factor: `2`
- Device profile: Pixel 4a-style mobile emulation
- Build: Vite production build
- Physical device: not available in this environment

Because the available renderer is headless Chromium with SwiftShader, this is a local real-asset audit and not a substitute for a physical Android or BrowserStack device pass.

## Baseline Method

Before adding the real-asset audit workload, the existing P5.07 proxy Scene 01 was measured in production build with the same mobile viewport. This established that the architecture proxy path could sustain roughly 60 FPS in the local harness.

## Final Workload Method

The audit then added a mobile benchmark mode to P5.07:

- Loaded the optimized gavel, seal, and desk GLBs from local public audit assets.
- Used local Draco decoder files to avoid external decoder fetches.
- Mounted a representative Scene 01 workload through `?audit=mobile`.
- Used device-tier query parameters for mid and low tier paths.
- Captured frame timings, draw calls, triangle counts, asset payload, console errors, shader failures, and fallback state.

## Pass / Fail Rules

The ticket hard floor requires Scene 01 to remain at or above 30 FPS after optimization. Runs below this floor must not be hidden as acceptable conditions.

Because the final representative workload repeatedly falls below 30 FPS, P5.08 is marked FAIL.

