# Mithaq 3D Feasibility Benchmark Report

**Official Ticket ID:** P1.05  
**Official Ticket Name:** 3D Feasibility Benchmark  
**Phase:** Phase 1, Research Synthesis & Direction Lock  
**Priority:** P0  
**Status:** PASS  
**Date:** 2026-06-18  

---

## 1. Executive Summary

A minimal React Three Fiber benchmark prototype was created and tested to validate Mithaq's planned hero direction at a technical level.

Prototype location:

`D:\Clinets\MITHAQ\mithaq-3d-benchmark`

Report decision:

**Option C - Vertical Slice Only Until Asset Optimization**

Reason:

- The benchmark works locally in Chromium with placeholder gavel/seal GLBs.
- Desktop local Chromium reached approximately 60 FPS in both lightweight and upper-budget asset scenarios.
- Mobile-sized Chromium viewport also remained around 60 FPS, but this is not a real mid-tier Android hardware test.
- DOM headline and CTA remained visible independently from canvas.
- Forced static fallback and forced reduced-motion fallback worked.
- Forced missing-GLB fallback worked, although it produced expected console errors that should be handled more quietly later.
- Final 3D assets, final shaders, real textures, BrowserStack/physical mobile testing, and final scroll choreography are not yet available.

The benchmark supports continuing with **Vertical Slice First**, but it does not yet justify committing to full production-grade 3D on all mobile tiers.

No final UI, final 3D model, final seal, final shader system, final sound design, or production website implementation was created.

---

## 2. Benchmark Context

This benchmark exists to reduce 3D risk before creative production continues.

It tested:

- Placeholder GLB loading.
- Minimal R3F canvas rendering.
- Scroll-driven camera/object motion.
- DOM-first headline and CTA.
- Static fallback.
- Reduced-motion fallback.
- Missing-asset fallback.
- Local Chromium desktop and mobile viewport behavior.

It did not test:

- Final gavel model.
- Final Mithaq Seal model.
- Final brand assets.
- Final Arabic/English typography.
- Final production shaders.
- Final sound design.
- BrowserStack or physical mobile devices.
- Safari, Samsung Internet, Firefox, or real mid-tier Android GPU behavior.

---

## 3. Current Mithaq Decisions from P0.06

- Mithaq is a premium bilingual 3D legal academy portfolio / landing experience.
- Opening direction: scroll-driven gavel trigger to Mithaq Seal reveal.
- The gavel is not the hero; the Seal is the hero.
- 3D style: symbolic realism.
- Primary conversion action: WhatsApp.
- MVP planning is bilingual.
- Sound effects are approved, but must be controlled and user-safe.
- Delivery approach: Vertical Slice First.
- Low-end devices must receive a static fallback.
- Reduced motion must avoid heavy camera movement.
- DOM content must be visible independently from canvas.

---

## 4. Device Targets from P1.04

| Device Tier | Target Experience | Benchmark Coverage |
| ----------- | ----------------- | ------------------ |
| High-End Desktop | Full R3F, 60 FPS target, 50 minimum | Locally tested in Chromium-like browser |
| Modern Mobile / Tablet | Simplified R3F, 45-60 FPS target, 35 minimum | Mobile viewport tested only, not physical device |
| Mid-Tier Mobile | Simplified/static hybrid, 30-45 FPS target | Not physically tested; must be validated later |
| Low-End / Reduced Motion | Static premium fallback | Forced fallback and forced reduced-motion tested |

Device coverage conclusion:

The local benchmark is sufficient for early feasibility, but not sufficient for final mobile performance approval.

---

## 5. Prototype Scope

| Element | Implemented? | Notes |
| ------- | ------------ | ----- |
| Fixed viewport R3F canvas | Yes | Canvas fills hero area |
| Perspective camera | Yes | Scroll-mapped camera position |
| Warm key/fill/rim lighting | Yes | Basic lighting only |
| Placeholder gavel-like object | Yes | Generated GLB placeholder |
| Placeholder circular seal object | Yes | Generated GLB placeholder |
| Desk/surface plane | Yes | R3F plane with dark material |
| Scroll-driven transform | Yes | Camera, object rotation, and seal reveal movement |
| DOM headline + CTA overlay | Yes | Visible before and independent from canvas |
| Static fallback | Yes | Forced with `?fallback=1` |
| Reduced-motion fallback | Yes | Forced with `?reduced=1` and media query support |
| Missing-GLB fallback | Yes | Forced with `?badmodel=1` |
| Optional audio policy check | Limited | No audio loaded; therefore no autoplay issue occurred |

---

