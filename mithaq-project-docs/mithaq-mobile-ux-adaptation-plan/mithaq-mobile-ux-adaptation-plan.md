# Mithaq Mobile UX Adaptation Plan

**Official Ticket ID:** P3.04  
**Official Ticket Name:** Mobile UX Adaptation Plan  
**Phase:** Phase 3 - UX / IA / Storyflow Planning  
**Owner:** Mobile UX Lead / UX Strategist  
**Status:** PASS WITH CONDITIONS  
**Date:** 2026-06-19  
**Scope:** Mobile adaptation for `/`, `/register`, and `/workshops/[slug]`

---

## 1. Executive Summary

This document defines how Mithaq's desktop cinematic 3D/scroll experience becomes a mobile-safe, conversion-safe, readable, bilingual, and performant experience.

Final mobile UX position:

**Mobile should be text-first, WhatsApp-first, static-capable, and progressively enhanced. Scene 01-02 may use simplified premium 3D on capable devices, but mobile users must never need full desktop choreography to understand Mithaq, reach WhatsApp, view workshops, submit interest, or read Arabic/English content.**

Mobile production posture:

- Scene 01-02 are the only mobile 3D vertical-slice candidates.
- Scene 03 may use minimal/static document atmosphere.
- Scene 04-10 should be DOM/editorial-first on mobile.
- Scene 05-10 must prioritize conversion clarity, tap safety, and readability over 3D.
- Reduced-motion, WebGL fallback, and weak-device fallback are first-class mobile experiences.

Status is **PASS WITH CONDITIONS** because final mobile UX still depends on final content, final 3D assets, final brand/seal assets, physical device validation, vertical-slice testing, stakeholder review, and performance QA.

This is mobile UX planning only. No responsive layout, CSS, device detection, WebGL fallback, mobile menu, final UI comp, final copy, or frontend implementation is created.

---

## 2. Current Mithaq Decisions

| Area | Current Decision |
| --- | --- |
| Product type | Premium bilingual 3D legal academy portfolio / landing experience. |
| Primary conversion | WhatsApp. |
| Secondary conversion | `/register` inquiry/register interest form. |
| MVP routes | `/`, `/register`, `/workshops/[slug]`. |
| Core concept | The Covenant Seal. |
| Opening direction | Scroll-Driven Seal-Led Opening. |
| 3D direction | Seal-Led Macro Legal Chamber. |
| Motion direction | Scroll-Led Ceremonial Restraint. |
| Feasibility decision | P1.05 Option C - Vertical Slice Only Until Asset Optimization. |
| 3D priority | Scene 01-02 are highest vertical-slice priority. |
| Mobile rule | Mobile must not receive full heavy desktop choreography by default. |
| Content rule | DOM-first content is mandatory. |
| Fallback rule | WebGL fallback and reduced motion are mandatory. |
| Bilingual rule | Arabic and English are real localized layouts. |
| Arabic typography | Tajawal 700 is Arabic display default; Lemonada accent-only pending review. |
| CTA color rule | Filled gold CTA uses near-black text. |
| Trust rule | No fake urgency, fake seat counters, fake proof, or unsupported claims. |
| Scope guardrail | No LMS, dashboard, checkout, booking, or course-platform behavior. |

---

## 3. Mobile UX Principles

| Principle | Meaning |
| --- | --- |
| Mobile content first | Text, CTA, and meaning appear before heavy 3D. |
| WhatsApp-first | WhatsApp must be easy to reach on phone screens. |
| Progressive enhancement | 3D enhances the scene only if the device can handle it. |
| No forced desktop choreography | Desktop scroll/camera paths must be shortened or simplified. |
| No scroll trap | Mobile users should never feel stuck in a pinned animation. |
| DOM-first meaning | Every message must exist in HTML, not canvas-only. |
| Static can still be premium | Static fallback must feel designed, not broken. |
| Bilingual-safe | Arabic and English layouts need separate mobile checks. |
| Tap-safe | All interactive targets must be 44px minimum. |
| Performance-safe | Low FPS or weak devices must receive simplified/static experience. |
| Accessibility-safe | Reduced motion, keyboard, screen reader, and focus behavior must be protected. |

---

## 4. Mobile Target Breakpoints

