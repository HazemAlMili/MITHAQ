# Mithaq Floating Documents Asset Report

Ticket: P5.05 — Floating Documents (Scene 03)

Status: PASS WITH CONDITIONS

## Concept Summary

The Floating Documents asset set was produced for Scene 03 — The Gap. The set visually represents the unresolved space between academic legal study and professional practice through quiet, fragmented legal/academic paper forms. The documents are lightweight, separate meshes intended for later slow drift, orbit, and convergence planning.

## Design Rationale

The documents use warm parchment tones, slight paper curvature, subtle thickness, and abstract line/block marks. They avoid white printer-paper brightness, clutter, trash/debris energy, fantasy scrolls, newspaper clippings, readable fake legal text, court/government marks, stamps, personal data, and official-looking seals.

## Object List

| Object | Role |
| --- | --- |
| `MITHAQ_Doc_01_Legal_Notes` | Legal notes fragment |
| `MITHAQ_Doc_02_Academic_Reference` | Academic reference fragment |
| `MITHAQ_Doc_03_Unfinished_Form` | Unfinished legal form impression |
| `MITHAQ_Doc_04_Case_Excerpt` | Case excerpt impression |
| `MITHAQ_Doc_05_Research_Sheet` | Legal research sheet impression |
| `MITHAQ_Doc_06_Memo_Draft` | Memo draft impression |
| `MITHAQ_Doc_07_Pleading_Fragment` | Pleading fragment impression |
| `MITHAQ_Doc_08_Practice_Checklist` | Practice checklist impression |

## Helper Anchors In Source

| Anchor | Purpose |
| --- | --- |
| `MITHAQ_Documents_Orbit_Center` | Future Scene 03 orbit center |
| `MITHAQ_Documents_Converge_Target` | Future Scene 04 convergence target |
| `MITHAQ_Documents_Camera_Preview` | Preview camera planning reference |

Helpers remain in the Blender source and are excluded from GLB export.

## Material List

| Material | Role |
| --- | --- |
| `MITHAQ_Mat_Parchment_Base` | Warm paper base |
| `MITHAQ_Mat_Parchment_Dim` | Paper edge/underside dim tone |
| `MITHAQ_Mat_Abstract_Ink_Marks` | Non-readable writing marks |
| `MITHAQ_Mat_Subtle_Gold_Line` | Rare decorative accent line |

## Dimensions / Scale Assumptions

The documents are roughly A-series paper proportions in Blender units, with each document between about `0.68–0.82` units wide and `0.95–1.16` units tall. The set is arranged in a loose floating cluster around the origin for preview, but each mesh can be repositioned independently in R3F.

## Scene Usage Mapping

| Scene | Usage |
| --- | --- |
| Scene 03 | Fragmented unresolved gap, slow orbit/drift |
| Scene 04 | Future convergence target for organized method transition |
| Static fallback | Can be represented as a poster-style document collage |

## Geometry Summary

| Metric | Value |
| --- | ---: |
| Total triangles | 760 |
| Meshes | 8 |
| Materials | 4 |
| Textures | 0 |

## Per-Document Triangle Counts

| Document | Triangles |
| --- | ---: |
| `MITHAQ_Doc_01_Legal_Notes` | 92 |
| `MITHAQ_Doc_02_Academic_Reference` | 100 |
| `MITHAQ_Doc_03_Unfinished_Form` | 92 |
| `MITHAQ_Doc_04_Case_Excerpt` | 98 |
| `MITHAQ_Doc_05_Research_Sheet` | 94 |
| `MITHAQ_Doc_06_Memo_Draft` | 90 |
| `MITHAQ_Doc_07_Pleading_Fragment` | 98 |
| `MITHAQ_Doc_08_Practice_Checklist` | 96 |

All documents are below the `500` triangle per-document target.

## Material / Texture Summary

All materials are procedural Blender materials. No external textures, stock images, watermarked assets, fake legal text, official marks, or personal information were used. Texture count is `0`.

## Visual Constraints Followed

- Exactly eight document assets were created.
- Each document remains independently addressable.
- Documents read as warm legal/academic paper fragments.
- Abstract writing marks are non-readable.
- No court/government marks, stamps, seals, case numbers, names, or fake legal claims are included.
- No animation, orbit behavior, convergence behavior, shaders, or frontend implementation was started.

## Visual Risks

- Procedural material grain may require R3F material tuning because GLB export cannot preserve every Blender procedural preview node as a runtime shader.
- Final Scene 03 motion validation is pending.
- Mobile may need a reduced 3–4 document set if later performance testing requires it.

## Final Recommendation

Use `exports/documents.opt.glb` as the validated P5.05 floating document asset set for later R3F import and Scene 03 motion planning, with final material and movement validation deferred to authorized later tickets.
