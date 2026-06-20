# Mithaq Opening Sequence Frame Comps

**Official Ticket ID:** P4.03  
**Official Ticket Name:** Opening Sequence Frame Comps  
**Phase:** Phase 4 - Visual System & Art Direction  
**Priority:** P0  
**Complexity:** High  
**Owner:** UI Art Director / Motion Art Director  
**Status:** PASS WITH CONDITIONS - Figma build pending  
**Prepared date:** 2026-06-20  

---

## 1. Executive Summary

This package creates visual keyframe compositions for Mithaq's scroll-driven opening sequence:

**black judicial void -> desk emergence -> gavel descent -> restrained strike -> authority ripple -> Covenant Seal reveal -> wordmark + CTA handoff.**

The visual keyframes are delivered as an HTML visual board, supported by this annotated handoff document. The HTML board satisfies the P4.03 rule that Markdown-only delivery is not accepted.

Visual board:

[mithaq-opening-sequence-frame-comps.html](D:/Clinets/MITHAQ/MITHAQ/mithaq-project-docs/mithaq-opening-sequence-frame-comps/mithaq-opening-sequence-frame-comps.html:1)

This task does not implement R3F, GSAP, Lenis, ScrollTrigger, shaders, production animation, final GLB assets, production sound, frontend components, final copy, or new roadmap tickets.

---

## 2. Current Mithaq Direction

| Area | Direction |
| --- | --- |
| Core concept | The Covenant Seal. |
| Opening direction | Scroll-Driven Seal-Led Opening. |
| 3D direction | Seal-Led Macro Legal Chamber. |
| Motion direction | Scroll-Led Ceremonial Restraint. |
| Hero object | Mithaq Seal. |
| Trigger object | Gavel, secondary and ceremonial only. |
| Visual world | Dark legal chamber, dark desk, muted brass/gold, parchment text, warm directional light. |
| CTA model | WhatsApp primary, Register Interest secondary. |
| Bilingual model | Arabic and English as separate DOM/localized elements. |
| Mobile model | Shortened/simplified/static opening with CTA visible earlier. |
| Fallback model | Premium static seal/desk poster with equivalent DOM content and CTA. |
| Feasibility rule | P1.05 Option C - Vertical Slice Only Until Asset Optimization. |

Forbidden in this ticket: bounce, jiggle, violent smash, horror, neon/sci-fi glow, game-like effects, canvas-only text, fake urgency, fake proof, fake WhatsApp number, and production implementation.

---

## 3. Delivery Format / Figma Or HTML Status

| Deliverable | Status | Notes |
| --- | --- | --- |
| Figma keyframe frames | Pending | Direct Figma access is unavailable in this workspace. |
| HTML visual keyframe board | PASS | 10 visual frames included: KF01-KF08 desktop, KF09 reduced motion, KF10 mobile. |
| Markdown annotations | PASS | This document provides implementation-safe notes and QA. |
| PNG/JPG exports | Not created | HTML visual board is the accepted visual fallback. |

Final status uses **PASS WITH CONDITIONS** because the visual frames exist, while Figma build, final assets, stakeholder review, accessibility QA, mobile device validation, and R3F/GSAP implementation remain pending.

---

## 4. Keyframe Index

| Keyframe | Frame Title | Breakpoint | Local Progress | Time Reference | Visual Board Status |
| --- | --- | --- | ---: | ---: | --- |
| KF01 | Black Judicial Void | Desktop 1440 x 900 | 0% | 0.0s | Visual comp included |
| KF02 | Desk Surface Emerges | Desktop 1440 x 900 | 15% | 1.0s | Visual comp included |
| KF03 | Gavel Descent | Desktop 1440 x 900 | 28% | 2.4s | Visual comp included |
| KF04 | Strike Moment | Desktop 1440 x 900 | 36% | 3.4s | Visual comp included |
| KF05 | Ripple / Authority Ring | Desktop 1440 x 900 | 45% | 4.0s | Visual comp included |
| KF06 | Seal Outline Forms | Desktop 1440 x 900 | 60% | 5.4s | Visual comp included |
| KF07 | Seal Completed / Hero Anchor | Desktop 1440 x 900 | 78% | 6.5s | Visual comp included |
| KF08 | Wordmark + CTA Handoff | Desktop 1440 x 900 | 100% | 8.5s | Visual comp included |
| KF09 | Reduced Motion Static Opening | Desktop 1440 x 900 | N/A | Static equivalent | Visual comp included |
| KF10 | Mobile Opening State | Mobile 390 x 844 | Condensed 0-100% | Mobile equivalent | Visual comp included |

