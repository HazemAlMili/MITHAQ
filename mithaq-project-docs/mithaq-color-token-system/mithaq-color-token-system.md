# Mithaq Color Token System

**Official Ticket ID:** P2.02  
**Official Ticket Name:** Color Token System  
**Phase:** Phase 2, Creative Concept Development  
**Priority:** P0  
**Status:** PASS WITH CONDITIONS  
**Prepared date:** 2026-06-18  

---

## 1. Executive Summary

This document defines the candidate color token system for Mithaq's premium bilingual 3D legal academy portfolio / landing experience.

Decision:

**Proceed with a dark ceremonial palette built around near-black chamber surfaces, parchment reading text, and restrained gold seal accents.**

The palette supports:

- The Covenant Seal concept.
- Scroll-driven gavel trigger into seal reveal.
- Symbolic realism in 3D and static fallback states.
- Arabic and English layouts from the beginning.
- WhatsApp-first conversion without fake urgency.
- Accessible text contrast on dark premium backgrounds.

This ticket does not create final UI, final seal, final 3D, production assets, or frontend implementation. It creates a design-system token foundation and contrast gate for later work.

---

## 2. Inputs Used

| Source | Relevant Decision |
| ------ | ----------------- |
| Direction plan Section 4.1 | Original Mithaq color tokens and palette philosophy |
| P0.06 Direction Lock | Bilingual MVP planning, gavel as trigger, seal as hero motif, no fake urgency |
| P1.04 Device Matrix | Static and reduced-motion fallbacks must look intentional |
| P1.05 3D Benchmark | Final 3D remains conditional; DOM content must remain readable |
| P2.01 Dark Premium Moodboard | Judicial chamber, legal desk, seal embossing, editorial restraint |
| Content and brand audits | Final logo, wordmarks, brand guidelines, content, and legal approvals are still missing |

P0.06 supersedes earlier Arabic-only recommendations. The token system must support bilingual MVP planning and RTL/LTR from the start.

---

## 3. Scope

Allowed in this ticket:

- Finalize candidate token names from Section 4.1.
- Generate contrast ratio table.
- Define Figma-ready swatch groups.
- Create CSS variable draft.
- Define usage rules for dark, light, accent, warning, focus, and fallback states.
- Flag accessibility risks before visual design begins.

Not allowed in this ticket:

- Final brand approval.
- Final logo or wordmark color adaptation.
- Final Mithaq Seal design.
- Final UI screens.
- Frontend production.
- Final 3D material tuning.
- Texture sourcing.
- Unsupported claims, urgency states, cohort timers, or conversion pressure patterns.

---

## 4. Core Token Palette

| Token | Hex | Role | Status |
| ----- | --- | ---- | ------ |
| `--mithaq-void` | `#08070F` | Absolute dark canvas and page base | Approved candidate |
| `--mithaq-ink` | `#0E0C1A` | Elevated dark surface, card base, overlay base | Approved candidate |
| `--mithaq-chamber` | `#161422` | Secondary scene surface and chamber depth | Approved candidate |
| `--mithaq-wood` | `#1C1510` | Legal desk / dark wood material base | Approved candidate |
| `--mithaq-seal-gold` | `#C4913A` | Primary accent for seal, gavel brass, dividers, CTA border | Approved candidate |
| `--mithaq-gold-light` | `#E8C97A` | Hover highlight, focus glow, premium edge highlight | Approved candidate |
| `--mithaq-gold-dim` | `#8B6420` | Subtle gold shadow, inactive metallic detail | Restricted |
| `--mithaq-parchment` | `#F2E8D0` | Primary readable text on dark backgrounds | Approved candidate |
| `--mithaq-parchment-dim` | `#BFB09A` | Body text, secondary copy, metadata on dark backgrounds | Approved candidate |
| `--mithaq-trust-navy` | `#1A2540` | Trust/support surface, secondary dark accent | Approved candidate |
| `--mithaq-red-authority` | `#8B1A1A` | Error or legal warning surface only | Restricted |

Palette philosophy:

- 90 percent of the experience should live in `void`, `ink`, `chamber`, and controlled material darkness.
- Gold is a signal, not a large background system.
- Parchment is for reading.
- Gold is for emphasis, seal language, focus, dividers, and CTA affordance.
- Red is not urgency marketing. It is reserved for true errors, legal warnings, or destructive states.
- The palette must not become brown/orange overall.

---

## 5. Semantic Token Layer

