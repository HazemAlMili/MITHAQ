# Mithaq Desk Asset Report

Ticket: P5.04 — Legal Desk Environment

Status: PASS WITH CONDITIONS

## Concept Summary

The Mithaq Legal Desk Environment was produced as a grounded premium legal stage for the gavel, Seal, and later scene objects. It is deliberately quiet and background-focused: dark wood surface, beveled front/side desk depth, dark aged leather writing pad, subtle groove details, and light placement cues for future dossier/document composition.

## Design Rationale

The desk supports symbolic realism without competing with the Seal. It avoids marble, glass, sci-fi shine, fantasy altar language, office clutter, and ornate courtroom cliche. The broad surface gives future R3F and shader work room for the gavel strike, authority ripple, Seal reveal, and workshop dossier placement while staying lightweight enough to persist across scenes.

## Object List

| Object | Role |
| --- | --- |
| `MITHAQ_Desk_Surface` | Main broad dark wood desk surface |
| `MITHAQ_Desk_Front_Edge` | Beveled front thickness and premium edge read |
| `MITHAQ_Desk_Side_Edge_Left` | Left desk side depth |
| `MITHAQ_Desk_Side_Edge_Right` | Right desk side depth |
| `MITHAQ_Leather_Writing_Pad` | Dark aged leather legal writing pad |
| `MITHAQ_Leather_Pad_Subtle_Groove` | Pad groove/seam detail |
| `MITHAQ_Desk_Subtle_Placement_Zones` | Low-relief future dossier placement cues only |

## Helper Anchors In Source

| Anchor | Purpose | Location |
| --- | --- | --- |
| `MITHAQ_Anchor_Gavel_Strike` | Future gavel strike/contact reference | `[-1.15, -0.30, 0.23]` |
| `MITHAQ_Anchor_Seal_Center` | Future Seal center reference | `[0.28, -0.24, 0.25]` |
| `MITHAQ_Anchor_Camera_Hero` | Future hero camera reference | `[2.4, -4.2, 2.25]` |

## Material List

| Material | Role |
| --- | --- |
| `MITHAQ_Mat_Dark_Wenge_Wood` | Main dark wood desk surface |
| `MITHAQ_Mat_Desk_Edge_Dark_Wood` | Slightly darker edge treatment |
| `MITHAQ_Mat_Aged_Dark_Leather` | Leather writing pad |
| `MITHAQ_Mat_Subtle_Groove_Shadow` | Grooves, seams, placement cues |

## Dimensions / Scale Assumptions

The desk is centered around world origin and modeled as a broad rectangular slab in the XY plane with Z as vertical height. The main slab is approximately `8.4 x 5.2` Blender units with visible thickness. The leather pad sits slightly above the surface and can be overridden as a separate material in R3F.

## Scene Usage Mapping

| Scene | Usage |
| --- | --- |
| Scene 01 | Gavel strike, authority ripple, Seal reveal stage |
| Scene 02 | Hero anchor support surface |
| Scene 04 | Organized legal desk transition base |
| Scene 06 | Workshop dossier placement zones |
| Scene 10 | Final covenant callback surface |

## Geometry Summary

| Metric | Value |
| --- | ---: |
| Triangles | 1,040 |
| Meshes | 7 |
| Materials | 4 |
| Textures | 0 |

The asset is well under the `5,000` triangle target and the `8,000` hard maximum.

## Material / Texture Summary

All materials are procedural Blender materials. No external textures, stock images, watermarked assets, fake document text, logos, or legal markings were used. Texture count is `0`.

## Preview-Only Imports

The P5.02 gavel and P5.03 Seal were imported only to render `desk-preview-hero-gavel-seal-layout.png`. They were removed before saving/exporting the desk asset and are not included in either `desk.raw.glb` or `desk.opt.glb`.

## Visual Constraints Followed

- Desk remains the stage, not the hero.
- Dark wood and leather define the physical legal world.
- No marble, glass, neon, sci-fi grid, fantasy altar, office clutter, or fake legal text is present.
- Subtle placement zones do not start P5.05 document production.

## Visual Risks

- Procedural Blender material grain may require R3F material tuning because GLB export cannot preserve every procedural node as a runtime shader.
- Future ripple shader validation remains pending.
- Final material/art approval is still required.

## Final Recommendation

Use `exports/desk.opt.glb` as the validated P5.04 desk asset for later R3F import tests, with material tuning and ripple shader validation handled in later authorized tickets.
