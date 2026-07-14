# Mithaq Floating Documents Optimization Report

Ticket: P5.05 — Floating Documents (Scene 03)

Status: PASS WITH CONDITIONS

## Tool Availability

| Tool | Result |
| --- | --- |
| Blender | Available: `C:\Program Files\Blender Foundation\Blender 5.1\blender.exe`, version 5.1.2 |
| `gltfpack -v` | Unavailable in this execution shell |

## Optimization Summary

| Metric | Raw GLB | Optimized GLB | Target | Status |
| --- | ---: | ---: | ---: | --- |
| File size | 50,164 bytes / 0.0478 MB | 28,652 bytes / 0.0273 MB | <= 500 KB preferred / <= 1.2 MB hard | PASS |
| Total triangle count | 760 | 760 | <= 4k target / <= 5.5k hard | PASS |
| Per-document triangles | 90-100 | 90-100 | <= 500 each | PASS |
| Mesh count | 8 | 8 | 8-16 | PASS |
| Material count | 4 | 4 | <= 4 | PASS |
| Texture count | 0 | 0 | 0-1 | PASS |

Compression ratio: approximately `1.75:1`.

## Command Attempted

```powershell
gltfpack -v
```

Result: `gltfpack` was not recognized in this execution shell.

## Optimization Method Used

Because `gltfpack` was unavailable, the optimized file was exported through Blender's real GLB exporter with Draco mesh compression enabled:

```txt
Blender GLTF exporter Draco compression fallback
```

This is not a renamed raw GLB. Blender logged Draco encoder activity during export, and the optimized GLB re-imported successfully through Blender's GLTF importer.

## Fallback Details

Blender export settings used:

- GLB format
- Selected document mesh objects only
- Applied export transforms
- Y-up export
- Cameras/lights excluded
- Helper empties excluded
- Draco mesh compression enabled
- Compression level: 6

## Result

The optimized GLB is under both the preferred `500 KB` target and the hard `1.2 MB` maximum. Full PASS is withheld only because the requested `gltfpack` optimization could not be run in this shell.
