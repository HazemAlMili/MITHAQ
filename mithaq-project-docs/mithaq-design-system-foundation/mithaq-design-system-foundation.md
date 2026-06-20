# Mithaq Design System Foundation

**Official Ticket ID:** P4.01  
**Official Ticket Name:** Design System Foundation  
**Phase:** Phase 4 - Visual System & Art Direction  
**Owner:** Design System Lead / UI Art Director  
**Status:** PASS WITH CONDITIONS - Figma build pending  
**Date:** 2026-06-20  
**Deliverable Type:** Repo-based design system specification and planning token draft

---

## 1. Executive Summary

This document defines Mithaq's design system foundation before scene-level visual compositions, opening keyframe comps, final UI design, or frontend implementation begin.

Because direct Figma access is unavailable in this workspace, this ticket is delivered as an implementation-safe repo-based design system specification. The actual Figma component library remains pending, but the foundation is defined enough for a designer to recreate the library in Figma without changing project scope.

Foundation direction:

**Mithaq's design system should feel like a restrained legal editorial system sitting inside a cinematic dark chamber: parchment text, muted brass/gold accents, serious typography, spacious layouts, low-pressure conversion components, DOM-first content, Arabic/English parity, and static fallback primitives that feel intentional rather than degraded.**

This task creates visual-system foundations only. It does not create full scene comps, final Figma screens, opening keyframe comps, React components, production CSS, GSAP/Lenis/R3F implementation, final content, or new roadmap tickets.

---

## 2. Current Mithaq Decisions

| Area | Current Decision |
| --- | --- |
| Product type | Premium bilingual 3D legal academy portfolio / landing experience. |
| Core concept | The Covenant Seal. |
| Opening direction | Scroll-Driven Seal-Led Opening. |
| 3D direction | Seal-Led Macro Legal Chamber. |
| Motion direction | Scroll-Led Ceremonial Restraint. |
| Primary conversion | WhatsApp. |
| Secondary conversion | `/register` inquiry/register interest form. |
| MVP routes | `/`, `/register`, `/workshops/[slug]`. |
| Bilingual support | Arabic and English are first-class layouts. |
| Arabic display | Tajawal 700 default. |
| Lemonada | Accent-only pending review. |
| Filled gold CTA | Must use near-black text. |
| Gold-dim | Decorative only. |
| Red | Not primary text on dark backgrounds if contrast fails. |
| Waitlist | Conditional only. |
| Content status | WhatsApp, workshops, mentors, proof, trust assets remain pending. |
| Forbidden patterns | Fake proof, testimonials, stats, urgency, seat counters, LMS/dashboard/course-platform behavior. |
| Fallback | Static fallback must feel premium, not degraded. |
| Accessibility baseline | WCAG 2.2 AA target; compliance not yet claimed. |

---

## 3. Design System Principles

| Principle | Meaning |
| --- | --- |
| Authority before decoration | Every component should feel serious, legal, and credible. |
| Editorial clarity | Layout, type, and spacing must support reading. |
| Cinematic restraint | Visual system supports 3D without becoming theatrical. |
| Conversion clarity | CTAs must always be recognizable and low-pressure. |
| Bilingual parity | Arabic and English components must both feel native. |
| Accessibility by default | Components should meet WCAG 2.2 AA requirements later. |
| DOM-first | Components must represent real content, not canvas-only visuals. |
| Mobile-safe | Components must work at 320-430px widths. |
| No LMS language | Components must not feel like dashboards/course marketplaces. |
| Placeholder-safe | Components must avoid fake proof, fake mentors, fake workshop facts. |

---

## 4. Color Styles

Source: P2.02 Color Token System.

### 4.1 Core Background Tokens

| Style Name | Token | Value | Usage |
| --- | --- | --- | --- |
| Mithaq / Void | `--mithaq-void` | `#08070F` | Deepest background. |
| Mithaq / Ink | `--mithaq-ink` | `#0E0C1A` | Main dark page background. |
| Mithaq / Chamber | `--mithaq-chamber` | `#161422` | Section/chamber background. |
| Mithaq / Wood | `--mithaq-wood` | `#1C1510` | Desk/material-inspired surface. |
| Mithaq / Panel | `--mithaq-panel` | `#14111F` | Elevated component background. |
| Mithaq / Trust Navy | `--mithaq-trust-navy` | `#1A2540` | Trust/proof background when needed. |

