# P5.07 R3F Performance Notes

## Observed Runtime

The PoC rendered successfully in local Chromium headless shell with all required screenshots captured and no console errors.

Formal FPS profiling was not performed in this ticket. This remains for P5.08 Mobile Performance Audit.

## Device / Browser Used

- Browser: Chromium headless shell
- Viewport for captures: 1440 x 900
- Device tier detected in validation: `high`

## DPR Strategy

`MithaqCanvas` caps DPR by device tier:

- high: `[1, 1.75]`
- mid: `[1, 1.35]`
- low: `[1, 1]`

## Low-Tier Simplifications

- Antialiasing disabled for low tier.
- Postprocessing gate disabled for low tier.
- Proxy complexity is already lightweight and does not import production GLBs.

## Bundle Notes

The final build passes but warns about a large single chunk:

```txt
assets/index-DJH8mo-Q.js: 993.17 kB / gzip 274.63 kB
```

This is acceptable for the isolated architecture PoC because Three/R3F/Drei are bundled without production chunking. Phase 8 should evaluate dynamic imports, route-level splitting, and manual chunks.

## What Remains For P5.08

- Real mobile device FPS checks
- Thermal/performance behavior on iOS and Android
- DPR tuning with final assets
- Shader + GLB integration profiling
- Reduced-motion and low-tier fallback validation on physical devices