The selected 8 desktop frames are the implementation keyframes from the fuller P2.05 storyboard. KF09 and KF10 are supporting frames required for fallback/mobile safety.

---

## 5. KF01 - Black Judicial Void

| Field | Direction |
| --- | --- |
| Keyframe ID | KF01 |
| Frame title | Black Judicial Void |
| Desktop/mobile | Desktop 1440 x 900 |
| Local progress | 0% |
| Time reference | 0.0s |
| Visual state | Near-black judicial entry, intentionally quiet. |
| Camera framing | No object / hidden camera. |
| 3D objects visible | None, or canvas visually empty. |
| Lighting state | Near-black, not broken; faint atmospheric depth only. |
| DOM overlay state | Hidden. |
| CTA state | Hidden. |
| Motion implied | Fade from black as local scroll begins. |
| Accessibility note | Essential hero content must exist outside canvas for fallback; this state must not be the only meaningful content. |
| Performance note | Canvas may initialize quietly; do not delay DOM content globally. |
| R3F handoff note | Empty/near-empty frame should still feel deliberate with subtle background treatment. |

---

## 6. KF02 - Desk Surface Emerges

| Field | Direction |
| --- | --- |
| Keyframe ID | KF02 |
| Frame title | Desk Surface Emerges |
| Desktop/mobile | Desktop 1440 x 900 |
| Local progress | 12-18%, represented at 15% |
| Time reference | 1.0s |
| Visual state | Dark desk surface revealed by warm upper-left light. |
| Camera framing | Low macro desk angle. |
| 3D objects visible | Desk plane/grain, subtle particles. |
| Lighting state | Warm key begins from upper-left; ambient stays low. |
| DOM overlay state | Hidden. |
| CTA state | Hidden. |
| Motion implied | Warm reveal grazes wood surface. |
| Accessibility note | Decorative reveal; fallback can show desk already visible. |
| Performance note | Use optimized desk plane/material; avoid large uncompressed wood textures. |
| R3F handoff note | Desk establishes legal stage; texture should read but remain restrained. |

---

## 7. KF03 - Gavel Descent

| Field | Direction |
| --- | --- |
| Keyframe ID | KF03 |
| Frame title | Gavel Descent |
| Desktop/mobile | Desktop 1440 x 900 |
| Local progress | 24-32%, represented at 28% |
| Time reference | 1.8-3.0s, represented at 2.4s |
| Visual state | Gavel suspended above desk, macro but non-aggressive. |
| Camera framing | Macro gavel close-up with center reserved for future seal. |
| 3D objects visible | Gavel, desk, gavel shadow, restrained brass detail. |
| Lighting state | Gavel wood/brass catches warm highlight. |
| DOM overlay state | Optional small skip/continue label only. |
| CTA state | Hidden. |
| Motion implied | Weighted descent approaching contact. |
| Accessibility note | Pause/scroll label cannot be required to understand the sequence. |
| Performance note | Gavel geometry and shadow must be optimized for vertical slice. |
| R3F handoff note | Gavel has presence, but framing must not make it the brand hero. |

---

## 8. KF04 - Strike Moment

| Field | Direction |
| --- | --- |
| Keyframe ID | KF04 |
| Frame title | Strike Moment |
| Desktop/mobile | Desktop 1440 x 900 |
| Local progress | 34-38%, represented at 36% |
| Time reference | 3.4s |
| Visual state | Gavel contacts desk with tiny controlled gold accent. |
| Camera framing | Tight impact point. |
| 3D objects visible | Gavel, impact point, desk. |
| Lighting state | Tiny gold contact accent, no floodlight. |
| DOM overlay state | Hidden. |
| CTA state | Hidden. |
| Motion implied | Short decisive contact. |
| Accessibility note | Sound and impact motion are optional; meaning must not depend on them. |
| Performance note | No physics simulation required; keyframed contact is enough. |
| R3F handoff note | Avoid violence, cracks, smash debris, shockwave, or horror framing. |