| Breakpoint | Width Range | Target Behavior |
| --- | ---: | --- |
| Small Mobile | 320-374px | Maximum simplification, static-first where needed. |
| Standard Mobile | 375-430px | Primary mobile design target. |
| Large Mobile | 431-767px | Mobile layout with more spacing and optional light 3D. |
| Tablet Portrait | 768-1023px | Hybrid layout, simplified 3D possible. |
| Tablet Landscape | 1024px+ | May use desktop-like composition if performance allows. |

Required testing widths:

- 320px
- 375px
- 390px
- 430px
- 768px

Device/browser emphasis:

- iOS Safari latest and previous major: P0.
- Chrome Android latest: P0.
- Samsung Internet: P1.
- Older mobile browsers: static fallback acceptable.
- BrowserStack or physical devices required later if physical device coverage is unavailable.

---

## 5. Mobile Experience Tiers

| Tier | Device Condition | Experience |
| --- | --- | --- |
| Tier M1 - Modern High-End Mobile | Recent iPhone / flagship Android. | Simplified premium 3D allowed for Scene 01-02. |
| Tier M2 - Standard/Mid Mobile | Common mid-tier Android / older iPhone. | Static poster + selective lightweight 3D only if stable. |
| Tier M3 - Low-End / Weak GPU | Low memory, poor FPS, old browser. | Static editorial experience. |
| Tier M4 - Reduced Motion / WebGL Unavailable | Reduced motion enabled or no WebGL. | Static/fade experience, no required 3D. |

Experience tier rule:

Do not make M1 the default assumption. M2 and M3 must still feel premium and complete, not like a broken version of desktop.

---

## 6. Mobile 3D Policy

| Scene | Desktop 3D Direction | Mobile Decision | Reason |
| --- | --- | --- | --- |
| Scene 01 | Gavel/Seal opening. | Simplified or static depending tier. | Highest risk / highest brand value. |
| Scene 02 | Seal hero anchor. | Simplified seal/poster. | Protect LCP and CTA. |
| Scene 03 | Fragmented documents. | Static collage or minimal objects. | Avoid many meshes. |
| Scene 04 | Documents align into method. | Static ordered layout. | Avoid expensive morph. |
| Scene 05 | Dossier/card anchors. | DOM cards, minimal/no 3D. | Readability priority. |
| Scene 06 | Workshop dossiers. | DOM cards, no Raycaster dependency. | Conversion priority. |
| Scene 07 | Mentor atmosphere. | Static/DOM cards. | Trust/readability priority. |
| Scene 08 | Trust/proof. | Static editorial. | No need for 3D. |
| Scene 09 | FAQ. | No 3D. | Reading/accessibility priority. |
| Scene 10 | Seal callback. | Static or very light seal poster. | CTA priority. |

Final policy:

- Mobile full 3D is not required for all scenes.
- Scene 01-02 may receive simplified 3D if performance allows.
- Scene 05-10 should be DOM/editorial-first on mobile.
- Static fallback must preserve the same content and conversion path.

---

## 7. Scene-by-Scene Mobile Adaptation

### 7.1 Scene 01 - Gavel / Seal Opening

| Field | Required Answer |
| --- | --- |
| Scene | Scene 01 - Gavel / Seal Opening. |
| Mobile objective | Create a premium first impression without trapping the user in a long animation. |
| Desktop behavior | Scroll-driven desk reveal, gavel trigger, ripple, Seal reveal, brand/CTA handoff. |
| Mobile behavior | Shortened intro; Seal as primary visual; brand and CTA appear earlier. |
| 3D treatment | Simplified on M1; static on M2/M3/M4. |
| DOM priority | Brand identity, short positioning line, WhatsApp/Register access. |
| CTA behavior | WhatsApp/Register visible by safe point; fallback shows CTA immediately. |
| Scroll behavior | Natural scroll; no long pinned intro. |
| Motion behavior | Reduced camera movement; optional gavel trigger; no heavy particles. |
| Arabic/RTL note | Arabic brand/tagline must be DOM text and allowed generous line-height. |
| Performance note | Highest mobile risk; vertical-slice validation required before active 3D. |
| Accessibility note | No content or CTA can depend on canvas or sound. |
| Fallback equivalent | Seal/desk poster + brand + CTA. |

Avoid:

- Long scroll-locked intro.
- Heavy particles.
- Full desktop camera path.
- CTA hidden until too late.
- Sound dependency.

### 7.2 Scene 02 - Hero / Mithaq Reveal

