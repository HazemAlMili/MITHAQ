# Mithaq Accessibility Requirements Specification

**Official Ticket ID:** P3.05  
**Official Ticket Name:** Accessibility Requirements Specification  
**Phase:** Phase 3 - UX / IA / Storyflow Planning  
**Owner:** Accessibility Lead / UX Strategist  
**Status:** PASS WITH CONDITIONS  
**Date:** 2026-06-19  
**Scope:** `/`, `/register`, `/workshops/[slug]`, 10-scene landing experience, WebGL/static fallback, bilingual Arabic/English UX

---

## 1. Executive Summary

This document defines Mithaq's accessibility requirements in a testable format before visual design or frontend implementation begins.

The specification converts the approved IA, storyflow, conversion funnel, mobile plan, color token findings, typography specimen, motion direction, device matrix, and 3D feasibility constraints into testable requirements with:

- Expected behavior
- Test method
- Pass criteria
- Fail criteria
- Priority
- Future validation phase
- Route/component/scene coverage

Accessibility position:

**Mithaq must be a DOM-first, keyboard-operable, screen-reader-understandable, reduced-motion-safe, WebGL-fallback-safe, bilingual/RTL-safe, mobile tap-safe experience. The cinematic 3D layer may enhance the experience, but it must never be required to read content, navigate, ask on WhatsApp, submit interest, or understand the Covenant Seal journey.**

Status is **PASS WITH CONDITIONS** because final compliance still depends on implementation, real content/assets, accessibility QA audits, screen reader testing, RTL validation, mobile device testing, and final legal/privacy review.

This task does not implement accessibility code, run final Axe/Lighthouse/screen reader audits, create UI comps, or claim WCAG compliance.

---

## 2. Current Mithaq Decisions

| Area | Current Decision |
| --- | --- |
| Product type | Premium bilingual 3D legal academy portfolio / landing experience. |
| Routes | `/`, `/register`, `/workshops/[slug]`. |
| Primary conversion | WhatsApp. |
| Secondary conversion | `/register` inquiry/register interest form. |
| Bilingual scope | Arabic/RTL and English/LTR are in scope. |
| Motion direction | Scroll-Led Ceremonial Restraint. |
| Reduced motion | Mandatory. |
| WebGL/static fallback | Mandatory. |
| DOM-first content | Mandatory. |
| Canvas rule | Canvas must never contain the only meaningful content. |
| Conversion rule | No conversion path should depend on 3D. |
| Mobile rule | 44px tap targets; mobile content/CTA before heavy 3D. |
| Color rule | Parchment/dim parchment safe on dark; white on gold fails; filled gold CTA needs near-black text. |
| Typography rule | DM Sans/Tajawal for readable UI; Tajawal 700 as safe Arabic display default; Lemonada accent-only pending review. |
| Content rule | No fake proof, fake urgency, fake seat counters, or unsupported claims. |
| Open blockers | WhatsApp number, final content/assets, privacy/legal wording, final QA. |

---

## 3. Accessibility Standard Baseline

| Area | Target |
| --- | --- |
| Standard | WCAG 2.2 AA unless project owner later chooses stricter standard. |
| Automated audit target | Zero critical violations later in QA. |
| Lighthouse accessibility target | >= 95 later in QA. |
| Keyboard navigation | Full operability. |
| Screen reader support | Semantic DOM and correct reading order. |
| Motion | Reduced-motion equivalent. |
| Color contrast | AA minimum. |
| Focus states | Visible and consistent. |
| Touch targets | Minimum 44px on mobile. |
| WebGL fallback | Equivalent content and conversion. |
| Bilingual/RTL | Semantic directionality and readable layout. |

Important:

This document defines requirements only. Axe, Lighthouse, keyboard QA, screen reader QA, reduced-motion QA, WebGL fallback QA, and device QA happen later in Phase 9 or implementation QA.

---

## 4. Requirement Format

Every requirement uses this testable format:

| Field | Required Answer |
| --- | --- |
| Requirement ID | Stable ID such as A11Y-001. |
| Requirement name | Short name. |
| Applies to | Route/component/scene. |
| Priority | P0/P1/P2. |
| Expected behavior | What should happen. |
| Test method | How it will be tested. |
| Pass criteria | Exact pass definition. |
| Fail criteria | Exact fail definition. |
| Future validation phase | Planned QA/implementation phase. |
| Notes | Context/constraints. |

---

## 5. Requirement Priority Levels

| Priority | Meaning |
| --- | --- |
| P0 | Must pass before launch. Blocks production if failed. |
| P1 | Should pass before launch. Requires documented exception if not fixed. |
| P2 | Nice-to-have enhancement or later improvement. |

Default rule:

If a requirement affects navigation, reading, conversion, forms, motion safety, fallback content, or bilingual access, it is P0.

---

## 6. Semantic Structure Requirements

### A11Y-001 - Semantic Page Structure

| Field | Requirement |
| --- | --- |
| Applies to | All routes. |
| Priority | P0 |
| Expected behavior | Each page uses semantic landmarks: header, main, nav, section, footer where appropriate. |
| Test method | Manual DOM inspection and screen reader landmark navigation. |
| Pass criteria | User can identify main regions and navigate page structure semantically. |
| Fail criteria | Page is mostly generic divs without meaningful landmarks. |
| Future validation phase | P9.02 / P9.03 |
| Notes | Applies to static fallback and WebGL-enhanced route. |

### A11Y-002 - Heading Hierarchy

| Field | Requirement |
| --- | --- |
| Applies to | `/`, `/register`, `/workshops/[slug]`. |
| Priority | P0 |
| Expected behavior | Each page has one logical H1; scene headings follow structured H2/H3 hierarchy. |
| Test method | Manual DOM inspection and accessibility tree review. |
| Pass criteria | Headings form a logical outline without skipped/confusing levels. |
| Fail criteria | Multiple unrelated H1s, missing H1, or headings used only for visual styling. |
| Future validation phase | P9.01 / P9.03 |
| Notes | Scene headings may be visually cinematic but must remain semantically clear. |

### A11Y-003 - Scene Sections Are Semantic

