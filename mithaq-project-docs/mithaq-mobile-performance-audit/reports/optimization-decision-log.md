# Optimization Decision Log

## Applied Optimizations

| Decision | Applied | Reason |
| --- | --- | --- |
| Local Draco decoder | Yes | Prevented blocked external decoder fetches from `gstatic`. |
| Optimized Phase 5 GLBs | Yes | Used `gavel.opt.glb`, `seal.opt.glb`, and `desk.opt.glb`. |
| Device-tier query forcing | Yes | Allowed deterministic mid/low-tier audit modes. |
| DPR cap | Yes | Mid/low tier cap set to `1`; high tier capped to `1.5`. |
| Disable post-processing below high tier | Yes | Protected mobile and reduced-motion paths from optional effects. |
| Disable antialias except high tier | Yes | Reduced renderer cost for mid/low tiers. |
| Lower particle counts | Yes | Reduced audit particle density for low-tier mode. |
| Avoid per-frame Zustand writes for audit progress | Yes | Used a mutable audit progress value to reduce React/store churn. |
| Keep text DOM-first | Yes | Maintained accessibility direction; no canvas-only meaningful text. |

## Intentionally Not Applied

| Decision | Reason |
| --- | --- |
| Remove real gavel/seal/desk assets from final workload | Would invalidate the representative Scene 01 audit. |
| Rename raw files as optimized | Not allowed and not needed. |
| Claim physical device performance | No physical device was available. |
| Proceed to P5.09 | Out of scope for P5.08. |

## Decision Outcome

The optimizations are directionally correct but insufficient. The Scene 01 real-asset workload remains under the hard 30 FPS floor in the available mobile-like audit harness.

Recommended next engineering decision: mobile should default to static/fallback poster or drastically simplified WebGL, and real-time Scene 01 mobile should remain blocked until a lighter workload is proven.

