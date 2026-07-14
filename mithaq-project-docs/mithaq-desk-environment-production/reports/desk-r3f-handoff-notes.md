# Mithaq Desk R3F Handoff Notes

Ticket: P5.04 — Legal Desk Environment

Status: PASS WITH CONDITIONS

## Recommended Import Path

```tsx
import { useGLTF } from '@react-three/drei';

const desk = useGLTF('/models/mithaq/desk.opt.glb');
```

Recommended future asset path:

```txt
/public/assets/models/mithaq/desk.opt.glb
```

Do not move the asset into production public assets until a later implementation ticket authorizes it.

## Scale Recommendation

Start with a uniform R3F scale around `1.0`. The desk is broad by design, approximately `8.4 x 5.2` Blender units for the main surface. It is intended to support macro camera crops, not necessarily appear fully visible in every scene.

## Rotation / Origin Notes

- Desk is centered around world origin.
- Surface lies on the XY plane.
- Z is vertical height.
- GLB export used Y-up settings.
- Desk should sit below the gavel and Seal assets.

## Placement Anchor Notes

The `.blend` source includes helper empties:

| Anchor | Suggested Use | Location |
| --- | --- | --- |
| `MITHAQ_Anchor_Gavel_Strike` | Gavel contact / strike point | `[-1.15, -0.30, 0.23]` |
| `MITHAQ_Anchor_Seal_Center` | Seal reveal / hero center | `[0.28, -0.24, 0.25]` |
| `MITHAQ_Anchor_Camera_Hero` | Starting hero composition reference | `[2.4, -4.2, 2.25]` |

Helper empties are not exported into `desk.raw.glb` or `desk.opt.glb`.

## Material Override Notes

Materials included:

- `MITHAQ_Mat_Dark_Wenge_Wood`
- `MITHAQ_Mat_Desk_Edge_Dark_Wood`
- `MITHAQ_Mat_Aged_Dark_Leather`
- `MITHAQ_Mat_Subtle_Groove_Shadow`

R3F may tune roughness, color, and normal/bump equivalents. Procedural Blender grain is used in the source for previewing, but runtime material appearance may need Three.js material overrides because GLB cannot preserve all Blender procedural node behavior.

## Lighting Recommendations

- Use warm key light from upper-left.
- Keep low ambient light but preserve leather/wood readability.
- Avoid mirror-polished reflections.
- Avoid neon, blue/purple sci-fi rim light, horror underlighting, and overexposed studio light.

## Future Ripple Shader Notes

The main desk surface is a separate mesh so later shader work can target it directly. A future ripple effect should overlay or override the desk surface material rather than requiring new desk geometry.

## Mobile Simplification Notes

- The desk is very low-poly and small enough for early vertical-slice testing.
- If mobile FPS drops, reduce realtime shadows first.
- Optional lower-detail static poster remains acceptable for reduced-motion/WebGL fallback.
- Avoid long pinned mobile choreography that hides CTA content.

## Reduced-Motion / Static Fallback Notes

- Reduced-motion mode can use the desk as a static background poster.
- No essential text is inside the desk asset.
- No CTA depends on desk visibility.
- If WebGL fails, a static desk/gavel/Seal composite can communicate the scene.

## Limitations

- `gltfpack` was unavailable in the execution shell; `desk.opt.glb` uses Blender Draco compression.
- Final material art approval remains pending.
- KTX2 conversion is pending because no texture maps were generated and runtime material strategy is not final.
- Final R3F import, Scene 01 lighting/ripple validation, mobile LOD, and real-device performance testing remain pending.
