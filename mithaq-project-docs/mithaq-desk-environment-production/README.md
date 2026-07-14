# Mithaq Legal Desk Environment

Ticket: P5.04 — Legal Desk Environment

Status: PASS WITH CONDITIONS

## Asset Name

Mithaq Legal Desk Environment

## Output Paths

| Output | Path |
| --- | --- |
| Blender source | `source/desk.blend` |
| Raw GLB | `exports/desk.raw.glb` |
| Optimized GLB | `exports/desk.opt.glb` |
| Preview renders | `renders/` |
| Reports | `reports/` |
| Production script | `scripts/create_mithaq_desk.py` |
| Validation script | `scripts/validate_mithaq_desk.py` |

## Quick Usage Summary

The desk is the grounded physical stage for Mithaq's gavel trigger, Seal reveal, hero anchor, organized legal desk transition, workshop dossier placement, and final covenant callback. It is intentionally not the hero object. It provides dark wood depth, premium legal tactility, a dark leather writing pad, subtle placement cues, and anchor points for later gavel/Seal composition.

Recommended future import path:

```tsx
import { useGLTF } from '@react-three/drei';

const desk = useGLTF('/models/mithaq/desk.opt.glb');
```

## Key Metrics

| Metric | Value |
| --- | ---: |
| Triangle count | 1,040 |
| Mesh count | 7 |
| Material count | 4 |
| Texture count | 0 |
| Raw GLB size | 43,276 bytes / 0.0413 MB |
| Optimized GLB size | 14,228 bytes / 0.0136 MB |
| Size target | PASS, under 1.2 MB |

## Known Conditions

- `gltfpack` was not available in the execution shell, so `desk.opt.glb` was created through Blender's real Draco-compressed GLB export.
- Final material/art approval, KTX2 conversion, mobile LOD, final R3F import validation, ripple shader validation, Scene 01 lighting validation, and real-device performance validation remain pending.
- Gavel and Seal were imported only for `renders/desk-preview-hero-gavel-seal-layout.png`; they are not baked into `desk.raw.glb` or `desk.opt.glb`.
