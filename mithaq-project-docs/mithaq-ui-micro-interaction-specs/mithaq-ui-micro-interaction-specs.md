# Mithaq UI Micro-interaction Specs

**Official Ticket ID:** P4.04  
**Official Ticket Name:** UI Micro-interaction Specs  
**Phase:** Phase 4 - Visual System & Art Direction  
**Priority:** P1  
**Complexity:** Medium  
**Owner:** Motion Designer / UI Interaction Designer  
**Status:** PASS WITH CONDITIONS  
**Prepared date:** 2026-06-20  

---

## 1. Executive Summary

This document defines Mithaq's official UI micro-interaction behavior for later frontend implementation. It covers default, hover, focus, active, disabled, loading, open/closed, selected/current, error/success, mobile tap, reduced-motion, and RTL/LTR behavior across the interactive UI system.

Interaction direction:

**Calm, restrained, accessible, DOM-first, conversion-clear, bilingual-safe, and premium.**

This task is specification only. It does not implement React components, production CSS, GSAP, Lenis, ScrollTrigger, R3F, mobile menu behavior, modal behavior, FAQ behavior, forms, WhatsApp links with a real number, or new roadmap tickets.

---

## 2. Current Mithaq Direction

| Area | Current Direction |
| --- | --- |
| Product type | Premium bilingual 3D legal academy portfolio / landing experience. |
| Core concept | The Covenant Seal. |
| Motion direction | Scroll-Led Ceremonial Restraint. |
| Interaction feel | Slow where ceremonial, quick where functional, always controlled. |
| Primary conversion | WhatsApp. |
| Secondary conversion | `/register`. |
| Waitlist | Conditional only; hidden unless approved. |
| Typography | Cormorant for English authority moments, DM Sans for body/UI, JetBrains Mono sparingly, Tajawal for Arabic, Lemonada accent-only. |
| CTA color rule | Filled gold CTAs use near-black text; white on gold is not allowed. |
| Accessibility baseline | WCAG 2.2 AA target; compliance not claimed yet. |
| Bilingual rule | Arabic and English are equal product requirements. |
| Fallback rule | WebGL/static fallback must retain interactions and CTAs. |

Forbidden: bounce, elastic easing, playful overshoot, jiggle, aggressive CTA pulse, game-like UI effects, neon hover glow, hover-only meaning, canvas-only CTAs, fake urgency, fake content, fake WhatsApp number, LMS/dashboard interactions, checkout/payment behavior.

---

## 3. Micro-interaction Principles

| Principle | Meaning |
| --- | --- |
| Restraint over spectacle | UI motion must support clarity, not show off. |
| Weight, not bounce | Interactions should feel deliberate and premium. |
| Conversion clarity | CTAs must always remain visible and understandable. |
| Focus is not optional | Keyboard focus must be stronger than hover decoration. |
| Mobile is tap-first | No hover-only information or CTA. |
| Arabic-safe motion | Arabic text uses block/line/fade behavior only. |
| Reduced-motion equivalent | Every animated state has a static/opacity alternative. |
| No fake urgency | No pulse, countdown, shake, scarcity, or pressure motion. |
| Component consistency | Similar elements share timing/easing. |
| Implementation-safe | Specs must be clear enough for frontend handoff. |

---

## 4. Motion Token Reference

Planning tokens for UI-state handoff. These are not production CSS and are not wired into the app.

| Token | Suggested Value | Usage |
| --- | ---: | --- |
| `duration-instant` | 80ms | Tiny state acknowledgement. |
| `duration-micro` | 140-180ms | Focus/hover response. |
| `duration-short` | 220-280ms | Button/card transition. |
| `duration-medium` | 360-480ms | Accordion/modal/menu reveal. |
| `duration-long` | 650-900ms | Larger scene UI handoff. |
| `ease-ui` | `power2.out` | Buttons, nav, simple cards. |
| `ease-reveal` | `power3.out` | Card/content reveal. |
| `ease-ceremonial` | `power4.out` / `expo.out` | Major CTA/hero reveal only. |
| `ease-ambient` | `sine.inOut` | Ambient decorative loops. |
| `ease-scroll` | `none` / scrub | Scroll-synced scene motion. |

Forbidden core UI eases:

- `bounce`
- `elastic`
- `back` overshoot
- springy cartoon motion
- repeated pulsing
- shake/jiggle effects

---

## 5. Global Interaction Rules

| Rule | Requirement |
| --- | --- |
| Hover | Enhances only; never reveals essential hidden content alone. |
| Focus | Clearly visible, keyboard-safe, and stronger than hover. |
| Active | Shows clear pressed/selected state. |
| Loading | Includes text/state, not spinner only. |
| Disabled | Looks disabled and includes reason if context needs it. |
| Motion | Subtle and restrained; no layout shift. |
| Reduced motion | Movement becomes opacity/color/border state. |
| Mobile | Tap behavior replaces hover. |
| Canvas | UI interactions remain DOM-based. |
| Sound | No UI sound unless user-enabled and optional. |
| CTA | No aggressive pulse, shake, or fake urgency animation. |