| Semantic Token | Value | Intended Use |
| -------------- | ----- | ------------ |
| `--color-bg-page` | `var(--mithaq-void)` | Main page background |
| `--color-bg-surface` | `var(--mithaq-ink)` | Standard dark surface |
| `--color-bg-surface-strong` | `var(--mithaq-chamber)` | Stronger surface or section transition |
| `--color-bg-material-wood` | `var(--mithaq-wood)` | Desk, wood, and material fallback base |
| `--color-bg-trust` | `var(--mithaq-trust-navy)` | Trust modules and institutional support blocks |
| `--color-text-primary` | `var(--mithaq-parchment)` | Primary headings and high-importance copy |
| `--color-text-secondary` | `var(--mithaq-parchment-dim)` | Body text and supporting copy |
| `--color-text-on-accent` | `var(--mithaq-void)` | Text on gold CTA fills, if filled CTAs are used |
| `--color-accent-primary` | `var(--mithaq-seal-gold)` | CTA border, seal, dividers, metadata accents |
| `--color-accent-hover` | `var(--mithaq-gold-light)` | Hover, active, focus emphasis |
| `--color-accent-muted` | `var(--mithaq-gold-dim)` | Decorative metallic shadows only |
| `--color-border-subtle` | `rgba(242, 232, 208, 0.14)` | Hairlines on dark surfaces |
| `--color-border-accent` | `rgba(196, 145, 58, 0.72)` | CTA border and active section divider |
| `--color-focus-ring` | `var(--mithaq-gold-light)` | Keyboard focus ring |
| `--color-status-error-bg` | `var(--mithaq-red-authority)` | Error/warning background |
| `--color-status-error-text` | `var(--mithaq-parchment)` | Error/warning text |

---

## 6. Contrast Ratio Table

Contrast was calculated using WCAG relative luminance. AA for normal text requires 4.5:1. AAA for normal text requires 7:1. Large text may pass AA at 3:1, but Mithaq should avoid relying on large-text exceptions for core reading.

| Foreground | Background | Ratio | Result | Usage Decision |
| ---------- | ---------- | ----: | ------ | -------------- |
| Parchment `#F2E8D0` | Void `#08070F` | 16.45:1 | AAA | Primary text safe |
| Parchment `#F2E8D0` | Ink `#0E0C1A` | 15.86:1 | AAA | Primary text safe |
| Parchment `#F2E8D0` | Chamber `#161422` | 14.89:1 | AAA | Primary text safe |
| Parchment `#F2E8D0` | Wood `#1C1510` | 14.80:1 | AAA | Primary text safe |
| Parchment `#F2E8D0` | Trust Navy `#1A2540` | 12.46:1 | AAA | Primary text safe |
| Parchment Dim `#BFB09A` | Void `#08070F` | 9.44:1 | AAA | Body text safe |
| Parchment Dim `#BFB09A` | Ink `#0E0C1A` | 9.11:1 | AAA | Body text safe |
| Parchment Dim `#BFB09A` | Chamber `#161422` | 8.55:1 | AAA | Body text safe |
| Parchment Dim `#BFB09A` | Wood `#1C1510` | 8.50:1 | AAA | Body text safe |
| Parchment Dim `#BFB09A` | Trust Navy `#1A2540` | 7.15:1 | AAA | Body text safe |
| Seal Gold `#C4913A` | Void `#08070F` | 7.12:1 | AAA | Accent text safe, but use sparingly |
| Seal Gold `#C4913A` | Ink `#0E0C1A` | 6.87:1 | AA | Accent text safe |
| Seal Gold `#C4913A` | Chamber `#161422` | 6.44:1 | AA | Accent text safe |
| Seal Gold `#C4913A` | Wood `#1C1510` | 6.41:1 | AA | Accent text safe |
| Seal Gold `#C4913A` | Trust Navy `#1A2540` | 5.39:1 | AA | Accent text safe |
| Gold Light `#E8C97A` | Void `#08070F` | 12.47:1 | AAA | Focus and hover safe |
| Gold Light `#E8C97A` | Ink `#0E0C1A` | 12.03:1 | AAA | Focus and hover safe |
| Gold Light `#E8C97A` | Chamber `#161422` | 11.29:1 | AAA | Focus and hover safe |
| Gold Light `#E8C97A` | Wood `#1C1510` | 11.22:1 | AAA | Focus and hover safe |
| Gold Dim `#8B6420` | Void `#08070F` | 3.76:1 | AA large only | Decorative only, not body text |
| Gold Dim `#8B6420` | Ink `#0E0C1A` | 3.63:1 | AA large only | Decorative only, not body text |
| Gold Dim `#8B6420` | Chamber `#161422` | 3.41:1 | AA large only | Decorative only, not body text |
| Void `#08070F` | Parchment `#F2E8D0` | 16.45:1 | AAA | Text on light swatch safe |
| Ink `#0E0C1A` | Parchment `#F2E8D0` | 15.86:1 | AAA | Text on light swatch safe |
| Chamber `#161422` | Parchment `#F2E8D0` | 14.89:1 | AAA | Text on light swatch safe |
| Wood `#1C1510` | Parchment `#F2E8D0` | 14.80:1 | AAA | Text on light swatch safe |
| Trust Navy `#1A2540` | Parchment `#F2E8D0` | 12.46:1 | AAA | Text on light swatch safe |
| Red Authority `#8B1A1A` | Void `#08070F` | 2.16:1 | Fail | Never use red text on dark |
| Parchment `#F2E8D0` | Red Authority `#8B1A1A` | 7.62:1 | AAA | Error/warning text safe |
| Gold Light `#E8C97A` | Red Authority `#8B1A1A` | 5.78:1 | AA | Icon/border only, avoid body copy |
| White `#FFFFFF` | Seal Gold `#C4913A` | 2.82:1 | Fail | Never use white on gold |
| Black `#000000` | Seal Gold `#C4913A` | 7.46:1 | AAA | Safe, but prefer `void` over pure black |

