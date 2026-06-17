# Mithaq Device & Browser Target Matrix

**Official Ticket ID:** P1.04  
**Official Ticket Name:** Device & Browser Target Matrix  
**Phase:** Phase 1, Research Synthesis & Direction Lock  
**Priority:** P0  
**Status:** PASS  
**Date:** 2026-06-18  

---

## 1. Executive Summary

Mithaq must be planned as a mobile-critical, bilingual, DOM-first, WebGL-enhanced website.

The target experience is not "full 3D everywhere." The target experience is:

- Full premium scroll-driven 3D on capable desktop devices.
- Simplified premium 3D on modern mobile and tablet devices.
- Simplified/static hybrid on mid-tier mobile devices.
- Static premium fallback for low-end devices, unsupported browsers, WebGL failures, and reduced-motion users.

The primary business action is WhatsApp. This means mobile performance, tap targets, language switching, readable content, and fast CTA access matter more than preserving the same 3D complexity across all devices.

This matrix is assumption-based because audience analytics, device distribution, and real user monitoring data are not yet available. The calibration should be validated later with real analytics, physical device testing, and performance QA.

No frontend implementation, 3D implementation, or QA automation is authorized by this document.

---

## 2. Research Context

This document follows:

- P0.06 Open Questions Resolution: PASS WITH CONDITIONS.
- P1.01 Reference Website Analysis: PASS.
- P1.02 Legal Education Competitor Audit: PASS.
- P1.03 Target Audience Profile: PASS.

Relevant findings:

- Target users are likely to browse on mobile first.
- WhatsApp conversion makes mobile a primary conversion environment.
- Competitors often under-serve premium mobile UX, bilingual quality, and clear conversion.
- Mithaq must preserve all essential content in DOM, not canvas-only.
- Reduced motion and WebGL fallback are mandatory.

---

## 3. Current Mithaq Decisions from P0.06

- Mithaq is a premium bilingual 3D legal academy portfolio / landing experience.
- Primary conversion action is WhatsApp.
- Secondary conversion action is a simple inquiry form.
- MVP planning is bilingual.
- Opening direction is scroll-driven: gavel trigger to Mithaq Seal reveal.
- Sound effects are approved but must be controlled, muted/user-initiated, and accessible.
- 3D style is symbolic realism.
- Delivery approach is Vertical Slice First.
- Mithaq must not become an LMS, dashboard, booking system, or operational course platform.
- Mobile experience must not be treated as an afterthought.
- Reduced motion and WebGL fallback are mandatory.
- Critical content must remain in DOM, not canvas-only.

---

## 4. Audience Device Assumptions from P1.03

These are reasoned assumptions, not market statistics.

| Assumption | Impact on Device Strategy |
| ---------- | ------------------------- |
| Many users will visit from mobile first. | Mobile is P0, not a secondary adaptation. |
| WhatsApp conversion is primary. | CTA must be visible, tappable, and fast on mobile. |
| Users may include mid-tier Android devices. | Do not assume iPhone-only or flagship-only performance. |
| Desktop remains important for credibility review. | Full cinematic 3D should be preserved for capable desktop. |
| Bilingual Arabic/English browsing is approved for MVP. | Test RTL and LTR layouts separately across breakpoints. |
| Some users may be on slower connections or older phones. | Content-first rendering and static fallback are required. |
| Junior lawyers may browse during work/public settings. | No unexpected sound; motion must not block content. |

Validation needed later:

- Analytics data after launch.
- Device/browser usage reports.
- Real-user WebGL performance data.
- Form/WhatsApp conversion by device and language.

---

## 5. Device Tier Model

| Tier | Device Class | Examples | Target Experience | Required Constraints |
| ---- | ------------ | -------- | ----------------- | -------------------- |
| Tier 1 | High-End Desktop | MacBook Pro, iMac, modern Windows laptop, capable GPU/integrated GPU | Full scroll-driven 3D, full gavel/seal opening, higher-quality materials/shadows, controlled sound available | Keep DOM content visible; fallback if WebGL/shader failure occurs |
| Tier 2 | Modern Mobile / Tablet | Recent iPhone, recent Samsung Galaxy S/Fold, recent iPad, high-end Android phones | Simplified but premium 3D, reduced post-processing, lower DPR, touch-first navigation | CTA visible early; no hover-only interactions; audio user-initiated |
| Tier 3 | Mid-Tier Mobile | Common Android phones, older iPhones, mid-range Samsung/Xiaomi/Oppo/Realme | Simplified 3D or static-render hybrid, no heavy post-processing, lower texture resolution | Prioritize content and WhatsApp CTA; fallback if FPS is poor |
| Tier 4 | Low-End / Unsupported / Reduced Motion | WebGL unavailable, old browser, low memory, reduced motion enabled, blocked WebGL | Static premium fallback with equivalent content and CTA access | No required 3D, no scroll-trapped animation, no sound dependency |

