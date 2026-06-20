# Material Usage Guide

## Usage Table

| Material Family | CSS Usage | 3D Usage | Scenes | Notes |
| --- | --- | --- | --- | --- |
| Dark Wood | Hero/fallback backgrounds, desk accents | Desk/gavel reference | 01, 02, 04, 10 | Subtle, not orange; use overlays near text. |
| Aged Parchment | Cards/documents, dossier accents | Paper planes/documents | 03, 05, 06 | Avoid noisy text background; subtle variant preferred near copy. |
| Gold Foil | Seal/card accents, linework, small decorative marks | Seal/brass/gold maps | 01, 02, 06, 10 | Signal only; not body text or broad background. |
| Dark Leather | Panels/writing pad, form/card accents | Desk/leather pad | 04, 06, 08 | Subtle grain; avoid overuse under small text. |

## CSS Overlay Guidance

| Family | Recommended Opacity Range | Notes |
| --- | ---: | --- |
| Dark Wood subtle | 8-22% visible texture after dark overlay | Good for section backgrounds and static fallback surfaces. |
| Aged Parchment subtle | 12-35% or solid card use | Verify contrast before text use. |
| Gold Foil subtle | 5-14% as accent mask | Decorative only; never behind body copy. |
| Dark Leather subtle | 8-18% visible texture after overlay | Good for panels and writing-pad surfaces. |

Planning example only:

```css
/* Planning example only - do not wire into production in P4.06 */
.surface-wood {
  background-image:
    linear-gradient(rgba(8, 7, 15, .82), rgba(8, 7, 15, .9)),
    url("./webp/wood-dark/mithaq-wood-dark-subtle-color-1024.webp");
}
```

## Design Tool Blend Guidance

| Family | Blend Direction |
| --- | --- |
| Dark Wood | Normal or multiply under dark overlay. |
| Aged Parchment | Normal for document surfaces; multiply only for aging accents. |
| Gold Foil | Overlay/soft light only as small accent; normal for seal material swatches. |
| Dark Leather | Normal or multiply with low opacity overlay. |

## Three.js / R3F Planning Notes

| Material | Three.js Direction |
| --- | --- |
| Dark wood | `MeshPhysicalMaterial`, high roughness, subtle normal once maps exist. |
| Parchment | `MeshStandardMaterial`, low roughness variation, paper normal later. |
| Gold foil | `MeshPhysicalMaterial`, high metalness, controlled roughness; avoid mirror chrome. |
| Leather | `MeshStandardMaterial`, high roughness, subtle normal once maps exist. |

KTX2 notes for later:

- Load KTX2 through `KTX2Loader` in Three.js later.
- Do not implement the loader in P4.06.
- Color maps should use sRGB handling later.
- Normal/roughness/metalness maps must not be treated as sRGB.

## Readability Warnings

- Use subtle variants near text.
- Do not place gold foil behind body copy.
- Avoid noisy parchment directly behind small text.
- Use solid panels over texture for FAQ, forms, and long paragraphs.
- Do not claim WCAG compliance until contrast is tested in final layouts.

## Mobile Simplification

- Prefer subtle WebP variants on mobile.
- Avoid loading all families at first paint.
- Exclude gold/leather decorative textures on low-tier mobile if not essential.
- Use static poster imagery for fallback rather than many layered backgrounds.