Global timing recommendation:

| Interaction Type | Duration | Ease |
| --- | ---: | --- |
| Hover/focus visual state | 140-180ms | `power2.out` |
| Active/pressed state | 80-140ms | `power2.out` |
| Button loading state | 140-220ms | `power2.out` |
| Card emphasis | 220-280ms | `power2.out` |
| Menu/accordion/modal | 360-480ms | `power3.out` |
| Hero/final CTA reveal | 650-900ms | `power3.out` or `power4.out` |

---

## 6. Button Interaction Specs

Applies to: Primary Gold Filled, Primary Gold Outline, Secondary Parchment, Ghost, Text Link Button, WhatsApp Button, Disabled Button, Loading Button.

| State | Visual Change | Motion / Timing | Accessibility Requirement | Reduced Motion |
| --- | --- | --- | --- | --- |
| Default | Stable contrast-safe surface; height fixed; label fully visible. | None. | Real button/link semantics later; accessible name required. | Same. |
| Hover | Subtle border/light/fill shift; no movement unless 1-2px tonal lift is approved. | `duration-micro`, `ease-ui`. | Hover cannot reveal essential action. | Instant or color/border only. |
| Focus | Strong visible focus ring on dark and gold; focus stronger than hover. | `duration-instant` to `duration-micro`, `ease-ui`. | Keyboard focus visible at all times; ring not clipped. | Same; no movement. |
| Active | Slight tonal deepening or 1px pressed state; no bounce. | 80-140ms, `ease-ui`. | Pressed state perceivable; no layout shift. | Tonal change only. |
| Disabled | Muted opacity/border; cursor/semantics disabled later; reason shown if user needs it. | None or 80ms. | Disabled controls must not be focusable unless explanatory pattern is used later. | Same. |
| Loading | Label changes to "Processing..." / "Opening..." / localized equivalent; spinner optional, never alone. | 140-220ms, `ease-ui`. | Announce loading later with `aria-live` or button text; prevent duplicate submit. | Text state changes immediately. |

Variant notes:

| Variant | Specific Interaction Direction |
| --- | --- |
| Primary Gold Filled | Near-black text always; hover can deepen gold or add dark border. |
| Primary Gold Outline | Hover may add low-opacity gold fill; focus ring remains separate. |
| Secondary Parchment | Hover shifts border/text toward parchment; avoid becoming primary CTA. |
| Ghost | Hover adds subtle panel tint or underline; never hides label. |
| Text Link Button | Underline/border reveal preferred; no animated icon-only affordance. |
| WhatsApp Button | See dedicated WhatsApp CTA section. |
| Disabled Button | Do not imply fake unavailable seat/waitlist state. |
| Loading Button | Preserve width/height to prevent layout shift. |

Rules:

- Button height remains stable.
- Arabic labels must not be compressed.
- No white text on filled gold.
- No pulsing CTA.
- No hover-only information.

---

## 7. CTA Interaction Specs

Applies to: Hero CTA Group, Workshop CTA Group, FAQ CTA Block, Final CTA Block, Register Interest CTA, Inline Soft CTA.

| State | Visual Change | Motion / Timing | Accessibility Requirement | Reduced Motion |
| --- | --- | --- | --- | --- |
| Default | Clear primary/secondary hierarchy; WhatsApp or Register label visible. | None. | DOM link/button; accessible name. | Same. |
| Hover | Calm gold emphasis, underline, border, or fill transition. | `duration-short`, `ease-ui`. | Action meaning visible without hover. | Color/border only. |
| Focus | Strong focus ring and visible label; primary CTA focus is unmistakable. | `duration-micro`, `ease-ui`. | Keyboard reachable in logical order. | Same. |
| Active | Pressed tonal state; no scale bounce. | 80-140ms. | Pressed state perceivable. | Tonal only. |
| Disabled | Only for staging/missing destination; label should explain pending internally. | None. | Do not ship disabled conversion CTA without alternate path. | Same. |
| Loading / Handoff | If route/contact opens, show "Opening..." only if delayed. | 140-220ms. | Text state, not spinner-only. | Immediate text change. |

CTA-specific behavior:

| CTA Type | Interaction Direction |
| --- | --- |
| Hero CTA | Calm gold emphasis; no motion that delays comprehension. |
| Workshop CTA | Clear per-card action; always visible in card. |
| FAQ CTA | Stable after answers; no attention-grabbing pulse. |
| Final CTA | Strong but calm; may use `ease-reveal` when entering scene. |
| Inline Soft CTA | Text underline/border reveal only. |
| Register CTA | Secondary but readable, never buried. |

CTA rules:

- CTA must be DOM.
- CTA must be visible without animation.
- CTA must be tap-safe on mobile.
- CTA cannot depend on 3D state.
- Waitlist CTA remains hidden/conditional unless approved.

---

## 8. WhatsApp CTA Interaction Specs

