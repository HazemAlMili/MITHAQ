# Mithaq Scene-Level Visual Comps

**Official Ticket ID:** P4.02  
**Official Ticket Name:** Scene-Level Visual Comps  
**Phase:** Phase 4 - Visual System & Art Direction  
**Owner:** UI Art Director / Senior Product Designer  
**Status:** PASS WITH CONDITIONS - Figma build pending  
**Date:** 2026-06-20  
**Deliverable Type:** Repo-based full-fidelity visual comp specification + standalone HTML comp board

---

## 1. Executive Summary

This document defines Mithaq's 20 scene-level visual compositions for the 10-scene landing journey at two breakpoints:

- Desktop: 1440px
- Mobile: 390px

Because direct Figma access is unavailable in this workspace, P4.02 is delivered as:

1. An implementation-safe visual comp specification.
2. A standalone HTML visual comp board that represents the 20 required frames using the P4.01 design system foundation.

The actual Figma file remains pending, but the frame names, visual hierarchy, component usage, DOM/canvas zones, CTA placement, mobile decisions, RTL/accessibility annotations, and handoff notes are documented for recreation in Figma.

Comp board:

[mithaq-scene-level-visual-comps.html](D:/Clinets/MITHAQ/MITHAQ/mithaq-project-docs/mithaq-scene-level-visual-comps/mithaq-scene-level-visual-comps.html:1)

This task does not create frontend implementation, production CSS, React components, R3F scenes, final 3D assets, opening keyframe sequences, static fallback full-page comps, micro-interaction specs, or final copy.

---

## 2. Current Mithaq Direction

| Area | Current Direction |
| --- | --- |
| Product | Premium bilingual 3D legal academy portfolio / landing experience. |
| Core concept | The Covenant Seal. |
| Opening | Scroll-Driven Seal-Led Opening. |
| 3D direction | Seal-Led Macro Legal Chamber. |
| Motion | Scroll-Led Ceremonial Restraint. |
| Conversion | WhatsApp primary, `/register` secondary. |
| Routes | `/`, `/register`, `/workshops/[slug]`. |
| Scene order | 10-scene journey locked. |
| 3D priority | Scene 01-02 vertical-slice priority. |
| Breakpoints | Desktop 1440px, Mobile 390px. |
| Arabic | Tajawal 700 default; Lemonada accent-only pending review. |
| Color | Filled gold CTA uses near-black; gold-dim decorative only. |
| Fallback | Static fallback preserves meaning and conversion. |
| Claims | No fake proof, testimonials, stats, urgency, seat counters, or waitlist. |
| Content | Workshop/mentor/proof/WhatsApp details remain pending. |

---

## 3. Figma Organization

Figma file name:

```text
Mithaq - Scene-Level Visual Comps
```

Required pages:

| Page | Content |
| --- | --- |
| 00 - Cover / Status | Version, task status, dependencies, conditions. |
| 01 - Desktop 1440 Scenes | 10 desktop scene comps. |
| 02 - Mobile 390 Scenes | 10 mobile scene comps. |
| 03 - Component References | Components from P4.01 used in scenes. |
| 04 - 3D / Canvas Zones | Annotated 3D placement per scene. |
| 05 - CTA / Conversion Notes | CTA placement map. |
| 06 - RTL / Mobile Notes | Arabic/RTL and mobile concerns. |
| 07 - Accessibility Notes | Contrast, focus, DOM-first, fallback notes. |
| 08 - Handoff Notes | Frontend/3D implementation notes. |

Current status:

```text
Figma build pending
```

---

## 4. Required Frame Names

### Desktop Frames