Tier policy:

- Full 3D is a premium enhancement, not a requirement for understanding Mithaq.
- Tier 3 and Tier 4 users must still receive the same core message and conversion path.
- Reduced-motion users always receive static/fade fallback behavior, regardless of hardware capability.

---

## 6. Browser Target Matrix

| Browser | Platform | Priority | Target Experience | Notes |
| ------- | -------- | -------- | ----------------- | ----- |
| Chrome latest | Android | P0 | Simplified or full mobile 3D depending on tier | Primary mobile Android target |
| Chrome latest | Windows/macOS | P0 | Full desktop 3D | Primary desktop target |
| Safari latest | iOS | P0 | Simplified mobile 3D | Primary iPhone target; audio/WebGL behavior must be tested |
| Safari latest | macOS | P0 | Full desktop 3D if performance passes | Important for premium/stakeholder review |
| Edge latest | Windows | P1 | Full desktop 3D if performance passes | Common Windows desktop fallback |
| Firefox latest | Windows/macOS | P1 | Full or simplified desktop 3D | Test WebGL/shader compatibility |
| Samsung Internet | Android | P1 | Simplified mobile 3D or fallback | Important for Samsung users |
| Older mobile browsers | Android/iOS | P2 | Static fallback | Do not over-optimize beyond reliable fallback |

Priority definitions:

- P0: must support.
- P1: should support.
- P2: graceful fallback only.

---

## 7. OS Target Matrix

| OS | Priority | Device Type | Expected Experience | Notes |
| -- | -------- | ----------- | ------------------- | ----- |
| iOS latest and previous major | P0 | Mobile | Simplified premium 3D / fallback if needed | Must test Safari behavior |
| Android recent versions | P0 | Mobile | Simplified 3D / fallback by tier | Must cover Chrome Android |
| Windows 10/11 | P0 | Desktop | Full 3D if browser supports | Main desktop QA |
| macOS recent versions | P0 | Desktop | Full 3D if browser supports | Safari and Chrome important |
| iPadOS recent versions | P1 | Tablet | Simplified or full 3D by tier | Layout should not feel stretched |
| Older OS versions | P2 | Mixed | Static fallback | No production-blocking optimization unless severe |

---

## 8. Viewport / Breakpoint Matrix

| Breakpoint | Width Range | Device Type | Experience Requirement |
| ---------- | ----------: | ----------- | ---------------------- |
| Small mobile | 320-374px | Older/small phones | Static/simplified, CTA visible, no horizontal overflow |
| Standard mobile | 375-430px | iPhone/common Android | Primary mobile layout |
| Large mobile | 431-767px | Large phones/foldables | Touch-first layout |
| Tablet | 768-1023px | iPad/tablet | Hybrid layout, simplified 3D |
| Small laptop | 1024-1279px | Laptop | Full layout with adjusted spacing |
| Desktop | 1280-1535px | Desktop | Primary desktop composition |
| Large desktop | 1536px+ | Large screens | Full cinematic composition, avoid over-stretching |

Breakpoint rules:

- Arabic and English must be tested at all major breakpoints.
- Arabic text may wrap differently and require more vertical space.
- Fixed-height sections must not crop Arabic copy.
- CTA buttons must not overflow in either language.

---

## 9. Performance Calibration

### 9.1 FPS Targets

| Tier | Target FPS | Minimum Acceptable FPS | Action if Below Minimum |
| ---- | ---------: | ---------------------: | ----------------------- |
| High-End Desktop | 60 | 50 | Reduce post-processing / particles |
| Modern Mobile | 45-60 | 35 | Reduce DPR / simplify shaders |
| Mid-Tier Mobile | 30-45 | 28-30 | Switch to simplified 3D/static hybrid |
| Low-End / Reduced Motion | Not applicable | Not applicable | Static fallback |

### 9.2 Core Web Vitals Targets

| Metric | Target | Hard Maximum |
| ------ | -----: | ------------: |
| LCP | < 2.0s | < 2.5s |
| INP | < 100ms | < 200ms |
| CLS | < 0.05 | < 0.1 |
| TBT | < 100ms | < 200ms |

Non-negotiable:

The 3D canvas must not delay readable hero text, CTA access, language switching, or form/WhatsApp paths.

### 9.3 Asset Budget Targets

