# Mithaq Floating Documents

Ticket: P5.05 — Floating Documents (Scene 03)

Status: PASS WITH CONDITIONS

## Asset Name

Mithaq Floating Documents

## Output Paths

| Output | Path |
| --- | --- |
| Blender source | `source/documents.blend` |
| Raw GLB | `exports/documents.raw.glb` |
| Optimized GLB | `exports/documents.opt.glb` |
| Preview renders | `renders/` |
| Reports | `reports/` |
| Production script | `scripts/create_mithaq_documents.py` |
| Validation script | `scripts/validate_mithaq_documents.py` |

## Quick Usage Summary

This package contains eight separate low-poly floating document meshes for Scene 03 — The Gap. The assets represent fragmented legal notes, academic references, unfinished forms, loose case papers, research sheets, memo drafts, pleading fragments, and practice checklists. The marks are abstract only; no readable fake legal text, court marks, personal data, case numbers, official stamps, or false legal claims are included.

Recommended future import path:

```tsx
import { useGLTF } from '@react-three/drei';

const documents = useGLTF('/models/mithaq/documents.opt.glb');
```

## Key Metrics

| Metric | Value |
| --- | ---: |
| Document count | 8 |
| Total triangle count | 760 |
| Mesh count | 8 |
| Material count | 4 |
| Texture count | 0 |
| Raw GLB size | 50,164 bytes / 0.0478 MB |
| Optimized GLB size | 28,652 bytes / 0.0273 MB |
| Preferred size target | PASS, under 500 KB |
| Hard size target | PASS, under 1.2 MB |

## Known Conditions

- `gltfpack` was not available in the execution shell, so `documents.opt.glb` was created through Blender's real Draco-compressed GLB export.
- Final material/art approval, mobile LOD, final R3F import validation, and Scene 03 orbit/convergence validation remain pending.
- No animation, R3F code, shaders, orbit behavior, or convergence logic was implemented in this ticket.