| Field | Required Answer |
| --- | --- |
| Scene | Scene 02 - Hero / Mithaq Reveal. |
| Mobile objective | Clarify value proposition and show primary conversion quickly. |
| Desktop behavior | Seal/gavel hero atmosphere with protected copy and CTA. |
| Mobile behavior | Text-first hero; Seal becomes simplified background/poster. |
| 3D treatment | Simplified seal/poster. |
| DOM priority | Hero headline, short body, WhatsApp/Register CTA. |
| CTA behavior | Primary WhatsApp/Register visible near first screen. |
| Scroll behavior | Natural scroll; no pinned hero dependency. |
| Motion behavior | Simple fade/slide only. |
| Arabic/RTL note | Arabic headline width and line-height must be generous. |
| Performance note | DOM content and CTA render before any 3D. |
| Accessibility note | Hero heading and CTAs appear early in DOM order. |
| Fallback equivalent | Static hero with same headline and CTA. |

Avoid:

- 3D object covering copy.
- CTA below multiple scrolls.
- English-only spacing.
- Huge heading cropping Arabic.

### 7.3 Scene 03 - The Gap

| Field | Required Answer |
| --- | --- |
| Scene | Scene 03 - The Gap. |
| Mobile objective | Make the problem clear with minimal visual complexity. |
| Desktop behavior | Fragmented documents drift around a protected text zone. |
| Mobile behavior | Problem text first; static collage or 2-3 light elements. |
| 3D treatment | Static or minimal. |
| DOM priority | Problem headline and concise explanation. |
| CTA behavior | Persistent WhatsApp only; no aggressive CTA. |
| Scroll behavior | Natural scroll. |
| Motion behavior | Minimal document drift or none. |
| Arabic/RTL note | Avoid narrow Arabic text column. |
| Performance note | Avoid many transparent paper meshes. |
| Accessibility note | No essential text inside document textures. |
| Fallback equivalent | Static fragmented document poster + DOM copy. |

Avoid:

- Too many floating papers.
- Essential text inside document textures.
- Chaotic motion.
- Overdramatic crisis tone.

### 7.4 Scene 04 - The Mithaq Method

| Field | Required Answer |
| --- | --- |
| Scene | Scene 04 - The Mithaq Method. |
| Mobile objective | Explain the method clearly without relying on object morphing. |
| Desktop behavior | Documents align into method desk structure. |
| Mobile behavior | Vertical method blocks with optional static ordered desk accent. |
| 3D treatment | Static or removed. |
| DOM priority | Method headline and principles. |
| CTA behavior | Soft "View Training Pillars" or continue. |
| Scroll behavior | Natural scroll. |
| Motion behavior | Simple stagger/fade only. |
| Arabic/RTL note | Method blocks must support longer Arabic. |
| Performance note | Avoid expensive convergence/morph animation. |
| Accessibility note | Method principles should be semantic list/card content. |
| Fallback equivalent | Static method list. |

Avoid:

- Complex document convergence animation.
- Tiny method cards.
- Dashboard-like blocks.

### 7.5 Scene 05 - Training Pillars

| Field | Required Answer |
| --- | --- |
| Scene | Scene 05 - Training Pillars. |
| Mobile objective | Make the five pillars readable and tappable. |
| Desktop behavior | Five pillars reveal with dossier/card anchors. |
| Mobile behavior | Vertical stack or clean swipe-safe cards. |
| 3D treatment | Removed or decorative static only. |
| DOM priority | Pillar titles, short descriptions, card order. |
| CTA behavior | View Workshops / Register Interest near bottom. |
| Scroll behavior | Natural vertical scroll. |
| Motion behavior | Simple card fade; no hover-only reveal. |
| Arabic/RTL note | Cards must allow longer Arabic labels and body text. |
| Performance note | DOM cards carry all meaning. |
| Accessibility note | 44px targets; cards readable by DOM order. |
| Fallback equivalent | DOM cards only. |

Approved pillars:

1. Legal Research
2. Legal Writing
3. Professional Readiness
4. Career Infrastructure
5. Practical Legal Mindset

Avoid:

- Course marketplace grid feel.
- Tiny card text.
- Horizontal scroll without clear affordance.
- Hover-only reveals.

### 7.6 Scene 06 - Workshops & Course Preview