Applies to: Header WhatsApp, Floating WhatsApp, Hero WhatsApp, Workshop WhatsApp, FAQ WhatsApp, Final WhatsApp.

| State | Visual Change | Motion / Timing | Accessibility Requirement | Reduced Motion |
| --- | --- | --- | --- | --- |
| Default | Clear WhatsApp intent with text label where primary; placeholder destination remains `WHATSAPP_NUMBER_PENDING`. | None. | Accessible name includes action, not icon only. | Same. |
| Hover | Subtle gold or restrained WhatsApp-safe green accent; no neon glow. | `duration-micro` to `duration-short`, `ease-ui`. | Meaning not dependent on hover. | Color/border only. |
| Focus | Strong focus ring; label visible. | `duration-micro`, `ease-ui`. | Keyboard reachable; focus not hidden under floating placement. | Same. |
| Active | Pressed state. | 80-140ms. | Clear activation feedback. | Tonal only. |
| Disabled | Staging only if number is missing; provide alternate register path. | None. | Do not ship dead primary CTA. | Same. |
| Loading | Usually not needed; if used, label changes to "Opening WhatsApp..." / localized. | 140-220ms. | Text state, not spinner-only. | Immediate text. |

Variant notes:

| Variant | Direction |
| --- | --- |
| Header WhatsApp | Compact but labeled if primary in nav context. |
| Floating WhatsApp | Non-blocking, stable, no pulse/shake. |
| Hero WhatsApp | Primary conversion; strongest CTA state. |
| Workshop WhatsApp | Indicates workshop-specific inquiry context once content is confirmed. |
| FAQ WhatsApp | Low-pressure "ask before registering" tone. |
| Final WhatsApp | Strong final action, no urgency animation. |

Rules:

- Do not invent WhatsApp number.
- Do not use icon-only label for primary WhatsApp CTA.
- Floating WhatsApp must not cover content.
- No constant shaking, pulsing, or bounce.
- Workshop WhatsApp context must use real confirmed workshop data later.

---

## 9. Navigation Interaction Specs

Desktop header elements: logo/home, nav links, section anchors, register CTA, WhatsApp CTA, language toggle.

| State | Visual Change | Motion / Timing | Accessibility Requirement | Reduced Motion |
| --- | --- | --- | --- | --- |
| Default | Readable over dark/3D backgrounds; active route if applicable. | None. | Semantic nav links later. | Same. |
| Hover | Subtle underline/gold line reveal or opacity shift. | `duration-micro`, `ease-ui`. | Link meaning visible without hover. | Instant underline/color. |
| Focus | Strong focus ring or underline + ring; not color-only. | `duration-micro`, `ease-ui`. | Focus order matches visual/nav order. | Same. |
| Active | Pressed tonal/underline state. | 80-140ms. | Activation state clear. | Tonal only. |
| Current/Selected | Persistent underline/dot/label; not color-only. | None or `duration-micro`. | Current page/section indicated semantically later. | Same. |
| Disabled | Only if route unavailable; avoid disabled nav in public launch. | None. | Explain unavailable route if shown. | Same. |

Element notes:

| Element | Interaction Direction |
| --- | --- |
| Logo | Hover/focus underline or opacity shift; links home. |
| Nav link | Subtle underline/gold line reveal. |
| Current section | Clear active/current state, not color-only. |
| Register CTA | Button behavior. |
| WhatsApp | WhatsApp CTA behavior. |
| Language toggle | Selected state clear. |

Rules:

- No mega-menu.
- No dashboard/login/account nav.
- Header state must remain readable over dark/3D.
- Active section indicator must not rely on color only.

---

## 10. Mobile Menu Interaction Specs

Elements: menu trigger, open panel, close button, nav links, WhatsApp link, Register link, language toggle.

| State | Visual Change | Motion / Timing | Accessibility Requirement | Reduced Motion |
| --- | --- | --- | --- | --- |
| Closed | Menu trigger visible; 44px minimum tap target. | None. | Button label/name required later. | Same. |
| Opening | Panel fades/slides from logical side; dark premium surface. | `duration-medium`, `ease-reveal`. | Focus management required later; no canvas dependency. | Instant or opacity-only. |
| Open | Links visible, close button visible, CTAs visible, language toggle visible. | None. | Close reachable; no keyboard trap; Escape behavior later. | Same. |
| Closing | Reverse fade/slide. | `duration-medium`, `ease-reveal`. | Return focus to trigger later. | Instant or opacity-only. |
| Focus | Ring visible on trigger, close, links, CTAs. | `duration-micro`. | Keyboard-safe. | Same. |
| Active | Pressed state for trigger/links. | 80-140ms. | Clear activation feedback. | Tonal only. |

Rules:

- No hover dependency.
- No menu hidden behind canvas.
- Mobile menu must not cover persistent CTA without a visible alternate.
- All tap targets 44px minimum.
- Focus management is required later, but not implemented here.

---

## 11. Language Toggle Interaction Specs

States: Arabic active, English active, hover, focus, active, disabled if route unavailable.

