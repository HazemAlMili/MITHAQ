# Isolated Performance Report

## Environment

| Area | Value |
| --- | --- |
| Browser | Chromium headless shell via Playwright |
| Host | Windows |
| Sandbox | Vite + React + R3F |
| Desktop viewport | 1440 x 900 |
| Mobile-light viewport | 390 x 844, DPR 2 |
| WebGL | Local headless WebGL renderer |

## Build Result

`npm install`: passed with `0` vulnerabilities.  
`npm run build`: passed after sandbox permission escalation for Vite `dist` writes.

Build output:

- CSS: `1.87 kB`, gzip `0.87 kB`
- JS: `1,075.68 kB`, gzip `299.69 kB`
- Warning: chunk larger than `500 kB`

The chunk warning is documented but not treated as a P5.09 blocker because this is an isolated validation sandbox, not the production site architecture.

## Sandbox Validation Results

| Mode | Average FPS | Draw Calls | Triangles | Geometries | Textures | Console Errors |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Resting | 49.02 | 7 | 1,492 | 7 | 1 | 0 |
| Hover | 66.72 | 7 | 1,492 | 7 | 1 | 0 |
| Multiple | 53.07 | 19 | 4,452 | 7 | 1 | 0 |
| Mobile-light | 60.10 | 4 | 388 | 4 | 0 | 0 |
| Selected | 53.38 | 8 | 1,684 | 8 | 1 | 0 |
| Wireframe | 69.30 | 7 | 1,492 | 7 | 1 | 0 |

Source: `reports/dossier-sandbox-validation.json`

## Variant Asset Metrics

| Variant | Triangles | Vertices | Meshes | Materials | GLB Size | Texture Payload | Draw Calls |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Desktop Optimized | 1,480 | 784 | 3 | 4 | 17,544 bytes | 3,020 bytes | 3 |
| Mobile Optimized | 420 | 224 | 3 | 4 | 8,304 bytes | 3,020 bytes | 3 |

Full table: `reports/asset-metrics.csv`

## Console and Shader Status

Final capture pass:

- Captures: `6`
- Console errors: `0`
- Material/shader warnings: `0` in final capture pass
- External HDR dependency removed from sandbox after validation exposed a network fetch

## Limitations

- Measurements are local headless-browser evidence, not real-device approval.
- P5.08 failed the full mobile runtime floor, so these assets must not be integrated into a complete mobile runtime without another audit.
- FPS values are isolated-sandbox references only.

