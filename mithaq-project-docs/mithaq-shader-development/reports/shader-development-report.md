# Mithaq Shader Development Report

Ticket: P5.06 — Shader Development

Status: PASS WITH CONDITIONS

## Shader Concept

The shader sandbox explores Mithaq's opening FX language in isolation: a restrained desk ripple, deliberate gold fracture paths, an official Seal reveal treatment, and quiet atmospheric particles. The visual language is dark, warm, legal, ceremonial, and controlled. The work intentionally avoids neon, sci-fi holograms, explosive particles, lightning, horror cracks, game-like motion, and full production timeline integration.

## Files Created

| Area | Files |
| --- | --- |
| App shell | `sandbox/src/main.tsx`, `sandbox/src/App.tsx`, `sandbox/src/styles.css` |
| Combined scene | `sandbox/src/components/ShaderSandboxScene.tsx` |
| Ripple demo | `sandbox/src/components/RippleShaderDemo.tsx` |
| Fracture demo | `sandbox/src/components/FractureLinesShaderDemo.tsx` |
| Seal demo | `sandbox/src/components/SealEmergenceShaderDemo.tsx` |
| Particles demo | `sandbox/src/components/AtmosphericParticlesDemo.tsx` |
| Shader uniforms | `sandbox/src/utils/shaderUniforms.ts` |
| Device quality | `sandbox/src/utils/deviceQuality.ts` |
| Capture script | `sandbox/scripts/capture_shader_sandbox.mjs` |

## Technical Approach

The sandbox uses React, TypeScript, Vite, Three.js, and React Three Fiber. Shader code is kept in standalone `.vert` and `.frag` files and imported as raw strings into R3F `shaderMaterial` instances. The combined sandbox uses local React state only; no routing, Zustand, Lenis, ScrollTrigger, or production scene manager is included.

## Uniform Lists

### Desk Ripple

`uProgress`, `uImpactPoint`, `uGoldColor`, `uOpacity`, `uRingWidth`, `uEchoStrength`, `uTime`

### Fracture Lines

`uProgress`, `uFractureProgress`, `uGoldColor`, `uLineCount`, `uLineWidth`, `uGlowStrength`, `uSeed`, `uOpacity`, `uTime`

### Seal Emergence

`uProgress`, `uGoldColor`, `uHighlightColor`, `uEmissiveStrength`, `uRevealSoftness`, `uOpacity`, `uTime`

### Atmospheric Particles

`uTime`, `uOpacity`, `uGoldColor`, `uPointSize`, `uDriftStrength`, `uDepthFade`

## Visual Decisions

- Gold is muted and warm, based on `#C4913A`.
- The ripple is an overlay ring, not a flash or explosion.
- Fracture paths are deliberate radial rays, not violent cracks.
- Seal emergence uses a circular reveal proxy and avoids text animation.
- Particles are low-opacity gold dust, not sparkle/firework effects.
- Reduced-motion mode dampens motion and opacity rather than removing all visual context.

## Scene Mapping

| Shader | Scene Mapping |
| --- | --- |
| Desk ripple | Scene 01 gavel contact on desk surface |
| Fracture lines | Scene 01 authority signal after ripple |
| Seal emergence | Scene 01 Seal reveal and Scene 02 hero anchor |
| Atmospheric particles | Scene 01/02 chamber atmosphere and idle ambience |

## Intentionally Avoided

- Full opening sequence timeline
- Production Scene 01 implementation
- R3F architecture proof of concept
- Lenis, ScrollTrigger, Zustand, routing, or app shell integration
- Asset mutation for P5.02-P5.05 GLBs
- Neon, sci-fi, magic sparkle, horror cracks, and game-like effects