| State | Visual Change | Motion / Timing | Accessibility Requirement | Reduced Motion |
| --- | --- | --- | --- | --- |
| Default | Current language clearly indicated; both labels readable. | None. | Text labels, not flags only. | Same. |
| Hover | Subtle border/fill or underline on target language. | `duration-micro`, `ease-ui`. | Current/target meaning visible without hover. | Color/border only. |
| Focus | Strong focus ring around toggle or focused option. | `duration-micro`. | Announces current/target language later. | Same. |
| Active | Pressed state on selected target. | 80-140ms. | Activation clear. | Tonal only. |
| Selected | Persistent active indicator for AR/EN. | None or `duration-micro`. | Not color-only. | Same. |
| Disabled | Only if route unavailable; show unavailable state conservatively. | None. | Do not trap user in language dead-end. | Same. |

Rules:

- Use text labels, not flags only.
- Works in RTL/LTR.
- Motion is fast and restrained.
- Do not animate Arabic letters.
- Do not make language toggle more dominant than conversion CTAs.

---

## 12. Card Interaction Specs

Applies to: Base Editorial Card, Pillar Card, Route Card, and shared card foundations. Specialized cards are detailed in later sections.

| State | Visual Change | Motion / Timing | Accessibility Requirement | Reduced Motion |
| --- | --- | --- | --- | --- |
| Default | Stable editorial surface; title/body/CTA visible as applicable. | None. | If interactive, card or inner action is keyboard reachable. | Same. |
| Hover | Slight border emphasis, light sweep, or 2-4px max lift. | `duration-short`, `ease-ui`. | No essential content revealed only on hover. | Border/opacity only; no lift. |
| Focus | Clear focus outline around interactive target. | `duration-micro`. | Focus not clipped by card overflow. | Same. |
| Active | Pressed/selected tonal state if clickable. | 80-140ms. | State perceivable. | Tonal only. |
| Disabled/Pending | Muted internal placeholder treatment; not public fake content. | None. | Avoid misleading users. | Same. |
| Mobile | CTAs/details visible; no hover dependency. | None or short opacity. | Tap targets 44px. | Same. |

Rules:

- No bounce.
- No 3D flip card.
- No hidden essential copy on hover.
- No course marketplace feel.
- Mobile cards show CTAs directly.

---

## 13. Workshop Card Interaction Specs

Interactions: card hover/focus, Ask About This Workshop CTA, View Details CTA, optional modal preview trigger, pending content state, mobile stacked state.

| State | Visual Change | Motion / Timing | Accessibility Requirement | Reduced Motion |
| --- | --- | --- | --- | --- |
| Default | Title, fit/level, skills, and CTAs visible when confirmed; pending fields internally marked. | None. | Actions are DOM links/buttons. | Same. |
| Hover | Subtle border/light change; optional 2px lift max. | `duration-short`, `ease-ui`. | CTA already visible; hover reveals no essential action. | Border/opacity only. |
| Focus | Strong outline on card action or card wrapper if clickable. | `duration-micro`. | CTA reachability via keyboard. | Same. |
| Active | Press feedback on card/CTA. | 80-140ms. | Activation clear. | Tonal only. |
| Pending content | Internal annotation only; do not present fake title/date/mentor as final. | None. | Avoid misleading public state. | Same. |
| Mobile | Stacked, CTAs always visible. | None or simple opacity. | 44px tap targets. | Same. |
| Modal trigger | Button/link state follows CTA/button behavior. | `duration-short`. | Modal is optional; detail page remains canonical. | Same. |

Rules:

- No hover-required CTA.
- No 3D raycaster-only interaction.
- No fake enrollment loading.
- No checkout/payment behavior.
- No fake waitlist state.
- `/workshops/[slug]` remains canonical for detail later.

---

## 14. Mentor Card Interaction Specs

| State | Visual Change | Motion / Timing | Accessibility Requirement | Reduced Motion |
| --- | --- | --- | --- | --- |
| Default | Portrait/name/title only if confirmed; placeholder-safe otherwise. | None. | Real image later needs alt text. | Same. |
| Hover | Subtle portrait light, border shift, or 2px lift max. | `duration-short`, `ease-ui`. | No credentials hidden behind hover. | Border/opacity only. |
| Focus | Clear outline if card/action is interactive. | `duration-micro`. | Keyboard reachable only if actionable. | Same. |
| Active | Optional details expansion if later approved. | 80-140ms for press; expansion `duration-medium`. | Expanded content must be accessible. | Instant/opacity only. |
| Placeholder | Safe non-fake placeholder treatment. | None. | Do not imply real mentor identity. | Same. |
| Mobile | Static/tap-safe card; no carousel dependency. | None. | Tap targets safe. | Same. |

Rules:

- Do not invent mentor data.
- Do not hide credentials behind hover.
- No auto-rotating carousel dependency.
- Alt text planning required when portraits arrive.

---

## 15. Trust / Proof Block Interaction Specs

