# Mithaq Motion Vocabulary Reference

**Official Ticket ID:** P2.07  
**Official Ticket Name:** Motion Vocabulary Reference  
**Phase:** Phase 2 - Creative Concept Development  
**Priority:** P1  
**Complexity:** Low  
**Owner:** Motion Director / Creative Director  
**Status:** PASS WITH CONDITIONS  
**Prepared date:** 2026-06-18  

---

## 1. Executive Summary

This document defines Mithaq's motion vocabulary for later GSAP, Lenis, ScrollTrigger, R3F camera movement, UI transitions, scene handoffs, CTA reveals, reduced-motion behavior, and mobile simplification.

Motion direction:

**Slow, decisive, weighted, ceremonial, premium, legal, controlled, calm, and scroll-led.**

Final motion recommendation:

**Use scroll-driven ceremonial reveals for major 3D beats, restrained fade/slide reveals for DOM content, subtle micro-interactions for CTA/card states, and static/fade equivalents for reduced motion and low-performance devices.**

This ticket does not implement GSAP, Lenis, ScrollTrigger, R3F camera paths, production animation, UI transitions in code, or sound.

Status is **PASS WITH CONDITIONS** because production motion still depends on vertical-slice testing, final assets, stakeholder review, mobile validation, and reduced-motion QA.

---

## 2. Current Mithaq Direction

- Mithaq is a premium bilingual 3D legal academy portfolio / landing experience.
- Core concept: The Covenant Seal.
- Opening direction: Scroll-Driven Seal-Led Opening.
- 3D direction: Seal-Led Macro Legal Chamber.
- The Seal is the hero.
- The gavel is the ceremonial trigger.
- Motion must feel like legal authority, not entertainment.
- No bouncing, jiggle, playful overshoot, trailer violence, game-like effects, or sci-fi hologram motion.
- Motion must not hide CTA or content.
- Reduced motion and static fallback are mandatory.
- Mobile simplification is mandatory.
- P1.05 feasibility decision: Vertical Slice Only Until Asset Optimization.
- Production-grade motion depends on vertical-slice validation.

---

## 3. Reference Sites Reviewed

Seven references were selected because each teaches a specific motion lesson relevant to Mithaq:

| Reference | Source URL | Reason Reviewed |
| --------- | ---------- | --------------- |
| Oryzo AI | https://oryzo.ai/ | Object-led hero pacing and symbolic visual focus. |
| KODE Immersive | https://kodeimmersive.com/ | Scroll-led immersive entry, spatial transitions, controlled experience pacing. |
| Immersive Garden | https://immersive-g.com/ | Premium scroll rhythm, reveal restraint, project/editorial motion discipline. |
| Floema | https://floema.com/ | Calm editorial transitions and understated premium motion. |
| Lenz & Staehelin | https://www.lenzstaehelin.com/ | Legal/institutional restraint and content-first motion tone. |
| ATMOS | https://atmos.leeroy.ca/ | Atmospheric scene motion and scroll-led sensory pacing. |
| Obys Agency | https://obys.agency/ | High-craft editorial transitions; useful mostly as an anti-excess boundary. |

No reference is copied directly. These are motion-language studies only.

---

## 4. Motion Reference Index

| ID | Reference Name | Motion Type | Applicable Mithaq Scenes |
| -- | -------------- | ----------- | ------------------------ |
| M01 | Oryzo AI Object-Led Hero | Object motion, hero reveal, CTA stabilization | Scenes 01, 02, 10 |
| M02 | KODE Immersive Spatial Entry | Scroll/camera, scene transition, immersive state | Scenes 01, 02, 03 |
| M03 | Immersive Garden Premium Scroll | Scroll, reveal, editorial scene handoff | Scenes 02-06 |
| M04 | Floema Editorial Restraint | Text reveal, page transition, hover restraint | Scenes 04-09 |
| M05 | Lenz & Staehelin Legal Restraint | Institutional content reveal, navigation, low-motion UI | Scenes 07-09 |
| M06 | ATMOS Atmospheric Scroll | Ambient motion, depth, sensory pacing | Scenes 01, 03, 10 |
| M07 | Obys Editorial Craft Boundary | Text/transition craft, high-energy caution | Scenes 02, 05, 06 |