### 4.2 Text Tokens

| Style Name | Token | Value | Usage |
| --- | --- | --- | --- |
| Text / Parchment | `--mithaq-parchment` | `#F2E8D0` | Primary text on dark. |
| Text / Ivory | `--mithaq-ivory` | `#FFF7E6` | High emphasis text, sparingly. |
| Text / Muted | `--mithaq-parchment-dim` | `#BFB09A` | Secondary body/helper text. |
| Text / Subtle | `--mithaq-text-subtle` | `#8F806E` | Metadata/helper only after contrast check. |
| Text / Inverse Dark | `--mithaq-text-inverse-dark` | `#08070F` | Text on filled gold buttons. |

### 4.3 Accent Tokens

| Style Name | Token | Value | Usage |
| --- | --- | --- | --- |
| Gold / Primary | `--mithaq-seal-gold` | `#C4913A` | Primary accent / CTA border. |
| Gold / Fill | `--mithaq-gold-fill` | `#C4913A` | Filled CTA background. |
| Gold / Light | `--mithaq-gold-light` | `#E8C97A` | Focus, hover, seal highlight. |
| Gold / Dim | `--mithaq-gold-dim` | `#8B6420` | Decorative only. |
| Brass / Muted | `--mithaq-brass` | `#A7782F` | Secondary metal accent. |
| Seal / Highlight | `--mithaq-seal-highlight` | `#E8C97A` | Seal/ceremonial highlight. |

### 4.4 Semantic Tokens

| Style Name | Token | Usage |
| --- | --- | --- |
| Status / Success | `--color-status-success-*` | Form success, with later contrast check. |
| Status / Warning | `--color-status-warning-*` | Warnings if needed. |
| Status / Error | `--color-status-error-*` | Error state with parchment-safe pairing. |
| Focus / Ring | `--color-focus-ring` | Focus ring on dark and gold. |
| Disabled / UI | `--color-disabled-*` | Disabled components. |

### 4.5 Color Rules

- Filled gold CTA must use near-black text.
- White text on gold is not allowed.
- Gold-dim is decorative only.
- Red cannot be used as primary body/error text on dark if contrast fails.
- Body text should use parchment/ivory-safe tokens.
- Focus ring must be visible on dark and gold.
- All text tokens must be checked against P2.02 contrast notes.
- No tiny gold text for critical information.
- No color-only error states.

---

## 5. Typography Styles

Source: P2.03 Typography Specimen.

### 5.1 English / Latin Styles

| Style | Font | Weight | Desktop Size / LH | Mobile Size / LH | Usage |
| --- | --- | ---: | --- | --- | --- |
| Display XL EN | Cormorant Garamond | 700 | 88 / 1.02 | 44-48 / 1.1 | Hero / ceremonial headings. |
| Display L EN | Cormorant Garamond | 600/700 | 72 / 1.05 | 38-42 / 1.12 | Scene headings. |
| Display M EN | Cormorant Garamond | 600 | 56 / 1.1 | 32-36 / 1.18 | Section headings. |
| Heading EN | Cormorant or DM Sans | 600 | 32-40 / 1.2 | 24-30 / 1.25 | Section/card headings. |
| Body L EN | DM Sans | 400/500 | 20 / 1.7 | 18 / 1.65 | Hero/support copy. |
| Body M EN | DM Sans | 400 | 18 / 1.7 | 16-18 / 1.65 | Main body. |
| Body S EN | DM Sans | 400 | 16 / 1.65 | 15-16 / 1.6 | Cards/forms/FAQ. |
| Label EN | JetBrains Mono | 500 | 12 / 1.35 | 11-12 / 1.3 | Scene labels/metadata. |
| Micro EN | JetBrains Mono | 400/500 | 11 / 1.3 | 11 / 1.3 | Small metadata only if readable. |

### 5.2 Arabic Styles