---

## 9. KF05 - Ripple / Authority Ring

| Field | Direction |
| --- | --- |
| Keyframe ID | KF05 |
| Frame title | Ripple / Authority Ring |
| Desktop/mobile | Desktop 1440 x 900 |
| Local progress | 40-50%, represented at 45% |
| Time reference | 3.6-4.4s, represented at 4.0s |
| Visual state | Controlled gold ring expands across desk. |
| Camera framing | Slight pullback/ripple view. |
| 3D objects visible | Desk, ripple, gavel partially visible. |
| Lighting state | Muted gold line against dark wood. |
| DOM overlay state | Hidden/minimal. |
| CTA state | Hidden. |
| Motion implied | Contact energy becomes official seal logic. |
| Accessibility note | Reduced motion can use static gold line or direct seal fade. |
| Performance note | Avoid expensive shader-only ripple; provide mesh/path/static fallback. |
| R3F handoff note | Ripple should feel official and structured, not magical or explosive. |

---

## 10. KF06 - Seal Outline Forms

| Field | Direction |
| --- | --- |
| Keyframe ID | KF06 |
| Frame title | Seal Outline Forms |
| Desktop/mobile | Desktop 1440 x 900 |
| Local progress | 52-65%, represented at 60% |
| Time reference | 5.0-5.8s, represented at 5.4s |
| Visual state | Circular seal outline forms at center. |
| Camera framing | Pullback enough for seal outline. |
| 3D objects visible | Seal outline/emboss, desk, secondary gavel. |
| Lighting state | Muted gold seal line catches light. |
| DOM overlay state | Brand/wordmark hidden or preparing. |
| CTA state | Hidden. |
| Motion implied | Ripple resolves into seal geometry. |
| Accessibility note | Critical identity text still needs DOM equivalent later. |
| Performance note | Seal geometry must be optimized; avoid dense unreadable text geometry. |
| R3F handoff note | This is the key transition where attention shifts away from gavel. |

---

## 11. KF07 - Seal Completed / Hero Anchor

| Field | Direction |
| --- | --- |
| Keyframe ID | KF07 |
| Frame title | Seal Completed / Hero Anchor |
| Desktop/mobile | Desktop 1440 x 900 |
| Local progress | 70-82%, represented at 78% |
| Time reference | 6.5s |
| Visual state | Seal complete, centered, and dominant; gavel resting secondary. |
| Camera framing | Ceremonial centered seal. |
| 3D objects visible | Seal, desk, secondary gavel, implied chamber depth. |
| Lighting state | Warm key, subtle gold rim, readable seal surface. |
| DOM overlay state | Wordmark zone begins faintly/annotated. |
| CTA state | Hidden. |
| Motion implied | Seal settles into hero anchor. |
| Accessibility note | DOM identity appears next; seal is motif, not sole text. |
| Performance note | Avoid heavy bevels, dense marks, and excessive bloom/glow. |
| R3F handoff note | Seal must dominate composition; gavel visually recedes. |

---

## 12. KF08 - Wordmark + CTA Handoff

| Field | Direction |
| --- | --- |
| Keyframe ID | KF08 |
| Frame title | Wordmark + CTA Handoff |
| Desktop/mobile | Desktop 1440 x 900 |
| Local progress | 90-100%, represented at 100% |
| Time reference | 7.8-8.5s, represented at 8.5s |
| Visual state | Mithaq identity, support line, and CTAs visible; seal/gavel become atmospheric anchor. |
| Camera framing | Stable hero overlay framing. |
| 3D objects visible | Seal, gavel, desk, chamber depth, restrained particles. |
| Lighting state | Text and CTA readability prioritized. |
| DOM overlay state | Wordmark/identity, candidate support line, and CTA visible. |
| CTA state | Visible; WhatsApp primary, Register Interest secondary. |
| Motion implied | Opening settles and hands off to Scene 02. |
| Accessibility note | CTA and text are DOM zones, not canvas-only. |
| Performance note | DOM content cannot wait for final 3D assets. |
| R3F handoff note | Canvas supports conversion; it must not cover or obscure CTA. |

