# Mithaq Dark Texture & Material Library

**Official Ticket ID:** P4.06  
**Official Ticket Name:** Dark Texture & Material Library  
**Phase:** Phase 4 - Visual System & Art Direction  
**Priority:** P1  
**Complexity:** Medium  
**Owner:** Material Artist / 3D Art Director  
**Status:** PASS WITH CONDITIONS - KTX2 conversion pending  
**Prepared date:** 2026-06-20  

---

## 1. Executive Summary

This folder contains Mithaq's official dark texture and material library for the premium legal academy visual system. It provides self-created procedural WebP texture assets for:

1. Dark wood grain
2. Aged parchment
3. Muted gold foil
4. Dark leather grain

These materials support future 3D materials, static fallback posters, CSS background textures, legal desk scenes, workshop dossier visuals, parchment/document surfaces, seal accents, and dark editorial section backgrounds.

The texture assets are source-safe: they were procedurally generated locally using Python/Pillow, with no third-party stock, scraped, watermarked, or unclear-license source images.

Status is **PASS WITH CONDITIONS** because required WebP assets, documentation, source/license register, optimization report, usage guide, and visual contact sheet exist, but KTX2 conversion is pending due missing local KTX2/Basis tooling.

This task does not wire textures into the frontend, implement R3F materials, create shaders, modify React/CSS production code, create final GLB assets, or add roadmap tickets.

---

## 2. Delivery Status

| Deliverable | Status | Notes |
| --- | --- | --- |
| Texture/material library folder | PASS | Created under `mithaq-project-docs/mithaq-dark-texture-material-library/`. |
| Actual texture files | PASS | 12 WebP files created. |
| Dark wood family | PASS | Base, subtle, preview WebP. |
| Aged parchment family | PASS | Base, subtle, preview WebP. |
| Gold foil family | PASS | Base, subtle, preview WebP. |
| Dark leather family | PASS | Base, subtle, preview WebP. |
| WebP optimized files | PASS | 1024px base/subtle and 512px previews. |
| KTX2 files | PASS WITH CONDITIONS | KTX2 conversion pending; no local `toktx`/`basisu` available. |
| Source/license register | PASS | Self-created procedural assets documented. |
| Material usage guide | PASS | Usage, CSS, R3F, readability, mobile notes included. |
| Optimization report | PASS | Sizes/dimensions documented. |
| Visual contact sheet | PASS | HTML and PNG contact sheets created. |
| Production integration | Not started | Correctly out of scope. |

---

## 3. Library Folder Structure

```txt
mithaq-dark-texture-material-library/
  README.md
  texture-license-register.md
  texture-optimization-report.md
  material-usage-guide.md

  webp/
    wood-dark/
    parchment-aged/
    gold-foil/
    leather-dark/

  ktx2/
    wood-dark/
    parchment-aged/
    gold-foil/
    leather-dark/

  preview/
    material-contact-sheet.html
    material-contact-sheet.png

  source/
    source-notes.md
```

Recommended future app path, if approved later:

```txt
/public/assets/textures/mithaq/
```

Do not move these files into production asset paths during P4.06.

---

## 4. Texture Family Index

| Family | WebP Base | WebP Subtle | KTX2 Base | KTX2 Subtle | Optional Maps | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Dark Wood | Yes | Yes | Pending | Pending | Not produced | WebP complete / KTX2 pending |
| Aged Parchment | Yes | Yes | Pending | Pending | Not produced | WebP complete / KTX2 pending |
| Gold Foil | Yes | Yes | Pending | Pending | Not produced | WebP complete / KTX2 pending |
| Dark Leather | Yes | Yes | Pending | Pending | Not produced | WebP complete / KTX2 pending |

---

## 5. Dark Wood Texture Notes

| Area | Direction |
| --- | --- |
| Visual feel | Dark wenge/walnut legal desk, subtle polished grain. |
| Intended use | Legal desk, gavel reference, dark section background accents, static hero/fallback desk imagery. |
| CSS use | Use subtle variant under dark overlay. |
| 3D use | Future desk/gavel reference; KTX2 conversion pending. |
| Tiling | Procedural seamless-style surface; verify before large hero repetition. |
| Readability | Subtle variant can sit behind overlays; avoid base directly behind small text. |
| Avoided | Orange/rustic farmhouse wood, glossy plastic, fantasy wood. |

Files:

- `webp/wood-dark/mithaq-wood-dark-base-color-1024.webp`
- `webp/wood-dark/mithaq-wood-dark-subtle-color-1024.webp`
- `webp/wood-dark/mithaq-wood-dark-preview-color-512.webp`

---

## 6. Aged Parchment Texture Notes