| Field | Requirement |
| --- | --- |
| Applies to | All 10 scenes on `/`. |
| Priority | P0 |
| Expected behavior | Each scene exists as semantic DOM content even if canvas is present. |
| Test method | Disable canvas/WebGL and inspect DOM. |
| Pass criteria | All scene messages are readable without 3D. |
| Fail criteria | A scene loses meaning because content exists only in canvas. |
| Future validation phase | P9.01 / P9.03 / P9.04 |
| Notes | Protects opening, workshop, FAQ, and final CTA meaning. |

### A11Y-004 - Main Content Target

| Field | Requirement |
| --- | --- |
| Applies to | All routes. |
| Priority | P0 |
| Expected behavior | Each page has a unique main content target for skip links and screen reader navigation. |
| Test method | Keyboard and DOM inspection. |
| Pass criteria | Skip link/focus can move directly to the main route content. |
| Fail criteria | No reliable main target exists. |
| Future validation phase | P9.02 / P9.03 |
| Notes | Especially important because the homepage has immersive opening content. |

---

## 7. Keyboard Navigation Requirements

### A11Y-010 - Full Keyboard Reachability

| Field | Requirement |
| --- | --- |
| Applies to | All interactive elements. |
| Priority | P0 |
| Expected behavior | User can reach every interactive element using keyboard only. |
| Test method | Manual Tab/Shift+Tab testing. |
| Pass criteria | Header links, mobile menu, CTAs, language toggle, FAQ, workshop cards, form fields, and footer links are reachable. |
| Fail criteria | Any essential CTA, nav item, or form field cannot be reached. |
| Future validation phase | P9.02 |
| Notes | Includes WhatsApp and workshop-specific CTAs. |

### A11Y-011 - No Keyboard Trap

| Field | Requirement |
| --- | --- |
| Applies to | Opening, scroll sections, mobile menu, overlays/previews, forms. |
| Priority | P0 |
| Expected behavior | Keyboard focus can always move forward/backward and escape overlays. |
| Test method | Manual keyboard testing. |
| Pass criteria | User can enter/exit menus, accordions, and pages without getting trapped. |
| Fail criteria | Focus becomes stuck in canvas, menu, modal, or scroll area. |
| Future validation phase | P9.02 |
| Notes | Avoid scroll-trapped cinematic intro behavior. |

### A11Y-012 - Skip to Content

| Field | Requirement |
| --- | --- |
| Applies to | All routes. |
| Priority | P0 |
| Expected behavior | Keyboard users can skip repeated navigation and move directly to main content. |
| Test method | Keyboard test from page load. |
| Pass criteria | Skip link appears on focus and moves focus to main content. |
| Fail criteria | User must tab through all nav/3D controls before content. |
| Future validation phase | P9.02 |
| Notes | Required before public launch. |

### A11Y-013 - Keyboard Activation Behavior

| Field | Requirement |
| --- | --- |
| Applies to | Buttons, links, FAQ controls, menu trigger, language toggle. |
| Priority | P0 |
| Expected behavior | Enter/Space activate controls according to native element behavior. |
| Test method | Manual keyboard activation test. |
| Pass criteria | Every interactive control activates predictably and announces state where relevant. |
| Fail criteria | Click-only behavior or custom controls ignore keyboard activation. |
| Future validation phase | P9.02 |
| Notes | Prefer native buttons/links during implementation. |

---

## 8. Focus Visibility Requirements

### A11Y-020 - Visible Focus States

| Field | Requirement |
| --- | --- |
| Applies to | All interactive elements. |
| Priority | P0 |
| Expected behavior | Focus state is clearly visible on dark backgrounds and gold elements. |
| Test method | Keyboard tab through all routes. |
| Pass criteria | Focus indicator is visible, high contrast, and not hidden by animation. |
| Fail criteria | Focus is invisible, low contrast, clipped, or only color-dependent. |
| Future validation phase | P9.02 / P9.01 |
| Notes | P2.02 recommends gold-light focus ring with minimum 2px visible outline. |

### A11Y-021 - Focus Order Matches Reading Order

| Field | Requirement |
| --- | --- |
| Applies to | All routes/scenes. |
| Priority | P0 |
| Expected behavior | Focus moves in a logical order matching DOM/reading flow. |
| Test method | Manual keyboard tab order test. |
| Pass criteria | Focus order follows page structure and user expectations. |
| Fail criteria | Focus jumps randomly due to visual animation order or canvas layering. |
| Future validation phase | P9.02 |
| Notes | Animation cannot define focus order. |

### A11Y-022 - Focus Not Obscured

| Field | Requirement |
| --- | --- |
| Applies to | Sticky header, mobile nav, CTAs, forms, FAQ. |
| Priority | P0 |
| Expected behavior | Focused element is not hidden behind fixed UI or clipped by overflow. |
| Test method | Keyboard test on desktop and mobile widths. |
| Pass criteria | Focused item remains visible enough for the user to operate it. |
| Fail criteria | Sticky header, canvas, or scroll container hides the focused element. |
| Future validation phase | P9.02 / P9.08 |
| Notes | Especially important for mobile menu and long scroll scenes. |

---

## 9. Screen Reader Requirements

### A11Y-030 - Meaningful Screen Reader Reading Order

| Field | Requirement |
| --- | --- |
| Applies to | All routes. |
| Priority | P0 |
| Expected behavior | Screen reader reads content in logical order independent of animation sequence. |
| Test method | VoiceOver + NVDA later. |
| Pass criteria | User can understand page purpose, sections, CTAs, form, FAQ, and workshop details. |
| Fail criteria | Screen reader reads decorative/canvas noise or misses essential content. |
| Future validation phase | P9.03 |
| Notes | DOM order should match intended narrative order. |

### A11Y-031 - Decorative 3D Hidden From Screen Readers

| Field | Requirement |
| --- | --- |
| Applies to | R3F canvas / visual-only 3D elements. |
| Priority | P0 |
| Expected behavior | Decorative 3D elements do not clutter the accessibility tree. |
| Test method | Accessibility tree inspection and screen reader testing. |
| Pass criteria | Canvas has appropriate label or is hidden when decorative; DOM carries meaning. |
| Fail criteria | Screen reader announces meaningless canvas internals or misses content. |
| Future validation phase | P9.03 |
| Notes | The Seal and gavel may be symbolically meaningful, but their meaning must be described in DOM content. |

### A11Y-032 - Essential Meaning Has Text Alternative