| Frame Name | Status |
| --- | --- |
| `P4.02 / Desktop / Scene 01 - Gavel Seal Opening / 1440` | Represented in HTML board and spec. |
| `P4.02 / Desktop / Scene 02 - Hero Mithaq Reveal / 1440` | Represented in HTML board and spec. |
| `P4.02 / Desktop / Scene 03 - The Gap / 1440` | Represented in HTML board and spec. |
| `P4.02 / Desktop / Scene 04 - Mithaq Method / 1440` | Represented in HTML board and spec. |
| `P4.02 / Desktop / Scene 05 - Training Pillars / 1440` | Represented in HTML board and spec. |
| `P4.02 / Desktop / Scene 06 - Workshops Preview / 1440` | Represented in HTML board and spec. |
| `P4.02 / Desktop / Scene 07 - Hall of Mentors / 1440` | Represented in HTML board and spec. |
| `P4.02 / Desktop / Scene 08 - Trust Credibility / 1440` | Represented in HTML board and spec. |
| `P4.02 / Desktop / Scene 09 - FAQ / 1440` | Represented in HTML board and spec. |
| `P4.02 / Desktop / Scene 10 - Final CTA / 1440` | Represented in HTML board and spec. |

### Mobile Frames

| Frame Name | Status |
| --- | --- |
| `P4.02 / Mobile / Scene 01 - Gavel Seal Opening / 390` | Represented in HTML board and spec. |
| `P4.02 / Mobile / Scene 02 - Hero Mithaq Reveal / 390` | Represented in HTML board and spec. |
| `P4.02 / Mobile / Scene 03 - The Gap / 390` | Represented in HTML board and spec. |
| `P4.02 / Mobile / Scene 04 - Mithaq Method / 390` | Represented in HTML board and spec. |
| `P4.02 / Mobile / Scene 05 - Training Pillars / 390` | Represented in HTML board and spec. |
| `P4.02 / Mobile / Scene 06 - Workshops Preview / 390` | Represented in HTML board and spec. |
| `P4.02 / Mobile / Scene 07 - Hall of Mentors / 390` | Represented in HTML board and spec. |
| `P4.02 / Mobile / Scene 08 - Trust Credibility / 390` | Represented in HTML board and spec. |
| `P4.02 / Mobile / Scene 09 - FAQ / 390` | Represented in HTML board and spec. |
| `P4.02 / Mobile / Scene 10 - Final CTA / 390` | Represented in HTML board and spec. |

---

## 5. Desktop / Mobile Pairing

| Scene | Desktop Design Intent | Mobile Adaptation Decision |
| --- | --- | --- |
| 01 | Cinematic seal/gavel resolved opening state. | Short/static seal hero with CTA earlier. |
| 02 | Editorial hero plus seal atmosphere. | Text-first hero. |
| 03 | Problem text plus floating documents. | Text plus static/minimal collage. |
| 04 | Text plus ordered desk/method blocks. | Vertical method blocks. |
| 05 | Pillar dossier layout. | Vertical pillar stack. |
| 06 | Workshop dossier cards. | Stacked workshop cards. |
| 07 | Mentor gallery. | Stacked mentor cards. |
| 08 | Trust/proof grid. | Single-column trust blocks. |
| 09 | FAQ editorial column. | Full-width accordion. |
| 10 | Seal closing CTA. | CTA-first closing section. |

---

## 6. Scene Annotation Matrix