| Style | Font | Weight | Desktop Size / LH | Mobile Size / LH | Usage |
| --- | --- | ---: | --- | --- | --- |
| Display AR | Tajawal | 700 | 48-56 / 1.25 | 36-44 / 1.25 | Arabic hero/scene display default. |
| Heading AR | Tajawal | 700/500 | 28-40 / 1.3 | 24-32 / 1.35 | Section/card headings. |
| Body L AR | Tajawal | 400/500 | 20 / 1.8 | 18 / 1.8 | Hero/support copy. |
| Body M AR | Tajawal | 400/500 | 18 / 1.8 | 16-18 / 1.75 | Main body. |
| Body S AR | Tajawal | 400 | 16 / 1.75 | 15-16 / 1.7 | Cards/forms/FAQ. |
| Label AR | Tajawal | 500 | 14 / 1.5 | 14 / 1.5 | Arabic labels. |
| Accent AR | Lemonada | 400-700 | Short accent only | Short accent only | Accent-only, not default display. |

### 5.3 Typography Rules

- Tajawal 700 is the safe Arabic display default.
- Lemonada is accent-only pending Arabic/client review.
- Do not use Lemonada for long Arabic headings or body text.
- Do not animate Arabic letter-by-letter later.
- Do not apply Latin letter-spacing to Arabic.
- Do not mix Arabic and English in the same animated line.
- Arabic needs more line-height and breathing room.
- Cormorant should be reserved for major English authority moments.
- DM Sans is used for clarity, not SaaS-style visual dominance.
- JetBrains Mono is used sparingly for scene numbers/metadata only.
- Typography must be tested at 320px mobile width.

---

## 6. Spacing Scale

| Token | Value | Usage |
| --- | ---: | --- |
| `space-2xs` | 4px | Micro gaps. |
| `space-xs` | 8px | Icon/text gap. |
| `space-sm` | 12px | Compact components. |
| `space-md` | 16px | Default component padding. |
| `space-lg` | 24px | Card padding/mobile section gap. |
| `space-xl` | 32px | Section internal spacing. |
| `space-2xl` | 48px | Desktop component grouping. |
| `space-3xl` | 64px | Section spacing. |
| `space-4xl` | 96px | Large desktop scene spacing. |
| `space-5xl` | 128px | Cinematic desktop spacing. |

Rules:

- Mobile should use tighter but readable spacing.
- Arabic text blocks may need extra vertical spacing.
- Premium feel depends on negative space.
- Cards must not become dense/course-catalog-like.
- Do not hide CTAs below too much mobile scroll.

---

## 7. Layout / Grid System

### Desktop

| Area | Rule |
| --- | --- |
| Main width | Content max-width: 1120-1240px candidate. |
| Scene width | Full viewport visual sections. |
| Text column | Protected readable column, 540-680px candidate. |
| 3D zone | Must not overlap DOM content. |
| CTA zone | Clear and stable. |
| Grid | 12-column or controlled editorial grid. |
| Section rhythm | Generous vertical spacing. |

### Mobile

| Area | Rule |
| --- | --- |
| Widths | 320, 375, 390, 430px supported. |
| Layout | Single-column first. |
| CTA | Early and reachable. |
| 3D | Poster/simplified background. |
| Cards | Stacked. |
| FAQ | Full-width semantic accordion. |
| Forms | Full-width inputs. |
| Nav | Menu plus WhatsApp/Register access. |

### Tablet

| Area | Rule |
| --- | --- |
| Layout | Hybrid single/two-column only if readable. |
| 3D | Simplified. |
| Cards | 2-column only if enough width. |
| CTA | Visible and tap-safe. |

---

## 8. Radius / Border / Divider System

| Token | Suggested Value | Suggested Use |
| --- | ---: | --- |
| `radius-none` | 0px | Formal editorial blocks. |
| `radius-sm` | 4px | Inputs, small tags. |
| `radius-md` | 8px | Cards/buttons. |
| `radius-lg` | 12px | Larger panels only. |
| `radius-pill` | 999px | Tags / compact CTAs only. |
| `border-subtle` | 1px | Card borders on dark. |
| `border-gold` | 1px | CTA and premium highlight. |
| `divider-soft` | 1px | Editorial section dividers. |

Rules:

- Avoid overly rounded SaaS buttons.
- Avoid playful pill-heavy UI.
- Borders should be subtle and legal/editorial.
- Gold border must not be overused.

---

## 9. Shadow / Depth System

| Depth Token | Usage |
| --- | --- |
| `depth-flat` | Editorial text blocks. |
| `depth-raised` | Cards/forms. |
| `depth-floating` | Modal/workshop preview. |
| `depth-ceremonial` | Seal/hero overlay areas. |