---

## 13. Optional KF09 - Reduced Motion Static Opening

| Field | Direction |
| --- | --- |
| Keyframe ID | KF09 |
| Frame title | Reduced Motion Static Opening |
| Desktop/mobile | Desktop static/fallback 1440 x 900 |
| Local progress | Applies to full opening |
| Time reference | Static equivalent |
| Visual state | Static seal/desk poster with identity and CTA visible immediately. |
| Camera framing | No camera movement. |
| 3D objects visible | Static seal, desk, optional secondary gavel, or non-WebGL poster. |
| Lighting state | Precomposed premium warm lighting. |
| DOM overlay state | Visible immediately. |
| CTA state | Visible immediately. |
| Motion implied | No gavel movement, no ripple, no seal draw, no pullback. |
| Accessibility note | `prefers-reduced-motion` should receive equivalent meaning without motion. |
| Performance note | Can avoid canvas entirely if WebGL fails. |
| R3F handoff note | Static fallback must feel intentional and premium, not degraded. |

---

## 14. Optional KF10 - Mobile Opening State

| Field | Direction |
| --- | --- |
| Keyframe ID | KF10 |
| Frame title | Mobile Opening State |
| Desktop/mobile | Mobile 390 x 844 |
| Local progress | Condensed 0-100% opening |
| Time reference | Mobile equivalent |
| Visual state | Simplified seal-first poster with CTA visible early. |
| Camera framing | Minimal movement; no long pinned intro. |
| 3D objects visible | Simplified seal, desk, optional static gavel, fewer/no particles. |
| Lighting state | Simple warm key; no complex shadows required. |
| DOM overlay state | Visible early; Arabic and English separate/localizable. |
| CTA state | Visible early, 44px+ tap targets. |
| Motion implied | Shortened reveal or static poster depending device. |
| Accessibility note | No hover-only behavior; Arabic line/block reveal only if animated later. |
| Performance note | Static fallback if FPS/memory is poor. |
| R3F handoff note | Mobile should not inherit full desktop choreography by default. |

---

## 15. Camera Direction Table

| Keyframe | Camera Direction | Engineer Note |
| --- | --- | --- |
| KF01 | No object / void | Canvas may not yet dominate; make darkness intentional. |
| KF02 | Low macro desk angle | Show grain and upper-left light direction. |
| KF03 | Macro gavel close-up | Keep gavel secondary to the story. |
| KF04 | Tight impact point | Avoid violence and theatrical smash framing. |
| KF05 | Slight pullback/ripple view | Ripple must be readable across desk. |
| KF06 | Pullback enough for seal outline | Seal becomes the center of attention. |
| KF07 | Ceremonial centered seal | Seal hero state; gavel recedes. |
| KF08 | Hero overlay framing | DOM readability and CTA protection are priority. |
| KF09 | Static poster framing | No camera movement. |
| KF10 | Mobile compact framing | Minimal depth shift, no long pin. |

---

## 16. Lighting Direction Table

| Keyframe | Lighting Intent |
| --- | --- |
| KF01 | Near-black, not broken. |
| KF02 | Warm key reveals desk. |
| KF03 | Gavel shadow creates controlled tension. |
| KF04 | Tiny gold contact accent. |
| KF05 | Gold ripple visible but restrained. |
| KF06 | Seal outline catches light. |
| KF07 | Seal is readable, premium, and not magically glowing. |
| KF08 | Text/CTA readability prioritized. |
| KF09 | Precomposed warm premium poster. |
| KF10 | Simplified warm key, mobile-safe contrast. |

Lighting rules:

- Avoid horror underlighting.
- Avoid neon glow.
- Avoid overexposure.
- Avoid magical fantasy particles.
- Gold is a signal, not a floodlight.

---

## 17. DOM / CTA Timing Table

| Keyframe | DOM State | CTA State |
| --- | --- | --- |
| KF01 | None/hidden. | Hidden. |
| KF02 | None. | Hidden. |
| KF03 | Optional skip/continue label only. | Hidden. |
| KF04 | None. | Hidden. |
| KF05 | None/minimal. | Hidden. |
| KF06 | Brand/wordmark still hidden or preparing. | Hidden. |
| KF07 | Wordmark zone begins. | Hidden. |
| KF08 | Wordmark, support line, WhatsApp/Register CTA visible. | Visible. |
| KF09 | Identity and CTA visible immediately. | Visible. |
| KF10 | Mobile identity and CTA visible early. | Visible early. |

