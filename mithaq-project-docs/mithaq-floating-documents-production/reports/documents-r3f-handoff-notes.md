# Mithaq Floating Documents R3F Handoff Notes

Ticket: P5.05 — Floating Documents (Scene 03)

Status: PASS WITH CONDITIONS

## Recommended Import Path

```tsx
import { useGLTF } from '@react-three/drei';

const documents = useGLTF('/models/mithaq/documents.opt.glb');
```

Recommended future asset path:

```txt
/public/assets/models/mithaq/documents.opt.glb
```

Do not move the asset into production public assets until a later implementation ticket authorizes it.

## Scale Recommendation

Start with a uniform R3F scale around `1.0`. Each document is intentionally small and separate, with a loose cluster centered around the origin. Adjust per scene camera rather than scaling individual documents heavily.

## Origin Notes

- The set is arranged around a central gap near world origin.
- Each document mesh has its own transform and can be animated independently.
- Helper empties in the `.blend` are for planning only and are not exported.

## Per-Document Mesh Naming

| Mesh | Role |
| --- | --- |
| `MITHAQ_Doc_01_Legal_Notes` | Legal notes fragment |
| `MITHAQ_Doc_02_Academic_Reference` | Academic reference fragment |
| `MITHAQ_Doc_03_Unfinished_Form` | Unfinished form impression |
| `MITHAQ_Doc_04_Case_Excerpt` | Case excerpt impression |
| `MITHAQ_Doc_05_Research_Sheet` | Research sheet impression |
| `MITHAQ_Doc_06_Memo_Draft` | Memo draft impression |
| `MITHAQ_Doc_07_Pleading_Fragment` | Pleading fragment impression |
| `MITHAQ_Doc_08_Practice_Checklist` | Practice checklist impression |

## Suggested Orbit / Convergence References

Source helper empties:

| Helper | Suggested Use |
| --- | --- |
| `MITHAQ_Documents_Orbit_Center` | Central Scene 03 drift/orbit target |
| `MITHAQ_Documents_Converge_Target` | Scene 04 transition target |
| `MITHAQ_Documents_Camera_Preview` | Preview camera reference |

Suggested future motion:

- Documents drift independently around the orbit center.
- Rotation should be slow and readable.
- No fast spinning, chaotic paper storm, or physics simulation is required.
- Convergence toward Scene 04 should be controlled and ceremonial, not magnetic or explosive.

## Suggested Rotation Ranges

| Axis | Suggested Range |
| --- | --- |
| X | `-12deg` to `18deg` slow drift |
| Y | `-18deg` to `20deg` slow drift |
| Z | `-35deg` to `35deg` scene composition variance |

## Mobile Simplification

- Use only 3-4 of the 8 meshes on low-end mobile if performance testing requires it.
- Disable non-essential rotation first.
- Reduced-motion can use a static poster render or fixed cluster.
- Avoid long pinned mobile choreography that hides CTA content.

## Reduced-Motion Fallback

- Show a static cluster/collage of documents.
- Do not require orbit motion to understand Scene 03.
- Keep DOM text responsible for actual content and meaning.

## Material Override Notes

Materials included:

- `MITHAQ_Mat_Parchment_Base`
- `MITHAQ_Mat_Parchment_Dim`
- `MITHAQ_Mat_Abstract_Ink_Marks`
- `MITHAQ_Mat_Subtle_Gold_Line`

Future R3F may tune parchment darkness, roughness, and environmental lighting. Do not make the pages bright white or certificate-like.

## Content Safety Warnings

- Do not add readable fake legal names, case numbers, court/government marks, official stamps, client data, signatures, or false legal claims.
- Do not animate Arabic or other text letter-by-letter.
- If real text is needed later, keep it DOM-first or use approved content only.

## Limitations

- `gltfpack` was unavailable in the execution shell; `documents.opt.glb` uses Blender Draco compression.
- Final material/art approval remains pending.
- Optional mobile LOD remains pending.
- Final R3F import, Scene 03 orbit/convergence validation, and real-device performance testing remain pending.