| Field | Requirement |
| --- | --- |
| Applies to | 3D scenes, static posters, images. |
| Priority | P0 |
| Expected behavior | Any meaningful visual has text equivalent in DOM. |
| Test method | Disable images/canvas and screen reader review. |
| Pass criteria | User can understand the same scene message without visuals. |
| Fail criteria | Visual metaphor is required to understand content. |
| Future validation phase | P9.03 / P9.04 |
| Notes | Applies to Covenant Seal, gap documents, method ordering, and final CTA. |

### A11Y-033 - Live Regions Are Limited

| Field | Requirement |
| --- | --- |
| Applies to | Form success/error, loading/fallback state, language switch. |
| Priority | P1 |
| Expected behavior | Only meaningful dynamic state changes are announced. |
| Test method | Screen reader dynamic state test. |
| Pass criteria | User hears useful updates without repeated noisy announcements. |
| Fail criteria | Motion, canvas, or repeated UI changes spam announcements. |
| Future validation phase | P9.03 / implementation QA |
| Notes | Avoid announcing decorative scroll animation changes. |

---

## 10. Color Contrast Requirements

### A11Y-040 - Text Contrast AA

| Field | Requirement |
| --- | --- |
| Applies to | All text. |
| Priority | P0 |
| Expected behavior | Normal text meets WCAG AA contrast on all approved backgrounds. |
| Test method | Contrast calculation and visual review. |
| Pass criteria | Normal text contrast >= 4.5:1; large text >= 3:1. |
| Fail criteria | Any body, form, FAQ, CTA, or nav text fails contrast. |
| Future validation phase | P9.01 / P9.05 |
| Notes | Parchment and parchment-dim are safe on primary dark backgrounds per P2.02. |

### A11Y-041 - Gold CTA Contrast Safety

| Field | Requirement |
| --- | --- |
| Applies to | Filled gold CTAs. |
| Priority | P0 |
| Expected behavior | Filled gold CTA uses near-black/void text, not white. |
| Test method | Contrast calculation and visual inspection. |
| Pass criteria | CTA label contrast meets AA and follows token rule. |
| Fail criteria | White text or low-contrast text is used on gold. |
| Future validation phase | P9.01 / P9.05 |
| Notes | P2.02 found white on seal-gold fails; near-black passes. |

### A11Y-042 - Restricted Color Usage

| Field | Requirement |
| --- | --- |
| Applies to | Labels, body text, status, accent text. |
| Priority | P0 |
| Expected behavior | `gold-dim` is decorative only; red is not used as body text on dark backgrounds. |
| Test method | Visual review and token/code inspection. |
| Pass criteria | Restricted colors are not used for critical text or sole status signal. |
| Fail criteria | Gold-dim or red text carries essential meaning and fails contrast. |
| Future validation phase | P9.01 / P9.05 |
| Notes | Error states should use parchment text plus icon/border, not red text alone. |

### A11Y-043 - Focus Contrast

| Field | Requirement |
| --- | --- |
| Applies to | Focus rings on all backgrounds. |
| Priority | P0 |
| Expected behavior | Focus indicators maintain visible contrast on dark, parchment, gold, and image/poster surfaces. |
| Test method | Keyboard visual inspection and contrast check where applicable. |
| Pass criteria | Focus is visible against every component background. |
| Fail criteria | Focus disappears on gold, dark canvas, or image surfaces. |
| Future validation phase | P9.01 / P9.02 |
| Notes | Use a consistent focus treatment; do not rely on subtle glow only. |

---

## 11. Typography / Readability Requirements

### A11Y-050 - Minimum Body Readability

| Field | Requirement |
| --- | --- |
| Applies to | Body text, cards, FAQ, forms, workshop detail. |
| Priority | P0 |
| Expected behavior | English body text uses readable size/line-height; Arabic uses larger line-height where needed. |
| Test method | Visual review at desktop/mobile widths and typography token inspection. |
| Pass criteria | English body is at least 16px; Arabic body is at least 16px with comfortable line-height. |
| Fail criteria | Body text is cramped, tiny, clipped, or hard to scan. |
| Future validation phase | P9.05 / P9.08 |
| Notes | P2.03 recommends Arabic body line-height around 1.75-1.85. |

### A11Y-051 - Arabic Display Readability

| Field | Requirement |
| --- | --- |
| Applies to | Arabic headings, CTAs, scene titles. |
| Priority | P0 |
| Expected behavior | Arabic headings default to Tajawal 700 unless accent use is approved. |
| Test method | Arabic visual review and typography inspection. |
| Pass criteria | Arabic headings are readable, mature, and not decorative-only. |
| Fail criteria | Lemonada or decorative treatment harms legal seriousness/readability. |
| Future validation phase | P8.18 / P9.08 |
| Notes | Lemonada remains accent-only pending review. |

### A11Y-052 - No Text In Critical Images

| Field | Requirement |
| --- | --- |
| Applies to | Static posters, 3D textures, workshop visuals, Seal visuals. |
| Priority | P0 |
| Expected behavior | Critical text exists in DOM, not only inside images/canvas/textures. |
| Test method | Disable images/canvas and inspect DOM. |
| Pass criteria | All meaningful copy remains available as selectable/readable DOM text. |
| Fail criteria | User loses content because it is baked into a poster or 3D material. |
| Future validation phase | P9.03 / P9.04 |
| Notes | Seal artwork may be visual; meaningful wording still needs DOM equivalent. |

---

## 12. Motion / Reduced Motion Requirements

### A11Y-060 - Reduced Motion Respected

| Field | Requirement |
| --- | --- |
| Applies to | All motion, scroll animation, 3D camera, particles, text reveals. |
| Priority | P0 |
| Expected behavior | `prefers-reduced-motion: reduce` receives static/fade equivalents and no mandatory camera movement. |
| Test method | Enable OS/browser reduced motion and inspect experience. |
| Pass criteria | Content and CTAs remain complete; motion is removed or minimized. |
| Fail criteria | User still receives required camera movement, parallax, or prolonged animation. |
| Future validation phase | P9.04 |
| Notes | Reduced motion is a first-class experience. |

### A11Y-061 - Motion Not Required For Meaning

| Field | Requirement |
| --- | --- |
| Applies to | All scenes and transitions. |
| Priority | P0 |
| Expected behavior | User can understand story and content without watching animation. |
| Test method | Force reduced/static mode and compare against standard narrative. |
| Pass criteria | Same narrative meaning and CTA opportunities remain. |
| Fail criteria | Important meaning only appears during animation. |
| Future validation phase | P9.04 / P9.07 |
| Notes | Applies to gavel trigger, Seal reveal, document alignment, and final CTA. |