---

## 5. Annotated Motion References

| Field | M01 - Oryzo AI Object-Led Hero |
| ----- | ------------------------------ |
| Source URL | https://oryzo.ai/ |
| Motion type | Object motion, hero reveal, CTA stabilization |
| What happens | A central symbolic/object-led visual experience anchors attention while content and action remain structured around it. |
| Timing feel | Medium-slow, authored, selective. |
| Easing feel | Premium ease-out, object stabilization, no playful bounce. |
| What Mithaq should borrow | Seal-as-object focus; one symbolic object should lead the memory of the hero. |
| What Mithaq should avoid | Tech-product playfulness, joke-like copy timing, or object animation becoming more important than conversion. |
| Applicable scenes | Scene 01, Scene 02, Scene 10 |
| Accessibility risk | If object motion becomes the only story, DOM meaning weakens. |
| Performance risk | Heavy hero object/post-processing can delay CTA. |
| GSAP translation | `power4.out` or `expo.out` for seal settle; `ScrollTrigger` scrub for entry only. |

| Field | M02 - KODE Immersive Spatial Entry |
| ----- | ---------------------------------- |
| Source URL | https://kodeimmersive.com/ |
| Motion type | Scroll/camera, scene transition, immersive state |
| What happens | Site motion creates the feeling of entering a designed world through scroll and spatial transitions. |
| Timing feel | Slow-to-medium, controlled, environmental. |
| Easing feel | Scroll-scrubbed progress with softened transitions. |
| What Mithaq should borrow | The sense of entering a chamber/world, while keeping scroll control visible. |
| What Mithaq should avoid | XR/sci-fi energy, overlong immersive waits, and motion that hides the message. |
| Applicable scenes | Scene 01, Scene 02, Scene 03 |
| Accessibility risk | Spatial entry can become a scroll trap or motion-sickness risk. |
| Performance risk | Camera transitions and layered media can be expensive on mobile. |
| GSAP translation | `scrub: true` or low scrub smoothing; avoid free-running camera flythroughs. |

| Field | M03 - Immersive Garden Premium Scroll |
| ----- | ------------------------------------ |
| Source URL | https://immersive-g.com/ |
| Motion type | Scroll, reveal, editorial scene handoff |
| What happens | Premium scroll rhythm moves content between focused visual states without frantic UI. |
| Timing feel | Medium, deliberate, polished. |
| Easing feel | `power3.out`, `power4.out`, occasional scroll-linked progress. |
| What Mithaq should borrow | Scene pacing, elegant reveals, and the discipline to let sections breathe. |
| What Mithaq should avoid | Agency/showcase excess that makes Mithaq feel like a portfolio rather than an academy. |
| Applicable scenes | Scenes 02, 03, 04, 05, 06 |
| Accessibility risk | Too many reveal dependencies can delay reading. |
| Performance risk | Multiple scroll observers/large media stacks can hurt low-tier devices. |
| GSAP translation | Section reveals with `power3.out`, 480-650ms; limited scroll triggers. |

| Field | M04 - Floema Editorial Restraint |
| ----- | -------------------------------- |
| Source URL | https://floema.com/ |
| Motion type | Text reveal, page transition, hover restraint |
| What happens | Editorial layouts use calm motion and avoid over-explaining through animation. |
| Timing feel | Medium-slow, quiet, refined. |
| Easing feel | Soft ease-out, restrained opacity/translate changes. |
| What Mithaq should borrow | Typographic restraint, short-distance text reveal, and non-distracting hover states. |
| What Mithaq should avoid | Lifestyle softness or motion that feels retail/catalog. |
| Applicable scenes | Scenes 04, 05, 06, 07, 08, 09 |
| Accessibility risk | Text reveal must not hide core reading content too long. |
| Performance risk | Low if limited to opacity/transform. |
| GSAP translation | `power2.out` / `power3.out`, 240-650ms, opacity + y: 12-24px max. |