| Asset Area | Desktop Target | Mobile Target | Notes |
| ---------- | -------------: | ------------: | ----- |
| Initial HTML/CSS/critical JS | <= 350KB compressed | <= 300KB compressed | Before immersive assets |
| Initial 3D asset load | <= 1.5MB compressed | <= 700KB compressed | Hero/gavel/seal only |
| Initial texture payload | <= 2MB | <= 1MB | Prefer KTX2/Basis |
| Total first-load page weight | <= 900KB before 3D | <= 800KB before 3D | Keep content visible |
| Fonts | <= 100KB WOFF2 | <= 80KB WOFF2 | Bilingual font strategy required |
| Particles | Desktop limited | Mobile heavily limited | Avoid GPU waste |

These are planning budgets. They must be validated during vertical-slice performance testing.

---

## 10. WebGL Capability Rules

| Condition | Detection Signal | Experience |
| --------- | ---------------- | ---------- |
| WebGL2 available + high tier | WebGL2 context + good memory/cores | Full 3D |
| WebGL available but limited device | WebGL context + low memory/cores | Simplified 3D |
| WebGL unavailable | No WebGL context | Static fallback |
| Reduced motion enabled | `prefers-reduced-motion: reduce` | Static/fade fallback |
| Low FPS detected | Runtime FPS below threshold | Reduce quality or switch fallback |
| Shader error | Shader compile/runtime failure | Fallback material or static fallback |
| Audio not allowed | No user interaction / browser block | Keep muted, no error |

Implementation note for later phases:

Detection must be conservative. If there is uncertainty, Mithaq should degrade gracefully rather than force a fragile cinematic experience.

---

## 11. Mobile-Specific Requirements

- WhatsApp CTA must be visible and reachable early.
- No essential information inside canvas only.
- No hover-only interactions.
- Workshop cards must be tap-friendly.
- Minimum tap target: 44px.
- Opening must not trap the user in scroll.
- Sound must not autoplay unexpectedly.
- Motion must be reduced if device struggles.
- Use vertical stacking instead of complex horizontal sections where needed.
- Avoid heavy post-processing on mobile.
- Use static poster fallback for low-tier devices.
- Test Arabic and English text wrapping.
- Avoid fixed-height sections that crop Arabic text.
- Avoid scroll-jacking that blocks normal navigation.
- Keep language toggle reachable.
- Keep the inquiry form short and easy to complete on touch devices.

---

## 12. Bilingual / RTL Requirements

| Requirement | Reason |
| ----------- | ------ |
| Test Arabic RTL on mobile Safari and Chrome Android | These are high-risk environments for layout issues |
| Test English LTR separately | Do not assume mirrored layout works automatically |
| Use CSS logical properties | Required for RTL/LTR maintainability |
| Avoid text baked into 3D textures unless duplicated in DOM | Prevent translation and accessibility problems |
| Allow longer Arabic/English wrapping | Prevent overflow |
| Language toggle must be reachable on mobile | Bilingual MVP requires easy access |
| Forms must support Arabic and English input | Conversion path depends on forms |
| WhatsApp prefilled messages must have language variants | CTA must match selected language |
| Test modals in both directions | Workshop modal previews must not break in RTL |
| Test `/workshops/[slug]` pages in both languages | Workshop details are part of Phase 1 scope |

---

## 13. Sound Effects Requirements

| Requirement | Reason |
| ----------- | ------ |
| Sound must be user-initiated or muted by default | Browser policy + professionalism |
| Add clear mute/unmute control | User control |
| No essential meaning in sound only | Accessibility |
| Sound disabled in reduced-motion fallback unless explicitly enabled | Calm accessibility mode |
| Test iOS Safari audio restrictions | iOS blocks many autoplay patterns |
| Keep sound assets small and lazy-loaded | Performance |
| Gavel sound should be deep, restrained, and short | Legal authority, not theatrical |
| Audio state must not block page interaction | Conversion and usability |

---

## 14. Testing Device List

| Test Device | Browser | Priority | Experience Expected |
| ----------- | ------- | -------- | ------------------- |
| iPhone recent model | Safari | P0 | Simplified premium 3D |
| iPhone older model | Safari | P0 | Simplified 3D or fallback |
| Samsung Galaxy recent | Chrome | P0 | Simplified premium 3D |
| Mid-tier Android | Chrome | P0 | Simplified 3D/static hybrid |
| Windows laptop | Chrome | P0 | Full desktop 3D |
| MacBook | Safari | P0 | Full desktop 3D if performance passes |
| Windows laptop | Edge | P1 | Full desktop 3D |
| Android Samsung | Samsung Internet | P1 | Simplified/fallback |
| Tablet / iPad | Safari | P1 | Tablet-optimized layout |