| Field | Required Answer |
| --- | --- |
| Scene | Scene 06 - Workshops & Course Preview. |
| Mobile objective | Drive workshop-specific WhatsApp/details actions clearly. |
| Desktop behavior | Workshop dossiers and cards appear with WhatsApp/detail CTAs. |
| Mobile behavior | Stacked workshop cards with clear per-card actions. |
| 3D treatment | Removed or static dossier accent. |
| DOM priority | Workshop title, level, skills, WhatsApp CTA, details link. |
| CTA behavior | "Ask About This Workshop" + "View Details"; 44px minimum. |
| Scroll behavior | Natural vertical scroll. |
| Motion behavior | Static or simple fade. |
| Arabic/RTL note | CTA labels and titles must wrap safely. |
| Performance note | No Raycaster dependency; DOM list is the product surface. |
| Accessibility note | CTAs are real links/buttons with clear labels. |
| Fallback equivalent | Full DOM workshop list. |

Rules:

- No fake pricing.
- No fake deadline.
- No fake seat count.
- No checkout.
- No LMS module behavior.

Avoid:

- Hover-only workshop details.
- 3D cards required for conversion.
- Swipe-only card discovery.
- Dense catalog filters.

### 7.7 Scene 07 - Hall of Mentors

| Field | Required Answer |
| --- | --- |
| Scene | Scene 07 - Hall of Mentors. |
| Mobile objective | Build trust with readable mentor cards/placeholders. |
| Desktop behavior | Subtle chamber/portrait atmosphere behind mentor cards. |
| Mobile behavior | Stacked mentor cards or simple carousel with explicit buttons. |
| 3D treatment | Static chamber atmosphere only or removed. |
| DOM priority | Mentor names, roles, bios, and placeholder-safe notes. |
| CTA behavior | Optional soft WhatsApp/Register. |
| Scroll behavior | Natural scroll. |
| Motion behavior | Simple fade only. |
| Arabic/RTL note | Mentor titles/bios need proper wrapping. |
| Performance note | Optimized/static placeholders if real photos are missing. |
| Accessibility note | No fake names/credentials; no image-only identity. |
| Fallback equivalent | Static mentor list. |

Avoid:

- Fake names/credentials.
- Tiny business-card layout.
- Auto-rotating carousel.
- Portrait effects that hurt clarity.

### 7.8 Scene 08 - Trust / Authority / Credibility

| Field | Required Answer |
| --- | --- |
| Scene | Scene 08 - Trust / Authority / Credibility. |
| Mobile objective | Show trust structure without fake proof and visual overload. |
| Desktop behavior | Minimal atmosphere and editorial trust blocks. |
| Mobile behavior | Single-column trust/proof blocks. |
| 3D treatment | Removed/static only. |
| DOM priority | Verified proof, methodology notes, or clearly marked placeholders. |
| CTA behavior | Soft WhatsApp/Register if appropriate. |
| Scroll behavior | Natural scroll. |
| Motion behavior | Minimal fade. |
| Arabic/RTL note | Proof labels and body copy must not be cramped. |
| Performance note | No mobile 3D needed. |
| Accessibility note | Proof content is DOM text and only verified. |
| Fallback equivalent | Same static editorial section. |

Avoid:

- Fake stats.
- Fake testimonials.
- Number counters without verified numbers.
- Heavy 3D behind proof text.

### 7.9 Scene 09 - FAQ

| Field | Required Answer |
| --- | --- |
| Scene | Scene 09 - FAQ. |
| Mobile objective | Answer objections with maximum readability and accessibility. |
| Desktop behavior | Semantic FAQ section with minimal/no 3D. |
| Mobile behavior | Vertical accessible accordion. |
| 3D treatment | Removed. |
| DOM priority | FAQ questions, answers, and follow-up CTA. |
| CTA behavior | WhatsApp/Register after FAQ plus persistent WhatsApp. |
| Scroll behavior | Natural scroll. |
| Motion behavior | Minimal/instant accordion. |
| Arabic/RTL note | Long Arabic questions must wrap cleanly. |
| Performance note | Static recommended. |
| Accessibility note | 44px rows; accessible accordion pattern later. |
| Fallback equivalent | Same semantic FAQ. |

Avoid:

- Tiny accordion rows.
- Nested accordions.
- Heavy animation.
- FAQ hidden behind 3D.

### 7.10 Scene 10 - Final CTA / Closing Covenant