---

## 7. Dark Swatch Set

Primary dark swatches for Figma:

| Swatch | Base | Text | Accent | Notes |
| ------ | ---- | ---- | ------ | ----- |
| Dark 01 - Void Hero | `#08070F` | `#F2E8D0` | `#C4913A` | Opening, hero, final CTA |
| Dark 02 - Ink Surface | `#0E0C1A` | `#F2E8D0` | `#C4913A` | Cards, form shell, FAQ blocks |
| Dark 03 - Chamber Depth | `#161422` | `#F2E8D0` | `#E8C97A` | Scene transitions, stronger panels |
| Dark 04 - Wood Material | `#1C1510` | `#F2E8D0` | `#C4913A` | Static fallback desk, 3D material references |
| Dark 05 - Trust Navy | `#1A2540` | `#F2E8D0` | `#C4913A` | Proof/support modules if approved content exists |

Dark swatch rule:

Text should use parchment or parchment-dim. Gold may label metadata, dividers, or CTA affordances, but should not become paragraph color.

---

## 8. Light Swatch Set

Light usage should be rare and content-specific. Mithaq is fundamentally dark premium, but parchment surfaces may support legal document moments, form confirmations, or print-like content blocks.

| Swatch | Base | Text | Accent | Notes |
| ------ | ---- | ---- | ------ | ----- |
| Light 01 - Parchment Sheet | `#F2E8D0` | `#08070F` | `#8B6420` | Legal-document style inserts, if needed |
| Light 02 - Parchment Muted | `#BFB09A` | `#08070F` | `#1A2540` | Disabled only after separate contrast checks |
| Light 03 - Gold Fill CTA | `#C4913A` | `#08070F` | `#08070F` | Filled CTA option, black/void text only |

Light swatch rule:

Do not use white text on gold. If a filled gold button is used, text must be `--mithaq-void` or equivalent near-black.

---

## 9. Component Usage Rules

### Body and Headings

- Main headings: `--color-text-primary` on `--color-bg-page` or `--color-bg-surface`.
- Body text: `--color-text-secondary` on dark backgrounds.
- Do not use gold for long headings or paragraphs.
- Do not place body text directly on unprocessed image, video, or WebGL backgrounds without a dark readability layer.

### CTAs

- Primary WhatsApp CTA should default to gold border with parchment text on dark background.
- Filled gold CTA is allowed only when text is near-black/void.
- CTA hover may use `--mithaq-gold-light`, but animation must be restrained.
- Do not use red, countdown, seat-counter, deadline, or fake urgency color systems.

### Forms

- Form surface: ink or chamber.
- Labels: parchment-dim.
- Inputs: dark surface with subtle parchment border.
- Focus: gold-light ring, minimum 2px visible outline.
- Error background: red-authority with parchment text.
- Error text on dark backgrounds should use parchment plus an error icon or border, not red text alone.

### 3D and Static Fallback

- 3D seal/gavel gold should reference seal-gold and gold-light, not saturated yellow.
- Dark wood should remain close to wood/void and avoid orange cast.
- Static fallback must use the same content colors as the main DOM experience.
- Reduced-motion mode should preserve the dark premium palette without relying on animated lighting to make text readable.

### Bilingual and RTL/LTR