## 6. Prototype Setup

| Area | Setup |
| ---- | ----- |
| Prototype folder | `mithaq-3d-benchmark` |
| Framework | Vite + React |
| 3D stack | React Three Fiber + Three.js |
| GLB loading | `GLTFLoader` from Three examples |
| Placeholder asset generation | `scripts/create-placeholder-glbs.mjs` |
| Static server | Local Node static server for built `dist` |
| Measurement method | In-browser DOM metrics panel + browser automation |
| Build command | `npm.cmd run build` |
| Asset generation command | `npm.cmd run generate:assets` |

Build output:

| Output | Size |
| ------ | ---: |
| `dist/index.html` | 459 bytes |
| CSS bundle | 2.59 KB, gzip 1.17 KB |
| JS bundle | 1,107.28 KB, gzip 308.32 KB |
| Lightweight GLB | 13,428 bytes |
| Upper-budget GLB | 1,272,152 bytes |

Build note:

Vite warned that the uncompressed JS chunk is larger than 500 KB. Gzipped JS is within the P1.04 initial critical JS budget, but production should still code-split/lazy-load 3D where possible.

---

## 7. Asset Scenarios Tested

| Scenario | Asset Size | Load Time | FPS Desktop | FPS Mobile | Result |
| -------- | ---------: | --------: | ----------: | ---------: | ------ |
| A - Lightweight | 13.4 KB GLB, 0 texture payload | 400 ms model-loaded marker; 23 ms GLB resource duration | 60.1 avg during scroll, 46.9 low | Not separately tested for A | Pass locally |
| B - Upper-Bound | 1.27 MB GLB, 0 texture payload | 401 ms model-loaded marker; 35 ms desktop GLB resource duration | 60.2 avg during scroll, 39.4 low | 60.0 avg, 53.5 low in mobile viewport | Pass locally, needs physical mobile validation |

Interpretation:

- Scenario A is far below the mobile hero budget.
- Scenario B is within the planned desktop GLB budget and above the planned mobile GLB target of 700 KB, but it remained smooth in local Chromium.
- No final textures were tested, so final KTX2/Basis texture payload remains a major unknown.

---

## 8. Scroll-Driven Motion Test

| Scroll Test | Result | Notes |
| ----------- | ------ | ----- |
| Camera scroll mapping | Pass locally | Camera position changes with scroll progress |
| Object scroll mapping | Pass locally | Placeholder group rotates and shifts slightly |
| Seal reveal mapping | Pass locally | Placeholder seal rotates/moves forward as scroll progresses |
| Pinned section behavior | Pass with caution | Sticky hero creates a simple pinned feel; no GSAP/ScrollTrigger tested |
| Mobile scroll behavior | Pass in mobile viewport | Scroll progress reached 0.77 after scroll on 390px viewport |
| CTA accessibility during scroll | Pass | CTA visible before 3D load and during benchmark |
| Scroll fatigue risk | Medium | Short benchmark is safe; final choreography must avoid long scroll traps |

---

## 9. Device / Browser Test Matrix

| Target | Browser | Priority | Test Method | Result |
| ------ | ------- | -------- | ----------- | ------ |
| Desktop Chrome | Chromium-like in-app browser | P0 | Local | Tested; pass |
| Desktop Safari | Safari latest | P0 | Not available locally | Not tested |
| iPhone Safari | Safari iOS | P0 | Physical/BrowserStack not available | Not tested |
| Android Chrome | Chrome Android | P0 | Physical/BrowserStack not available | Not tested |
| Mid-tier Android Chrome | Chrome Android | P0 | Physical/BrowserStack not available | Not tested |
| Samsung Internet | Samsung Internet | P1 | Physical/BrowserStack not available | Not tested |
| Firefox desktop | Firefox latest | P1 | Not available in this pass | Not tested |
| Mobile viewport | Chromium-like browser at 390x844 | Supporting check | Local viewport override | Tested; pass as viewport-only evidence |

Device test limitation:

The mobile result is **not** a substitute for real mid-tier Android or iPhone Safari testing. It only verifies responsive layout, DPR cap behavior, scroll stability, and canvas behavior in a small viewport.

---

## 10. Loading Measurements