| Scene | Funnel Stage | Primary Message | Primary CTA | 3D / Canvas Zone | DOM Content Zone | Component Usage | Content Dependency |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | Awareness | Mithaq is a serious legal training covenant that bridges legal study and professional readiness. | WhatsApp / Register by handoff. | Large central seal/gavel canvas. | Lower/center brand and CTA overlay. | Header note, CTA buttons, static hero poster. | Logo/wordmark/seal pending. |
| 02 | Awareness | Mithaq prepares law graduates and early-career legal professionals for practical legal work. | WhatsApp / Register. | Seal as side/background anchor. | Protected editorial text column. | Header, hero CTA group. | Hero copy pending P6.01. |
| 03 | Problem | Legal study gives knowledge, but practice demands skills many graduates were never trained to use. | Persistent WhatsApp only. | Fragmented documents around edges. | Protected problem text zone. | Text block, floating CTA note. | Final problem copy pending. |
| 04 | Solution | Mithaq turns legal knowledge into practical readiness through structured, skill-first training. | View Training Pillars. | Ordered desk/method support. | Method heading and principle blocks. | Method cards, soft CTA. | Method copy pending P6.02. |
| 05 | Solution / Offer | Mithaq focuses on practical legal skills that move users from knowledge to action. | View Workshops / Register. | Dossier atmosphere only. | Five pillar cards. | Pillar cards, CTA group. | Pillar copy pending final writing. |
| 06 | Offer | Each workshop is a focused practical training path around a specific legal skill need. | Ask About This Workshop. | Desk/dossier background. | Workshop cards and CTAs. | Workshop cards, buttons. | Workshop titles/details pending. |
| 07 | Trust | Training credibility depends on honestly documented mentors. | Optional WhatsApp/Register. | Subtle chamber/portrait atmosphere. | Mentor cards/placeholders. | Mentor cards. | Mentor names/bios/photos pending. |
| 08 | Trust | Credibility must come from verified proof or honest methodology. | Optional soft CTA. | Minimal seal watermark/atmosphere. | Trust/proof blocks. | Trust/proof blocks. | Proof/testimonials/logos pending. |
| 09 | Objection | Clear answers help users decide whether to ask or register. | Ask via WhatsApp. | None/minimal ambient. | FAQ accordion and CTA. | FAQ accordion, FAQ CTA block. | Final FAQ answers pending. |
| 10 | Conversion | The next step is a low-pressure WhatsApp conversation or register-interest inquiry. | WhatsApp. | Seal callback, gavel secondary. | Final headline, support, CTAs. | Final CTA block, footer note. | WhatsApp number pending. |

---

## 7. 3D / Canvas Zone Decisions

| Scene | Desktop 3D Zone | Mobile 3D Decision | Notes |
| --- | --- | --- | --- |
| 01 | High-impact seal/gavel. | Simplified/static. | Resolved state only; P4.03 owns keyframes. |
| 02 | Seal anchor. | Simplified/poster. | 3D never blocks hero copy. |
| 03 | Document fragments. | Static/minimal. | Limit visual clutter. |
| 04 | Ordered desk/method. | Static/removed. | Avoid expensive morph dependency. |
| 05 | Dossier atmosphere. | Removed/static accent. | DOM cards carry meaning. |
| 06 | Workshop dossier atmosphere. | Removed/static accent. | No 3D card interaction required. |
| 07 | Chamber/portrait atmosphere. | Static/removed. | Mentor cards remain DOM. |
| 08 | Minimal atmosphere. | Removed. | Proof is editorial. |
| 09 | None/minimal. | Removed. | Reading-first section. |
| 10 | Seal callback. | Static/light. | CTA not delayed by seal motion. |

---

## 8. CTA / Conversion Map

| Scene | CTA Requirement | Visual Treatment |
| --- | --- | --- |
| 01 | CTA by handoff or fallback note. | Low-pressure CTA group near resolved brand state. |
| 02 | WhatsApp/Register clearly visible. | Primary outline/fill pair above fold. |
| 03 | Persistent WhatsApp only / low pressure. | Floating/global note, no aggressive scene CTA. |
| 04 | Soft CTA toward pillars. | Ghost/text CTA or secondary button. |
| 05 | View Workshops / Register Interest. | Button group after pillar cards. |
| 06 | Per-workshop WhatsApp + View Details. | Card-level CTAs. |
| 07 | Optional soft WhatsApp/Register. | Secondary CTA, not dominant. |
| 08 | Optional soft trust CTA. | Subtle CTA after proof structure. |
| 09 | CTA after FAQ. | FAQ CTA block. |
| 10 | WhatsApp primary + Register secondary. | Strong final CTA block. |

Rules:

