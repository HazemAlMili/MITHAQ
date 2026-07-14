# Mithaq Seal R3F Handoff Notes

Ticket: P5.03 — Mithaq Seal Model Production

Status: PASS WITH CONDITIONS

## Recommended Import Path

```tsx
import { useGLTF } from '@react-three/drei';

const seal = useGLTF('/models/mithaq/seal.opt.glb');
```

Recommended future asset path:

```txt
/public/assets/models/mithaq/seal.opt.glb
```

Do not move the asset into production public assets until the relevant implementation ticket authorizes it.

## Scale Recommendation

Start with a uniform R3F scale around `1.0`, then adjust per camera. The asset is centered around the origin and built as a medallion-like seal with radius about `1.82` Blender units.

## Rotation / Origin Notes

- The Seal is centered at world origin.
- The front face is modeled on the XY plane with depth on Z.
- GLB export used Y-up settings.
- In R3F, orient the Seal face toward the active camera for Scene 01 and Scene 02.
- Treat the full Seal as one hero object for reveal timing; do not animate the Arabic text letter-by-letter.

## Material Override Notes

Materials included:

- `MITHAQ_Mat_Brass_Gold`
- `MITHAQ_Mat_Gold_Highlight`
- `MITHAQ_Mat_Dark_Bronze`
- `MITHAQ_Mat_Shadow_Groove`

Future R3F may tune roughness, metalness, environment intensity, or add subtle emissive/rim treatment. Avoid strong bloom across the whole object. If an emissive reveal is needed later, use a separate shader ring or controlled material override rather than turning the entire Seal into a glowing object.

## Lighting Recommendations

- Use warm key light from upper-left.
- Use subtle rim light for edge definition.
- Keep ambient low but not unreadable.
- Let raised rings and text catch light naturally.
- Avoid neon, sci-fi blue/purple rim light, horror underlighting, and mirror-polished gold.

## Animation Notes For Scene 01

- Seal should reveal after gavel trigger.
- Animate the Seal as a whole object, through ring reveal, material reveal, or controlled opacity/lighting.
- Do not animate Arabic glyphs individually.
- Use scroll-led timing, not a fixed trailer intro.
- Keep gavel secondary in framing after Seal emergence.

## Mobile Simplification Notes

- Same optimized GLB is small enough for early vertical-slice testing.
- If mobile FPS drops, use a static render or simplified material lighting first.
- Optional mobile LOD remains pending and can be considered later if real-device testing requires it.
- Avoid long pinned mobile sequences that hide CTA content.

## Reduced-Motion / Static Fallback Notes

- Reduced-motion mode can show the Seal as a static hero poster with DOM identity and CTA visible.
- No essential text should depend on the GLB.
- Arabic/English content must remain DOM-first.
- If WebGL fails, the static Seal render can carry the visual identity without requiring animated reveal.

## Limitations

- `gltfpack` was unavailable in the execution shell; `seal.opt.glb` uses Blender Draco compression.
- Arabic mesh text uses a Blender presentation-form workaround and requires final wordmark/calligraphy approval.
- Final R3F import, Scene 01 lighting validation, mobile performance, and stakeholder art approval remain pending.