| State | Visual Change | Motion / Timing | Accessibility Requirement | Reduced Motion |
| --- | --- | --- | --- | --- |
| Default | Trust/proof block visible; source/status only if approved. | None. | Text must be real DOM. | Same. |
| Hover | Optional subtle emphasis only. | `duration-short`, `ease-ui`. | Proof meaning not hover-dependent. | Border/opacity only. |
| Focus | If interactive, clear outline. | `duration-micro`. | Keyboard reachable if link/action exists. | Same. |
| Verified | May show subtle verified/source marker. | None or `duration-micro`. | Marker not color-only; source text later. | Same. |
| Pending | Internal only; not public fake proof. | None. | Avoid fake testimonials/stats. | Same. |
| Mobile | Static single-column. | None. | Readable at 320-390px. | Same. |

Rules:

- No animated number counters unless verified and later approved.
- No fake proof, testimonials, logos, or metrics.
- No decorative interaction that looks like real evidence.

---

## 16. FAQ Accordion Interaction Specs

| State | Visual Change | Motion / Timing | Accessibility Requirement | Reduced Motion |
| --- | --- | --- | --- | --- |
| Closed | Question visible, indicator clear. | None. | Later use semantic button behavior. | Same. |
| Hover | Subtle row emphasis. | `duration-micro`, `ease-ui`. | Question remains readable. | Color/border only. |
| Focus | Strong focus ring/outline. | `duration-micro`. | Keyboard operability; focus not clipped. | Same. |
| Active | Press feedback on question row. | 80-140ms. | State clear. | Tonal only. |
| Open | Answer appears with height/opacity transition; indicator changes. | `duration-medium`, `ease-reveal`. | Expanded state announced later; answer DOM remains accessible. | Instant open/close or opacity-only. |
| Mobile | Full-width 44px+ tap row. | Same or shorter. | Tap-safe, no nested tiny controls. | Instant or opacity-only. |

Rules:

- FAQ content does not depend on animation.
- No nested accordions unless necessary.
- Indicator placement mirrors in RTL.
- No bounce on open/close.

---

## 17. Form Input Interaction Specs

Applies to `/register` components: text input, tel input, email input, select/radio, textarea, helper text, error message, success message.

| State | Visual Change | Motion / Timing | Accessibility Requirement | Reduced Motion |
| --- | --- | --- | --- | --- |
| Default | Visible label and input boundary; helper text if needed. | None. | No placeholder-only labels. | Same. |
| Hover | Subtle border shift. | `duration-micro`, `ease-ui`. | Meaning not hover-dependent. | Color/border only. |
| Focus | Strong focus border/ring; label remains visible. | `duration-micro`. | Label associated later; focus visible. | Same. |
| Filled | Value clearly visible; no layout shift. | None. | Value readable in Arabic/English. | Same. |
| Error | Error border plus text message; icon optional. | `duration-micro` or immediate. | Error is not color-only; associated with field later. | Immediate text. |
| Success | Accessible confirmation or field-level success where useful. | `duration-micro`. | Success message not color-only. | Immediate text. |
| Disabled | Muted boundary/text; not interactive. | None. | Disabled semantics later. | Same. |
| Loading | Usually submit-level; field-level loading only if validation delayed. | 140-220ms. | Text status if used. | Immediate status. |

Form rules:

- Phone input plans tel keyboard later.
- Arabic labels align correctly in RTL.
- Error text must be contrast-safe.
- Form must not feel like account, application, or LMS system.
- Required field behavior is documented later in implementation, not invented here.

---

## 18. Form Submission / Error / Success Specs

| State | Visual Change | Motion / Timing | Accessibility Requirement | Reduced Motion |
| --- | --- | --- | --- | --- |
| Ready | Submit CTA visible; privacy/data note area reserved. | None. | Button accessible. | Same. |
| Submitting | Button label changes to "Sending..." / localized; spinner optional. | 140-220ms. | Prevent duplicate submit; status announced later. | Immediate label. |
| Field error | Field receives error style and text message. | `duration-micro` or immediate. | Error associated with field. | Immediate. |
| Form error | Top or inline summary explains issue. | `duration-short`. | Error summary focus behavior later. | Immediate. |
| Success | Confirmation message with next step and WhatsApp alternative. | `duration-medium`, `ease-reveal`. | Announced later; keyboard focus managed. | Immediate/opacity only. |
| Disabled submit | Muted only when form cannot submit; reason visible if needed. | None. | Avoid unexplained blocked state. | Same. |

Rules:

- Loading text required; spinner alone is not enough.
- No fake approval, certificate, or enrollment success.
- No payment/checkout state.
- No account/password flow.

---

## 19. Modal / Workshop Preview Interaction Specs

Modal preview is optional; `/workshops/[slug]` remains canonical.