- WhatsApp number remains `WHATSAPP_NUMBER_PENDING`.
- CTA labels are candidates only.
- Waitlist hidden unless conditional/internal note.
- No aggressive CTA pulse.
- No fake urgency.

---

## 9. Bilingual / RTL Notes

The comp board includes Arabic stress labels in the mobile scenes where layout risk is highest: Scene 02, Scene 05, Scene 06, Scene 09, and Scene 10.

| Scene | RTL / Arabic Visual Concern | Design Decision |
| --- | --- | --- |
| 01 | Arabic wordmark/tagline may need more height. | Keep brand text DOM and allow expanded line-height. |
| 02 | Arabic hero can wrap longer than English. | Text-first mobile and protected desktop text column. |
| 03 | Problem language must not feel accusatory. | Use respectful short copy zones. |
| 04 | Method bullets may expand. | Use flexible block height. |
| 05 | Pillar labels may need localization. | Cards stack on mobile; avoid fixed tight heights. |
| 06 | Workshop titles/CTAs may wrap. | Stacked card CTAs, 44px+ targets. |
| 07 | Role titles/bios can be longer. | Mentor cards allow text growth. |
| 08 | Proof language must be precise. | Single-column mobile proof blocks. |
| 09 | FAQ questions may be long. | Full-width accordion rows. |
| 10 | Arabic CTA block may need vertical rhythm. | CTA-first stack on mobile. |

---

## 10. Accessibility Notes

| Requirement | Visual Implication |
| --- | --- |
| Contrast | Parchment/ivory text on dark backgrounds; near-black on filled gold. |
| Focus | Components should have visible focus states in Figma state references. |
| Tap targets | Mobile CTAs/cards/FAQ rows must be 44px+. |
| DOM-first | Text/CTA zones are outside canvas zones. |
| Reduced motion | Static equivalent noted per scene. |
| WebGL fallback | Scene meaning not dependent on canvas. |
| RTL | Arabic layout concerns documented. |
| FAQ | Semantic accordion implied. |
| WhatsApp | Clear text label, not icon-only. |

No WCAG compliance is claimed in P4.02.

---

## 11. Visual Continuity Requirements

| Element | Requirement |
| --- | --- |
| Seal motif | Recurs in Scene 01, 02, 06, 10, optionally cards. |
| Gavel | Scene 01 and 10 only, secondary. |
| Dark chamber atmosphere | Present across journey, but not repetitive. |
| Gold | Used as signal, not decoration everywhere. |
| Parchment text | Main reading color on dark. |
| Scene numbers/labels | Consistent JetBrains/Tajawal label system. |
| CTAs | Consistent P4.01 component usage. |
| Cards | Same editorial/dossier family. |
| Motion implication | Slow, weighted, restrained. |
| Mobile | Same brand, not separate template. |

---

## 12. Handoff Notes

| Annotation | Purpose |
| --- | --- |
| DOM zone | Shows where real HTML content lives. |
| Canvas zone | Shows where R3F/background lives. |
| CTA zone | Shows conversion target. |
| Sticky/fixed elements | Header/WhatsApp behavior. |
| Mobile simplification | Shows what is removed/simplified. |
| Pending content | Marks missing real assets/facts. |
| Accessibility note | Contrast/focus/fallback concerns. |
| Performance note | 3D complexity caution. |
| Component references | Links to P4.01 components. |

---

## 13. Required Documentation Table

| Scene | Desktop Frame Exists | Mobile Frame Exists | CTA Present | 3D Zone Annotated | Mobile 3D Decision | Pending Content Notes | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | Yes | Yes | Yes | Yes | Simplified/static | Logo/wordmark/seal pending. | PASS |
| 02 | Yes | Yes | Yes | Yes | Simplified/poster | Hero copy pending. | PASS |
| 03 | Yes | Yes | Persistent only | Yes | Static/minimal | Final problem copy pending. | PASS |
| 04 | Yes | Yes | Soft | Yes | Static/removed | Method copy pending. | PASS |
| 05 | Yes | Yes | Yes | Yes | Removed/static accent | Pillar copy finalization pending. | PASS |
| 06 | Yes | Yes | Yes | Yes | Removed/static accent | Workshop facts pending. | PASS |
| 07 | Yes | Yes | Optional | Yes | Static/removed | Mentor profiles pending. | PASS |
| 08 | Yes | Yes | Optional | Yes | Removed | Proof assets pending. | PASS |
| 09 | Yes | Yes | Yes | Yes | Removed | FAQ copy pending. | PASS |
| 10 | Yes | Yes | Yes | Yes | Static/light | WhatsApp number pending. | PASS |

