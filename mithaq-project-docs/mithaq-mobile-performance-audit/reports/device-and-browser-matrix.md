# Device and Browser Matrix

## Tested Matrix

| Profile | Coverage | Result | Notes |
| --- | --- | --- | --- |
| Mobile mid-tier emulation | Tested | FAIL | Pixel 4a-style viewport, real-asset Scene 01 workload, headless Chromium SwiftShader. |
| Mobile low-tier emulation | Tested | FAIL | One warm run crossed 30 FPS average, but 1% low and repeated runs failed. |
| Reduced motion | Tested | FAIL | Reduced-motion architecture exists, but representative workload still rendered too slowly in this harness. |
| WebGL fallback | Tested | PASS | Forced fallback rendered without canvas and stayed stable. |
| Scene 01–10 scroll regression | Tested | PASS WITH CONDITIONS | Scene switching and scroll mapping passed in local Chromium harness. |
| Physical Android mid-tier | Not available | BLOCKED | Required for a full production confidence pass. |
| iOS Safari | Not available | BLOCKED | Still requires later device validation. |
| Samsung Internet | Not available | BLOCKED | Still requires later device validation. |

## Browser Detail

| Area | Value |
| --- | --- |
| Browser | Headless Chromium 149.0.7827.55 |
| WebGL | WebGL2 |
| Renderer | ANGLE / Vulkan / SwiftShader |
| Viewport | 390 x 844 |
| DPR | 2 |

## Matrix Decision

The available matrix is sufficient to identify a blocking performance risk, but it is not sufficient for a PASS. Physical Android and iOS validation remain required before mobile WebGL can be treated as approved.