### A11Y-062 - No Harmful Motion Patterns

| Field | Requirement |
| --- | --- |
| Applies to | GSAP/ScrollTrigger/R3F motion later. |
| Priority | P0 |
| Expected behavior | Avoid bounce, elastic, fast flythrough, excessive parallax, violent gavel smash, and pulsing CTA. |
| Test method | Motion review and reduced-motion comparison. |
| Pass criteria | Motion remains slow, controlled, readable, and non-essential. |
| Fail criteria | Motion causes disorientation, hides content, or pressures conversion. |
| Future validation phase | P9.04 |
| Notes | From P2.07 motion guardrails. |

---

## 13. WebGL / Canvas Accessibility Requirements

### A11Y-070 - Canvas Is Enhancement Only

| Field | Requirement |
| --- | --- |
| Applies to | WebGL/R3F canvas on `/`. |
| Priority | P0 |
| Expected behavior | Canvas enhances the scene but does not own the only content, CTA, or interaction path. |
| Test method | Disable WebGL and compare DOM journey. |
| Pass criteria | User can read all sections and convert without canvas. |
| Fail criteria | Blank/failed canvas blocks story or conversion. |
| Future validation phase | P9.04 / P9.07 |
| Notes | Required by IA, storyflow, mobile, and 3D feasibility docs. |

### A11Y-071 - Canvas Load Failure Safe

| Field | Requirement |
| --- | --- |
| Applies to | Scene 01-02 and any later 3D scene. |
| Priority | P0 |
| Expected behavior | Failed GLB/shader/WebGL load presents static fallback and DOM content. |
| Test method | Force asset failure/no-WebGL mode. |
| Pass criteria | No blocking spinner; CTA and content remain usable. |
| Fail criteria | Loader blocks content or route appears broken. |
| Future validation phase | P9.07 / P9.08 |
| Notes | CTA must never be hidden behind 3D loader. |

### A11Y-072 - No Essential Canvas Hotspots

| Field | Requirement |
| --- | --- |
| Applies to | Workshop cards, Seal/gavel, documents, CTAs. |
| Priority | P0 |
| Expected behavior | Essential interactions use DOM controls, not only raycaster/canvas hotspots. |
| Test method | Keyboard and no-WebGL test. |
| Pass criteria | CTAs and workshop actions work without canvas interaction. |
| Fail criteria | User must click/tap 3D object to convert or navigate. |
| Future validation phase | P9.02 / P9.07 |
| Notes | Workshop cards are DOM-first. |

---

## 14. Mobile / Touch Accessibility Requirements

### A11Y-080 - Minimum Touch Targets

| Field | Requirement |
| --- | --- |
| Applies to | Mobile CTAs, nav, menu, FAQ, language toggle, form controls. |
| Priority | P0 |
| Expected behavior | Touch targets are at least 44px in usable size. |
| Test method | Mobile layout inspection at 320/375/390/430/768px. |
| Pass criteria | All essential controls meet or exceed 44px target. |
| Fail criteria | Small/tiny controls cause tap errors. |
| Future validation phase | P9.08 |
| Notes | Especially important for WhatsApp and workshop CTAs. |

### A11Y-081 - No Hover-Only Mobile Interaction

| Field | Requirement |
| --- | --- |
| Applies to | Workshop cards, mentor cards, nav, CTAs, FAQ. |
| Priority | P0 |
| Expected behavior | Mobile users can access all content/actions without hover. |
| Test method | Touch-only mobile QA. |
| Pass criteria | All details and CTAs are available through tap or visible content. |
| Fail criteria | Content appears only on hover or pointer movement. |
| Future validation phase | P9.08 |
| Notes | Applies to workshop detail previews. |

### A11Y-082 - No Mobile Scroll Trap

| Field | Requirement |
| --- | --- |
| Applies to | Opening sequence, scroll-driven scenes, pinned sections. |
| Priority | P0 |
| Expected behavior | Mobile users can scroll naturally and are not trapped in long pinned animation. |
| Test method | Mobile scroll QA on target widths/devices. |
| Pass criteria | User can progress smoothly and reach CTAs without forced choreography. |
| Fail criteria | User feels stuck or cannot bypass animation. |
| Future validation phase | P9.08 / P9.04 |
| Notes | P3.04 requires short/no pinned mobile sections. |

---

## 15. Navigation Accessibility Requirements

### A11Y-090 - Semantic Navigation

| Field | Requirement |
| --- | --- |
| Applies to | Header nav, footer nav, mobile menu. |
| Priority | P0 |
| Expected behavior | Navigation uses semantic nav structure and real links/buttons. |
| Test method | DOM inspection and keyboard/screen reader testing. |
| Pass criteria | Users can understand and operate navigation semantically. |
| Fail criteria | Navigation is built from inaccessible clickable divs or canvas controls. |
| Future validation phase | P9.02 / P9.03 |
| Notes | Minimal premium nav still needs accessibility. |

### A11Y-091 - Mobile Menu Operability

| Field | Requirement |
| --- | --- |
| Applies to | Mobile header/menu. |
| Priority | P0 |
| Expected behavior | Mobile menu opens/closes by keyboard and touch, announces state, and restores focus appropriately. |
| Test method | Keyboard, touch, and screen reader QA. |
| Pass criteria | Menu state is clear and focus behavior is predictable. |
| Fail criteria | Menu traps focus, cannot close, or hides current page content unpredictably. |
| Future validation phase | P9.02 / P9.03 / P9.08 |
| Notes | No mega-menu required. |

### A11Y-092 - Language Toggle Accessibility

| Field | Requirement |
| --- | --- |
| Applies to | Header/mobile nav/footer language toggle. |
| Priority | P0 |
| Expected behavior | Toggle identifies current language and target language clearly. |
| Test method | Keyboard and screen reader QA in Arabic/English. |
| Pass criteria | User understands active locale and can switch language. |
| Fail criteria | Toggle is ambiguous, hidden, or inaccessible. |
| Future validation phase | P9.03 / P9.08 |
| Notes | Must work in RTL and LTR. |

---

## 16. CTA / WhatsApp Accessibility Requirements

### A11Y-100 - WhatsApp CTA Accessible

