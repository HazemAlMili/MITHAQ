# Final Mobile Performance Report

## Executive Verdict

Status: FAIL

P5.08 cannot pass because the representative Scene 01 real-asset WebGL workload does not meet the hard mobile floor. The fallback path works, but the real-time mobile opening path is not validated.

## Final Performance Summary

| Profile | Runs | Average FPS Range | 1% Low Range | p95 Frame Time Range | Verdict |
| --- | ---: | ---: | ---: | ---: | --- |
| Mid-tier mobile emulation | 3 | 18.26–20.73 | 6.67–10.00 | 99.9–116.6 ms | FAIL |
| Low-tier mobile emulation | 3 | 13.94–30.17 | 8.57–14.99 | 50.1–116.6 ms | FAIL |
| Reduced motion | 3 | 12.15–14.66 | 8.57–10.00 | 100.0–116.7 ms | FAIL |
| WebGL fallback | 1 | 60.00 | 59.52 | 16.8 ms | PASS |

## Render Cost Snapshot

| Metric | Value |
| --- | ---: |
| Draw calls | 28 |
| Triangles | 24,356 |
| Geometries | 28 |
| Textures | 0 |
| Shader programs | 3 |
| Loaded asset payload | 1,489,413 bytes |
| Phase 5 hero GLB payload | 161,296 bytes |

## Asset Budget Verdict

The hero GLB payload is healthy. The Phase 5 gavel, seal, and desk optimized files total approximately `161 KB`, well below mobile asset payload risk thresholds.

The failure is runtime/rendering stability, not GLB file size.

## Recommendation

Use FALLBACK as the mobile-safe decision for the opening until a simpler Scene 01 workload passes on real devices. Do not increase mobile 3D complexity, particles, post-processing, shader effects, or camera choreography before a new audit proves the hard floor.