DOM rules:

- Main meaning must eventually be real DOM.
- CTA must be visible by handoff/fallback.
- CTA cannot be canvas-only.
- Wordmark cannot be unreadable behind 3D.
- Arabic/English text must be separate/localizable.

---

## 18. Mobile Opening Notes

| Area | Rule |
| --- | --- |
| 3D | Simplified/static poster by default unless vertical slice proves mobile performance. |
| Intro length | Shorter than desktop; avoid empty scroll delay. |
| CTA | Visible earlier and reachable. |
| Text | Text-first by handoff; no cropped Arabic/English. |
| Particles | Reduced or removed. |
| Camera | Minimal movement; no large depth travel. |
| Sound | Off/muted unless explicitly enabled by user-safe interaction. |
| Scroll | No long scroll trap or touch friction. |
| Fallback | Static seal/desk poster with same DOM content and CTA. |

Mobile visual status:

**PASS WITH CONDITIONS** - KF10 provides a mobile visual opening state. Physical mobile validation remains pending.

---

## 19. Reduced Motion / Static Fallback Notes

Required static state is included as KF09.

| Requirement | Status |
| --- | --- |
| Static seal/desk poster | PASS |
| Mithaq identity visible | PASS |
| Brand anchor/support line visible | PASS |
| WhatsApp/Register CTA visible | PASS |
| No gavel movement required | PASS |
| No ripple required | PASS |
| No seal draw required | PASS |
| Content equivalent to animated opening | PASS WITH CONDITIONS - final copy pending |

Reduced-motion rule:

Users who prefer reduced motion should receive KF09-style experience with no required gavel strike, no scroll-scrubbed camera, no ripple animation, no animated seal drawing, no mandatory sound, and immediate access to CTA.

---

## 20. R3F Handoff Notes

| Area | Required Note |
| --- | --- |
| Gavel position | Off-center, macro during KF03-KF04; resting and secondary by KF07-KF08. |
| Seal position | Hidden until KF06; central and dominant by KF07; atmospheric anchor by KF08. |
| Desk | Low macro surface in KF02; broad legal stage through KF08. |
| Particles | Sparse, warm, decorative only; disable on mobile/reduced motion if needed. |
| Ripple | Direction expands from contact point toward seal logic; structured and restrained. |
| Camera | Macro-to-pullback progression; scroll-led, not timed autoplay. |
| Lights | Warm upper-left key, low ambient, subtle brass rim only where useful. |
| DOM overlay | Hidden early; wordmark zone begins KF07; full DOM/CTA visible KF08. |
| CTA | Visible by handoff and immediately in fallback. |
| Fallback | Static poster equivalent with DOM content and CTA. |
| Mobile | Condensed/static path, no full desktop choreography by default. |

Implementation guardrail:

These notes are visual and directional only. They are not R3F/GSAP implementation code, not camera path code, and not shader instructions.

---

## 21. Content Safety Notes

Allowed in this comp package:

- Mithaq / ميثاق
- Candidate identity/support wording from prior planning
- Candidate CTA labels
- `WHATSAPP_NUMBER_PENDING`
- Placeholder-safe identity text

Not used:

- Fake WhatsApp number
- Fake certificate claims
- Fake limited seats
- Fake testimonials
- Fake partner logos
- Fake instructor claims
- Fake launch/cohort dates
- Fake proof/statistics

Final copy, Arabic review, wordmarks, seal, gavel model, and WhatsApp number remain pending.

---

## 22. Opening Keyframe Guardrail Table

| Keep | Avoid |
| --- | --- |
| Seal-led covenant reveal | Gavel as the brand hero |
| Scroll-driven local progress | Fixed trailer intro |
| Weighted gavel trigger | Violent smash |
| Controlled authority ripple | Explosion/shockwave |
| Muted brass/gold signal | Neon glow or fake gold |
| DOM-first wordmark and CTA | Canvas-only text |
| Reduced-motion equivalent | Mandatory camera movement |
| Mobile simplification | Full desktop choreography on every phone |
| Premium darkness | Horror black crush |
| Placeholder-safe text | Fake facts or urgency |