If physical devices are unavailable, use BrowserStack or equivalent during later validation phases. This document does not authorize setting up test automation now.

---

## 15. Device-to-Experience Decision Table

| Device Tier | Canvas Mode | Postprocessing | Particle Count | DPR Cap | Fallback? | Notes |
| ----------- | ----------- | -------------- | --------------: | ------: | --------- | ----- |
| High-End Desktop | Full R3F | Allowed | Full but capped | 1.5-2 max | No unless error | Premium hero experience |
| Modern Mobile | Simplified R3F | Minimal/Off | Reduced | 1-1.5 max | Conditional | Keep smooth and clear |
| Mid-Tier Mobile | Simplified/Static Hybrid | Off | Minimal | 1 max | Yes if low FPS | Prioritize CTA/content |
| Low-End / Reduced Motion | Static | None | None | N/A | Yes | Full content equivalent |

Decision rule:

If maintaining 3D quality conflicts with readability, CTA access, bilingual layout, or scroll comfort, content and conversion win.

---

## 16. Risk Matrix

| Risk | Affected Devices | Severity | Mitigation |
| ---- | ---------------- | -------- | ---------- |
| WebGL unsupported or unstable | Older mobile browsers | High | Static fallback |
| Low FPS on mid-tier Android | Mid-tier Android | Critical | Simplify 3D, reduce DPR, fallback |
| iOS Safari audio restrictions | iPhone/iPad | Medium | User-initiated audio only |
| RTL text overflow | Mobile Arabic layouts | High | CSS logical properties + real Arabic testing |
| Canvas delays hero content | All | Critical | DOM-first hero content |
| Shader compilation issues | Older GPUs / Firefox / Samsung Internet | Medium | Fallback material/static poster |
| Scroll-jacking fatigue | Mobile users | High | Normal scroll, short pinned sequences |
| High font payload due to bilingual MVP | All | Medium | Limit font weights, preload carefully |
| Touch interaction issues | Mobile | High | No hover-only critical interactions |
| Workshop modal overflow | Small mobile / Arabic RTL | High | Responsive modals and scrollable content areas |
| Language toggle hidden | Mobile | Medium | Keep toggle reachable in nav and menu |
| Static fallback feels cheap | Tier 4 / reduced motion | Medium | Use premium still renders, typography, and DOM content |

---

## 17. Performance Calibration Summary

| Area | Final Calibration |
| ---- | ----------------- |
| Full 3D target | Tier 1 desktop only, plus capable desktop browsers after testing |
| Simplified 3D target | Tier 2 modern mobile/tablet and some capable P1 desktop browsers |
| Static fallback target | Tier 4, reduced motion, unsupported WebGL, shader failure, severe low FPS |
| Desktop FPS target | 60 target, 50 minimum acceptable |
| Mobile FPS target | 45-60 modern mobile, 30-45 mid-tier mobile |
| DPR cap | Desktop 1.5-2 max, modern mobile 1-1.5 max, mid-tier mobile 1 max |
| Initial asset budget | <= 900KB before 3D; initial 3D <= 1.5MB compressed desktop |
| Mobile asset budget | <= 800KB before 3D; initial 3D <= 700KB compressed mobile |
| WebGL fallback trigger | No WebGL, shader failure, low FPS below threshold, blocked context |
| Reduced motion behavior | Static/fade fallback; no required 3D or sound |
| Sound behavior | Muted or user-initiated; small lazy-loaded assets; visible control |
| Bilingual testing rule | Test Arabic RTL and English LTR separately on P0 mobile and desktop browsers |

---

## 18. Final Device Strategy Recommendation

Mithaq should be built around a progressive enhancement strategy:

1. Start with DOM-first bilingual content, visible CTA, accessible forms, and a premium static composition.
2. Add simplified 3D for mobile where performance allows.
3. Add full cinematic R3F experience for capable desktops.
4. Degrade early and gracefully when WebGL, FPS, memory, reduced-motion, or browser constraints require it.

The winning device strategy is not identical visuals everywhere. It is equivalent clarity, trust, and conversion everywhere.

Final strategy:

- P0 mobile browsers must support fast reading, WhatsApp conversion, bilingual navigation, and simplified/fallback visuals.
- P0 desktop browsers should carry the full premium cinematic impression.
- Tier 3 devices should never be punished with heavy WebGL.
- Tier 4 users must still understand Mithaq and convert.
- Performance, accessibility, bilingual layout, and conversion take priority over visual excess.

PASS - P1.04 complete. Device/browser targets and performance calibration are clear and actionable.
