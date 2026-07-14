# Gavel Asset Report

**Ticket:** P5.02 - Gavel Model Production  
**Status:** PASS WITH CONDITIONS  
**Date:** 2026-06-21  

---

## 1. Executive Summary

The Mithaq judicial gavel has been produced as a real Blender asset and exported to raw and optimized GLB files. It is designed as a premium legal object and ceremonial trigger for the opening sequence, while keeping the Mithaq Seal as the hero object.

The optimized GLB is **87.4 KB**, well under the **1.2 MB** target. The geometry is **15,084 triangles**, within the required **8k-18k** range.

Condition: `gltfpack` is still unavailable from this shell, so `gavel.opt.glb` was created with Blender GLTF Draco compression as a real optimization fallback.

---

## 2. Production Method

The asset was generated in Blender 5.1.2 using a local Blender Python production script:

```txt
tools/create_gavel_asset.py
```

Blender command used:

```powershell
& "C:\Program Files\Blender Foundation\Blender 5.1\blender.exe" --background --python mithaq-project-docs\mithaq-gavel-model-production\tools\create_gavel_asset.py
```

The script creates the model, procedural PBR materials, UV unwraps, pivot/contact helpers, preview renders, `.blend` source, raw GLB, optimized GLB, and initial validation JSON.

---

## 3. Model Description

The gavel includes:

- Cylindrical judicial head
- Dark wood handle
- Beveled dark end faces
- Muted brass bands around the head
- Brass collar at the handle/head joint
- Subtle brass handle end band
- Named pivot helper
- Named contact-point helper

Visual direction:

- Premium judicial object
- Dark walnut/wenge-inspired wood
- Muted brass/gold
- Formal and ceremonial
- Non-violent, non-cartoon, non-fantasy

---

## 4. Geometry Summary

| Metric | Value |
| --- | ---: |
| Triangle count | 15,084 |
| Mesh count | 13 |
| Material count | 4 |
| Hidden junk geometry | None exported |
| Preview-only floor | Hidden before save/export |

Primary object names:

- `Gavel_Head`
- `Gavel_Handle`
- `Gavel_Brass_Band_Left`
- `Gavel_Brass_Band_Right`
- `Gavel_Brass_Collar`
- `Gavel_Handle_End_Knob`
- `Gavel_Handle_Subtle_Brass_End_Band`
- `Gavel_Pivot_Helper`
- `Gavel_Contact_Point_Negative_X`

---

## 5. Material Summary

| Material | Purpose | Direction |
| --- | --- | --- |
| `Mithaq_Dark_Wood` | Head and handle | Dark walnut/wenge, high roughness, procedural noise bump. |
| `Mithaq_Dark_Wood_Darker_Endgrain` | Contact/end faces | Darker endgrain, high roughness. |
| `Mithaq_Muted_Brass` | Main brass bands/collar | Muted brass/gold, high metalness, controlled roughness. |
| `Mithaq_Edge_Wear_Optional` | Thin brass grooves | Subtle official highlight, not glitter. |

No external texture images are used. Materials are procedural, so there is no unclear texture licensing risk.

---

## 6. UV Summary

Smart UV Project was applied to visible mesh objects. Because materials are procedural and no image textures are used, UVs are safe for current production use and future texture baking if needed.

UV status:

- Head, handle, bands, and contact faces have UVs.
- No final brand marks or text are baked into UV textures.
- Wood grain is procedural rather than texture-map dependent.

---

## 7. Texture Summary

| Texture Type | Status |
| --- | --- |
| External image textures | None |
| Procedural wood | Included in Blender materials |
| Procedural brass | Included in Blender materials |
| KTX2 textures | Pending from P4.06; not required for this procedural asset |

Texture count in GLB: `0`.

---

## 8. Export Summary

| Export | Status | Notes |
| --- | --- | --- |
| `source/gavel.blend` | PASS | Blender source saved. |
| `exports/gavel.raw.glb` | PASS | Raw GLB exported from Blender. |
| `exports/gavel.opt.glb` | PASS WITH CONDITIONS | Real Draco-compressed GLB exported from Blender; gltfpack unavailable. |

Both raw and optimized GLBs were re-imported into Blender successfully.

---

## 9. Optimization Summary

Raw GLB:

- 416,000 bytes / 406.3 KB

Optimized GLB:

- 89,480 bytes / 87.4 KB

Optimization method:

- Blender GLTF exporter Draco mesh compression fallback

Condition:

- `gltfpack` still does not resolve in this shell, so gltfpack optimization could not be used.

---

## 10. Preview Render Index

| Preview | Purpose | Path |
| --- | --- | --- |
| Front | Silhouette and proportions | `preview/gavel-preview-front.png` |
| Side | Handle/head relationship | `preview/gavel-preview-side.png` |
| Perspective | Material read | `preview/gavel-preview-perspective.png` |
| Opening angle | Scene 01 macro framing | `preview/gavel-preview-opening-angle.png` |
| Wireframe | Geometry density | `preview/gavel-preview-wireframe.png` |

Render style:

- Dark Mithaq background
- Warm upper-left light
- Subtle rim highlight
- No neon
- No busy environment

---

## 11. Opening Sequence Compatibility

| Keyframe | Compatibility |
| --- | --- |
| KF03 - Gavel Descent | Reads clearly in macro/upper-frame composition. |
| KF04 - Strike Moment | Negative-X contact face and contact helper support impact alignment. |
| KF07 - Seal Completed | Gavel can rest secondary beside Seal. |
| Scene 10 Final CTA | Gavel can reappear as callback object. |

The gavel is intentionally detailed enough for macro frames but still lightweight.

---

## 12. Mobile / Reduced-Motion Notes

- Same GLB is small enough for possible mobile use, but mobile validation remains pending.
- Optional mobile LOD remains pending.
- Reduced-motion mode should use static poster/fallback and does not require gavel motion.
- Gavel animation should be skipped or simplified on weak devices.

---

## 13. Accessibility / Fallback Notes

- The gavel is symbolic/decorative.
- No essential text is inside the model.
- No CTA depends on the model.
- Screen readers do not need to interpret the gavel.
- If the gavel fails to load, static seal/desk fallback still communicates the opening.
- Gavel must not obscure DOM headline or CTA zones in R3F composition.

---

## 14. Known Limitations

- `gltfpack` unavailable in the current shell; optimized GLB uses Blender Draco compression instead.
- KTX2 texture conversion remains pending from P4.06.
- Stakeholder art approval pending.
- Optional mobile LOD pending.
- Final R3F import/lighting validation pending.
- Real-device performance validation pending.
- Relative scale against final Seal and desk remains pending.

---

## 15. Final Recommendation

Proceed with this gavel asset as the P5.02 production output for technical review and later R3F import testing. Before final launch, validate the asset in Scene 01 lighting, compare scale against the final Seal/desk, and decide whether a mobile LOD is necessary.