| Field | Requirement |
| --- | --- |
| Applies to | Header, floating CTA, hero, workshops, FAQ, final CTA, `/register`, `/workshops/[slug]`. |
| Priority | P0 |
| Expected behavior | WhatsApp CTA is a real link/button with clear accessible label. |
| Test method | Keyboard, screen reader, mobile tap QA. |
| Pass criteria | User can find, understand, and activate WhatsApp CTA without WebGL. |
| Fail criteria | CTA is icon-only without label, canvas-only, hidden, or unreachable. |
| Future validation phase | P9.02 / P9.03 / P9.08 |
| Notes | Uses `WHATSAPP_NUMBER_PENDING` until final number is confirmed. |

### A11Y-101 - CTA Meaning Clear

| Field | Requirement |
| --- | --- |
| Applies to | All CTAs. |
| Priority | P0 |
| Expected behavior | CTA label communicates action: contact, register interest, ask about workshop, view details. |
| Test method | Content review and screen reader review. |
| Pass criteria | User understands destination/action before activation. |
| Fail criteria | Vague labels like "click here" or unlabeled icon-only buttons. |
| Future validation phase | P8 content QA / P9.03 |
| Notes | Labels are candidates until final copy approval. |

### A11Y-102 - CTA Does Not Depend On Motion

| Field | Requirement |
| --- | --- |
| Applies to | Opening, hero, workshops, FAQ, final CTA. |
| Priority | P0 |
| Expected behavior | CTA remains available without waiting for animation or canvas load. |
| Test method | Reduced-motion/no-WebGL/load-failure test. |
| Pass criteria | CTA is visible/reachable in standard and fallback experiences. |
| Fail criteria | CTA appears only after successful 3D animation. |
| Future validation phase | P9.04 / P9.07 |
| Notes | Conversion never disappears. |

---

## 17. Form Accessibility Requirements

### A11Y-110 - Form Labels

| Field | Requirement |
| --- | --- |
| Applies to | `/register` form. |
| Priority | P0 |
| Expected behavior | Every input has a persistent programmatic label. |
| Test method | DOM inspection, keyboard, screen reader QA. |
| Pass criteria | Name, phone/WhatsApp, email, interest, language, message labels are announced correctly. |
| Fail criteria | Placeholder-only labels or unlabeled controls. |
| Future validation phase | P9.02 / P9.03 |
| Notes | Required fields: name and phone/WhatsApp only. |

### A11Y-111 - Form Errors

| Field | Requirement |
| --- | --- |
| Applies to | `/register` form. |
| Priority | P0 |
| Expected behavior | Errors are clear, inline, associated with fields, and not color-only. |
| Test method | Manual form validation and screen reader QA. |
| Pass criteria | User can identify which field failed and how to fix it. |
| Fail criteria | Error is only red color, generic, or not announced. |
| Future validation phase | P9.03 / implementation QA |
| Notes | Red text on dark is restricted; use accessible error pattern. |

### A11Y-112 - Form Success State

| Field | Requirement |
| --- | --- |
| Applies to | `/register` form. |
| Priority | P0 |
| Expected behavior | Successful submission gives clear confirmation and next step. |
| Test method | Form QA and screen reader live-region review. |
| Pass criteria | User knows submission succeeded and can still access WhatsApp. |
| Fail criteria | No confirmation, silent submit, or user stranded. |
| Future validation phase | P9.03 / implementation QA |
| Notes | Inline success is acceptable; `/thank-you` is optional/deferred. |

### A11Y-113 - Privacy Notice Before Data Collection

| Field | Requirement |
| --- | --- |
| Applies to | `/register`. |
| Priority | P0 before public launch |
| Expected behavior | Form includes clear privacy/data-use note before collecting real user data. |
| Test method | Content/legal review. |
| Pass criteria | User understands what happens to submitted data. |
| Fail criteria | Data collected without clear notice. |
| Future validation phase | P10 pre-launch / legal review |
| Notes | Final privacy/legal wording is still pending. |

---

## 18. FAQ / Accordion Accessibility Requirements

### A11Y-120 - Semantic FAQ Accordion

| Field | Requirement |
| --- | --- |
| Applies to | Scene 09 FAQ and workshop FAQ. |
| Priority | P0 |
| Expected behavior | FAQ uses semantic accessible accordion controls. |
| Test method | Keyboard and screen reader QA. |
| Pass criteria | Questions are reachable, expandable/collapsible, and state is announced. |
| Fail criteria | FAQ is click-only, inaccessible, or visual-only. |
| Future validation phase | P9.02 / P9.03 |
| Notes | Native disclosure patterns may be acceptable if designed well. |

### A11Y-121 - FAQ Content Readable Without Animation

| Field | Requirement |
| --- | --- |
| Applies to | FAQ sections. |
| Priority | P0 |
| Expected behavior | FAQ answers remain readable in reduced-motion and static modes. |
| Test method | Reduced-motion and keyboard test. |
| Pass criteria | FAQ can be opened/read without animated dependency. |
| Fail criteria | Animation hides, clips, or delays FAQ content. |
| Future validation phase | P9.04 |
| Notes | Mobile can use instant/native accordion. |

---

## 19. Workshop Accessibility Requirements

### A11Y-130 - Workshop Cards Accessible

| Field | Requirement |
| --- | --- |
| Applies to | Scene 06 workshop cards. |
| Priority | P0 |
| Expected behavior | Workshop cards expose title, level, skill bullets, detail link, and WhatsApp CTA in DOM. |
| Test method | Keyboard, screen reader, no-WebGL QA. |
| Pass criteria | User can understand and act on each workshop without canvas interaction. |
| Fail criteria | Card details or CTAs are hidden behind hover/3D/raycaster only. |
| Future validation phase | P9.02 / P9.03 / P9.07 |
| Notes | No LMS/dashboard/course catalog behavior. |

### A11Y-131 - Workshop Detail Page Semantic

| Field | Requirement |
| --- | --- |
| Applies to | `/workshops/[slug]`. |
| Priority | P0 |
| Expected behavior | Detail page uses semantic sections for overview, skills, format, mentor, FAQ, and CTA. |
| Test method | DOM inspection and screen reader review. |
| Pass criteria | User can understand workshop content and reach Ask About This Workshop CTA. |
| Fail criteria | Page relies on visual cards only or lacks clear structure. |
| Future validation phase | P9.03 |
| Notes | Placeholder content should be clearly non-final if used internally. |