| Field | Required Answer |
| --- | --- |
| Scene | Scene 10 - Final CTA / Closing Covenant. |
| Mobile objective | Convert with a calm, clear, premium closing section. |
| Desktop behavior | Seal callback with WhatsApp/Register CTA. |
| Mobile behavior | CTA-first closing section with static seal/desk poster or very light seal. |
| 3D treatment | Static or very light. |
| DOM priority | Final headline, support line, WhatsApp CTA, Register CTA. |
| CTA behavior | WhatsApp primary, Register secondary; visible immediately after headline. |
| Scroll behavior | Natural scroll; stable end state. |
| Motion behavior | Simple fade only. |
| Arabic/RTL note | CTA and headline must not overflow. |
| Performance note | Static fallback likely preferred unless final slice approves 3D callback. |
| Accessibility note | End CTAs remain visible and keyboard/tap accessible. |
| Fallback equivalent | Static closing CTA. |

Avoid:

- Countdown timers.
- Too many CTAs.
- CTA below footer clutter.
- Heavy seal animation delaying action.

---

## 8. Mobile Navigation Plan

| Element | Requirement |
| --- | --- |
| Logo | Links to home/top. |
| Menu trigger | Clear hamburger/menu button with accessible label. |
| Primary links | Method, Workshops, FAQ, Register. |
| WhatsApp CTA | Prominent in menu and/or floating CTA. |
| Language toggle | Reachable, clear current language, tap-safe. |
| Menu behavior | Opens/closes clearly; no scroll trap. |
| Sticky behavior | Header may be sticky if it does not crowd content. |
| Focus behavior | Focus order follows DOM; menu close returns focus later. |
| CTA priority | WhatsApp and Register outrank secondary anchors. |

Mobile nav rules:

- No mega-menu.
- No hover-only dropdown.
- No hiding WhatsApp inside a deep menu only.
- No full-screen menu that obscures close controls.
- Header should not consume excessive vertical space.
- Language toggle must remain reachable in both Arabic and English.

---

## 9. Mobile CTA Rules

| CTA Area | Mobile Rule |
| --- | --- |
| Persistent WhatsApp | Visible but not blocking content. |
| Hero CTA | Must appear early. |
| Workshop CTA | Large, per-card, direct. |
| Final CTA | Immediately after closing headline. |
| Register CTA | Secondary but accessible. |
| Form CTA | Full-width or highly visible. |
| Language toggle | Easy but not more prominent than conversion. |
| Waitlist | Hidden unless real waitlist approved. |

Rules:

- No aggressive pulsing.
- No fake urgency.
- No tiny gold text.
- No hover-only CTA reveal.
- No CTA inside canvas only.
- No CTA delayed by 3D loader.
- Filled gold CTA uses near-black text.
- Tap targets must be at least 44px.

---

## 10. Mobile Form UX Plan

| Area | Mobile Requirement |
| --- | --- |
| Form length | Short and low-friction. |
| Required fields | Name + Phone/WhatsApp only. |
| Optional fields | Email, interest area, preferred language, message. |
| Input size | Large enough for phone typing. |
| Labels | Always visible. |
| Errors | Clear, inline, not color-only. |
| Submit button | Full-width or very clear. |
| WhatsApp alternative | Visible near form. |
| Keyboard type | Phone input uses tel keyboard. |
| Privacy note | Planned before launch. |
| Success state | Clear inline success. |

Avoid:

- Multi-step application.
- Password/account creation.
- Payment fields.
- Upload fields.
- Long qualification form.
- Hidden required fields.

---

## 11. Mobile Workshop Detail Plan

| Section | Mobile Requirement |
| --- | --- |
| Workshop hero | Clear title, level, format placeholder. |
| CTA | Ask About This Workshop visible early. |
| Details | Vertical readable sections. |
| Skills | Bullets/cards, not dense paragraphs. |
| Mentor | Optional if confirmed. |
| FAQ | Workshop-specific accordion. |
| Related workshops | Optional, not distracting. |
| WhatsApp | Workshop-specific CTA repeated. |
| Register | Secondary CTA. |

Rules:

- No checkout.
- No LMS lesson layout.
- No fake pricing/date/capacity.
- No module dashboard.
- No hover-only cards.
- No waitlist CTA unless real waitlist is approved.

---

## 12. Mobile Bilingual / RTL Rules

| Area | Arabic/RTL Requirement | English/LTR Requirement |
| --- | --- | --- |
| Header | RTL nav order must feel natural. | LTR nav order normal. |
| Hero | Arabic headline needs generous width/line-height. | English headline can be tighter. |
| CTA | Arabic labels must not overflow. | English labels should avoid all-caps overload. |
| Cards | Arabic text expansion supported. | English labels checked for length. |
| FAQ | Long Arabic questions wrap safely. | English accordion remains readable. |
| Forms | Arabic labels align correctly. | English labels align normally. |
| Workshop detail | Arabic content not cramped. | English content not over-wide. |
| Motion | No Arabic letter-by-letter animation. | Restrained text reveal. |

