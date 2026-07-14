# Mithaq Shader R3F Handoff Notes

Ticket: P5.06 — Shader Development

Status: PASS WITH CONDITIONS

## Import Pattern

Example:

```tsx
import rippleVertexShader from './shaders/ripple.vert?raw';
import rippleFragmentShader from './shaders/ripple.frag?raw';
```

Use each shader with a `THREE.ShaderMaterial` or R3F `shaderMaterial`.

## Recommended Material Setup

| Shader | Setup |
| --- | --- |
| Ripple | Transparent overlay plane above desk surface |
| Fracture lines | Transparent overlay plane or decal-style layer |
| Seal emergence | Shader material on circular proxy or adapted to selected Seal meshes |
| Particles | `points` with custom buffer attributes |

## Driving Values

Later GSAP/R3F work should drive uniforms directly:

- `uProgress`: scene-local normalized scroll or timeline value
- `uTime`: render-loop elapsed time
- `uOpacity`: scene handoff / reduced-motion state
- `uImpactPoint`: UV strike coordinate on desk
- `uFractureProgress`: delayed phase after ripple trigger

## Desk Ripple Integration

For P5.04 desk integration, place a transparent ripple plane slightly above the desk surface or target a custom material layer on `MITHAQ_Desk_Surface`. The shader should remain an overlay so the desk material can retain dark wood readability.

## Seal Emergence Integration

For P5.03 Seal integration, start with a proxy ring or selectively apply the shader to rim/highlight meshes. Do not animate Arabic text letter-by-letter. If the final Seal uses multiple materials, the reveal may be better handled through material overrides or a separate reveal ring.

## Fracture Lines Integration

Use fracture lines as controlled authority rays after the ripple. They should draw outward from the gavel impact area toward the Seal reveal path. Avoid jagged lightning, violent cracks, or random procedural chaos.

## Atmospheric Particle Integration

Use a capped `points` geometry with low opacity. Particles are visual atmosphere only and must not communicate essential content.

## Mobile / Reduced Motion

- Low mode: 80 particles or fewer.
- Reduced motion: static/faded states, particles disabled or nearly static.
- No flashing, strobing, or rapid changes.
- CTA and DOM content must never depend on shader animation.

## Risks Before Production Integration

- Need P5.07 architecture decision for persistent canvas and uniform orchestration.
- Need P5.08 mobile profiling.
- Need final desk/Seal material tuning in real scene lighting.
- Need ScrollTrigger/GSAP timing only in later authorized tickets.