| Measurement | Scenario A Desktop | Scenario B Desktop | Scenario B Mobile Viewport | Notes |
| ----------- | -----------------: | -----------------: | -------------------------: | ----- |
| Initial page load time | 85 ms browser navigation metric | 126 ms browser navigation metric | 107 ms browser navigation metric | Local server; not real network |
| Canvas mount time | 98 ms | 91 ms | 103 ms | From page start marker |
| First DOM content visible | 0 ms | 0 ms | 0 ms | DOM overlay renders immediately in app state |
| 3D asset loaded time | 400 ms | 401 ms | 414 ms | From page start marker |
| Time to interactive feel | 400 ms | 401 ms | 414 ms | Same as placeholder model-loaded marker |
| Total JS bundle estimate | 1,107,578 bytes transfer uncompressed | 1,107,578 bytes | 1,107,578 bytes | Gzip build estimate: 308.32 KB |
| Total GLB size | 13,728 bytes transfer | 1,272,452 bytes transfer | 1,272,452 bytes transfer | Includes local transfer overhead |
| Total texture size | 0 | 0 | 0 | Textures not tested |

Important limitation:

These load timings are local-server timings, not real network timings. Production must test throttled network and mobile hardware.

---

## 11. Runtime Measurements

| Measurement | Desktop | Modern Mobile | Mid-Tier Mobile | Notes |
| ----------- | ------: | ------------: | --------------: | ----- |
| Average FPS idle | 61.2 Scenario A / 60.6 Scenario B | 60.1 mobile viewport | Not tested | Local Chromium only |
| Average FPS during scroll | 60.1 Scenario A / 60.2 Scenario B | 60.0 mobile viewport | Not tested | Scroll progress reached 0.903 desktop / 0.77 mobile viewport |
| Lowest FPS during scroll | 46.9 Scenario A / 39.4 Scenario B | 53.5 mobile viewport | Not tested | Scenario B desktop low sample below 50 but average remained stable |
| Memory pressure observed | Not measured | Not measured | Not measured | Needs browser profiling later |
| Scroll smoothness | Good locally | Good in mobile viewport | Not tested | No visible trap in benchmark |
| Canvas stability | Stable locally | Stable in mobile viewport | Not tested | No console errors in valid GLB scenarios |
| Shader/material issues | None observed | None observed | Not tested | Only basic standard materials tested |

Runtime interpretation:

- Desktop average FPS is promising.
- Scenario B low-FPS sample suggests final assets should keep DPR/post-processing conservative.
- Mid-tier mobile feasibility remains unresolved until real device testing.

---

## 12. UX Safety Measurements

| UX Area | Result | Notes |
| ------- | ------ | ----- |
| CTA visible before 3D load | Pass | CTA visible in DOM overlay before/independent from canvas |
| DOM content available without canvas | Pass | Forced fallback and reduced-motion routes preserve heading/CTA |
| Reduced motion fallback works | Pass | `?reduced=1` shows static fallback, no canvas |
| WebGL fallback works | Pass as forced fallback | `?fallback=1` shows static fallback; actual unavailable-WebGL device not tested |
| No scroll trap | Pass locally | Normal page scroll still works |
| No audio autoplay issue | Pass | No audio loaded in benchmark |
| Mobile touch behavior stable | Pass in viewport only | Physical touch devices not tested |
| Bilingual layout not blocked by canvas | Partial pass | DOM-first architecture supports it; actual Arabic/English layouts not implemented in benchmark |

---

## 13. Fallback Validation

| Fallback Scenario | Expected Behavior | Result |
| ----------------- | ----------------- | ------ |
| WebGL unavailable | Static premium hero appears | Forced fallback passed; actual no-WebGL device not tested |
| Reduced motion enabled | Static/fade version appears | Passed with `?reduced=1` |
| GLB fails to load | Static fallback or placeholder appears | Passed with `?badmodel=1`; console error occurred |
| Shader/material fails | Basic material or static fallback appears | Not directly tested; no custom shaders used |
| Audio blocked | Site remains silent and functional | Passed by absence of audio; final audio policy still needs testing |
| Slow network | DOM content and CTA appear first | Architecture supports DOM-first; throttled network not tested |

Fallback notes:

- Missing-GLB fallback preserved heading and CTA.
- Missing-GLB route logged an expected GLTFLoader error. Production should catch/report this cleanly and avoid noisy user-visible failures.

---

## 14. Performance Issues Found

