# Mithaq Static Fallback Layout

**Official Ticket ID:** P4.05  
**Official Ticket Name:** Static Fallback Layout  
**Phase:** Phase 4 - Visual System & Art Direction  
**Priority:** P1  
**Complexity:** High  
**Owner:** UI Art Director / Accessibility-Aware Product Designer  
**Status:** PASS WITH CONDITIONS - Figma build pending  
**Prepared date:** 2026-06-20  

---

## 1. Executive Summary

This package defines Mithaq's full static fallback layout for users without WebGL, users with reduced motion, failed 3D assets, weak devices, or non-animated accessible contexts.

The fallback is not an error page. It is a premium editorial version of the same 10-scene Mithaq journey:

**Static Seal hero -> Mithaq reveal -> readiness gap -> method -> pillars -> workshop dossiers -> mentors -> trust -> FAQ -> final covenant CTA.**

Visual layout:

[mithaq-static-fallback-layout.html](D:/Clinets/MITHAQ/MITHAQ/mithaq-project-docs/mithaq-static-fallback-layout/mithaq-static-fallback-layout.html:1)

This task does not implement WebGL detection, reduced-motion mode, React components, production CSS, final static hero assets, final copy, final Arabic localization, final privacy/legal copy, or new roadmap tickets.

---

## 2. Current Mithaq Direction

| Area | Direction |
| --- | --- |
| Product type | Premium bilingual 3D legal academy portfolio / landing experience. |
| Fallback purpose | Full editorial non-WebGL/reduced-motion equivalent. |
| Core concept | The Covenant Seal. |
| Opening translation | Animated gavel/seal opening becomes static seal/desk hero. |
| 3D translation | Seal-Led Macro Legal Chamber becomes static imagery and editorial composition. |
| Motion translation | Scroll-Led Ceremonial Restraint becomes calm section rhythm. |
| Primary conversion | WhatsApp. |
| Secondary conversion | `/register`. |
| MVP routes | `/`, `/register`, `/workshops/[slug]`. |
| Bilingual | Arabic and English are first-class layouts. |
| CTA rule | Filled gold CTAs use near-black text. |
| Accessibility baseline | WCAG 2.2 AA target; compliance not claimed. |
| Fallback mode | DOM-first, SEO-readable, no canvas dependency. |
| Placeholder rule | Use pending labels internally; do not invent facts. |

---

## 3. Delivery Format / Figma Or HTML Status

| Deliverable | Status | Notes |
| --- | --- | --- |
| Figma static fallback comp | Pending | Direct Figma access unavailable in this workspace. |
| HTML visual fallback comp | PASS | Desktop 1440 and mobile 390 full fallback layouts exist. |
| Markdown handoff document | PASS | This file documents structure, QA, accessibility, RTL, and implementation handoff. |
| Exported image frames | Not created | HTML visual board is accepted fallback output. |

Final status is **PASS WITH CONDITIONS** because visual fallback layouts exist while Figma build, final assets, Arabic review, accessibility QA, frontend implementation, and stakeholder approval remain pending.

---

## 4. Static Fallback Principles

| Principle | Meaning |
| --- | --- |
| Beautiful fallback | Fallback must feel intentionally designed. |
| Same content meaning | Every scene's message remains intact. |
| DOM-first | All text and CTAs are real HTML later. |
| No canvas dependency | No content requires WebGL. |
| Static imagery as premium | Posters, textures, and seal imagery replace motion. |
| Conversion preserved | WhatsApp/Register remain visible. |
| Mobile-first clarity | Mobile fallback should be clearer than desktop 3D. |
| Accessibility safe | Reduced motion and screen readers lose no meaning. |
| SEO-readable | Fallback content can be indexed where appropriate. |
| No fake content | Missing workshop/mentor/proof content remains pending. |

---

## 5. Visual System Used

| Area | Direction |
| --- | --- |
| Background | Mithaq Void / Ink / Chamber dark surfaces. |
| Text | Parchment / ivory-safe text tokens. |
| Accent | Gold as signal only. |
| Typography | Tajawal for Arabic later; Cormorant/DM Sans direction for English. |
| Cards | Editorial/dossier style. |
| Buttons | P4.01 CTA/button system. |
| FAQ | P4.01 FAQ accordion style. |
| Forms | Not shown on fallback `/`; Register link remains clear. |
| Imagery | Static seal/desk/dossier/chamber placeholder visuals. |
| Texture | Subtle dark wood/parchment/leather-inspired surfaces. |

No new design language is introduced.

---

## 6. Static Imagery Plan