| Field | M05 - Lenz & Staehelin Legal Restraint |
| ----- | -------------------------------------- |
| Source URL | https://www.lenzstaehelin.com/ |
| Motion type | Institutional content reveal, navigation, low-motion UI |
| What happens | Legal-sector digital presence uses restraint, content hierarchy, and confidence over spectacle. |
| Timing feel | Slow/medium, minimal, composed. |
| Easing feel | Simple ease-out or near-instant UI feedback. |
| What Mithaq should borrow | Legal calm, content-first pacing, and avoidance of dramatic animation around credibility. |
| What Mithaq should avoid | Law-firm service-site structure or overly conservative static feeling in the hero. |
| Applicable scenes | Scenes 07, 08, 09 |
| Accessibility risk | Low; keep navigation/focus immediate. |
| Performance risk | Low if no heavy motion is added. |
| GSAP translation | Use CSS/GSAP micro-reveals with `power2.out`, 160-320ms; no big effects. |

| Field | M06 - ATMOS Atmospheric Scroll |
| ----- | ----------------------------- |
| Source URL | https://atmos.leeroy.ca/ |
| Motion type | Ambient motion, depth, sensory pacing |
| What happens | Atmospheric visual movement supports mood and depth across an experience. |
| Timing feel | Slow, ambient, immersive. |
| Easing feel | `sine.inOut`, linear loops, scroll softness. |
| What Mithaq should borrow | Ambient dust/light motion and controlled sensory depth for the chamber. |
| What Mithaq should avoid | Overly sensory experience that competes with legal clarity or CTA. |
| Applicable scenes | Scene 01, Scene 03, Scene 10 |
| Accessibility risk | Ambient motion must stop/reduce for reduced motion. |
| Performance risk | Particles/transparency can be expensive; disable on mobile if needed. |
| GSAP translation | `sine.inOut` for low-opacity ambient loops; disable under `prefers-reduced-motion`. |

| Field | M07 - Obys Editorial Craft Boundary |
| ----- | ---------------------------------- |
| Source URL | https://obys.agency/ |
| Motion type | Text/transition craft, high-energy editorial effects |
| What happens | Strong motion craft and transitions create high-impact editorial experience. |
| Timing feel | Medium/fast, high craft, sometimes intense. |
| Easing feel | Custom/expo/power curves, energetic transitions. |
| What Mithaq should borrow | Craft discipline and confidence in transition timing. |
| What Mithaq should avoid | High-energy agency tone, aggressive text effects, or motion becoming a spectacle. |
| Applicable scenes | Scenes 02, 05, 06 |
| Accessibility risk | Fast text/transition effects can hurt readability and motion comfort. |
| Performance risk | Complex transitions can trigger layout and paint costs. |
| GSAP translation | Use only the restrained end: `power3.out` / `power4.out`; avoid rapid chained transitions. |

---

## 6. Required Motion Categories

### 6.1 Scroll-Driven Camera Motion

| Motion Area | Direction |
| ----------- | --------- |
| Camera movement | Slow, scroll-controlled, short range. |
| Easing | Scrubbed but softened; no autonomous flythrough. |
| Feeling | Weighted, ceremonial, user-led. |
| Avoid | Fast flythroughs, shaky camera, game-like navigation, long scroll trap. |

Use for:

- Scene 01 opening
- Scene 02 hero handoff
- Scene 03 gap reveal
- Scene 10 closing seal callback

### 6.2 Object Motion

| Object | Motion Direction |
| ------ | ---------------- |
| Gavel | Weighted descent, short decisive strike, no bounce. |
| Seal | Draw/reveal/settle, subtle light catch, no pulse. |
| Documents | Controlled drift into alignment. |
| Dossiers | Soft rise/fade, no card bounce. |
| Particles | Slow ambient movement only; disable/reduce on mobile. |