Rules:

- Shadows must be soft and dark, not bright/glowy.
- Avoid neon glows.
- Avoid game-like floating UI.
- Use depth to clarify hierarchy, not decorate.

---

## 10. Icon System Direction

| Icon Type | Usage |
| --- | --- |
| WhatsApp/contact | Conversion. |
| Arrow/chevron | Navigation/accordion. |
| Language | i18n toggle. |
| Workshop/detail | Workshop cards. |
| Level/format | Workshop metadata. |
| Mentor/expertise | Mentor cards. |
| Trust/proof | Credibility blocks. |
| Form status | Success/error/warning. |
| Accessibility/reduced motion | Optional settings. |

Rules:

- Use restrained line-based or engraved-feeling icons.
- Icons must remain readable at small size.
- Icons cannot replace labels for primary CTAs.
- WhatsApp icon must have accessible text label.
- Avoid generic scales-of-justice cliche unless highly restrained.
- Avoid decorative icon overload.

---

## 11. Button Components

### 11.1 Required Variants

| Component | Usage |
| --- | --- |
| Button / Primary Gold Filled | Main CTA where appropriate. |
| Button / Primary Gold Outline | Premium CTA on dark backgrounds. |
| Button / Secondary Parchment | Secondary CTA. |
| Button / Ghost | Low-emphasis action. |
| Button / Text Link | Editorial navigation. |
| Button / WhatsApp | Primary contact CTA. |
| Button / Disabled | Disabled/unavailable state. |
| Button / Loading | Form submission state. |

### 11.2 Sizes

| Size | Use | Candidate Dimensions |
| --- | --- | --- |
| Large | Hero/final CTA. | 52-56px height, 20-28px horizontal padding. |
| Medium | Cards/nav/forms. | 44-48px height, 16-24px horizontal padding. |
| Small | Secondary inline actions. | 36-40px height; not for primary mobile CTA. |

### 11.3 States

| State | Requirement |
| --- | --- |
| Default | Clear contrast. |
| Hover | Subtle, no bounce. |
| Focus | Strong visible focus ring. |
| Active | Clear but restrained. |
| Disabled | Visibly disabled and non-confusing. |
| Loading | Accessible loading text/state. |

Button rules:

- Filled gold CTA must use near-black text.
- Buttons must be at least 44px tall on mobile.
- Primary buttons must not rely on icon-only labels.
- No pulsing desperate CTA.
- No fake urgency copy.
- No hover-only meaning.
- Arabic labels must fit mobile.

---

## 12. CTA Components

| CTA Component | Usage |
| --- | --- |
| Hero CTA Group | Scene 02. |
| Workshop CTA Group | Scene 06 and `/workshops/[slug]`. |
| FAQ CTA Block | Scene 09. |
| Final CTA Block | Scene 10. |
| Floating WhatsApp CTA | Global/mobile. |
| Register Interest CTA | Header, hero, final CTA, workshop detail secondary. |

Rules:

- WhatsApp remains the primary conversion path.
- Register Interest links to `/register`.
- Workshop CTAs can include workshop context only when confirmed.
- Waitlist CTA is hidden unless real process is approved.
- CTA copy remains candidate only until Phase 6.
- CTA components must be real DOM links/buttons later.

---

## 13. Form Components

| Component | Requirement |
| --- | --- |
| Text Input | Label, helper, error, disabled, focus. |
| Phone Input | Tel keyboard later; used for phone/WhatsApp. |
| Email Input | Optional. |
| Select / Radio | Interest area, preferred language. |
| Textarea | Optional message. |
| Submit Button | Full-width on mobile or highly visible. |
| Form Helper | Low-pressure inquiry/register explanation. |
| Form Error | Not color-only; associated with field. |
| Form Success | Clear confirmation and WhatsApp alternative. |

Form rules:

- Required fields: name + phone/WhatsApp only.
- No multi-step application.
- No payment fields.
- No account/password.
- No hidden required fields.
- Privacy/data-use note required before launch.

---

## 14. Navigation Components

| Component | Requirement |
| --- | --- |
| Header / Desktop | Logo, minimal anchors, Register, WhatsApp, language toggle. |
| Header / Mobile | Logo, menu trigger, WhatsApp/Register access, language toggle. |
| Footer | Minimal premium nav with WhatsApp/Register/FAQ/privacy if approved. |
| Anchor Link | Smooth later, but semantic and not motion-dependent. |
| Current Item | Visible state when applicable. |