| Image / Poster | Usage | Current Status |
| --- | --- | --- |
| Static Seal / Desk Hero Poster | Scene 01-02 fallback hero | Placeholder visual included; final render pending. |
| Fragmented Documents Poster | Scene 03 | Placeholder visual included. |
| Ordered Desk / Method Poster | Scene 04 | Placeholder visual included. |
| Dossier / Pillar Texture | Scene 05 | Represented through dossier cards. |
| Workshop Dossier Poster | Scene 06 | Represented through workshop cards; final imagery pending. |
| Mentor Hall / Portrait Placeholder Treatment | Scene 07 | Placeholder-safe portrait slots included. |
| Trust Editorial Texture / Seal Mark | Scene 08 | Placeholder trust blocks included. |
| Minimal FAQ Background Texture | Scene 09 | Minimal typography-led section included. |
| Final Seal CTA Poster | Scene 10 | Placeholder visual included. |

Required labels retained where relevant:

- `Static hero poster pending final render`
- `Seal asset pending`
- `Workshop dossier imagery pending`
- `WHATSAPP_NUMBER_PENDING`

---

## 7. Desktop Static Fallback Layout

Desktop visual frame:

| Requirement | Status | Notes |
| --- | --- | --- |
| Width 1440px | PASS | HTML board includes a 1440px desktop frame. |
| Full 10-section editorial page | PASS | Scenes 01-10 represented as long-scroll editorial sections. |
| Static hero imagery | PASS | Static seal/desk poster area included. |
| Header/nav | PASS | Header with nav/language placeholder. |
| CTA visibility | PASS | WhatsApp/Register appear early and again later. |
| Section rhythm | PASS | Premium editorial spacing and section boundaries. |
| Cards | PASS | Pillars, workshops, mentors, trust blocks represented. |
| FAQ | PASS | Typography-led FAQ block represented. |
| Final CTA | PASS | Static seal closing CTA included. |
| Pending content labels | PASS | Pending labels used safely and internally. |
| No WebGL error language | PASS | Fallback never says "3D failed." |

Desktop direction:

The desktop fallback reads like a normal premium legal academy landing page, with dark editorial sections and static poster imagery replacing 3D motion.

---

## 8. Mobile Static Fallback Layout

Mobile visual frame:

| Requirement | Status | Notes |
| --- | --- | --- |
| Width 390px | PASS | HTML board includes a 390px mobile frame. |
| Text-first hero | PASS | Hero meaning appears quickly. |
| CTA early | PASS | WhatsApp/Register visible in Scene 01. |
| Stacked cards | PASS | Pillars/workshops/mentors/trust stack vertically. |
| FAQ rows | PASS | Full-width tap-safe FAQ visual rows. |
| Final CTA | PASS | Final CTA visible after heading. |
| Arabic stress | PASS | Arabic sample labels included in hero/FAQ/final CTA. |
| No heavy visuals | PASS | Static poster blocks only. |
| No hidden actions | PASS | CTAs visible without hover. |
| Floating WhatsApp | Not shown | Avoids obstruction in visual comp; can be added later if non-blocking. |

Mobile direction:

The mobile fallback prioritizes comprehension and conversion over cinematic atmosphere. It keeps the seal motif, but the text and CTA come forward earlier than in desktop 3D.

---

## 9. Scene 01 Fallback - Static Seal / Opening Hero

| Area | Direction |
| --- | --- |
| Visual | Static seal/desk hero poster. |
| Heading | Covenant Seal / Mithaq identity anchor. |
| Copy | One-sentence positioning, placeholder-safe. |
| CTA | WhatsApp/Register visible early. |
| Navigation | Header visible and usable. |
| Texture | Dark desk/chamber atmosphere. |
| Accessibility | No motion required. |
| Mobile | CTA visible without long scroll. |

Purpose:

Preserve the premium opening without animation and without making the gavel dominate.

Avoided:

- "WebGL unavailable" error language
- blank hero
- long loading substitute
- gavel domination

---

## 10. Scene 02 Fallback - Hero / Mithaq Reveal

| Area | Direction |
| --- | --- |
| Text | Strong hero headline and support copy. |
| Visual | Seal poster/mark as editorial anchor. |
| CTA | WhatsApp/Register or View Workshops visible. |
| Secondary CTA | View Workshops/Pillars. |
| Mobile | Text-first. |

Purpose:

Clarify that Mithaq helps law students, graduates, and early-career legal professionals move toward practical readiness.

Avoided:

- hiding CTA under visual poster
- English-only composition assumptions
- excessive decorative 3D language

---