### 6.3 Text Reveal Motion

| Text Area | Motion Direction |
| --------- | ---------------- |
| Hero headline | Slow fade/slide, no gimmick-heavy split text. |
| Arabic headline | Full-word/line reveal; no letter-by-letter Arabic animation. |
| Body copy | Simple fade/up, short distance. |
| Labels | Precise fade; slight tracking reveal only if safe. |
| CTA | Soft reveal, stable after appearance, no pulsing. |

### 6.4 UI Micro-Interactions

| UI Element | Motion Direction |
| ---------- | ---------------- |
| CTA | Subtle border/gold fill transition; focus remains visible. |
| Workshop card | Gentle lift or light sweep only; no bounce. |
| FAQ | Smooth height/fade, no bounce; instant in reduced motion. |
| Language toggle | Fast and clear; no long transition. |
| Nav | Calm fade/slide; no sticky jump. |
| WhatsApp CTA | Visible, stable, not pulsing aggressively. |

### 6.5 Scene Transitions

| Transition | Direction |
| ---------- | --------- |
| Opening to hero | Seal resolves, text stabilizes, CTA becomes available. |
| Hero to gap | Chamber darkens; documents fragment into problem field. |
| Gap to method | Fragments align into ordered desk/method structure. |
| Pillars to workshops | Pillar cards lead into dossier-style workshop previews. |
| FAQ to final CTA | Reading section clears into seal callback and WhatsApp CTA. |

---

## 7. GSAP Easing Reference List

| Easing | Use Case | Why It Fits Mithaq | Avoid For |
| ------ | -------- | ------------------ | --------- |
| `power2.out` | Small UI reveals, cards, buttons | Controlled and natural. | Major cinematic beats. |
| `power3.out` | Text reveal, scene elements | Strong but not theatrical. | Tiny UI details. |
| `power4.out` | Hero text, seal reveal settle | Premium deceleration and authority. | Repeated micro-interactions. |
| `expo.out` | Major reveal / seal emergence | Ceremonial, decisive, memorable. | Long repeated scroll sections. |
| `circ.out` | Soft chamber/desk reveal | Smooth premium curve. | Sharp impact moments. |
| `sine.inOut` | Ambient particles / subtle loops | Calm and non-distracting. | Primary CTA attention. |
| `none` / linear with scrub | Scroll-synced camera progress | User-controlled scroll mapping. | Free-running animations. |
| Custom ease | Gavel strike / seal drawing | Needs crafted weight and restraint. | Generic UI components. |

Forbidden as core Mithaq motion:

- `bounce`
- `elastic`
- `back`
- playful overshoot curves
- endless pulse loops

---

## 8. Candidate Motion Tokens

These are planning tokens only. Do not implement them into production CSS or JS yet.

```css
:root {
  --motion-duration-micro: 160ms;
  --motion-duration-short: 280ms;
  --motion-duration-medium: 560ms;
  --motion-duration-long: 1000ms;
  --motion-duration-ceremonial: 1500ms;

  --motion-ease-ui: power2.out;
  --motion-ease-reveal: power3.out;
  --motion-ease-hero: power4.out;
  --motion-ease-ceremonial: expo.out;
  --motion-ease-ambient: sine.inOut;
  --motion-ease-scroll: none;
}
```

| Token | Suggested Value | Use |
| ----- | --------------- | --- |
| `motion-duration-micro` | 120-180ms | Focus/hover response. |
| `motion-duration-short` | 220-320ms | Button/card reveal. |
| `motion-duration-medium` | 420-650ms | Text/section reveal. |
| `motion-duration-long` | 800-1200ms | Scene transitions. |
| `motion-duration-ceremonial` | 1200-1800ms | Seal/gavel major beats. |
| `motion-ease-ui` | `power2.out` | UI micro-interactions. |
| `motion-ease-reveal` | `power3.out` | Text and card reveal. |
| `motion-ease-hero` | `power4.out` / `expo.out` | Hero/seal reveal. |
| `motion-ease-ambient` | `sine.inOut` | Particles / subtle light. |
| `motion-ease-scroll` | `none` / scrub | Scroll-driven mapping. |

