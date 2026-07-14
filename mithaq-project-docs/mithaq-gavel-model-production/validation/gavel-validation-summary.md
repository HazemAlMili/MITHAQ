# Gavel Validation Summary

**Ticket:** P5.02 - Gavel Model Production  
**Status:** PASS WITH CONDITIONS  
**Date:** 2026-06-21  

---

## Tool Versions

| Tool | Version / Status |
| --- | --- |
| Blender | 5.1.2 |
| Blender executable | `C:\Program Files\Blender Foundation\Blender 5.1\blender.exe` |
| gltfpack | Unavailable in this shell; `gltfpack -h` failed |
| Optimization fallback | Blender GLTF Draco compression |

---

## Required Output Validation

| Check | Status | Notes |
| --- | --- | --- |
| `source/gavel.blend` exists | PASS | Blender source created. |
| `exports/gavel.raw.glb` exists | PASS | Raw GLB created. |
| `exports/gavel.opt.glb` exists | PASS | Optimized GLB created with Blender Draco compression. |
| Optimized GLB is not a renamed raw GLB | PASS | Separate compressed GLB export. |
| Front preview exists | PASS | `preview/gavel-preview-front.png` |
| Side preview exists | PASS | `preview/gavel-preview-side.png` |
| Perspective preview exists | PASS | `preview/gavel-preview-perspective.png` |
| Opening angle preview exists | PASS | `preview/gavel-preview-opening-angle.png` |
| Wireframe preview exists | PASS | `preview/gavel-preview-wireframe.png` |
| Asset report exists | PASS | `gavel-asset-report.md` |
| Optimization report exists | PASS | `gavel-optimization-report.md` |
| R3F handoff exists | PASS | `gavel-r3f-handoff-notes.md` |
| File-size report exists | PASS | `validation/gavel-file-size.txt` |
| GLTF inspect JSON exists | PASS | `validation/gavel-gltf-inspect.json` |

---

## Metrics

| Metric | Value | Target | Status |
| --- | ---: | ---: | --- |
| Raw GLB size | 416,000 bytes / 406.3 KB | Document | PASS |
| Optimized GLB size | 89,480 bytes / 87.4 KB | <= 1.2 MB | PASS |
| Triangle count | 15,084 | 8k-18k | PASS |
| Mesh count | 13 | Low | PASS |
| Material count | 4 | 2-4 | PASS |
| Texture count | 0 | Minimal | PASS |
| Texture dimensions | N/A | <= 1024px if used | PASS |

---

## Import / Export Status

| File | Import Test | Mesh Count | Material Count | Triangle Count |
| --- | --- | ---: | ---: | ---: |
| `gavel.raw.glb` | PASS | 13 | 4 | 15,084 |
| `gavel.opt.glb` | PASS | 13 | 4 | 15,084 |

Validation method:

```txt
Blender 5.1.2 background import_scene.gltf import test
```

---

## Pivot / Origin

| Element | Location | Purpose |
| --- | --- | --- |
| `Gavel_Pivot_Helper` | `(0, -0.18, 0)` | Intended descent/strike animation pivot near handle/head joint. |
| `Gavel_Contact_Point_Negative_X` | `(-0.78, 0, 0)` | Intended desk impact/contact reference. |

---

## UV Status

Smart UV Project was applied to visible mesh objects. Materials are procedural and no external image textures are required.

---

## Final Validation Status

**PASS WITH CONDITIONS - The real Blender source, raw GLB, optimized GLB, previews, validation, and reports exist. The optimized GLB meets the <= 1.2 MB target. Condition: gltfpack is still unavailable in this shell, so Blender Draco compression was used as the real optimization path.**