Rules:

- No mega-menu.
- No LMS dashboard navigation.
- No hidden WhatsApp path.
- Mobile menu must later be keyboard and focus safe.

---

## 15. Language Toggle Component

| Element | Requirement |
| --- | --- |
| Current language | Clearly indicated. |
| Target language | Clear and reachable. |
| RTL/LTR behavior | Layout and labels mirror/adapt. |
| Mobile behavior | Tap-safe and visible in nav/menu. |
| Accessibility | Announces current language later. |

Rules:

- Arabic and English are equal product requirements.
- Do not bury language toggle behind multiple interactions.
- Do not mix Arabic/English in one display line.

---

## 16. WhatsApp CTA Component

| Element | Requirement |
| --- | --- |
| Destination | `https://wa.me/WHATSAPP_NUMBER_PENDING` placeholder only. |
| Label | Visible text label, not icon-only. |
| Variants | Header, floating, hero, workshop, FAQ, final, register alternative. |
| Mobile | Reachable without blocking content. |
| Accessibility | Clear accessible name later. |

Rules:

- Do not invent WhatsApp number.
- No aggressive pulsing.
- Workshop-specific prefill only with confirmed workshop title/slug.
- Static fallback must retain WhatsApp CTA.

---

## 17. Card Components

| Base Card Element | Requirement |
| --- | --- |
| Label | Optional metadata. |
| Title | Required. |
| Body | Optional/supporting. |
| CTA | Optional. |
| Status | Optional placeholder/pending/verified. |
| Icon | Optional. |
| Visual slot | Optional image/3D/poster. |

Rules:

- Cards must feel editorial/premium, not SaaS dashboards.
- Workshop cards must not feel like marketplace course tiles.
- Placeholder/fake proof must not appear public as real.
- Card content must be DOM text later.
- Mobile cards stack.
- Tap targets must be safe.

---

## 18. Workshop Card Component

| Element | Status |
| --- | --- |
| Workshop title | Required. |
| Level / audience fit | Required if known, otherwise pending. |
| Skill focus | Required. |
| Format | Pending unless confirmed. |
| Duration | Pending unless confirmed. |
| Mentor | Pending unless confirmed. |
| CTA: Ask About This Workshop | Required. |
| CTA: View Details | Required. |
| Status note | Internal only if placeholder. |

Rules:

- Do not show fake dates.
- Do not show fake capacity.
- Do not show fake pricing.
- Do not show fake certificate.
- Do not use "Enroll Now" unless real enrollment process exists.
- No checkout/payment UI.
- No lesson/module dashboard layout.

---

## 19. Mentor Card Component

| Element | Requirement |
| --- | --- |
| Portrait/image slot | Placeholder-safe. |
| Name | Only if confirmed. |
| Role/title | Only if confirmed. |
| Expertise tags | Only if confirmed. |
| Short bio | Only if confirmed. |
| Placeholder state | Must not fake identity. |
| CTA | Optional ask/register. |

Rules:

- Do not invent names.
- Do not invent credentials.
- Do not invent years of experience.
- Use safe placeholder treatment if assets missing.
- Alt text planning required later.

---

## 20. Trust / Proof Block Component

| Type | Use |
| --- | --- |
| Verified testimonial | Only with consent. |
| Quantitative proof | Only with verified source. |
| Institutional affiliation | Only with permission. |
| Press mention | Only verified. |
| Placeholder proof slot | Internal/Figma only, not public as real. |
| Trust principle block | Safe if phrased without unsupported claim. |

Rules:

- No fake testimonials.
- No fake stats.
- No fake logos.
- No "best academy."
- Every proof card should include internal source/approval status.
- If proof is missing, design forward-compatible empty structure.

---

## 21. FAQ Accordion Component

| Element | Requirement |
| --- | --- |
| Question button | Required. |
| Answer panel | Required. |
| Open/closed indicator | Required. |
| Focus state | Required. |
| Keyboard behavior note | Required for later. |
| Reduced-motion note | Required. |

Rules:

- Must be semantic later.
- Must work without animation.
- Mobile tap targets 44px.
- No nested accordion unless necessary.
- FAQ text is final later in P6.04, not here.

---

## 22. Modal / Workshop Preview Component

| Element | Requirement |
| --- | --- |
| Modal title | Workshop title. |
| Close button | Required. |
| Summary | Short workshop preview. |
| Skill bullets | If confirmed. |
| CTA: Ask on WhatsApp | Required. |
| CTA: Full Details | Links to `/workshops/[slug]`. |
| Status/fallback | If content pending. |

Rules:

- Modal must not be the only way to access workshop details.
- `/workshops/[slug]` remains canonical detail page.
- Modal must be keyboard/focus-safe later.
- Do not implement modal.
- Do not design full final modal flow beyond component foundation.

---

## 23. Static Fallback Components

| Component | Usage |
| --- | --- |
| Static Hero Poster Block | Scene 01/02 fallback. |
| Static Scene Section | Scenes 03-10 fallback. |
| Static Seal CTA Block | Scene 10 fallback. |
| Editorial Workshop List | Scene 06 fallback. |
| Editorial FAQ | Scene 09 fallback. |
| Fallback Notice | Optional, only if needed. |

Rules:

- Fallback must feel premium, not broken.
- Fallback must contain same content and CTAs.
- No "your browser is bad" language.
- 3D absence must not reduce conversion.

---

## 24. RTL / LTR Component Rules

| Component | RTL Requirement |
| --- | --- |
| Header | Nav order and alignment must feel natural. |
| Buttons | Icon placement mirrors where appropriate. |
| Cards | Text alignment and metadata flow adapt. |
| Forms | Labels/inputs align correctly. |
| FAQ | Accordion icon placement mirrors. |
| Workshop cards | CTA and metadata remain readable. |
| Language toggle | Current language clear. |
| Floating CTA | Does not cover content in either direction. |

Rules:

- Use logical spacing rules in design annotations.
- Arabic should not be visually smaller/weaker.
- Do not force English layout proportions onto Arabic.
- Do not use Arabic letter-spacing.
- Do not mix Arabic/English in one display line.
- Test 320px Arabic components.

---

## 25. Mobile Component Rules

| Component | Mobile Rule |
| --- | --- |
| Buttons | 44px minimum height. |
| Cards | Stack vertically. |
| Workshop cards | CTA visible without hover. |
| FAQ | Full-width tap-safe rows. |
| Form inputs | Full-width, visible labels. |
| Header | Compact with menu. |
| Floating WhatsApp | Does not block content. |
| Hero CTA | Appears early. |
| Modals | Full-screen or sheet-like if later designed. |
| Trust cards | Single column. |

Rules:

- No hover-only states.
- No dense card grids.
- No tiny gold metadata as critical text.
- No CTA hidden below long cinematic content.

---

## 26. Accessibility Component Requirements

| Component | P0 Accessibility Requirements |
| --- | --- |
| Header nav | Semantic nav, keyboard, focus. |
| Mobile menu | Focus management later, close button. |
| Buttons/CTAs | Real DOM elements, accessible names. |
| WhatsApp CTA | Clear label, no icon-only main CTA. |
| Form inputs | Visible labels, errors, success. |
| FAQ accordion | Keyboard/screen reader pattern later. |
| Workshop card | Keyboard reachable, no hover-only. |
| Modal preview | Focus trap/escape later. |
| Language toggle | Announces current language. |
| Static fallback blocks | Equivalent content/CTA. |

Important:

Do not claim accessibility compliance yet. This section maps component requirements only.

---

## 27. Component State Inventory

| Component | States Required |
| --- | --- |
| Button | default, hover, focus, active, disabled, loading. |
| CTA group | default, responsive stack, focus. |
| Input | default, focus, filled, error, disabled. |
| Select/radio | default, focus, selected, error. |
| Card | default, hover/focus, active/selected if needed. |
| Workshop card | default, focus, pending content, verified content. |
| FAQ item | closed, open, focus. |
| Modal | closed, open, loading/pending content. |
| Nav item | default, hover, focus, current. |
| Language toggle | AR active, EN active, focus. |
| Floating WhatsApp | default, focus, mobile-safe. |

Detailed animation behavior belongs to P4.04. P4.01 defines only static visual states and the state inventory.

---

## 28. Figma Library Organization

Figma file name:

```text
Mithaq - Design System Foundation
```

| Page | Contents |
| --- | --- |
| 00 - Cover / Status | Status, dependencies, conditions. |
| 01 - Foundations | Colors, typography, spacing, grid. |
| 02 - Components / Buttons & CTAs | Buttons, CTA groups, WhatsApp. |
| 03 - Components / Forms | Inputs, selects, textarea, states. |
| 04 - Components / Cards | Pillar, workshop, mentor, trust cards. |
| 05 - Components / Navigation | Header, mobile nav, language toggle. |
| 06 - Components / FAQ & Modal | Accordion, workshop preview modal. |
| 07 - Static Fallback Primitives | Fallback blocks. |
| 08 - RTL / Mobile Notes | RTL and mobile component notes. |
| 09 - Accessibility Notes | A11Y requirements mapped to components. |

Current status:

```text
Figma library pending
```

---

## 29. Design Token Export Notes

| Token Type | Export Note |
| --- | --- |
| Colors | Candidate values from P2.02. |
| Typography | Candidate styles from P2.03. |
| Spacing | Scale from P4.01. |
| Radius | Candidate. |
| Shadow | Candidate. |
| Motion | Refer to P2.07; do not implement here. |
| Component states | Document only. |

Rules:

- Token draft can be created for design consistency.
- Do not wire tokens into app frontend.
- Do not claim production CSS is ready.
- Do not modify existing implementation unless explicitly requested.

Supporting token draft:

[mithaq-design-system-tokens.css](D:/Clinets/MITHAQ/MITHAQ/mithaq-project-docs/mithaq-design-system-foundation/mithaq-design-system-tokens.css:1)

---

## 30. Component Usage Guardrails

| Component Area | Keep | Avoid |
| --- | --- | --- |
| Buttons | Clear, calm, contrast-safe CTAs. | Pulsing/aggressive CTA. |
| Cards | Editorial, spacious, premium. | SaaS dashboard/course marketplace. |
| Workshop cards | Skill-focused dossier feel. | Checkout/enrollment tile. |
| Mentor cards | Honest confirmed info. | Fake credentials. |
| Trust blocks | Verified proof only. | Fake stats/testimonials. |
| FAQ | Readable semantic structure. | Decorative hidden answers. |
| Forms | Simple inquiry/register interest. | Long application/account flow. |
| Navigation | Minimal conversion-led nav. | LMS mega-menu. |
| Icons | Restrained legal/editorial symbols. | Clipart/generic legal icons. |
| Fallback blocks | Premium editorial fallback. | Broken degraded page. |

---

## 31. Required Design System Deliverable Checklist

| Deliverable Item | Status |
| --- | --- |
| Color style system | PASS |
| Typography style system | PASS |
| Spacing scale | PASS |
| Layout/grid rules | PASS |
| Radius/border/divider rules | PASS |
| Shadow/depth rules | PASS |
| Icon direction | PASS |
| Button variants | PASS |
| CTA components | PASS |
| Form components | PASS |
| Navigation components | PASS |
| Language toggle | PASS |
| WhatsApp CTA | PASS |
| Card components | PASS |
| Workshop card | PASS |
| Mentor card | PASS |
| Trust/proof block | PASS |
| FAQ accordion | PASS |
| Modal preview component | PASS |
| Static fallback components | PASS |
| RTL/LTR rules | PASS |
| Mobile rules | PASS |
| Accessibility mapping | PASS |
| State inventory | PASS |
| Figma organization notes | PASS WITH CONDITIONS - Figma build pending |
| Guardrail table | PASS |

---

## 32. Final Design System Recommendation

| Decision Area | Recommendation |
| --- | --- |
| Design system status | Proceed with repo-based foundation; build Figma library when access/assets are available. |
| Visual system model | Dark legal editorial system with restrained brass/gold accents. |
| Component style | Premium, spacious, DOM-first, low-pressure conversion components. |
| CTA model | WhatsApp primary, Register Interest secondary, workshop-specific CTAs where relevant. |
| Fallback model | Static editorial components with equivalent content and CTAs. |
| Arabic/RTL model | Component parity with logical layout, Tajawal-first Arabic typography. |
| Mobile model | Single-column, 44px tap targets, stacked cards, visible CTAs. |
| Accessibility model | WCAG 2.2 AA requirements mapped, compliance pending later QA. |
| Production readiness | Not production-ready; planning/spec foundation only. |