- Color semantics must not change by language.
- Arabic and English layouts should use the same accessible foreground/background pairings.
- Avoid using color alone to indicate language, direction, active state, error, or selected workshop.
- Focus and active states must remain visible in both RTL and LTR layouts.

---

## 10. Accessibility Gates

Before any UI design or frontend implementation is approved:

1. All normal body text must meet at least 4.5:1.
2. Preferred target for body text on primary dark backgrounds is AAA.
3. Gold-dim must not be used for normal text.
4. Red-authority must not be used as text on dark backgrounds.
5. White must not be used on seal-gold.
6. Image, video, canvas, or 3D backgrounds require a tested overlay or DOM layer.
7. Focus states must use visible outline/ring and cannot rely on subtle color shifts alone.
8. Static fallback and reduced-motion states must pass the same contrast requirements.
9. Arabic and English samples must both be tested because glyph density and perceived readability differ.

---

## 11. CSS Variable Draft

The companion CSS token file is:

`mithaq-color-token-system/mithaq-color-tokens.css`

The file contains:

- Core raw color tokens.
- Semantic aliases.
- Interaction aliases.
- Status aliases.
- Dark and light scheme notes.

This CSS is a token draft only. It is not frontend production code.

---

## 12. Figma Token Setup

Recommended Figma collections:

| Collection | Variables |
| ---------- | --------- |
| `Mithaq / Core` | Raw brand candidates: void, ink, chamber, wood, seal-gold, gold-light, gold-dim, parchment, parchment-dim, trust-navy, red-authority |
| `Mithaq / Semantic` | Background, text, accent, border, focus, status variables |
| `Mithaq / Components` | CTA, form, card, nav, seal, fallback variables |
| `Mithaq / Modes` | Dark default, light parchment, reduced-motion/static fallback |

Figma swatch cards should include:

- Token name.
- Hex value.
- Usage role.
- Contrast-safe foregrounds.
- Restricted uses.
- Approval status.

---

## 13. Conditions and Blockers

P2.02 passes with conditions because the palette can be used for planning, but brand approval is not complete.

| Condition | Status | Impact |
| --------- | ------ | ------ |
| Official brand guidelines missing | Open | Tokens remain candidate, not final brand law |
| Official logo missing | Open | Cannot approve exact logo usage on dark/gold surfaces |
| Arabic and English wordmarks missing | Open | Cannot approve final seal/wordmark color behavior |
| Final seal approval missing | Open | Seal material colors remain directional |
| Final content missing | Open | Cannot test all real headings, CTAs, FAQ, and workshop copy |
| Legal/compliance guidance missing | Open | Warning/error/disclaimer treatments remain structural |
| Final 3D assets missing | Open | 3D material palette must be retested later |
| Physical mobile and Safari testing missing | Open | Perceived contrast and WebGL fallback need later QA |

---

## 14. Acceptance Checklist

| Requirement | Status | Notes |
| ----------- | ------ | ----- |
| Color tokens from Section 4.1 finalized as candidates | PASS | Names and hex values retained with semantic aliases |
| Contrast ratio table generated | PASS | Core pairings calculated |
| Dark swatches created | PASS | Five primary dark swatches defined |
| Light swatches created | PASS | Three restricted light/inverse swatches defined |
| Text passes AA on primary backgrounds | PASS | Parchment, parchment-dim, seal-gold pass on dark primary surfaces |
| Restricted colors documented | PASS | Gold-dim, red-authority, white-on-gold limitations recorded |
| CSS variables drafted | PASS | Companion CSS file created |
| Bilingual/RTL/LTR considered | PASS | Same semantic roles apply across languages |
| Static/reduced-motion fallback considered | PASS | Same contrast gate required |
| Production boundaries preserved | PASS | No final UI, seal, 3D, or frontend implementation started |

---

## 15. Handoff to P2.03

Recommended next official ticket:

**P2.03 - Typography Specimen**

P2.03 should:

- Test English display/body candidates against the dark token system.
- Test Arabic display/body candidates against the same token system.
- Include long Arabic and English headlines.
- Include CTA labels, form labels, FAQ text, metadata, and workshop card samples.
- Validate font payload and licensing assumptions.
- Avoid final UI screens until content and brand assets are approved.

---

## 16. Final Status

**P2.02 status: PASS WITH CONDITIONS.**

The Mithaq color token system is ready for Figma setup, typography testing, static fallback planning, and later vertical-slice design validation.

Final production approval remains blocked until official brand assets, wordmarks, seal approval, content, legal guidance, and real device QA are complete.
