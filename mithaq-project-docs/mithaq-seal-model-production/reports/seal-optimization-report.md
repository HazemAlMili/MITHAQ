# Mithaq Seal Optimization Report

Ticket: P5.03 — Mithaq Seal Model Production

Status: PASS WITH CONDITIONS

## Tool Availability

| Tool | Result |
| --- | --- |
| Blender | Available: `C:\Program Files\Blender Foundation\Blender 5.1\blender.exe`, version 5.1.2 |
| `gltfpack -v` | Unavailable in this execution shell |

## Optimization Summary

| Metric | Raw GLB | Optimized GLB | Target | Status |
| --- | ---: | ---: | ---: | --- |
| File size | 296,872 bytes / 0.2831 MB | 57,588 bytes / 0.0549 MB | <= 1.2 MB | PASS |
| Triangle count | 8,578 | 8,578 | <= 8k preferred / <= 12k hard | PASS WITH NOTE |
| Mesh count | 8 | 8 | <= 10 | PASS |
| Material count | 4 | 4 | <= 4 | PASS |
| Texture count | 0 | 0 | 0-2 | PASS |
| Largest texture | N/A | N/A | <= 1024px | PASS |

Compression ratio: approximately `5.15:1`.

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
- Selected Seal mesh objects only
- Applied export transforms
- Y-up export
- Cameras/lights excluded
- Draco mesh compression enabled
- Compression level: 6
- Position quantization: 14
- Normal quantization: 10
- Texcoord quantization: 12

## Result

The optimized GLB is under both the required `1.2 MB` target and the preferred `500 KB` target. Full PASS is withheld only because the requested `gltfpack` optimization could not be run in this shell.