| Area | Direction |
| --- | --- |
| Visual feel | Warm legal paper, subtle fibers, aged but not dirty. |
| Intended use | Workshop dossier cards, document visuals, fragmented document posters, card accents. |
| CSS use | Use as card/document surface; verify contrast before text. |
| 3D use | Future paper planes/documents; KTX2 conversion pending. |
| Tiling | Procedural paper surface; best used in contained card/document areas. |
| Readability | Subtle variant preferred near text; base decorative or large document surface. |
| Avoided | Medieval scroll, pirate map, high-noise dirty paper. |

Files:

- `webp/parchment-aged/mithaq-parchment-aged-base-color-1024.webp`
- `webp/parchment-aged/mithaq-parchment-aged-subtle-color-1024.webp`
- `webp/parchment-aged/mithaq-parchment-aged-preview-color-512.webp`

---

## 7. Gold Foil Texture Notes

| Area | Direction |
| --- | --- |
| Visual feel | Muted stamped brass-gold foil, ceremonial and official. |
| Intended use | Seal material reference, stamped accents, card seals, gold linework. |
| CSS use | Decorative accent only; not body text background. |
| 3D use | Future seal/brass/gold maps; KTX2 conversion pending. |
| Tiling | Use sparingly as accent/mask; avoid large repeated fields. |
| Readability | Unsafe behind text unless heavily masked and tested. |
| Avoided | Neon, mirror chrome, glitter, fantasy magic, plastic shine. |

Files:

- `webp/gold-foil/mithaq-gold-foil-base-color-1024.webp`
- `webp/gold-foil/mithaq-gold-foil-subtle-color-1024.webp`
- `webp/gold-foil/mithaq-gold-foil-preview-color-512.webp`

---

## 8. Dark Leather Texture Notes

| Area | Direction |
| --- | --- |
| Visual feel | Dark legal writing pad / folio with subtle grain. |
| Intended use | Leather pad, legal folio/dossier feeling, dark premium panel accents. |
| CSS use | Use subtle variant for panels; overlay required near text. |
| 3D use | Future desk/leather pad material; KTX2 conversion pending. |
| Tiling | Procedural fine grain; verify repetition on large surfaces. |
| Readability | Subtle variant safer; avoid base behind small body copy. |
| Avoided | Fashion handbag leather, reptile skin, high-gloss plastic. |

Files:

- `webp/leather-dark/mithaq-leather-dark-base-color-1024.webp`
- `webp/leather-dark/mithaq-leather-dark-subtle-color-1024.webp`
- `webp/leather-dark/mithaq-leather-dark-preview-color-512.webp`

---

## 9. WebP Asset Index

| File | Family | Dimensions | Size | Intended Usage | Tiling | Color Space | Compression | Source | License |
| --- | --- | --- | ---: | --- | --- | --- | --- | --- | --- |
| `mithaq-wood-dark-base-color-1024.webp` | Wood | 1024 x 1024 | 9.4 KB | CSS / static / future 3D source | Seamless-style, verify | sRGB | WebP q78 | Procedural | Self-created |
| `mithaq-wood-dark-subtle-color-1024.webp` | Wood | 1024 x 1024 | 5.5 KB | CSS subtle background | Seamless-style, verify | sRGB | WebP q72 | Procedural | Self-created |
| `mithaq-wood-dark-preview-color-512.webp` | Wood | 512 x 512 | 3.2 KB | Preview/contact sheet | N/A | sRGB | WebP q76 | Procedural | Self-created |
| `mithaq-parchment-aged-base-color-1024.webp` | Parchment | 1024 x 1024 | 13.0 KB | Document/card surface | Contained use preferred | sRGB | WebP q78 | Procedural | Self-created |
| `mithaq-parchment-aged-subtle-color-1024.webp` | Parchment | 1024 x 1024 | 4.3 KB | Text-adjacent document surface | Contained use preferred | sRGB | WebP q72 | Procedural | Self-created |
| `mithaq-parchment-aged-preview-color-512.webp` | Parchment | 512 x 512 | 2.3 KB | Preview/contact sheet | N/A | sRGB | WebP q76 | Procedural | Self-created |
| `mithaq-gold-foil-base-color-1024.webp` | Gold | 1024 x 1024 | 22.2 KB | Seal/accent reference | Accent use preferred | sRGB | WebP q78 | Procedural | Self-created |
| `mithaq-gold-foil-subtle-color-1024.webp` | Gold | 1024 x 1024 | 9.3 KB | Decorative accent | Accent use preferred | sRGB | WebP q72 | Procedural | Self-created |
| `mithaq-gold-foil-preview-color-512.webp` | Gold | 512 x 512 | 6.9 KB | Preview/contact sheet | N/A | sRGB | WebP q76 | Procedural | Self-created |
| `mithaq-leather-dark-base-color-1024.webp` | Leather | 1024 x 1024 | 12.3 KB | Panel/leather surface | Seamless-style, verify | sRGB | WebP q78 | Procedural | Self-created |
| `mithaq-leather-dark-subtle-color-1024.webp` | Leather | 1024 x 1024 | 2.9 KB | Subtle panel surface | Seamless-style, verify | sRGB | WebP q72 | Procedural | Self-created |
| `mithaq-leather-dark-preview-color-512.webp` | Leather | 512 x 512 | 1.1 KB | Preview/contact sheet | N/A | sRGB | WebP q76 | Procedural | Self-created |