---

## 9. Scene-Level Motion Vocabulary

| Scene | Motion Role | Recommended Motion | GSAP/Easing Direction | Reduced Motion |
| ----- | ----------- | ------------------ | --------------------- | -------------- |
| Scene 01 | Opening seal reveal | Scroll-driven ceremonial progression | scrub + custom / `power4.out` / `expo.out` | Static seal/desk fade. |
| Scene 02 | Hero stabilization | Slow text/CTA reveal | `power3.out` | Immediate visible content. |
| Scene 03 | Gap recognition | Documents drift/fragment | `sine.inOut` / `power2.out`, very subtle | Static document collage. |
| Scene 04 | Method order | Documents align | `power3.out` | Static ordered desk. |
| Scene 05 | Pillars | Card/dossier reveal | `power2.out` | Static cards. |
| Scene 06 | Workshops | Dossier/card entrance | `power2.out` / `power3.out` | Static list/grid. |
| Scene 07 | Mentors | Portrait/card fade | `power2.out` | Static grid. |
| Scene 08 | Trust | Editorial fade/number reveal if real | `power2.out` | Static proof blocks. |
| Scene 09 | FAQ | Accordion height/fade | `power2.out` | Native accordion/no animation. |
| Scene 10 | Final CTA | Seal callback + CTA reveal | `power3.out` / `expo.out` | Static final poster. |

---

## 10. Opening-Specific Motion Vocabulary

| Beat | Motion | Easing / Timing | Notes |
| ---- | ------ | --------------- | ----- |
| Darkness entry | Fade from black | Slow linear / scrub | No theatrical reveal. |
| Dust appears | Ambient slow drift | `sine.inOut` | Low opacity; disable on reduced motion/mobile if needed. |
| Desk reveal | Light sweep / fade | `circ.out` / scrub | Controlled warmth. |
| Gavel descent | Weighted drop | Custom ease | No bounce. |
| Gavel strike | Short decisive contact | Custom sharp curve | No smash; no trailer impact. |
| Ripple | Controlled outward line | `power3.out` | No explosion. |
| Seal outline | Draw path | `power4.out` / custom | Ceremonial and precise. |
| Seal settle | Subtle stabilization | `expo.out` | No pulse. |
| Wordmark | Fade/slide | `power3.out` | DOM text. |
| CTA | Soft reveal | `power2.out` | Stable, no pulsing. |

---

## 11. Bilingual / RTL Motion Rules

Rules:

- Do not animate Arabic letter-by-letter.
- Do not apply Latin split-text assumptions to Arabic.
- Keep Arabic text as full words/lines when animating.
- Use fade/slide/block reveal for Arabic.
- Use DOM text, not canvas text, for Arabic/English.
- Test RTL direction with actual Arabic phrases.
- Avoid motion that changes reading order.
- Language toggle motion must be fast and clear.
- Do not place Arabic and English in the same animated text line.
- Respect Tajawal 700 as Arabic display default; Lemonada accent-only.

| Motion Area | Arabic Rule | English Rule |
| ----------- | ----------- | ------------ |
| Hero headline | Full-line fade/slide; no letter splitting. | Restrained line/block reveal; split text only if subtle. |
| Labels | Use Tajawal/DOM labels; avoid tracking tricks that harm Arabic. | JetBrains Mono labels may fade/track slightly. |
| CTA | Fade/opacity/short translate as whole button. | Same; sentence/title case, no pulsing. |
| Workshop cards | Animate card container, not Arabic text fragments. | Animate card container; no stagger that delays readability. |
| FAQ | Instant or simple height/fade; preserve reading order. | Same; keep focus state stable. |
| Language toggle | Fast state change; no long crossfade that confuses reading direction. | Same; clear active/focus state. |