### A11Y-132 - No Fake Proof Or Urgency

| Field | Requirement |
| --- | --- |
| Applies to | Workshop cards, trust section, CTAs, detail pages. |
| Priority | P0 |
| Expected behavior | No fake seat counts, countdowns, testimonials, stats, pricing, dates, or urgency claims. |
| Test method | Content review. |
| Pass criteria | All proof/urgency claims are verified or absent. |
| Fail criteria | Unsupported claims pressure user into action. |
| Future validation phase | P8 content QA / P10 legal review |
| Notes | Accessibility includes cognitive trust and non-deceptive UX. |

---

## 20. Bilingual / RTL Accessibility Requirements

### A11Y-140 - Semantic Directionality

| Field | Requirement |
| --- | --- |
| Applies to | Arabic and English routes. |
| Priority | P0 |
| Expected behavior | Arabic pages/elements use `dir="rtl"`; English uses `dir="ltr"`. |
| Test method | DOM inspection, screen reader, visual RTL test. |
| Pass criteria | Directionality is semantic and layout reads naturally. |
| Fail criteria | Direction simulated visually only or broken reading order. |
| Future validation phase | P9.03 / P9.08 |
| Notes | Route strategy remains pending, but directionality requirement is fixed. |

### A11Y-141 - CSS Logical Layout

| Field | Requirement |
| --- | --- |
| Applies to | Bilingual layouts. |
| Priority | P0 |
| Expected behavior | Layout uses logical spacing/flow suitable for RTL/LTR. |
| Test method | Visual and code inspection later. |
| Pass criteria | Arabic and English layouts mirror/adapt without broken alignment. |
| Fail criteria | Hardcoded left/right causes broken RTL. |
| Future validation phase | P9.08 / P8.18 QA |
| Notes | Especially important for cards, nav, forms, and CTAs. |

### A11Y-142 - Arabic Motion Safety

| Field | Requirement |
| --- | --- |
| Applies to | Arabic headings/body/CTA. |
| Priority | P0 |
| Expected behavior | Arabic text is not animated letter-by-letter and remains readable. |
| Test method | Visual/motion review. |
| Pass criteria | Arabic uses line/block/fade reveals only. |
| Fail criteria | Arabic split-letter animation breaks readability. |
| Future validation phase | P9.04 / P9.08 |
| Notes | From P2.07 motion rules. |

### A11Y-143 - Arabic Mobile Wrapping

| Field | Requirement |
| --- | --- |
| Applies to | Arabic mobile layouts at 320-430px. |
| Priority | P0 |
| Expected behavior | Arabic headings, cards, FAQ, CTA, and form labels wrap without clipping/overflow. |
| Test method | Mobile visual QA at 320/375/390/430px. |
| Pass criteria | No horizontal overflow or clipped Arabic text. |
| Fail criteria | Arabic content is cramped, clipped, or visually secondary. |
| Future validation phase | P9.08 / Arabic review |
| Notes | Arabic must not be treated as an afterthought. |

---

## 21. Images / Media / Sound Requirements

### A11Y-150 - Image Alt Text

| Field | Requirement |
| --- | --- |
| Applies to | Mentor portraits, workshop images, static fallback posters. |
| Priority | P0 |
| Expected behavior | Informative images have useful alt text; decorative images are empty/hidden. |
| Test method | Screen reader and DOM inspection. |
| Pass criteria | Screen reader receives helpful image context without clutter. |
| Fail criteria | Missing alt text on meaningful images or noisy decorative descriptions. |
| Future validation phase | P9.03 |
| Notes | Do not invent mentor details in alt text. |

### A11Y-151 - Sound Is Optional

| Field | Requirement |
| --- | --- |
| Applies to | Opening sound, gavel sound, UI sounds. |
| Priority | P0 |
| Expected behavior | Sound is muted/off by default or user-controlled; no meaning depends on sound. |
| Test method | Browser audio behavior and accessibility review. |
| Pass criteria | Site works silently and user can control sound. |
| Fail criteria | Autoplay sound, no mute, or sound required to understand state. |
| Future validation phase | P9.04 / P9.08 |
| Notes | iOS restrictions require user-initiated audio if audio is ever added. |

### A11Y-152 - Media Does Not Block Content

| Field | Requirement |
| --- | --- |
| Applies to | Images, posters, canvas, media assets. |
| Priority | P0 |
| Expected behavior | Failed media does not prevent reading or conversion. |
| Test method | Asset failure test. |
| Pass criteria | DOM content and CTAs remain visible and usable. |
| Fail criteria | Missing asset leaves blank critical area or broken conversion path. |
| Future validation phase | P9.07 |
| Notes | Applies to final logo, Seal poster, and mentor/workshop imagery. |

---

## 22. Static Fallback Accessibility Requirements

### A11Y-160 - Static Fallback Full Equivalence

| Field | Requirement |
| --- | --- |
| Applies to | WebGL fallback, reduced-motion path. |
| Priority | P0 |
| Expected behavior | Static fallback contains same content hierarchy, CTAs, workshops, FAQ, and conversion path. |
| Test method | Force fallback and compare against standard route. |
| Pass criteria | User can complete same information/conversion journey. |
| Fail criteria | Fallback is incomplete, broken, or missing CTA. |
| Future validation phase | P9.04 / P9.07 / P9.08 |
| Notes | Fallback is a complete editorial experience. |

### A11Y-161 - Fallback Is Premium, Not Broken

| Field | Requirement |
| --- | --- |
| Applies to | WebGL/reduced-motion fallback. |
| Priority | P1 |
| Expected behavior | Fallback feels intentionally designed and trustworthy. |
| Test method | Visual review. |
| Pass criteria | Fallback reads as a complete premium editorial page. |
| Fail criteria | Fallback looks like an error state or degraded leftover. |
| Future validation phase | P4.05 / P9.08 |
| Notes | Static can still be premium. |

---

## 23. Analytics / Privacy Accessibility Notes

### A11Y-170 - Tracking Does Not Block Access

| Field | Requirement |
| --- | --- |
| Applies to | Analytics events, conversion events. |
| Priority | P0 |
| Expected behavior | Analytics failure must not block CTAs, forms, navigation, or content. |
| Test method | Later implementation test with analytics blocked. |
| Pass criteria | Site works if analytics fails or is blocked. |
| Fail criteria | CTA/form depends on tracking script. |
| Future validation phase | P9.07 / implementation QA |
| Notes | Analytics event planning exists, but no code is implemented now. |