Final recommendation:

**Use this foundation to build the Figma component library before scene comps. Keep all final brand, workshop, mentor, proof, WhatsApp, Arabic review, and accessibility validation conditions visible in the Figma file and do not let components imply fake content or production readiness.**

---

## 33. Quality Gate

| Gate | Status | Notes |
| --- | --- | --- |
| Design system foundation created | PASS | Repo-based foundation created. |
| Colors included from P2.02 | PASS | Token values and usage rules included. |
| Typography styles included from P2.03 | PASS | English/Arabic styles and rules included. |
| Spacing scale included | PASS | Scale included. |
| Layout/grid rules included | PASS | Desktop/mobile/tablet rules included. |
| Button variants included | PASS | Variants/sizes/states included. |
| CTA components included | PASS | CTA groups and rules included. |
| Form components included | PASS | Inputs/states/form rules included. |
| Navigation components included | PASS | Header/mobile/footer rules included. |
| Language toggle specified | PASS | Component rules included. |
| WhatsApp CTA specified with placeholder | PASS | `WHATSAPP_NUMBER_PENDING` used. |
| Card components included | PASS | Base and specialized cards included. |
| Workshop card specified | PASS | Anatomy/rules included. |
| Mentor card specified | PASS | Placeholder-safe rules included. |
| Trust/proof component specified | PASS | Verified-only proof rules included. |
| FAQ accordion specified | PASS | Component anatomy/rules included. |
| Modal/workshop preview specified | PASS | Component foundation only. |
| Static fallback components included | PASS | Fallback primitives included. |
| RTL/LTR rules included | PASS | Component-level RTL table included. |
| Mobile rules included | PASS | Mobile component table included. |
| Accessibility component requirements mapped | PASS | Mapped to P3.05 requirement areas. |
| Component state inventory included | PASS | State table included. |
| Figma organization notes included | PASS WITH CONDITIONS | Actual Figma build pending. |
| Usage guardrails included | PASS | Guardrail table included. |
| Avoided full scene comps | PASS | No scene comps created. |
| Avoided frontend implementation | PASS | No app code modified. |
| Avoided new roadmap tickets | PASS | No new tickets created. |

---

## 34. Acceptance Criteria

| Acceptance Criteria | Status |
| --- | --- |
| Repo-based design system spec created because Figma is unavailable | PASS WITH CONDITIONS |
| Color styles documented | PASS |
| Typography styles documented | PASS |
| Spacing scale documented | PASS |
| Layout/grid rules documented | PASS |
| Button variants documented | PASS |
| CTA components documented | PASS |
| Form components documented | PASS |
| Navigation components documented | PASS |
| Language toggle documented | PASS |
| WhatsApp CTA documented with `WHATSAPP_NUMBER_PENDING` | PASS |
| Base card components documented | PASS |
| Workshop card component documented | PASS |
| Mentor card component documented | PASS |
| Trust/proof block component documented | PASS |
| FAQ accordion component documented | PASS |
| Workshop preview/modal component documented | PASS |
| Static fallback component primitives documented | PASS |
| RTL/LTR component rules included | PASS |
| Mobile component rules included | PASS |
| Accessibility requirements mapped to components | PASS |
| Component state inventory included | PASS |
| Figma library organization documented | PASS |
| Design token export notes included | PASS |
| Component usage guardrails included | PASS |
| No full scene visual comps created | PASS |
| No opening keyframe comps created | PASS |
| No frontend implementation started | PASS |
| No production CSS/React implementation wired into app | PASS |
| No new roadmap tickets created | PASS |

---

## 35. Final Status

**PASS WITH CONDITIONS - P4.01 complete. Implementation-safe design system foundation includes colors, typography, spacing, grid, components, states, RTL/mobile/accessibility notes, token export notes, Figma organization guidance, and guardrails.**

Conditions remaining:

- Actual Figma library creation is pending.
- Final brand assets, logo, wordmarks, and Seal approval remain pending.
- Final workshop content remains pending.
- Mentor/proof assets remain pending.
- Final WhatsApp number remains pending.
- Final Arabic/client review remains pending.
- Final accessibility validation remains pending.
- Frontend token implementation remains pending.