| State | Visual Change | Motion / Timing | Accessibility Requirement | Reduced Motion |
| --- | --- | --- | --- | --- |
| Trigger hover/focus | Clear action state on preview/detail trigger. | `duration-micro`, `ease-ui`. | Trigger is DOM button/link. | Color/border only. |
| Opening | Restrained fade/scale or slide; dark overlay. | `duration-medium`, `ease-reveal`. | Focus management required later. | Instant or opacity-only. |
| Open | Content readable, close visible, CTAs visible. | None. | Focus trap/escape required later; close reachable. | Same. |
| Closing | Reverse transition. | `duration-medium`, `ease-reveal`. | Return focus to trigger later. | Instant or opacity-only. |
| Focus | Ring on close, CTAs, links, fields. | `duration-micro`. | No keyboard trap. | Same. |
| Mobile | Fullscreen or sheet-like if used. | `duration-medium`, `ease-reveal`. | Close visible; tap targets safe. | Instant/opacity only. |

Rules:

- Modal cannot be the only path to workshop details.
- No fake workshop content.
- No auto-open modal.
- No scroll trap.

---

## 20. Floating CTA Interaction Specs

Applies mainly to persistent WhatsApp/floating CTA.

| State | Visual Change | Motion / Timing | Accessibility Requirement | Reduced Motion |
| --- | --- | --- | --- | --- |
| Default | Visible, stable, non-blocking; label or accessible label clear. | None or one-time fade if entering. | Keyboard reachable if visible. | Static visible. |
| Hover | Subtle border/fill emphasis; no pulse. | `duration-micro`, `ease-ui`. | Meaning visible without hover. | Color/border only. |
| Focus | Strong accessible focus ring. | `duration-micro`. | Focus not obscured by viewport edge. | Same. |
| Active | Pressed state. | 80-140ms. | Activation clear. | Tonal only. |
| Hidden state | Only if overlapping critical content; safe reappearance. | `duration-short`. | Hidden state must not remove only conversion path. | Instant hide/show. |
| Mobile | Does not cover FAQ/form/card CTAs. | None or opacity. | 44px tap target; avoid content obstruction. | Static or disabled if obstructive with alternate CTA visible. |

Rules:

- No shaking.
- No constant pulsing.
- No blocking mobile content.
- Must have accessible label.

---

## 21. Links / Text Links Specs

Applies to inline links, footer links, anchor links, workshop detail links, privacy links, and back links.

| State | Visual Change | Motion / Timing | Accessibility Requirement | Reduced Motion |
| --- | --- | --- | --- | --- |
| Default | Underline, border, or clear affordance; not color-only. | None. | Semantic link later. | Same. |
| Hover | Underline/border strengthens; color may shift to gold/parchment. | `duration-micro`, `ease-ui`. | Meaning not hover-only. | Instant/color only. |
| Focus | Strong focus ring or outline plus underline. | `duration-micro`. | Keyboard-visible. | Same. |
| Active | Pressed tonal state. | 80-140ms. | Activation clear. | Tonal only. |
| Current | Persistent active/current marker if section/page link. | None. | Not color-only. | Same. |
| External | If used later, clear external indication. | None. | Accessible text/icon label later. | Same. |

Rules:

- Arabic link text must not be cramped.
- Link affordance cannot rely only on color.
- External links need clear indication later if introduced.

---

## 22. Static Fallback Interaction Specs

Static fallback must retain interaction quality if WebGL or motion is unavailable.

| Component | Static Fallback Behavior |
| --- | --- |
| Header navigation | Same link/focus/current behavior; no canvas dependency. |
| WhatsApp CTA | Visible and usable with `WHATSAPP_NUMBER_PENDING` until final number exists. |
| Register CTA | Visible link to `/register`. |
| Workshop cards | DOM CTAs always visible. |
| FAQ accordion | Semantic open/close behavior; animation optional. |
| Language toggle | Same AR/EN state behavior. |
| Form links | Same link/button behavior. |
| Footer links | Same link behavior. |

Rules:

- Fallback interactions feel intentionally designed.
- No broken/disabled CTAs because 3D is unavailable.
- Reduced-motion and static fallback may share interaction rules.
- No canvas-only interaction.

---

## 23. Reduced-Motion Interaction Rules

| Component | Standard Motion | Reduced-Motion Behavior |
| --- | --- | --- |
| Buttons | Color/fill/border transition. | Instant or short opacity/color. |
| CTAs | Fade/reveal or border/fill transition. | Visible immediately or color/border only. |
| WhatsApp CTA | Subtle emphasis. | Static, no entrance motion. |
| Cards | Slight lift/light sweep. | Border/opacity only. |
| Workshop cards | Border/lift/card reveal. | Border/opacity only; CTAs visible. |
| Mentor cards | Portrait light/border shift. | Border/opacity only. |
| Trust blocks | Subtle emphasis. | Static/border only. |
| FAQ | Height/opacity transition. | Instant open/close or opacity-only. |
| Modal | Fade/scale/slide. | Instant/opacity only. |
| Mobile menu | Slide/fade. | Instant/opacity only. |
| Floating CTA | Fade/slide entrance. | Static visible. |
| Hero CTA | Fade/reveal. | Visible immediately. |
| Language toggle | Sliding indicator. | Instant state change. |
| Form errors | Fade/slide. | Immediate text. |