---

## 14. Visual Direction Guardrails

| Keep | Avoid |
| --- | --- |
| Seal-led cinematic authority. | Gavel-dominated or violent imagery. |
| Dark premium legal chamber. | Generic course website brightness. |
| Editorial typography hierarchy. | SaaS/dashboard typography. |
| DOM-first text and CTA zones. | Canvas-only messaging. |
| Spacious legal/dossier cards. | Course marketplace cards. |
| Honest trust placeholders. | Fake proof/testimonials. |
| Mobile text-first conversion. | Desktop 3D forced onto mobile. |
| Gold as signal. | Gold overload/neon glow. |
| Parchment/ivory readable copy. | Tiny decorative gold body text. |
| WhatsApp/Register clarity. | Hidden conversion path. |
| RTL-aware spacing. | English-only composition logic. |
| Static fallback awareness. | 3D-dependent meaning. |

---

## 15. Full-Fidelity Definition Check

| Requirement | Status | Notes |
| --- | --- | --- |
| Real design system colors | PASS | Uses P4.01 token values. |
| Real type styles | PASS | Uses P4.01 typography direction. |
| Real spacing rhythm | PASS | Uses P4.01 spacing and card rhythm. |
| Final-level visual hierarchy | PASS WITH CONDITIONS | Spec/HTML board defines hierarchy; Figma finalization pending. |
| Component-level buttons/cards/FAQ/nav | PASS | Represented in board and notes. |
| CTA placement | PASS | All scenes mapped. |
| 3D/canvas zone representation | PASS | Annotated in all scenes. |
| Scene atmosphere direction | PASS | Dark premium legal chamber direction. |
| Mobile layout direction | PASS | 390px frames represented. |
| Accessibility-aware contrast | PASS WITH CONDITIONS | Planned from tokens; QA pending. |
| Handoff annotations | PASS | Included in doc and board. |

---

## 16. Final Recommendation

| Decision Area | Recommendation |
| --- | --- |
| Desktop visual system | Use dark ceremonial editorial layouts with strong DOM zones and restrained 3D canvas regions. |
| Mobile visual system | Use text-first 390px layouts with simplified/static 3D and early CTAs. |
| 3D scene visual priority | Scene 01-02 are visual priority; Scene 10 seal callback is secondary priority. |
| CTA visual model | WhatsApp primary, Register secondary, workshop-specific card CTAs in Scene 06. |
| Card visual model | Spacious legal/dossier cards, not LMS/course marketplace tiles. |
| Trust/proof visual model | Verified-only or clearly pending internal placeholders. |
| RTL/mobile risk | Arabic wrapping, CTA length, and card expansion require Figma/native QA. |
| Biggest visual blocker | Final assets/content: seal/logo, workshops, mentors, proof, WhatsApp number. |
| Ready for P4.03? | Yes, with conditions; P4.03 should create opening keyframes only after Scene 01 resolved comp is reviewed. |
| Ready for frontend? | Not yet; Phase 5/8 required. |

Final recommendation:

**Proceed with these P4.02 scene-level visual comp specifications as the design contract draft, while keeping the actual Figma build, final assets, final content, Arabic/client review, accessibility QA, and frontend/3D validation as conditions.**

---

## 17. Quality Gate

