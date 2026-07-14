# Mithaq Seal Asset Report

Ticket: P5.03 — Mithaq Seal Model Production

Status: PASS WITH CONDITIONS

## Concept Summary

The Mithaq Seal was produced as the primary ceremonial 3D brand object for the Mithaq website. The object is a circular embossed legal seal with restrained brass/gold materials, concentric official-feeling rims, raised Arabic brand text, and a minimal abstract scales motif. The design keeps the Seal as the hero object while the gavel remains only the ceremonial trigger.

## Design Rationale

The form avoids government, court, state, crest, flag, crown, sword, or ministry-like symbolism. The legal motif is intentionally abstract and secondary, while the circular rim and raised Arabic wordmark carry the official covenant feeling. The material direction follows Mithaq's dark premium world: muted gold, dark bronze, shallow relief, and warm highlights rather than shiny fake luxury.

## Object List

| Object | Role |
| --- | --- |
| `MITHAQ_Seal_Back_Plate` | Dark bronze underside and side-depth credibility |
| `MITHAQ_Seal_Base` | Main brass face of the seal |
| `MITHAQ_Seal_Outer_Rim` | Hero readable outer raised circular rim |
| `MITHAQ_Seal_Inner_Rim` | Secondary concentric official ring |
| `MITHAQ_Seal_Shadow_Groove_Outer` | Restrained engraved shadow groove |
| `MITHAQ_Seal_Shadow_Groove_Inner` | Inner engraved shadow groove |
| `MITHAQ_Seal_Arabic_Text` | Raised mesh Arabic text for `ميثاق` |
| `MITHAQ_Seal_Legal_Motif` | Minimal abstract scales reference |

## Material List

| Material | Role |
| --- | --- |
| `MITHAQ_Mat_Brass_Gold` | Main muted brass/gold surface |
| `MITHAQ_Mat_Gold_Highlight` | Raised rim, text, and motif highlights |
| `MITHAQ_Mat_Dark_Bronze` | Back plate and underside depth |
| `MITHAQ_Mat_Shadow_Groove` | Dark recessed groove contrast |

## Dimensions / Scale Assumptions

The seal is modeled around a centered circular origin with a radius of roughly `1.82` Blender units and shallow embossed depth. It is intended to be scaled in R3F rather than remodeled for each scene. The face is oriented toward the positive Z/front preview plane and exported with Three.js-compatible Y-up GLB settings.

## Scene Usage Mapping

| Scene | Usage |
| --- | --- |
| Scene 01 | Main seal reveal after gavel trigger |
| Scene 02 | Hero anchor object behind/near DOM identity |
| Scene 06 | Subtle stamped/accent motif reference |
| Scene 10 | Closing covenant symbol callback |

## Geometry Summary

| Metric | Value |
| --- | ---: |
| Triangles | 8,578 |
| Meshes | 8 |
| Materials | 4 |
| Textures | 0 |

The asset is within the hard triangle maximum of 12,000 tris. It slightly exceeds the preferred 8,000-triangle target, but remains close enough for the hero seal use case and validates under the file-size target.

## Material / Texture Summary

All materials are procedural Blender node materials. No external stock textures, watermarked images, brand marks, government symbols, or baked content were used. Texture count is `0`.

## Arabic Text Summary

The text `ميثاق` is included as raised mesh geometry. Blender background text conversion did not reliably shape Arabic using plain Unicode text, so the production script uses Arabic presentation-form glyphs in visual order to preserve legibility in the converted mesh. This is an honest production workaround and must be reviewed against final approved Arabic wordmark/calligraphy assets later.

## Visual Constraints Followed

- Seal remains the hero object.
- Gavel remains the trigger only.
- Circular official seal language is used without copying state/court/government marks.
- Muted gold/brass is used instead of shiny fake gold.
- No flags, eagles, crowns, swords, official crests, religious-state symbols, cartoon styling, sci-fi hologram, or neon glow are present.
- Text is geometric on the asset but must not replace DOM-accessible Arabic/English content later.

## Visual Risks

- Arabic mesh text is a planning/production approximation until final wordmark approval.
- The abstract scales motif is intentionally minimal, but should be stakeholder-reviewed so it does not feel generic.
- Final shader and lighting decisions may change perceived gold tone in R3F.

## Final Recommendation

Use `exports/seal.opt.glb` as the P5.03 validated Seal asset for future R3F import tests, with the conditions documented in the optimization and validation reports.