Bilingual rules:

- Use localized layout behavior.
- Do not force Arabic into English spacing.
- Do not bake text into 3D textures.
- Do not use letter-spacing on Arabic body text.
- Test 320px Arabic layouts.
- Language toggle must be reachable.
- Tajawal 700 remains the safe Arabic display default.
- Lemonada remains accent-only pending review.

---

## 13. Mobile Reduced-Motion Plan

Mobile and reduced motion are separate but overlapping.

| Scene | Standard Mobile | Reduced-Motion Mobile |
| --- | --- | --- |
| 01 | Simplified seal reveal or static. | Static seal poster. |
| 02 | Seal poster/simple fade. | Static hero. |
| 03 | Static/minimal document collage. | Static document collage. |
| 04 | Static method blocks. | Static method blocks. |
| 05 | Static pillar cards. | Static pillar cards. |
| 06 | Static workshop cards. | Static workshop cards. |
| 07 | Static mentor cards. | Static mentor cards. |
| 08 | Static trust blocks. | Static trust blocks. |
| 09 | Semantic FAQ. | Semantic FAQ. |
| 10 | Static final CTA. | Static final CTA. |

Rule:

Reduced-motion mobile must not lose content, CTA access, route access, or the meaning of the Covenant Seal.

---

## 14. Mobile Performance Plan

| Area | Mobile Rule |
| --- | --- |
| DPR | Cap at 1-1.5 depending tier. |
| Particles | Reduce heavily or disable. |
| Post-processing | Off by default on mobile. |
| Shadows | Baked/static preferred. |
| Textures | Use mobile-optimized textures. |
| GLB | Use compressed/simplified hero assets. |
| Lazy loading | Non-critical scenes lazy-loaded or static. |
| Canvas | Should not block DOM content. |
| Render loop | Pause/limit when offscreen. |
| Fallback | Trigger if WebGL unavailable or FPS unstable. |
| CTA | Never hidden behind loader. |

Recommended mobile targets:

| Metric | Target |
| --- | ---: |
| Mobile FPS | 30-45 FPS if 3D active. |
| LCP | < 2.5s target. |
| INP | < 200ms. |
| CLS | < 0.1. |
| Tap target | >= 44px. |
| Initial content visibility | Immediate DOM-first. |

Important:

These are planning targets, not verified production results. They must be validated later on real or equivalent devices.

---

## 15. Mobile Fallback Triggers

| Trigger | Required Response |
| --- | --- |
| WebGL unavailable | Static editorial experience. |
| `prefers-reduced-motion: reduce` | Reduced-motion static/fade path. |
| Low FPS detected | Simplify 3D or switch to static. |
| GLB fails | Static poster with DOM content. |
| Shader error | Fallback material or static poster. |
| Memory pressure | Disable non-essential 3D. |
| Slow network | DOM content and CTA first. |
| iOS audio restrictions | Sound remains muted/off. |
| Android browser instability | Static fallback if needed. |

Fallback principle:

Fallback is not a failure state. It is a premium editorial version of the same journey.

---

## 16. Mobile Interaction Rules

| Interaction | Mobile Rule |
| --- | --- |
| Scroll | Natural, no long trapping. |
| Pinned sections | Short and used sparingly. |
| Hover | Not required. |
| Tap | 44px target minimum. |
| Workshop card | Tap to details/WhatsApp, no hover reveal. |
| FAQ | Tap accordion, accessible later. |
| Menu | Clear open/close. |
| Language toggle | Tap-safe and visible. |
| Audio | User-initiated only. |
| Form | Mobile keyboard-friendly. |
| Canvas | No essential tap-only hotspots. |

Avoid:

- Multitouch gestures.
- Drag-only navigation.
- Horizontal scroll dependency.
- Tiny hotspots.
- Scroll-jacking.
- Forced landscape orientation.

---

## 17. Mobile Scene Adaptation Matrix