| Issue | Severity | Notes | Required Response Later |
| ----- | -------- | ----- | ----------------------- |
| Uncompressed JS bundle is large | Medium | 1.107 MB uncompressed, 308.32 KB gzip | Lazy-load 3D bundle and split vendor chunks in production |
| No real mobile hardware test | High | Mobile viewport is not GPU/thermal/memory evidence | Test BrowserStack/physical Android and iPhone before production approval |
| No final texture/shader test | High | Placeholder GLBs used no textures and basic materials | Test KTX2/Basis textures and final material complexity in vertical slice |
| Scenario B desktop low-FPS sample below desktop minimum | Medium | Low sample 39.4 FPS, average remained 60.2 | Keep post-processing conservative and monitor low-percentile FPS |
| Missing-GLB fallback logs console errors | Low/Medium | Error boundary catches UI failure but console logs remain | Add cleaner production error handling |
| No memory profiling | Medium | FPS is not enough for mobile feasibility | Add memory/GPU profiling in later QA |
| No Safari/Samsung/Firefox coverage | Medium | Browser compatibility still unknown | Test P0/P1 browsers later |

---

## 15. Quality Reduction Rules

| Trigger | Required Downgrade |
| ------- | ------------------ |
| FPS below mobile minimum | Disable post-processing |
| FPS still low | Reduce DPR to 1 |
| FPS still low | Reduce particles / remove expensive materials |
| FPS still low | Use simplified 3D |
| FPS still low | Use static fallback |
| WebGL unavailable | Static fallback |
| Reduced motion enabled | Static/fade fallback |
| Shader compile error | Fallback material or static poster |
| Audio blocked | Keep muted; no user-facing error |
| GLB load error | Static fallback or lightweight placeholder |

---

## 16. Feasibility Decision Matrix

| Area | Result | Decision |
| ---- | ------ | -------- |
| Desktop performance | Local Chromium passes average FPS target | Proceed with full desktop vertical slice |
| Modern mobile performance | Mobile viewport passes, physical device not tested | Proceed with simplified mobile plan only |
| Mid-tier mobile performance | Not tested on real device | Keep unresolved; require physical/BrowserStack validation |
| Asset load budget | Placeholder GLBs fit Scenario A/B budgets; JS gzip within budget | Proceed, but code-split/lazy-load 3D later |
| Scroll-driven motion safety | Pass locally | Continue with short, controlled scroll-driven opening |
| Fallback reliability | Forced fallback, reduced-motion, and bad-GLB fallback passed | Keep fallback as mandatory |
| Reduced motion safety | Pass | Preserve static/fade mode |
| Sound policy safety | Not fully tested; no audio loaded | Keep sound user-initiated/muted in later prototype |
| Bilingual DOM safety | DOM-first structure passes; real bilingual content not tested | Test real Arabic/English layouts later |
| Overall feasibility | Promising but not production-proven | Option C - Vertical Slice Only Until Asset Optimization |

---

## 17. Final Feasibility Decision

**Option C - Vertical Slice Only Until Asset Optimization**

This benchmark proves that a minimal R3F gavel/seal hero is technically plausible in local Chromium with placeholder assets.

It does not yet prove that the final Mithaq 3D direction is safe for:

- Mid-tier Android devices.
- iPhone Safari.
- Samsung Internet.
- Final GLB geometry.
- Final textures.
- Final materials/shaders.
- Final sound.
- Full scroll choreography.
- Real throttled mobile networks.

Approved next posture:

Proceed with a constrained vertical slice that validates the opening/hero/core scroll/CTA experience before expanding 3D scope.

Do not approve full 3D production complexity across all devices yet.

---

## 18. Recommendation for Phase 2

Phase 2 should use the benchmark results this way:

- Keep desktop full 3D as the premium target.
- Plan simplified mobile 3D from the beginning.
- Keep static fallback as a first-class experience, not an afterthought.
- Use real gavel/seal proxy assets as soon as available, but keep them below P1.04 budgets.
- Test mid-tier Android and iPhone Safari before locking animation complexity.
- Lazy-load the 3D bundle after DOM content and CTA are available.
- Avoid heavy post-processing in the first vertical slice.
- Keep scroll-driven opening short and user-controlled.
- Preserve DOM-first bilingual content.
- Keep audio out of the benchmark until a dedicated sound policy test exists.

---

## 19. Known Limitations

- No final Mithaq logo, wordmark, seal, or brand assets were available.
- No final gavel, seal, desk, texture, or shader assets were tested.
- No physical devices were tested.
- No BrowserStack run was performed.
- No iOS Safari, Android Chrome, Samsung Internet, Firefox, or macOS Safari run was completed.
- Mobile test was viewport-only in Chromium.
- No throttled network test was run.
- No Lighthouse report was generated.
- No Axe accessibility audit was run.
- No memory/GPU profiling was performed.
- No final bilingual Arabic/English layout was implemented.
- No final sound design was implemented.

These limitations do not block P1.05 as a feasibility benchmark, but they do prevent full production confidence.

PASS - P1.05 complete. Benchmark results are documented and the feasibility decision is clear.