---

## 10. KTX2 Asset Index

KTX2 conversion is pending. Placeholder conversion notes exist in each KTX2 family folder.

| Planned File | Family | Status | Reason |
| --- | --- | --- | --- |
| `mithaq-wood-dark-base-color-1024.ktx2` | Wood | Pending | No local KTX2/Basis encoder available. |
| `mithaq-wood-dark-subtle-color-1024.ktx2` | Wood | Pending | No local KTX2/Basis encoder available. |
| `mithaq-parchment-aged-base-color-1024.ktx2` | Parchment | Pending | No local KTX2/Basis encoder available. |
| `mithaq-parchment-aged-subtle-color-1024.ktx2` | Parchment | Pending | No local KTX2/Basis encoder available. |
| `mithaq-gold-foil-base-color-1024.ktx2` | Gold | Pending | No local KTX2/Basis encoder available. |
| `mithaq-gold-foil-subtle-color-1024.ktx2` | Gold | Pending | No local KTX2/Basis encoder available. |
| `mithaq-leather-dark-base-color-1024.ktx2` | Leather | Pending | No local KTX2/Basis encoder available. |
| `mithaq-leather-dark-subtle-color-1024.ktx2` | Leather | Pending | No local KTX2/Basis encoder available. |

Do not silently substitute WebP for KTX2 in WebGL production. Real KTX2 files must be generated later using verified tooling such as `toktx` or `basisu`.

---

## 11. Source / License Summary

See:

[texture-license-register.md](D:/Clinets/MITHAQ/MITHAQ/mithaq-project-docs/mithaq-dark-texture-material-library/texture-license-register.md:1)

Summary:

- Source type: locally procedurally generated
- Tool: Python/Pillow
- External source images: none
- License risk: low
- Commercial use: allowed for project use, subject to owner approval
- Attribution: none required

---

## 12. Material Usage Guide Summary

See:

[material-usage-guide.md](D:/Clinets/MITHAQ/MITHAQ/mithaq-project-docs/mithaq-dark-texture-material-library/material-usage-guide.md:1)

Core use:

- Wood for desk/gavel/background surfaces.
- Parchment for documents and dossier cards.
- Gold foil for seal and small ceremonial accents.
- Leather for writing pad/panel surfaces.

---

## 13. CSS Background Usage Notes

CSS examples are planning notes only. Do not import these textures into production CSS during P4.06.

```css
/* Planning example only - do not wire into production in this task */
.surface-wood {
  background-image:
    linear-gradient(rgba(8, 7, 15, .82), rgba(8, 7, 15, .9)),
    url("./webp/wood-dark/mithaq-wood-dark-subtle-color-1024.webp");
}
```

Rules:

- Use subtle variants under text-adjacent surfaces.
- Add solid/dark overlays to protect readability.
- Avoid global texture loading.
- Avoid gold behind text.
- Use static poster assets rather than layered texture stacks where performance matters.

---

## 14. Three.js / R3F Usage Notes

Three.js/R3F notes are for later implementation only.

| Material | Three.js Direction |
| --- | --- |
| Dark wood | `MeshPhysicalMaterial`, high roughness, subtle normal later. |
| Parchment | `MeshStandardMaterial`, low roughness variation, paper normal later. |
| Gold foil | `MeshPhysicalMaterial`, high metalness, controlled roughness. |
| Leather | `MeshStandardMaterial`, high roughness, subtle normal later. |

Later KTX2 usage:

- Load KTX2 through Three.js `KTX2Loader` later.
- Do not implement loader in P4.06.
- Color maps should use sRGB handling later.
- Normal/roughness/metalness maps must not be treated as sRGB.

---

## 15. Accessibility / Readability Notes

| Risk | Rule |
| --- | --- |
| Noisy texture under body copy | Use subtle variant + dark overlay. |
| Gold behind text | Avoid unless contrast tested. |
| Parchment behind small text | Use clean overlay or solid surface. |
| Leather/wood contrast too low | Ensure CTA and text remain clear. |
| Mobile compression artifacts | Avoid noisy large texture backgrounds. |
| CSS texture overuse | Use texture sparingly to keep premium feel. |