Reduced-motion rules:

- Reduced motion must not remove content.
- Reduced motion must not remove CTA access.
- No UI camera movement.
- No long animated delays.
- No sound-dependent interaction.

---

## 24. Mobile / Touch Interaction Rules

| Interaction | Rule |
| --- | --- |
| Hover | Not required for meaning. |
| Tap | Primary action. |
| Tap target | 44px minimum. |
| Workshop cards | CTAs always visible. |
| FAQ | Tap-safe rows. |
| Menu | Clear open/close. |
| Floating CTA | Non-blocking. |
| Forms | Full-width inputs with visible labels. |
| Modal | Fullscreen/sheet if used. |
| Horizontal swipe | Avoid unless visible controls exist. |

Avoid:

- hover-only details
- tiny hotspots
- drag-only interaction
- multitouch requirement
- long pinned interaction
- CTA hidden behind motion
- mobile 3D interaction as the only path

---

## 25. RTL / Arabic Interaction Rules

| Area | Arabic / RTL Rule |
| --- | --- |
| Buttons | Icon placement mirrors where appropriate; labels not compressed. |
| Nav | Focus/order feels natural in RTL. |
| Cards | Text alignment and CTA order adapt. |
| FAQ | Indicator placement mirrors. |
| Forms | Labels and errors align correctly. |
| Language toggle | Current language clear. |
| Motion | Line/block/fade reveals only. |
| Text | No letter-by-letter animation. |
| Focus | Focus ring not clipped by RTL layout. |
| Mobile | Test 320-390px Arabic labels. |

Rules:

- Do not use Latin letter-spacing on Arabic.
- Do not compress Arabic CTA labels.
- Do not mix Arabic and English in one animated line.
- Arabic motion prioritizes readability.
- Tajawal remains default Arabic UI/display choice; Lemonada accent-only pending review.

---

## 26. Accessibility Interaction Requirements

This section maps requirements only. It does not claim accessibility compliance.

| Component | Accessibility Interaction Requirement |
| --- | --- |
| Buttons/CTAs | Keyboard reachable, visible focus, accessible names. |
| WhatsApp CTA | Clear label, no icon-only primary CTA. |
| Nav | Semantic links, active state not color-only. |
| Mobile menu | Focus management later, close reachable, Escape behavior later. |
| Language toggle | Announces current/current target language later. |
| Cards | No hover-only essential content. |
| Workshop cards | CTAs reachable; no card-only hidden actions. |
| FAQ | Keyboard/screen-reader operability later. |
| Forms | Visible labels, error association later. |
| Modal | Focus trap/escape/return focus later. |
| Floating CTA | Keyboard reachable if visible; does not obscure content. |
| Static fallback | Same interactions without canvas. |

Focus rules:

- Focus ring must be visible on dark backgrounds and gold buttons.
- Focus must not be removed for aesthetic reasons.
- Focus state is stronger than hover state.
- Focus order follows reading and visual order in each language.

---

## 27. Frontend Handoff Matrix

| Component | States Needed | Motion Token | Reduced Motion | Notes |
| --- | --- | --- | --- | --- |
| Primary Button | default/hover/focus/active/loading/disabled | `duration-micro`, `duration-short`, `ease-ui` | color/border/text only | Filled gold uses near-black text. |
| WhatsApp CTA | default/hover/focus/active/loading-if-delayed | `duration-micro`, `ease-ui` | static/color only | Use `WHATSAPP_NUMBER_PENDING` until final. |
| Nav Link | default/hover/focus/current/active | `duration-micro`, `ease-ui` | instant underline/color | Current state not color-only. |
| Mobile Menu | closed/opening/open/closing/focus | `duration-medium`, `ease-reveal` | instant/opacity only | Focus management later. |
| Language Toggle | AR active/EN active/hover/focus/disabled | `duration-micro`, `ease-ui` | instant state | Text labels, no flags-only. |
| Pillar Card | default/hover/focus/mobile | `duration-short`, `ease-ui` | border/opacity only | No hidden content on hover. |
| Workshop Card | default/hover/focus/modal/mobile/pending | `duration-short`, `ease-ui` | border/opacity only | CTAs always visible. |
| Mentor Card | default/hover/focus/placeholder/mobile | `duration-short`, `ease-ui` | border/opacity only | No fake mentor data. |
| Trust Block | default/verified/pending/hover-if-interactive | `duration-short`, `ease-ui` | static/border only | No fake proof or counters. |
| FAQ Item | closed/open/focus/active/reduced | `duration-medium`, `ease-reveal` | instant/opacity only | Semantic button later. |
| Form Input | default/focus/filled/error/success/disabled | `duration-micro`, `ease-ui` | immediate text/color | Visible labels, no color-only errors. |
| Form Submit | ready/submitting/error/success/disabled | `duration-short`, `ease-ui` | immediate text | Text status required. |
| Modal | trigger/opening/open/closing/focus/mobile | `duration-medium`, `ease-reveal` | instant/opacity only | Not canonical path; `/workshops/[slug]` remains canonical. |
| Floating CTA | default/hover/focus/active/mobile/hidden-if-overlap | `duration-micro`, `duration-short`, `ease-ui` | static visible | No pulse/shake; non-blocking. |
| Text Link | default/hover/focus/active/current | `duration-micro`, `ease-ui` | instant underline | Affordance not color-only. |
| Static Fallback Controls | same as DOM controls | same as component | same as reduced motion | No canvas dependency. |