---

## 12. Accessibility / Reduced Motion Rules

| Motion Type | Standard Behavior | Reduced-Motion Behavior |
| ----------- | ----------------- | ----------------------- |
| Camera movement | Scroll-controlled camera shift. | Static poster/fade. |
| Gavel motion | Weighted descent/strike. | Static gavel/seal. |
| Seal draw | Scroll-driven line draw. | Seal visible via fade. |
| Documents drift | Subtle object drift. | Static composition. |
| Text reveal | Fade/slide. | Immediate or simple fade. |
| Card entrance | Gentle rise/fade. | No movement, opacity only. |
| Accordion | Smooth height/fade. | Instant open/close. |
| Ambient particles | Slow drift. | Disabled or static texture. |

Accessibility rules:

- Motion must never be required to understand content.
- CTA must remain accessible.
- Focus states must not depend on motion.
- No keyboard trap.
- No scroll trap.
- No autoplay sound tied to motion.
- Reduced-motion mode is a first-class experience, not a broken version.

---

## 13. Mobile Motion Rules

| Motion Area | Desktop Direction | Mobile Direction |
| ----------- | ----------------- | ---------------- |
| Opening | Full scroll-led sequence. | Shortened/simplified. |
| Camera | Controlled depth movement. | Reduced camera distance. |
| Particles | Subtle atmospheric. | Fewer or disabled. |
| Documents | Controlled drift. | Static or very limited. |
| Workshop cards | Gentle reveal. | Simple fade/stack. |
| Mentor cards | Fade/slide. | Static stack/fade. |
| FAQ | Accordion motion. | Minimal/instant. |
| Final CTA | Seal callback. | Static seal/CTA. |

Mobile rules:

- No long pinned sections on mobile unless tested.
- No CTA hidden behind motion.
- No hover-only motion.
- No excessive parallax.
- No high-DPR motion dependency.
- If FPS drops, disable non-essential motion.
- Keep scroll response direct; no sluggish smooth-scroll layer if it hurts touch feel.

---

## 14. Performance Motion Guardrails

| Risk | Guardrail |
| ---- | --------- |
| Too many ScrollTriggers | Group reveals by section; avoid per-word/per-card excessive triggers. |
| Layout shift | Animate opacity/transform, not layout dimensions, except controlled FAQ. |
| GPU pressure | Limit particles, post-processing, transparent layers, and blur. |
| Mobile FPS drops | Disable particles, reduce camera movement, use static posters. |
| Long load before motion | DOM text/CTA render before heavy 3D. |
| Shader failure | Static gold lines/fallback poster. |
| Scroll fatigue | Keep ceremonial sequence short and user-controlled. |
| Smooth-scroll conflicts | Test Lenis carefully; disable or simplify on touch devices if needed. |
| Bilingual overflow | Animate containers, not individual glyphs; test Arabic and English separately. |

P1.05 rule:

**Vertical Slice Only Until Asset Optimization.**

Do not approve production motion complexity across all scenes until the opening/hero vertical slice proves performance on target devices.

---

## 15. Motion Anti-Patterns

| Avoid | Why |
| ----- | --- |
| Bounce easing | Too playful, weakens legal authority. |
| Elastic easing | Game-like / cartoonish. |
| Back overshoot | Too casual for legal premium tone. |
| Constant pulsing CTA | Feels cheap and desperate. |
| Violent gavel smash | Wrong emotional signal. |
| Explosive shockwaves | Movie trailer / game effect. |
| Fast flythrough camera | Motion sickness risk. |
| Excessive parallax | Mobile performance and readability risk. |
| Arabic letter-by-letter animation | Breaks readability and can look awkward. |
| Canvas-only text reveals | Accessibility/SEO failure. |
| Scroll trap | User loses control. |
| Sound-dependent reveal | Accessibility and browser-policy issue. |

---

## 16. Motion Vocabulary Guardrail Table