Safe for text backgrounds with overlay:

- `mithaq-wood-dark-subtle-color-1024.webp`
- `mithaq-leather-dark-subtle-color-1024.webp`

Use with caution:

- `mithaq-parchment-aged-subtle-color-1024.webp`

Decorative only unless heavily masked/tested:

- Gold foil base/subtle
- Parchment base behind small text
- Wood/leather base behind body copy

No WCAG compliance is claimed until final contrast testing.

---

## 16. Performance Notes

| Area | Rule |
| --- | --- |
| Critical path | Do not load all textures on first paint. |
| Hero | Use static poster/subtle texture only if needed. |
| Non-critical sections | Lazy-load or use CSS subtle variants. |
| Mobile | Prefer 512-1024px texture versions. |
| DPR | Avoid oversized textures on mobile. |
| KTX2 | Preferred for WebGL texture maps once converted. |
| CSS | WebP preferred for backgrounds. |
| Total | Keep library optimized and modular. |

The current WebP set is very small, but production should still avoid global loading and should only load scene-relevant textures.

---

## 17. Texture Preview / Contact Sheet Link

Visual previews:

- [material-contact-sheet.html](D:/Clinets/MITHAQ/MITHAQ/mithaq-project-docs/mithaq-dark-texture-material-library/preview/material-contact-sheet.html:1)
- [material-contact-sheet.png](D:/Clinets/MITHAQ/MITHAQ/mithaq-project-docs/mithaq-dark-texture-material-library/preview/material-contact-sheet.png)

---

## 18. Optimization Summary

See:

[texture-optimization-report.md](D:/Clinets/MITHAQ/MITHAQ/mithaq-project-docs/mithaq-dark-texture-material-library/texture-optimization-report.md:1)

Summary:

- Total WebP library size: 92.6 KB
- Contact sheet PNG: 464.2 KB
- KTX2 complete size: 0 bytes; conversion pending
- Largest WebP: gold foil base at 22.2 KB
- Recommended critical path: none by default, or one subtle hero texture only if required
- Recommended lazy load: parchment/workshop/leather/gold section textures

---

## 19. QA Checklist

| Check | Status | Notes |
| --- | --- | --- |
| Actual texture files created | PASS | 12 WebP files exist. |
| WebP files present | PASS | Base/subtle/preview for all families. |
| KTX2 files present or pending | PASS WITH CONDITIONS | Pending; no local encoder available. |
| Dark wood texture present | PASS | WebP family complete. |
| Aged parchment texture present | PASS | WebP family complete. |
| Gold foil texture present | PASS | WebP family complete. |
| Dark leather texture present | PASS | WebP family complete. |
| Base and subtle variants included | PASS | All families include both. |
| File sizes documented | PASS | README and optimization report. |
| Dimensions documented | PASS | README and optimization report. |
| Source/license notes documented | PASS | License register and source notes. |
| Commercial-use status clear | PASS | Self-created procedural assets. |
| Material usage guide created | PASS | `material-usage-guide.md`. |
| Contact sheet/visual preview created | PASS | HTML and PNG. |
| CSS usage notes included | PASS | README and usage guide. |
| Three.js/R3F usage notes included | PASS | README and usage guide. |
| Accessibility/readability warnings included | PASS | README and usage guide. |
| Performance notes included | PASS | README and optimization report. |
| Unsafe/decorative-only variants marked | PASS | Gold and base texture warnings included. |
| Production integration avoided | PASS | No app/frontend files modified. |
| New roadmap tickets avoided | PASS | No new tickets created. |

---

## 20. Final Recommendation

Use this WebP texture library as the Phase 4 material source of truth for design review, Figma swatches, static fallback placeholders, and later texture conversion.

Recommended next steps in later phases:

1. Review visual material fit with stakeholder/art direction.
2. Convert base/subtle color textures to KTX2 using verified tooling.
3. Create optional PBR normal/roughness/metalness maps only if P5/P8 implementation needs them.
4. Do not load all textures globally.
5. Do not wire into frontend or R3F until implementation tickets authorize it.

---

## 21. Final Status

**PASS WITH CONDITIONS - P4.06 complete. Optimized WebP texture library exists for dark wood, aged parchment, gold foil, and leather grain, with source/license register, optimization report, contact sheet, material usage guide, performance/accessibility notes, and no production integration. KTX2 conversion remains pending because no local KTX2/Basis encoder is available.**

Conditions remaining:

- KTX2 conversion pending.
- Optional PBR maps pending.
- Final model texture assignment pending.
- Figma material swatches pending.
- Stakeholder visual approval pending.
- Frontend/R3F integration pending.
- Final accessibility/performance QA pending.