## 11. Scene 03 Fallback - The Gap

| Area | Direction |
| --- | --- |
| Text | Problem headline and concise explanation. |
| Visual | Static fragmented document collage. |
| CTA | Soft ask/WhatsApp path. |
| Mobile | Text first, collage secondary. |

Purpose:

Explain that academic knowledge alone does not equal practice readiness without insulting law school or students.

Avoided:

- overdramatic failure tone
- unreadable document microtext as key content
- floating 3D document dependency

---

## 12. Scene 04 Fallback - The Mithaq Method

| Area | Direction |
| --- | --- |
| Text | Method headline and structured principles. |
| Visual | Ordered legal desk/file structure. |
| CTA | Soft transition toward pillars. |
| Mobile | Vertical method blocks. |

Purpose:

Show that Mithaq turns legal knowledge into practical readiness through structure and legal craft.

Avoided:

- corporate process diagram
- dashboard/module style
- over-jargon

---

## 13. Scene 05 Fallback - Training Pillars

Required pillars represented:

1. Legal Research
2. Legal Writing
3. Professional Readiness
4. Career Infrastructure
5. Practical Legal Mindset

| Area | Direction |
| --- | --- |
| Cards | Five editorial/dossier pillar cards. |
| Text | One-line meaning per pillar. |
| CTA | View Workshops / Register Interest. |
| Mobile | Vertical card stack. |

Purpose:

Communicate practical legal skill focus without course marketplace behavior.

Avoided:

- fake module counts
- tiny text
- hover-only information
- LMS tile design

---

## 14. Scene 06 Fallback - Workshops & Course Preview

| Area | Direction |
| --- | --- |
| Cards | Static workshop dossier cards. |
| CTA | Ask About This Workshop + View Details. |
| Status | Pending content marked internally. |
| Mobile | Stacked cards with visible CTAs. |

Purpose:

Support workshop-specific inquiry without 3D cards, payment behavior, or fake content.

Rules preserved:

- No fake pricing
- No fake dates
- No fake duration unless confirmed
- No fake capacity
- No fake waitlist
- No "Enroll Now" unless real
- No checkout/payment UI

---

## 15. Scene 07 Fallback - Hall of Mentors

| Area | Direction |
| --- | --- |
| Cards | Mentor placeholder-safe editorial cards. |
| Image | Portrait slots only. |
| Text | Confirmed names/bios only later. |
| CTA | Optional ask/register. |
| Mobile | Stacked mentor cards. |

Purpose:

Reserve premium credibility space without inventing people or credentials.

Avoided:

- fake names
- fake credentials
- fake years of experience
- cheap stock-card style

---

## 16. Scene 08 Fallback - Trust / Authority / Credibility

| Area | Direction |
| --- | --- |
| Blocks | Trust/proof blocks. |
| Status | Verified/pending source status internally. |
| CTA | Optional soft ask/register. |
| Mobile | Single-column blocks. |

Purpose:

Create a verified trust structure without manufacturing proof.

Avoided:

- fake testimonials
- fake statistics
- fake partner logos
- "best academy" claims
- animated counters without verified numbers

---

## 17. Scene 09 Fallback - FAQ

| Area | Direction |
| --- | --- |
| FAQ | Semantic/editorial accordion style later. |
| CTA | WhatsApp/Register after FAQ. |
| Visual | Minimal/no distraction. |
| Mobile | Full-width tap-safe FAQ rows. |

FAQ categories represented/planned:

- Who Mithaq is for
- Difference from university/legal study
- Workshop format
- Level suitability
- Registration/contact
- Certificate only if confirmed
- Pricing only if confirmed
- Online/offline only if confirmed

Avoided:

- heavy visual background behind FAQ
- tiny question text
- unconfirmed certificate/pricing facts

---

## 18. Scene 10 Fallback - Final CTA / Closing Covenant

| Area | Direction |
| --- | --- |
| Visual | Static seal/desk closing poster. |
| Text | Final calm conversion message. |
| CTA | WhatsApp primary, Register secondary. |
| Footer | Minimal. |
| Mobile | CTA immediately after heading. |

Purpose:

Close the fallback journey with the Seal motif and a clear low-pressure conversion path.

Avoided:

- countdown
- limited seats
- fake urgency
- too many CTAs
- footer clutter

---

## 19. Fallback CTA Map