| Keep | Avoid |
| ---- | ----- |
| Slow, decisive, controlled motion | Bounce, elastic, jiggle |
| Scroll-driven ceremonial reveal | Fixed trailer intro |
| Weighted gavel movement | Violent smash |
| Seal reveal with restraint | Magic sparkle / explosion |
| DOM text reveals | Canvas-only text |
| Arabic line/block reveals | Arabic letter-by-letter animation |
| Subtle CTA transitions | Pulsing desperate CTA |
| Reduced-motion equivalent | Mandatory camera movement |
| Mobile simplification | Full desktop choreography on all phones |
| GSAP tokens as planning reference | Production animation implementation |

---

## 17. Final Motion Direction Recommendation

Selected direction:

**Scroll-Led Ceremonial Restraint**

Motion should feel like entering a quiet legal chamber and witnessing a covenant become visible, not like watching a trailer or playing an interactive game.

Recommended implementation posture for later phases:

1. Use scroll-scrubbed camera/object progress only for major 3D beats.
2. Use `power3.out`, `power4.out`, and `expo.out` for premium reveal/settle moments.
3. Use `power2.out` for UI and card motion.
4. Use `sine.inOut` only for ambient particles/light loops.
5. Use custom easing for gavel contact and seal drawing.
6. Avoid bounce/elastic/back curves entirely for core motion.
7. Keep Arabic motion line/block-based.
8. Prioritize reduced-motion and mobile simplification from the beginning.

---

## 18. Quality Gate

| Gate | Status | Notes |
| ---- | ------ | ----- |
| 5-8 motion references collected | PASS | 7 references reviewed. |
| All references annotated | PASS | Full reference annotations included. |
| Easing/timing lessons documented | PASS | Per reference and GSAP table. |
| GSAP easing mapping included | PASS | Required easing list included. |
| Motion tokens included | PASS | Candidate token table and CSS-style snippet included. |
| Scene 01 opening motion documented | PASS | Dedicated opening section included. |
| Scenes 01-10 covered | PASS | Scene-level motion table included. |
| Bilingual/RTL rules documented | PASS | Dedicated section included. |
| Mobile rules documented | PASS | Dedicated table included. |
| Reduced-motion rules documented | PASS | Dedicated table included. |
| Accessibility risks documented | PASS | Reference and reduced-motion sections. |
| Performance guardrails documented | PASS | Dedicated section included. |
| Anti-patterns documented | PASS | Dedicated table included. |
| Motion feels legal/premium, not playful | PASS | Guardrails prohibit playful motion. |
| Avoided implementation | PASS | No GSAP/Lenis/R3F code created. |
| Avoided new roadmap tickets | PASS | No new tickets created. |

---

## 19. Acceptance Criteria

| Acceptance Criteria | Status |
| ------------------- | ------ |
| Motion vocabulary reference document created | PASS |
| 5-8 motion references reviewed | PASS |
| Every reference includes source URL and annotation | PASS |
| GSAP easing reference list included | PASS |
| Candidate motion tokens included | PASS |
| Scene-level motion vocabulary included for Scenes 01-10 | PASS |
| Opening-specific motion vocabulary included | PASS |
| Bilingual/RTL motion rules included | PASS |
| Accessibility/reduced-motion rules included | PASS |
| Mobile motion rules included | PASS |
| Performance guardrails included | PASS |
| Motion anti-patterns included | PASS |
| Final motion direction recommendation clear | PASS |
| No GSAP implementation started | PASS |
| No Lenis implementation started | PASS |
| No R3F camera path implemented | PASS |
| No production animation created | PASS |
| No new roadmap tickets created | PASS |

---

## 20. Final Status

**PASS WITH CONDITIONS - P2.07 complete. 7 motion references, GSAP easing list, motion tokens, bilingual/mobile/reduced-motion rules, and final motion direction are documented.**

Final production motion remains conditional on vertical-slice testing, final assets, stakeholder review, mobile validation, reduced-motion QA, and performance verification.
