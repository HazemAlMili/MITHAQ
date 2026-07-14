# Mithaq Seal Model Production

Ticket: P5.03 — Mithaq Seal Model Production

Status: PASS WITH CONDITIONS

## Asset Name

Mithaq Seal

## Output Paths

| Output | Path |
| --- | --- |
| Blender source | `source/seal.blend` |
| Raw GLB | `exports/seal.raw.glb` |
| Optimized GLB | `exports/seal.opt.glb` |
| Preview renders | `renders/` |
| Reports | `reports/` |
| Production script | `scripts/create_mithaq_seal.py` |
| Validation script | `scripts/validate_mithaq_seal.py` |

## Quick Usage Summary

The Seal is the primary hero 3D brand object for Mithaq. It is built as a circular embossed legal seal with muted brass/gold materials, concentric raised rims, converted mesh Arabic text for `ميثاق`, and a minimal abstract scales motif. It is intended for Scene 01 reveal, Scene 02 hero anchoring, Scene 06 stamped/accent usage, and Scene 10 closing covenant callback.

Recommended future import path:

```tsx
import { useGLTF } from '@react-three/drei';

const seal = useGLTF('/models/mithaq/seal.opt.glb');
```

## Key Metrics

| Metric | Value |
| --- | ---: |
| Triangle count | 8,578 |
| Mesh count | 8 |
| Material count | 4 |
| Texture count | 0 |
| Raw GLB size | 296,872 bytes / 0.2831 MB |
| Optimized GLB size | 57,588 bytes / 0.0549 MB |
| Size target | PASS, under 1.2 MB |

## Known Conditions

- `gltfpack` was not available in the execution shell, so `seal.opt.glb` was created through Blender's real Draco-compressed GLB export.
- Arabic text is present as raised geometry using an Arabic presentation-form workaround for Blender mesh legibility; final logo/wordmark/calligraphy approval remains pending.
- Final stakeholder art approval, mobile LOD, final R3F import validation, Scene 01 lighting validation, and real-device performance validation remain pending.