| Section | Primary CTA | Secondary CTA |
| --- | --- | --- |
| Scene 01 | WhatsApp/Register by hero | None |
| Scene 02 | WhatsApp/Register | View Workshops/Pillars |
| Scene 03 | Persistent/soft WhatsApp | None/soft |
| Scene 04 | View Pillars | Register soft |
| Scene 05 | View Workshops | Register Interest |
| Scene 06 | Ask About Workshop | View Details |
| Scene 07 | Ask/Register soft | None |
| Scene 08 | Ask/Register soft | None |
| Scene 09 | Ask via WhatsApp | Register Interest |
| Scene 10 | WhatsApp | Register Interest |

CTA rules:

- WhatsApp number remains pending.
- CTAs must be visible as DOM zones later.
- Waitlist hidden/conditional.
- No aggressive urgency language.
- No icon-only primary CTA.

---

## 20. Accessibility Notes

This layout designs toward accessibility but does not claim compliance.

| Requirement | Fallback Design Implication |
| --- | --- |
| Semantic sections | Every scene becomes a normal HTML section later. |
| Heading hierarchy | Each section has a clear heading. |
| Keyboard navigation | Header, CTAs, cards, FAQ, and links reachable later. |
| Visible focus | Component focus states planned via P4.04. |
| Reduced motion | This layout is the reduced-motion equivalent. |
| WebGL fallback | This is the complete non-WebGL experience. |
| Screen reader | All meaning exists as text later. |
| Color contrast | Parchment/ivory on dark planned for AA checks. |
| Mobile tap target | CTA and FAQ rows visually support 44px+ controls. |
| RTL | Arabic layout can mirror/adapt. |

Implementation notes:

- FAQ should become semantic button/region or equivalent later.
- Workshop cards should expose real links/buttons.
- No critical content should be baked into static images.
- Static poster imagery needs alt text or decorative handling depending usage.

---

## 21. RTL / Bilingual Notes

| Area | Requirement |
| --- | --- |
| Direction | Arabic version uses `dir="rtl"` later; English uses `dir="ltr"`. |
| Headings | Arabic headings need extra line-height. |
| CTA labels | Arabic CTA labels must fit at 390px. |
| Text mixing | Arabic/English should not be forced into one line. |
| Language toggle | Present or annotated in header/menu. |
| Cards | Allow Arabic text expansion. |
| FAQ | Allow longer Arabic questions. |
| Images | Do not bake Arabic or English text into static images. |

Stress-test sections represented:

- Hero
- Pillar cards
- Workshop cards
- FAQ
- Final CTA

Arabic examples in the visual board are stress labels only, not final approved copy.

---

## 22. Content Safety Notes

Allowed:

- Draft-level scene messages
- Candidate CTA labels
- Placeholder-safe workshop cards
- Internal pending labels
- Static image placeholders

Not allowed and not used:

- Final copy approval
- Fake WhatsApp number
- Fake workshop facts
- Fake mentor credentials
- Fake testimonials
- Fake stats
- Fake logos
- Fake pricing
- Fake certificate policy
- Fake limited seats
- Fake waitlist

Pending labels used:

- `Workshop title pending`
- `Mentor profile pending`
- `Proof point pending verification`
- `WHATSAPP_NUMBER_PENDING`
- `Certificate policy pending`
- `Pricing pending`

---

## 23. Handoff Notes

| Area | Handoff Note |
| --- | --- |
| Fallback trigger | WebGL unavailable / reduced motion / failed GLB / weak device. |
| Layout | Full editorial 10-section page. |
| Hero image | Static seal/desk poster pending final asset. |
| DOM | All content and CTAs as semantic HTML later. |
| CTA | WhatsApp/Register visible and not canvas-dependent. |
| FAQ | Semantic accordion later. |
| Workshop cards | DOM cards with detail links. |
| Mobile | Single-column fallback. |
| RTL | Logical CSS and `dir` later. |
| Assets | WebP/AVIF optimized later. |
| Implementation phase | P8.17 / P8.20. |

Implementation guardrail:

This document and HTML board are design artifacts only. Do not treat the HTML/CSS in the visual board as production frontend code.

---

## 24. Static Fallback Index Table