### A11Y-171 - Data Collection Notice

| Field | Requirement |
| --- | --- |
| Applies to | `/register`, any lead capture. |
| Priority | P0 before public launch |
| Expected behavior | Users receive clear notice before submitting personal data. |
| Test method | Content/legal review. |
| Pass criteria | Notice is readable and linked/placed near form submission. |
| Fail criteria | Form collects data without data-use guidance. |
| Future validation phase | P10 pre-launch / legal review |
| Notes | Privacy/legal wording remains a project blocker. |

---

## 24. Accessibility QA Matrix

| Category | Representative Requirement IDs | Test Method | Future Phase | Launch Blocking? |
| --- | --- | --- | --- | --- |
| Semantic structure | A11Y-001 to A11Y-004 | DOM inspection, screen reader landmarks. | P9.01 / P9.03 | Yes |
| Keyboard navigation | A11Y-010 to A11Y-013 | Manual keyboard QA. | P9.02 | Yes |
| Focus visibility | A11Y-020 to A11Y-022 | Keyboard visual QA. | P9.02 | Yes |
| Screen reader behavior | A11Y-030 to A11Y-033 | VoiceOver/NVDA. | P9.03 | Yes for P0 |
| Color contrast | A11Y-040 to A11Y-043 | Contrast tools, visual QA. | P9.01 / P9.05 | Yes |
| Typography/readability | A11Y-050 to A11Y-052 | Visual QA, token inspection. | P9.05 / P9.08 | Yes for P0 |
| Motion/reduced motion | A11Y-060 to A11Y-062 | OS setting, visual review. | P9.04 | Yes |
| WebGL/canvas | A11Y-070 to A11Y-072 | Forced no-WebGL/failure mode. | P9.07 | Yes |
| Mobile/touch | A11Y-080 to A11Y-082 | Device/browser QA. | P9.08 | Yes |
| Navigation/menu | A11Y-090 to A11Y-092 | Keyboard, screen reader, touch. | P9.02 / P9.03 / P9.08 | Yes |
| CTA/WhatsApp | A11Y-100 to A11Y-102 | Keyboard, screen reader, fallback. | P9.02 / P9.07 | Yes |
| Forms | A11Y-110 to A11Y-113 | Manual form and legal review. | P9 / P10 | Yes |
| FAQ | A11Y-120 to A11Y-121 | Keyboard and screen reader QA. | P9.02 / P9.03 | Yes |
| Workshops | A11Y-130 to A11Y-132 | DOM, keyboard, content review. | P9 / P10 | Yes |
| Bilingual/RTL | A11Y-140 to A11Y-143 | RTL visual/screen reader/mobile review. | P8.18 / P9.08 | Yes |
| Media/sound | A11Y-150 to A11Y-152 | Screen reader/media failure/audio review. | P9.03 / P9.07 | Yes for P0 |
| Static fallback | A11Y-160 to A11Y-161 | Forced fallback comparison. | P9.04 / P9.07 | Yes for A11Y-160 |
| Analytics/privacy | A11Y-170 to A11Y-171 | Blocked analytics/legal review. | P9.07 / P10 | Yes |

---

## 25. Scene-Level Accessibility Matrix

| Scene | Main Accessibility Risk | Required Mitigation | Priority |
| --- | --- | --- | --- |
| Scene 01 | Heavy motion / canvas-only meaning. | Reduced motion + DOM brand/CTA. | P0 |
| Scene 02 | Canvas blocking hero content. | DOM-first headline/CTA. | P0 |
| Scene 03 | Visual documents carrying meaning. | Text problem statement in DOM. | P0 |
| Scene 04 | Method morph needed to understand. | Static method list in DOM. | P0 |
| Scene 05 | Cards too small / hover-only. | DOM pillar cards and tap-safe CTAs. | P0 |
| Scene 06 | Workshop cards rely on 3D/raycaster. | DOM cards + keyboard CTAs. | P0 |
| Scene 07 | Fake/unclear portraits. | Confirmed alt text and safe placeholder labels. | P0 |
| Scene 08 | Fake proof/stat counters. | Verified proof only; semantic text. | P0 |
| Scene 09 | Accordion operability. | Semantic accessible FAQ. | P0 |
| Scene 10 | CTA hidden by animation. | CTA visible in DOM and fallback. | P0 |

---

## 26. Route-Level Accessibility Matrix

| Route | Key Requirements | Priority |
| --- | --- | --- |
| `/` | Semantic 10-section DOM, canvas enhancement, reduced motion, WebGL fallback, accessible CTAs. | P0 |
| `/register` | Accessible form labels/errors/success, privacy note, WhatsApp alternative. | P0 |
| `/workshops/[slug]` | Semantic content, accessible workshop CTA, FAQ, no LMS-only interaction. | P0 |
| Optional `/privacy` | Readable legal/privacy text. | P1/P0 before live data collection. |
| Optional `/about` | Semantic editorial content. | P2 |
| Optional `/instructors` | Accessible mentor cards/portraits. | P2 |

---

## 27. Tool / Test Method Matrix

| Test Type | Tool / Method | Future Phase |
| --- | --- | --- |
| Automated accessibility | Axe DevTools or equivalent. | P9.01 |
| Keyboard QA | Manual Tab/Shift+Tab/Enter/Escape. | P9.02 |
| Screen reader QA | VoiceOver Safari/macOS + NVDA Windows/Chrome. | P9.03 |
| Reduced motion QA | OS setting + browser inspection. | P9.04 |
| Lighthouse accessibility | Lighthouse CI/manual Lighthouse. | P9.05 |
| Mobile device QA | Physical devices / BrowserStack. | P9.08 |
| Contrast validation | Contrast tool / computed CSS values. | P9.01 |
| RTL validation | Arabic layout review + native reader if possible. | P8.18 / P9.08 |
| WebGL fallback | Forced no-WebGL mode / browser setting / asset failure. | P9.07 / P9.08 |
| Form QA | Manual form validation. | Implementation QA / P9 |

No final audit is claimed in this document.

---

## 28. Accessibility Blocker Rules

### P0 Launch Blockers

The site must not launch if any of these fail:

- Missing semantic page structure.
- Essential content exists only in canvas.
- Keyboard trap.
- Invisible focus state.
- Primary CTA unreachable by keyboard.
- WhatsApp CTA inaccessible.
- Form inputs unlabeled.
- Form collects data without privacy/data-use notice.
- Reduced motion not respected.
- WebGL/static fallback missing or broken.
- Critical contrast failure.
- Mobile CTAs below usability threshold.
- Arabic RTL layout unreadable.
- FAQ inaccessible.
- Screen reader cannot understand page purpose.
- Static fallback missing core conversion path.
- Analytics failure blocks access.
- Sound autoplays or is required for meaning.

---

## 29. Accessibility Guardrail Table

| Keep | Avoid |
| --- | --- |
| Semantic DOM-first content. | Canvas-only meaning. |
| Keyboard-reachable CTAs. | Mouse/3D-only interactions. |
| Visible focus states. | Hidden or low-contrast focus. |
| Reduced-motion static/fade path. | Mandatory camera movement. |
| WebGL fallback with full content. | Blank canvas or broken fallback. |
| Accessible WhatsApp CTA labels. | Icon-only buttons. |
| Labeled form inputs. | Placeholder-only forms. |
| Semantic FAQ accordion. | Decorative inaccessible accordion. |
| Arabic `dir="rtl"` and readable layout. | Visual-only RTL hacks. |
| Sound as optional enhancement. | Sound required for meaning. |

---

## 30. Final Accessibility Recommendation

| Decision Area | Recommendation |
| --- | --- |
| Accessibility baseline | WCAG 2.2 AA target. |
| Launch-blocking priority | Navigation, reading, conversion, forms, motion safety, fallback, and RTL are P0. |
| 3D/canvas stance | Canvas is enhancement only; DOM owns meaning and conversion. |
| Reduced-motion stance | Static/fade equivalent required for every scene. |
| Mobile stance | 44px targets, no hover-only interaction, no scroll trap. |
| WhatsApp stance | Always keyboard/touch/screen-reader reachable; no canvas-only CTA. |
| Form stance | Persistent labels, accessible errors/success, privacy note before public launch. |
| Arabic/RTL stance | Semantic `dir`, logical layout, no letter-by-letter Arabic animation. |
| QA stance | Final compliance depends on Phase 9 audits and device/screen reader validation. |

Final recommendation:

**Proceed with WCAG 2.2 AA as the project accessibility baseline. Treat DOM-first content, keyboard access, visible focus, WhatsApp reachability, reduced motion, WebGL fallback, accessible forms, semantic FAQ, and Arabic/RTL readability as launch blockers. Do not claim compliance until implementation and Phase 9 QA are complete.**

---

## 31. Quality Gate

| Gate | Status | Notes |
| --- | --- | --- |
| All accessibility categories covered | PASS | 22 categories represented across requirements and matrices. |
| Every requirement includes expected behavior | PASS | All A11Y items include expected behavior. |
| Every requirement includes test method | PASS | All A11Y items include test method. |
| Every requirement includes pass/fail criteria | PASS | All A11Y items include pass and fail criteria. |
| P0 blockers clearly identified | PASS | Dedicated blocker list included. |
| Keyboard requirements documented | PASS | A11Y-010 to A11Y-013. |
| Screen reader requirements documented | PASS | A11Y-030 to A11Y-033. |
| Contrast requirements documented | PASS | A11Y-040 to A11Y-043. |
| Reduced-motion requirements documented | PASS | A11Y-060 to A11Y-062. |
| WebGL/canvas fallback requirements documented | PASS | A11Y-070 to A11Y-072 and A11Y-160. |
| Mobile/touch requirements documented | PASS | A11Y-080 to A11Y-082. |
| Form requirements documented | PASS | A11Y-110 to A11Y-113. |
| FAQ requirements documented | PASS | A11Y-120 to A11Y-121. |
| WhatsApp/CTA requirements documented | PASS | A11Y-100 to A11Y-102. |
| Bilingual/RTL requirements documented | PASS | A11Y-140 to A11Y-143. |
| Sound/media requirements documented | PASS | A11Y-150 to A11Y-152. |
| Scene-level risks mapped | PASS | Scene-level matrix included. |
| Route-level risks mapped | PASS | Route-level matrix included. |
| Future validation phases mapped | PASS | Each requirement includes future validation phase. |
| Avoided implementation and new roadmap tickets | PASS | No code, audit, UI comp, or new ticket created. |

---

## 32. Acceptance Criteria

| Acceptance Criteria | Status |
| --- | --- |
| Accessibility specification document created | PASS |
| Requirements are written in testable format | PASS |
| Every requirement includes expected behavior | PASS |
| Every requirement includes test method | PASS |
| Every requirement includes pass/fail criteria | PASS |
| Semantic structure requirements documented | PASS |
| Keyboard navigation requirements documented | PASS |
| Focus visibility requirements documented | PASS |
| Screen reader requirements documented | PASS |
| Color contrast requirements documented | PASS |
| Typography/readability requirements documented | PASS |
| Motion/reduced-motion requirements documented | PASS |
| WebGL/canvas requirements documented | PASS |
| Static fallback requirements documented | PASS |
| Mobile/touch requirements documented | PASS |
| Navigation/menu requirements documented | PASS |
| WhatsApp/CTA requirements documented | PASS |
| Form requirements documented | PASS |
| FAQ requirements documented | PASS |
| Workshop requirements documented | PASS |
| Bilingual/RTL requirements documented | PASS |
| Images/media/sound requirements documented | PASS |
| Scene-level matrix included | PASS |
| Route-level matrix included | PASS |
| Tool/test method matrix included | PASS |
| Accessibility blocker rules included | PASS |
| Accessibility guardrail table included | PASS |
| No implementation started | PASS |
| No UI comps created | PASS |
| No automated audit claimed unless actually run | PASS |
| No new roadmap tickets created | PASS |

---

## 33. Final Status

**PASS WITH CONDITIONS - P3.05 complete. Accessibility requirements are documented in a testable format with expected behavior, test method, pass/fail criteria, scene/route matrices, validation methods, and blocker rules.**

Final accessibility compliance remains conditional on implementation, real content/assets, QA audits, screen reader testing, RTL validation, mobile device testing, WebGL fallback testing, reduced-motion QA, privacy/legal review, and stakeholder approval.
