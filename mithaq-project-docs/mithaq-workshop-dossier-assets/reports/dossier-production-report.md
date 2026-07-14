# Dossier Production Report

## Final Visual Direction

The workshop dossier is a restrained premium legal case folder: dark leather/paperboard cover, visible spine, warm parchment stack, muted brass title plate, and a small embossed geometric Mithaq seal treatment. It is meant to sit on the legal desk as an atmospheric Scene 06 object, not replace semantic workshop content.

## Source Assets Used

| Source | Use | Notes |
| --- | --- | --- |
| P4.06 Dark Texture & Material Library | Shared atlas reference | `workshop-dossier-atlas.webp` copied from the approved dark leather subtle WebP. |
| P5.03 Seal direction | Seal treatment reference | Full seal mesh was not imported because it is too heavy for a small dossier accent. |
| P5.04 Desk environment | Scale/material reference | Dossier proportions are designed to rest on the existing dark legal desk. |
| P5.08 Mobile audit | Constraint reference | Dossier remains isolated and lightweight because full mobile runtime failed. |

## Geometry Strategy

Desktop variant:

- `MITHAQ_Workshop_Dossier_Desktop_Cover`
- `MITHAQ_Workshop_Dossier_Desktop_Paper_Stack`
- `MITHAQ_Workshop_Dossier_Desktop_Brass_Details`

Mobile variant:

- `MITHAQ_Workshop_Dossier_Mobile_Cover`
- `MITHAQ_Workshop_Dossier_Mobile_Paper_Stack`
- `MITHAQ_Workshop_Dossier_Mobile_Brass_Details`

The desktop dossier uses `1,480` triangles, under the `2,000` triangle hard maximum. The mobile variant uses `420` triangles.

## Material Strategy

| Material | Direction |
| --- | --- |
| `MITHAQ_Mat_Dossier_Dark_Leather` | Dark high-roughness cover; no glossy plastic. |
| `MITHAQ_Mat_Dossier_Parchment_Stack` | Warm parchment paper stack. |
| `MITHAQ_Mat_Dossier_Muted_Brass` | Restrained brass title plate and seal accent. |
| `MITHAQ_Mat_Dossier_Shadow_Groove` | Neutral line marks and subtle grooves. |

The GLBs use procedural/material values only; no heavy embedded texture payload. The WebP atlas is kept as a shared external reference for future material tuning.

## Seal Treatment

The dossier includes a tiny geometric circular seal mark with restrained gold linework. It intentionally avoids government/state symbols, fake accreditation marks, unreadable official text, or workshop-specific claims.

## Desktop / Mobile Differences

| Area | Desktop | Mobile-Light |
| --- | --- | --- |
| Triangles | 1,480 | 420 |
| Meshes | 3 | 3 |
| Brass details | Title plate, neutral marks, seal disc | Reduced title plate and seal disc |
| Interaction | Resting, hover, selected reference | Static/lightweight reference |
| Runtime guidance | Isolated validation only | No production mobile approval claimed |

## Rejected Visual Directions

- Generic SaaS course card
- School notebook
- Fantasy artifact
- Game inventory item
- Confidential client case folder
- Heavy distressed leather
- Mirror-gold luxury object
- Fake workshop titles, dates, prices, or urgency

## Created and Modified Files

Created P5.09 package files under `mithaq-project-docs/mithaq-workshop-dossier-assets/`, including Blender source, GLB exports, local sandbox, captures, scripts, and reports.

Modified within the P5.09 package only after creation:

- `scripts/capture_dossier_sandbox.mjs`
- `sandbox/src/components/DossierSandboxScene.tsx`

No previous Phase 5 source assets were overwritten.

