# Dossier Handoff Notes

## Recommended Production Asset

Use `exports/workshop-dossier.desktop.opt.glb` for desktop Scene 06 validation and `exports/workshop-dossier.mobile.opt.glb` for mobile-light experiments.

Future production path example:

```tsx
import { useGLTF } from '@react-three/drei';

const dossier = useGLTF('/models/mithaq/workshop-dossier.desktop.opt.glb');
```

Do not move these files into production public assets until a later implementation ticket authorizes it.

## Instancing / Reuse Strategy

- Treat the dossier as one reusable master asset.
- Use shared geometry/materials for multiple workshop dossiers.
- Prefer instancing or cloned scene objects that share buffers.
- Avoid exporting several independently heavy dossier models.
- Variant numbers may be handled through HTML or tiny neutral 3D marks only.

## HTML Overlay Relationship

The GLB must remain atmospheric. Production workshop content should stay in semantic HTML:

- workshop title
- details
- dates
- duration
- price
- instructor
- CTA
- availability

No real or fake workshop content is baked into the GLB.

## Interaction Limits

Resting:

- Dossier lies on the desk with minimal tilt.

Hover:

- Controlled lift of about `0.05` scene units.
- Small camera-facing tilt.
- Smooth weighted transition.
- No bounce, spin, physics, elastic easing, or page flipping.

Selected reference:

- Slight gold/light response.
- Dossier remains closed.
- Details remain in DOM.

## Mobile Recommendation

Because P5.08 failed the full real-asset mobile runtime floor:

- Do not include these dossiers in the complete mobile runtime until re-audited.
- Use the mobile-light GLB only in isolated or later vertical-slice tests.
- Prefer static poster imagery or DOM-first workshop cards on low-tier mobile.
- Avoid raycaster interaction and continuous animation on mobile.

## Known Risks

- `gltfpack` unavailable; Blender Draco compression was used.
- KTX2 texture workflow remains pending.
- Final approved Mithaq seal artwork is not available.
- Real-device validation remains pending.
- Production Scene 06 integration is not started.

## Scope Confirmation

P5.09 produced isolated dossier assets and sandbox validation only. It did not implement final Scene 06, add HTML workshop cards, add routes/forms/CTAs, modify scene ranges, start Phase 6, or execute P6.01.