---

## 28. QA Checklist

| Check | Pass Criteria | Status |
| --- | --- | --- |
| Buttons | All states defined. | PASS |
| CTAs | WhatsApp/Register states defined. | PASS |
| Focus | Every interactive element has visible focus spec. | PASS |
| Hover | No hover-only essential info. | PASS |
| Active | Pressed state defined. | PASS |
| Loading | Form submit/button loading defined. | PASS |
| Disabled | Disabled styling defined. | PASS |
| FAQ | Open/closed behavior defined. | PASS |
| Modal | Open/close/focus notes defined. | PASS |
| Mobile | Tap behavior defined. | PASS |
| Reduced motion | Alternative state defined. | PASS |
| RTL | Arabic interaction notes included. | PASS |
| Accessibility | P3.05-style requirements mapped. | PASS |
| Frontend | Handoff matrix complete. | PASS |
| Scope | No code implementation. | PASS |

---

## 29. Interaction Guardrails

| Keep | Avoid |
| --- | --- |
| Calm, restrained UI motion | Bounce/elastic/jiggle |
| Visible focus states | Hover-only polish |
| DOM-based CTAs | Canvas-only interaction |
| Tap-safe mobile states | Tiny hotspots |
| No hover-only content | Hidden essential info |
| Reduced-motion alternatives | Mandatory movement |
| WhatsApp label clarity | Icon-only primary CTA |
| Subtle card emphasis | 3D flip cards |
| Semantic FAQ behavior | Decorative inaccessible accordion |
| Low-pressure conversion | Pulsing urgency CTA |
| Arabic block/line motion | Arabic letter-by-letter animation |

---

## 30. Final Recommendation

Recommended micro-interaction direction:

**Restrained Legal Editorial Interactions**

Use short, predictable UI transitions for functional elements; reserve longer ceremonial reveal timing only for major hero/CTA handoff moments. Keep focus states strong, CTA states stable, Arabic motion block-based, mobile tap-first, and reduced-motion equivalent from the start.

Implementation posture for later phases:

1. Build DOM controls first, then layer visual polish.
2. Create focus states before hover refinements.
3. Keep WhatsApp and Register CTAs visible without animation.
4. Use one shared motion-token set across buttons, cards, nav, FAQ, modal, and forms.
5. Validate Arabic labels at 320-390px before approving component states.
6. Treat Figma prototype states and frontend implementation as future work, not part of this ticket.

---

## 31. Acceptance Criteria

| Acceptance Criteria | Status |
| --- | --- |
| Micro-interaction spec document created | PASS |
| All button variants have states documented | PASS |
| CTA components have states documented | PASS |
| WhatsApp CTA states are documented | PASS |
| Navigation states are documented | PASS |
| Mobile menu states are documented | PASS |
| Language toggle states are documented | PASS |
| Card states are documented | PASS |
| Workshop card interactions are documented | PASS |
| Mentor card interactions are documented | PASS |
| Trust/proof block states are documented | PASS |
| FAQ accordion states are documented | PASS |
| Form input states are documented | PASS |
| Form loading/error/success states are documented | PASS |
| Modal/workshop preview states are documented | PASS |
| Floating CTA states are documented | PASS |
| Link/text-link states are documented | PASS |
| Static fallback interactions are documented | PASS |
| Reduced-motion behavior documented | PASS |
| Mobile/touch behavior documented | PASS |
| RTL/Arabic interaction rules documented | PASS |
| Accessibility interaction requirements mapped | PASS |
| Frontend handoff matrix complete | PASS |
| QA checklist included | PASS |
| Interaction guardrails included | PASS |
| No frontend implementation started | PASS |
| No production CSS/React written | PASS |
| No GSAP/Lenis/R3F implementation started | PASS |
| No new roadmap tickets created | PASS |

---

## 32. Final Status

**PASS WITH CONDITIONS - P4.04 complete. All interactive UI elements have hover, focus, active, loading/disabled/open states, transition timing/easing, reduced-motion, mobile, RTL, accessibility, and frontend handoff notes.**

Conditions remaining:

- Final Figma prototype states are pending.
- Final frontend implementation is pending.
- Final CTA copy is pending.
- Final WhatsApp number is pending.
- Final workshop/mentor/proof content is pending.
- Accessibility QA is pending.
- RTL validation is pending.
- Reduced-motion QA is pending.
- Stakeholder approval is pending.