| Scene | Mobile Layout | 3D Treatment | CTA Treatment | Fallback |
| --- | --- | --- | --- | --- |
| 01 | Short opening / static hero intro. | Simplified/static. | CTA by safe point. | Static seal poster. |
| 02 | Text-first hero. | Simplified seal/poster. | CTA early. | Static hero. |
| 03 | Problem text + collage. | Static/minimal. | Persistent WhatsApp. | Static collage. |
| 04 | Vertical method blocks. | Static/removed. | Soft CTA. | Static method. |
| 05 | Vertical pillar cards. | Removed/static accent. | View Workshops/Register. | DOM cards. |
| 06 | Stacked workshop cards. | Removed/static accent. | Per-card WhatsApp/details. | DOM list. |
| 07 | Stacked mentor cards. | Removed/static atmosphere. | Optional soft CTA. | DOM mentor list. |
| 08 | Single-column proof blocks. | Removed. | Optional soft CTA. | Editorial blocks. |
| 09 | FAQ accordion. | Removed. | CTA after FAQ. | Semantic FAQ. |
| 10 | Closing CTA section. | Static/light seal. | WhatsApp primary. | Static closing poster. |

---

## 18. Mobile Priority by Scene

| Priority | Scenes | Reason |
| --- | --- | --- |
| P0 | Scene 02, Scene 06, Scene 10 | Conversion and clarity. |
| P0 | Header/mobile nav/WhatsApp | Conversion access. |
| P1 | Scene 01 | Brand impression, but must not block action. |
| P1 | Scene 03, Scene 05, Scene 09 | Problem, offer clarity, objection handling. |
| P2 | Scene 04, Scene 07, Scene 08 | Important but can remain editorial/static first. |

Note:

Mobile priority is not identical to desktop visual priority. On mobile, conversion access and clarity outrank cinematic complexity.

---

## 19. Mobile QA Checklist

| Check | Pass Criteria |
| --- | --- |
| 320px layout | No horizontal overflow. |
| 375px layout | Hero/CTA readable. |
| 390px layout | Main target clean. |
| 430px layout | Large phone spacing stable. |
| Arabic RTL | No clipping or cramped text. |
| English LTR | No awkward wrapping. |
| WhatsApp CTA | Reachable and tap-safe. |
| Register CTA | Reachable. |
| Workshop cards | CTAs visible and 44px+. |
| FAQ | Tap-safe accordion. |
| Header menu | Opens/closes clearly. |
| Language toggle | Reachable and clear. |
| Reduced motion | Static/fade path works. |
| WebGL fallback | Full content still present. |
| Form | Labels visible, keyboard type correct. |
| Performance | No obvious jank on mid-tier target. |
| Orientation | Portrait works; no forced landscape. |
| Sound | No unexpected autoplay. |

Additional QA notes:

- Test 320px Arabic specifically.
- Test iOS Safari and Chrome Android before launch.
- Test Samsung Internet if possible.
- If physical devices are unavailable, use BrowserStack or equivalent later.

---

## 20. Mobile Risk Map

| Risk | Why It Matters | Mitigation |
| --- | --- | --- |
| Heavy 3D blocks first content | Bad trust and LCP. | DOM-first hero/CTA. |
| CTA hidden behind cinematic intro | Conversion loss. | CTA by safe point / fallback early. |
| Arabic text overflows | Premium feel breaks. | RTL testing at 320-430px. |
| Workshop cards too dense | Users cannot choose. | Stacked simple cards. |
| Hover-only details | Mobile users miss content. | Tap/direct details. |
| Long pinned scroll | Feels trapped. | Short/no pinned mobile sections. |
| Low FPS | Cheap feeling / battery drain. | Simplify/static. |
| Fake urgency near CTA | Trust damage. | Keep waitlist conditional. |
| Form too long | Drop-off. | Minimal fields. |
| Nav hides WhatsApp | Conversion loss. | WhatsApp in menu/floating CTA. |

---

## 21. Mobile UX Guardrail Table

| Keep | Avoid |
| --- | --- |
| Text-first mobile hero. | Canvas-first mobile loading. |
| WhatsApp always reachable. | CTA hidden behind animation. |
| Simplified Scene 01-02 3D. | Full desktop 3D on all phones. |
| Static editorial scenes where needed. | 3D-dependent meaning. |
| Stacked workshop cards. | Hover-only course cards. |
| Semantic FAQ. | Decorative FAQ animation. |
| Arabic RTL mobile testing. | English-only mobile assumptions. |
| 44px tap targets. | Tiny hotspots. |
| Short/no pinned mobile sections. | Scroll traps. |
| Static fallback that looks premium. | Broken degraded fallback. |

---

## 22. Final Mobile UX Recommendation