| Scene | Desktop Fallback Exists | Mobile Fallback Exists | Static Imagery | CTA Present | Pending Content | Status |
| --- | --- | --- | --- | --- | --- | --- |
| 01 | Yes | Yes | Seal/desk hero poster | Yes | Hero poster, WhatsApp | PASS WITH CONDITIONS |
| 02 | Yes | Yes | Seal editorial anchor | Yes | Final copy/assets | PASS WITH CONDITIONS |
| 03 | Yes | Yes | Document collage | Soft | Final copy | PASS |
| 04 | Yes | Yes | Ordered desk/method poster | Soft | Final copy | PASS |
| 05 | Yes | Yes | Dossier cards | Yes | Final pillar copy | PASS |
| 06 | Yes | Yes | Workshop cards/dossiers | Yes | Workshop details | PASS WITH CONDITIONS |
| 07 | Yes | Yes | Portrait placeholders | Soft | Mentor profiles | PASS WITH CONDITIONS |
| 08 | Yes | Yes | Trust blocks | Soft | Proof/trust assets | PASS WITH CONDITIONS |
| 09 | Yes | Yes | Minimal FAQ texture | Yes | FAQ answers/cert/pricing | PASS WITH CONDITIONS |
| 10 | Yes | Yes | Final seal poster | Yes | WhatsApp/form destination | PASS WITH CONDITIONS |

---

## 25. Quality Gate

| Gate | Status | Notes |
| --- | --- | --- |
| Visual static fallback layout exists | PASS | HTML visual board created. |
| More than Markdown | PASS | Desktop and mobile visual frames exist. |
| All 10 scenes included | PASS | Scene 01-10 represented. |
| Desktop fallback included | PASS | 1440px full page frame. |
| Mobile fallback included | PASS | 390px full page frame. |
| Primary messages preserved | PASS | All scene meanings mapped. |
| Key CTA paths preserved | PASS | WhatsApp/Register/workshop CTAs represented. |
| Premium, not degraded | PASS | Editorial dark visual system used. |
| P4.01 design system used | PASS | Tokens/components followed. |
| P3.06 content priority followed | PASS | No fake content; pending labels used. |
| P3.03 conversion map followed | PASS | CTA map included. |
| P3.05 accessibility supported | PASS WITH CONDITIONS | Design notes included; QA pending. |
| P3.04 mobile rules supported | PASS | 390px mobile fallback included. |
| Fake content avoided | PASS | No invented facts. |
| LMS/course-dashboard UI avoided | PASS | Editorial/dossier treatment. |
| Implementation avoided | PASS | No WebGL/React/reduced-motion code. |
| New roadmap tickets avoided | PASS | No new tickets created. |

---

## 26. Final Recommendation

Recommended fallback direction:

**Premium Editorial Static Fallback**

Use the static fallback as a first-class version of Mithaq, not a degraded technical backup. The fallback should preserve the complete 10-scene story and primary conversion path while removing the risk of WebGL, motion, shader, asset-load, and mobile performance failure.

Implementation posture later:

1. Build fallback as semantic DOM sections.
2. Use final static WebP/AVIF poster assets when available.
3. Ensure fallback is available for reduced motion, failed WebGL, missing GLB, and low-performance devices.
4. Keep WhatsApp/Register CTAs functional independent of canvas.
5. Validate Arabic at 320-390px before launch.
6. Do not expose pending labels publicly in production.

---

## 27. Acceptance Criteria

| Acceptance Criteria | Status |
| --- | --- |
| Static fallback layout package created | PASS |
| Visual output exists beyond Markdown | PASS |
| Desktop static fallback layout exists | PASS |
| Mobile static fallback layout exists | PASS |
| All 10 scenes are represented | PASS |
| Same scene meanings are preserved | PASS |
| Static hero imagery area included | PASS |
| Static final CTA area included | PASS |
| WhatsApp/Register CTAs represented | PASS |
| Workshop cards represented without 3D dependency | PASS |
| FAQ represented as accessible editorial accordion layout | PASS |
| Mentor/trust sections placeholder-safe | PASS |
| RTL/bilingual notes included | PASS |
| Accessibility notes included | PASS |
| Content safety notes included | PASS |
| Handoff notes for P8.17/P8.20 included | PASS |
| Fallback feels premium, not degraded | PASS |
| No WebGL implementation started | PASS |
| No reduced-motion implementation started | PASS |
| No React/CSS production code created | PASS |
| No final assets invented | PASS |
| No fake content used | PASS |
| No new roadmap tickets created | PASS |

---

## 28. Final Status

**PASS WITH CONDITIONS - P4.05 complete. A premium static fallback visual layout exists for desktop and mobile, representing all 10 scenes with static imagery placeholders, DOM-first content zones, CTA paths, accessibility/RTL/mobile notes, and safe handoff guidance.**

Conditions remaining:

- Figma build is pending.
- Final static hero imagery is pending.
- Final seal/logo assets are pending.
- Final workshop content is pending.
- Final mentor/proof content is pending.
- Final WhatsApp number is pending.
- Final Arabic copy/client review is pending.
- Final accessibility QA is pending.
- Final implementation is pending.
- Stakeholder approval is pending.
