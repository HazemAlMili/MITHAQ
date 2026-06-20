# Texture Optimization Report

## Summary

| Metric | Value |
| --- | ---: |
| Total WebP library size | 94,850 bytes / 92.6 KB |
| Total KTX2 library size | 0 bytes complete / conversion pending |
| Contact sheet PNG size | 475,382 bytes / 464.2 KB |
| Largest WebP texture | `mithaq-gold-foil-base-color-1024.webp` at 22.2 KB |
| Critical path recommendation | Use no texture by default, or one subtle hero texture only if required. |
| Lazy-load recommendation | Load parchment/workshop/leather/gold textures only in relevant sections. |
| Mobile recommendation | Prefer subtle variants; avoid decorative gold/leather if not essential. |

## Optimization Table

| File | Original Size | Optimized Size | Dimensions | Format | Conversion Tool | Notes |
| --- | ---: | ---: | --- | --- | --- | --- |
| `mithaq-wood-dark-base-color-1024.webp` | Procedural source | 9.4 KB | 1024 x 1024 | WebP | Pillow WebP q78 | Dark legal desk base. |
| `mithaq-wood-dark-subtle-color-1024.webp` | Procedural source | 5.5 KB | 1024 x 1024 | WebP | Pillow WebP q72 | Text-adjacent background variant. |
| `mithaq-wood-dark-preview-color-512.webp` | Procedural source | 3.2 KB | 512 x 512 | WebP | Pillow WebP q76 | Preview/swatch. |
| `mithaq-parchment-aged-base-color-1024.webp` | Procedural source | 13.0 KB | 1024 x 1024 | WebP | Pillow WebP q78 | Document/card surface. |
| `mithaq-parchment-aged-subtle-color-1024.webp` | Procedural source | 4.3 KB | 1024 x 1024 | WebP | Pillow WebP q72 | Safer near text with contrast check. |
| `mithaq-parchment-aged-preview-color-512.webp` | Procedural source | 2.3 KB | 512 x 512 | WebP | Pillow WebP q76 | Preview/swatch. |
| `mithaq-gold-foil-base-color-1024.webp` | Procedural source | 22.2 KB | 1024 x 1024 | WebP | Pillow WebP q78 | Seal/accent reference. |
| `mithaq-gold-foil-subtle-color-1024.webp` | Procedural source | 9.3 KB | 1024 x 1024 | WebP | Pillow WebP q72 | Decorative-only accent. |
| `mithaq-gold-foil-preview-color-512.webp` | Procedural source | 6.9 KB | 512 x 512 | WebP | Pillow WebP q76 | Preview/swatch. |
| `mithaq-leather-dark-base-color-1024.webp` | Procedural source | 12.3 KB | 1024 x 1024 | WebP | Pillow WebP q78 | Dark writing pad/folio surface. |
| `mithaq-leather-dark-subtle-color-1024.webp` | Procedural source | 2.9 KB | 1024 x 1024 | WebP | Pillow WebP q72 | Text-adjacent panel variant. |
| `mithaq-leather-dark-preview-color-512.webp` | Procedural source | 1.1 KB | 512 x 512 | WebP | Pillow WebP q76 | Preview/swatch. |
| `material-contact-sheet.png` | Generated preview | 464.2 KB | 1040 x 1120 | PNG | Pillow PNG | Visual review surface. |

## KTX2 Conversion Status

KTX2 conversion is pending because no local KTX2/Basis encoder was available:

- `toktx`: not found
- `basisu`: not found

Required later conversion targets:

- `ktx2/wood-dark/mithaq-wood-dark-base-color-1024.ktx2`
- `ktx2/wood-dark/mithaq-wood-dark-subtle-color-1024.ktx2`
- `ktx2/parchment-aged/mithaq-parchment-aged-base-color-1024.ktx2`
- `ktx2/parchment-aged/mithaq-parchment-aged-subtle-color-1024.ktx2`
- `ktx2/gold-foil/mithaq-gold-foil-base-color-1024.ktx2`
- `ktx2/gold-foil/mithaq-gold-foil-subtle-color-1024.ktx2`
- `ktx2/leather-dark/mithaq-leather-dark-base-color-1024.ktx2`
- `ktx2/leather-dark/mithaq-leather-dark-subtle-color-1024.ktx2`

Do not claim KTX2 completion until real `.ktx2` files are produced by a verified encoder.