| Decision Area | Recommendation |
| --- | --- |
| Mobile experience model | Text-first, WhatsApp-first, progressively enhanced. |
| Primary mobile 3D scope | Scene 01-02 only, simplified and conditional. |
| Static/editorial scenes | Scene 04-10 should be static/DOM-first by default. |
| Workshop mobile UX | Stacked DOM cards with per-card WhatsApp and details CTA. |
| Mobile navigation | Compact header/menu with reachable WhatsApp, Register, and language toggle. |
| Mobile form UX | Simple `/register` form with only name and phone required. |
| Mobile workshop detail | Early workshop-specific WhatsApp, vertical detail sections, no LMS behavior. |
| Arabic/RTL | Separate mobile QA at 320-430px; no Arabic text in canvas textures. |
| Reduced motion | Static/fade path with full content and CTA access. |
| Performance | DOM before canvas, low DPR, no post-processing by default, fallback on instability. |
| Production risk | Medium/high until mobile device validation and final assets exist. |

Final recommendation:

**Proceed with a mobile adaptation strategy that treats the cinematic 3D layer as optional enhancement and the DOM layer as the complete experience. Protect WhatsApp, Register Interest, Arabic readability, workshop clarity, and static fallback before approving any mobile 3D expansion beyond Scene 01-02.**

---

## 23. Quality Gate

| Gate | Status | Notes |
| --- | --- | --- |
| All 10 scenes covered | PASS | Scene 01-10 mobile adaptations included. |
| Every scene has mobile-specific adaptation | PASS | Full required field table per scene. |
| Simplified/static/removed 3D decisions documented | PASS | Mobile 3D policy and scene matrix included. |
| Mobile navigation planned | PASS | Dedicated navigation section included. |
| WhatsApp mobile access protected | PASS | CTA rules, nav, matrix, and risk map cover this. |
| `/register` mobile form UX planned | PASS | Dedicated form UX plan included. |
| `/workshops/[slug]` mobile UX planned | PASS | Dedicated workshop detail plan included. |
| Bilingual/RTL mobile rules included | PASS | Dedicated Arabic/English table included. |
| Reduced-motion mobile rules included | PASS | Dedicated reduced-motion table included. |
| Mobile performance rules included | PASS | Dedicated performance plan included. |
| Fallback triggers documented | PASS | Dedicated fallback trigger table included. |
| Mobile interaction rules documented | PASS | Dedicated interaction table included. |
| Mobile QA checklist included | PASS | Practical QA checklist included. |
| Mobile risk map included | PASS | Risk and mitigation table included. |
| Avoided implementation | PASS | No CSS, code, device detection, WebGL fallback, or UI comps created. |
| Avoided new roadmap tickets | PASS | No new tickets created. |

---

## 24. Acceptance Criteria

| Acceptance Criteria | Status |
| --- | --- |
| Mobile UX adaptation document created | PASS |
| Scene 01 mobile adaptation is defined | PASS |
| Scene 02 mobile adaptation is defined | PASS |
| Scene 03 mobile adaptation is defined | PASS |
| Scene 04 mobile adaptation is defined | PASS |
| Scene 05 mobile adaptation is defined | PASS |
| Scene 06 mobile adaptation is defined | PASS |
| Scene 07 mobile adaptation is defined | PASS |
| Scene 08 mobile adaptation is defined | PASS |
| Scene 09 mobile adaptation is defined | PASS |
| Scene 10 mobile adaptation is defined | PASS |
| 3D simplified/static/removed decisions are documented | PASS |
| Mobile navigation plan is included | PASS |
| Mobile CTA rules are included | PASS |
| Mobile form UX is included | PASS |
| Mobile workshop detail UX is included | PASS |
| Bilingual/RTL mobile rules are included | PASS |
| Reduced-motion mobile plan is included | PASS |
| Mobile performance plan is included | PASS |
| Fallback triggers are included | PASS |
| Mobile QA checklist is included | PASS |
| Mobile risk map is included | PASS |
| Mobile UX guardrail table is included | PASS |
| No UI comps are created | PASS |
| No frontend implementation is started | PASS |
| No device detection code is written | PASS |
| No new roadmap tickets are created | PASS |

---

## 25. Final Status

**PASS WITH CONDITIONS - P3.04 complete. Mobile UX adaptation is defined for all 10 scenes with 3D simplification/static/removal decisions, mobile navigation, CTA, form, workshop, bilingual, reduced-motion, performance, fallback, QA, and risk notes.**

Final mobile UX remains conditional on final content, final assets, mobile device validation, vertical-slice testing, stakeholder approval, and performance QA.