---

## 23. Quality Gate

| Gate | Status | Notes |
| --- | --- | --- |
| At least 6 visual opening keyframe comps | PASS | 10 visual frames included in HTML board. |
| Keyframes are visual, not Markdown-only | PASS | HTML visual board created. |
| Local progress documented for every keyframe | PASS | KF01-KF08 include local progress; KF09/KF10 are fallback equivalents. |
| Original time reference documented | PASS | KF01-KF08 include time references. |
| Visual state clear | PASS | Each keyframe has visual comp and annotation. |
| Camera framing annotated | PASS | Per-keyframe and camera table included. |
| Lighting state annotated | PASS | Per-keyframe and lighting table included. |
| 3D object state annotated | PASS | Per-keyframe and R3F notes included. |
| DOM/CTA state included | PASS | DOM/CTA timing table included. |
| Seal is hero by later frames | PASS | KF06-KF08 shift dominance to seal. |
| Gavel only trigger | PASS | Gavel recedes by KF07-KF08. |
| Strike restrained and non-violent | PASS | KF04 guardrails documented. |
| Reduced-motion/static fallback included | PASS | KF09 included. |
| Mobile opening included | PASS | KF10 included. |
| R3F handoff notes included | PASS | Dedicated table included. |
| Content safe and placeholder-aware | PASS | No fake facts used. |
| Avoided implementation | PASS | No R3F/GSAP/frontend code. |
| Avoided new roadmap tickets | PASS | No new tickets created. |

---

## 24. Acceptance Criteria

| Acceptance Criteria | Status |
| --- | --- |
| Opening keyframe comp package created | PASS |
| At least 6 visual keyframe comps exist | PASS |
| Recommended 8 keyframes included | PASS |
| Keyframes show opening exact visual states | PASS |
| Each keyframe includes local scroll progress | PASS |
| Each keyframe includes original time reference | PASS |
| Each keyframe includes camera framing notes | PASS |
| Each keyframe includes lighting notes | PASS |
| Each keyframe includes 3D object state | PASS |
| Each keyframe includes DOM/CTA state | PASS |
| Reduced-motion/static opening frame included | PASS |
| Mobile opening state included | PASS |
| R3F handoff notes included | PASS |
| Visual output is HTML visual board | PASS |
| Markdown-only delivery not treated as PASS | PASS |
| No R3F implementation started | PASS |
| No GSAP implementation started | PASS |
| No shaders created | PASS |
| No production animation created | PASS |
| No final GLB assets created | PASS |
| No fake content used | PASS |
| No new roadmap tickets created | PASS |

---

## 25. Final Recommendation

Selected opening keyframe direction:

**Seal-Led Scroll-Driven Ceremonial Opening**

Use KF01-KF08 as the desktop visual source of truth for the later opening vertical slice, with KF09 as the reduced-motion/WebGL fallback target and KF10 as the mobile simplification target.

Recommended next implementation posture:

1. Build only the Scene 01 vertical slice first.
2. Keep the gavel as the trigger and the Seal as the hero.
3. Prioritize DOM/CTA readiness before final 3D complexity.
4. Treat all 3D/shader/ripple detail as conditional until asset optimization and mobile testing pass.
5. Build reduced-motion and mobile fallback paths at the same time as the opening prototype.

---

## 26. Final Status

**PASS WITH CONDITIONS - P4.03 complete. 10 visual opening keyframe comps exist: 8 desktop opening keyframes, 1 reduced-motion/static fallback frame, and 1 mobile opening frame, with local progress, time reference, camera, lighting, 3D state, DOM/CTA state, mobile/fallback notes, and R3F handoff guidance.**

Conditions remaining:

- Actual Figma keyframe page is pending.
- Final gavel model is pending.
- Final seal/logo/wordmark assets are pending.
- Final material/texture assets are pending.
- Final Arabic/client copy review is pending.
- R3F/GSAP implementation is pending.
- Physical mobile validation is pending.
- Reduced-motion behavior QA is pending.
- Accessibility QA is pending.
- Stakeholder approval is pending.
