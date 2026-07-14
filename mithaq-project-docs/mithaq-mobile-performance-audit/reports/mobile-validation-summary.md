# Mobile Validation Summary

## Validation Checklist

| Check | Result | Notes |
| --- | --- | --- |
| Baseline before optimization recorded | PASS | Proxy Scene 01 baseline saved in `data/baseline-proxy-runs.json`. |
| Production build used | PASS | Vite production build was measured. |
| Mid-tier mobile profile measured | FAIL | Average FPS stayed below 30 in all three final runs. |
| Low-tier mobile profile measured | FAIL | Only one average crossed 30 FPS, with poor 1% low and failing repeated runs. |
| Reduced-motion profile measured | FAIL | Architecture exists, but real-asset workload stayed below hard floor. |
| WebGL fallback measured | PASS | Forced fallback rendered without canvas and no console errors. |
| Scene 01–10 scroll regression | PASS WITH CONDITIONS | Forward/reverse sweep passed in local Chromium harness. |
| Portrait/landscape resize smoke check | PASS WITH CONDITIONS | Canvas remained mounted in both orientations. |
| Console runtime errors | PASS | Final runs reported 0 console errors and 0 shader failures. |
| Captures exist | PASS | Four required captures exist and are non-empty. |
| Physical Android validation | BLOCKED | Not available in this execution environment. |
| iOS Safari validation | BLOCKED | Not available in this execution environment. |
| P5.09 started | PASS | Not started. |

## Regression Evidence

Scene sweep and fallback evidence is saved in `data/scene-regression.json`.

The sweep confirms:

- Scene 01 and Scene 10 direct access render.
- Forward and reverse scroll-map traversal completes.
- WebGL fallback path is visible when forced.
- Canvas count remains stable in portrait and landscape smoke checks.

## Final Validation Decision

FAIL. The mobile fallback path is viable, but the real-time WebGL Scene 01 path cannot be approved from this audit.