| Gate | Status | Notes |
| --- | --- | --- |
| 10 desktop scene comps represented at 1440px | PASS WITH CONDITIONS | HTML board frames exist; Figma pending. |
| 10 mobile scene comps represented at 390px | PASS WITH CONDITIONS | HTML board frames exist; Figma pending. |
| Total 20 comps represented | PASS WITH CONDITIONS | 20 frames in board/spec. |
| Each comp uses P4.01 foundation | PASS | Colors, type, components, state notes used. |
| DOM content zone shown | PASS | Annotated per scene. |
| CTA placement shown | PASS | All relevant scenes include CTA placement. |
| 3D/canvas zone annotated | PASS | Desktop and mobile decisions documented. |
| Mobile follows P3.04 | PASS | Text-first/stacked/mobile 3D decisions. |
| CTA follows P3.03 | PASS | Conversion map used. |
| Content follows P3.06 | PASS | Primary messages and placeholder rules used. |
| Accessibility follows P3.05 | PASS | Notes included; compliance not claimed. |
| RTL/bilingual concerns documented | PASS | Dedicated section and mobile stress notes. |
| Pending content clearly marked | PASS | Pending content table/notes included. |
| No fake facts used | PASS | Pending labels used. |
| No frontend implementation | PASS | Static design artifact only. |
| No final 3D assets created | PASS | Canvas zones are visual placeholders. |
| No opening keyframe sequence comps | PASS | Scene 01 resolved state only. |
| No new roadmap tickets | PASS | No tickets created. |

---

## 18. Acceptance Criteria

| Acceptance Criteria | Status |
| --- | --- |
| 10 desktop scene visual comps created at 1440px | PASS WITH CONDITIONS |
| 10 mobile scene visual comps created at 390px | PASS WITH CONDITIONS |
| Total 20 scene comps exist | PASS WITH CONDITIONS |
| Scene 01 desktop and mobile comps exist | PASS |
| Scene 02 desktop and mobile comps exist | PASS |
| Scene 03 desktop and mobile comps exist | PASS |
| Scene 04 desktop and mobile comps exist | PASS |
| Scene 05 desktop and mobile comps exist | PASS |
| Scene 06 desktop and mobile comps exist | PASS |
| Scene 07 desktop and mobile comps exist | PASS |
| Scene 08 desktop and mobile comps exist | PASS |
| Scene 09 desktop and mobile comps exist | PASS |
| Scene 10 desktop and mobile comps exist | PASS |
| Each comp uses P4.01 foundation | PASS |
| Each comp shows DOM content zone | PASS |
| Each comp shows CTA placement where relevant | PASS |
| Each comp shows or annotates 3D/canvas zone | PASS |
| Mobile comps follow P3.04 mobile adaptation | PASS |
| CTA placement follows P3.03 conversion funnel | PASS |
| Content hierarchy follows P3.06 matrix | PASS |
| Accessibility notes follow P3.05 requirements | PASS |
| RTL/bilingual concerns are documented | PASS |
| Pending content is clearly marked | PASS |
| No fake workshop/mentor/proof facts are used | PASS |
| No frontend implementation is started | PASS |
| No final 3D assets are created | PASS |
| No opening keyframe sequence comps are created beyond Scene 01 resolved state | PASS |
| No new roadmap tickets are created | PASS |

---

## 19. Final Status

**PASS WITH CONDITIONS - P4.02 complete. 20 scene-level visual comp representations exist: 10 desktop at 1440px and 10 mobile at 390px, with DOM zones, CTA placement, 3D/canvas annotations, mobile/RTL/accessibility notes, and safe content handling.**

Conditions remaining:

- Actual Figma file/link is pending.
- Final seal/logo assets are pending.
- Final workshop content is pending.
- Mentor photos/bios are pending.
- Trust/proof content is pending.
- WhatsApp number is pending.
- Arabic final copy/localization is pending.
- Stakeholder/client visual approval is pending.
- Accessibility QA is pending.
- Frontend/3D implementation validation is pending.
