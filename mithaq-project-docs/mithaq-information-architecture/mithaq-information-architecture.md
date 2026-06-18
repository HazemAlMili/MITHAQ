# Mithaq Information Architecture Document

**Official Ticket ID:** P3.01  
**Official Ticket Name:** Information Architecture  
**Phase:** Phase 3 - UX / IA / Storyflow Planning  
**Priority:** P0  
**Complexity:** Low  
**Owner:** UX Strategist / Information Architect  
**Status:** PASS WITH CONDITIONS  
**Prepared date:** 2026-06-18  

---

## 1. Executive Summary

This document defines Mithaq's official Information Architecture before storyflow, wireframes, UI comps, or implementation.

Core IA decision:

**Mithaq MVP uses a compact portfolio-first architecture: `/`, `/register`, and `/workshops/[slug]`, supported by WhatsApp-first conversion, a simple inquiry form, bilingual route planning, semantic DOM content, and static/WebGL fallback access.**

The IA intentionally avoids LMS, dashboard, booking, checkout, account, and course-management patterns.

Status is **PASS WITH CONDITIONS** because final IA still depends on final WhatsApp number, final workshop content, final instructor/proof assets, privacy/legal review, and stakeholder approval.

No UI design, wireframes, route files, React components, API implementation, analytics implementation, SEO copy, final content, or new roadmap tickets were created.

---

## 2. Current Mithaq Decisions

- Mithaq is a premium bilingual 3D legal academy portfolio / landing experience.
- Mithaq is not an LMS.
- Mithaq is not a course dashboard.
- Mithaq is not a booking/payment platform.
- Mithaq is not a student portal.
- Primary conversion action: WhatsApp.
- Secondary conversion action: simple inquiry form.
- MVP planning is bilingual.
- Core creative concept: The Covenant Seal.
- Opening direction: Scroll-Driven Seal-Led Opening.
- 3D direction: Seal-Led Macro Legal Chamber.
- Motion direction: Scroll-Led Ceremonial Restraint.
- MVP confirmed routes: `/`, `/register`, `/workshops/[slug]`.
- `/about` and `/instructors` are future/optional unless explicitly approved.
- Workshop content may still be placeholder-based.
- Mentor and trust/proof content may still be placeholder/pending.
- No fake proof.
- No fake urgency.
- No fake seat counters.
- No unsupported claims.
- No final content creation in this task.

---

## 3. IA Principles

| Principle | Meaning |
| --------- | ------- |
| Portfolio-first | Mithaq is a premium presentation experience, not a platform. |
| Conversion-first | Every major path must make WhatsApp or inquiry accessible. |
| DOM-first | Critical meaning must exist in semantic HTML, not canvas-only. |
| Bilingual-ready | Arabic and English routes must be planned from the start. |
| Low-friction | No complex enrollment flow in MVP. |
| No LMS patterns | No dashboards, student accounts, lesson libraries, checkout, or progress tracking. |
| Trust-safe | No fake proof, fake urgency, or invented instructor/workshop claims. |
| Fallback-safe | Every page must work without WebGL. |
| Mobile-clear | Navigation and CTAs must be usable on small screens. |
| SEO-readable | Key page content should be indexable where appropriate. |

---

## 4. MVP Core Routes

| Route | Page Type | Priority | Purpose | Primary CTA | Status |
| ----- | --------- | -------- | ------- | ----------- | ------ |
| `/` | Main landing experience | P0 | 10-scene brand/conversion journey | WhatsApp / Register Interest | MVP Core |
| `/register` | Simple inquiry/register interest page | P0 | Capture structured lead/inquiry | Submit form / WhatsApp | MVP Core |
| `/workshops/[slug]` | Individual workshop detail page | P0/P1 | Show detail for one workshop placeholder/real workshop | Ask via WhatsApp | MVP Core |

Notes:

- Do not add `/workshops` index as MVP Core.
- If `/workshops` is later needed, classify it as deferred or MVP conditional.
- MVP route scope must stay compact to avoid course platform drift.

---

## 5. MVP Supporting Technical Routes

| Route | Type | Purpose | Notes |
| ----- | ---- | ------- | ----- |
| `/api/contact` | Server/API route | Handles simple inquiry form submission | Required only if form is implemented. |
| `/robots.txt` | SEO technical | Search engine crawling guidance | Later technical output. |
| `/sitemap.xml` | SEO technical | Sitemap for indexable pages | Later technical output. |
| `/manifest.webmanifest` | Optional technical | Browser metadata | Optional. |

Do not implement these in this task.

---

## 6. Optional / Deferred Routes

| Route | Page Type | Priority | Why Deferred |
| ----- | --------- | -------- | ------------ |
| `/about` | Brand story / mission page | P2 | Landing page can carry brand story first. |
| `/instructors` | Full mentor listing | P2 | Mentor section can live on homepage first. |
| `/workshops` | Workshop index/listing | P2 or conditional | Not required if individual detail pages are linked from the homepage. |
| `/privacy` | Legal/privacy page | P1/P2 | Required before collecting real user data. |
| `/terms` | Terms page | P2 | Needed if formal enrollment/payment appears later. |
| `/thank-you` | Form confirmation page | P2 | Can be inline confirmation in MVP. |
| `/blog` | Content/archive | Future | Not part of portfolio MVP. |
| `/resources` | Resource library | Future | Risks LMS/content-platform scope. |

---

## 7. Routes Explicitly Out Of Scope

| Route / Feature | Reason Out Of Scope |
| --------------- | ------------------- |
| `/dashboard` | LMS/student portal behavior. |
| `/login` | Not needed for portfolio MVP. |
| `/account` | No user account system. |
| `/checkout` | No payment platform in MVP. |
| `/courses` as full catalog | Risks marketplace/LMS feel. |
| `/lessons/[slug]` | LMS content structure. |
| `/certificates` user verification | Not currently approved. |
| `/calendar-booking` | Not primary conversion. |
| `/admin` | Not part of public portfolio. |
| Student progress pages | Explicitly not a course platform. |

---

## 8. Page-By-Page IA

### 8.1 `/` - Main Landing Experience

| Area | Requirement |
| ---- | ----------- |
| Page purpose | Present Mithaq, build authority, explain gap/method/workshops/mentors/trust, convert. |
| Structure | 10-scene scroll experience. |
| Primary CTA | WhatsApp / Register Interest. |
| Secondary CTA | View workshops / inquiry form. |
| Content source | Scene 01-10 structure from P2.06. |
| 3D layer | Narrative atmosphere only. |
| DOM layer | All critical content. |
| SEO | Indexable main brand page. |
| Fallback | Static editorial version with same meaning. |

Scene list:

1. Scene 01 - Gavel / Seal Opening
2. Scene 02 - Hero / Mithaq Reveal
3. Scene 03 - The Gap
4. Scene 04 - The Mithaq Method
5. Scene 05 - Training Pillars
6. Scene 06 - Workshops & Course Preview
7. Scene 07 - Hall of Mentors
8. Scene 08 - Trust / Authority / Credibility
9. Scene 09 - FAQ
10. Scene 10 - Final CTA / Closing Covenant

### 8.2 `/register` - Register Interest / Inquiry Page

| Area | Requirement |
| ---- | ----------- |
| Page purpose | Let users express interest without complexity. |
| Primary CTA | Submit inquiry. |
| Secondary CTA | WhatsApp. |
| Form fields | Name, phone/WhatsApp, interest area, optional message. |
| Form style | Simple and low-friction. |
| Not allowed | Account creation, payment, course selection complexity. |
| Success state | Inline success or optional future thank-you page. |
| SEO | Indexable or noindex pending final strategy. |
| Fallback | Normal HTML form. |

Recommended fields:

| Field | Required? | Notes |
| ----- | --------- | ----- |
| Name | Required | Text input. |
| Phone / WhatsApp | Required | Phone input. |
| Email | Optional | Useful but do not overcomplicate. |
| Interest area | Optional | Dropdown or radio. |
| Preferred language | Optional | Arabic / English. |
| Message | Optional | Textarea. |

### 8.3 `/workshops/[slug]` - Workshop Detail Page

| Area | Requirement |
| ---- | ----------- |
| Page purpose | Explain one workshop clearly and invite inquiry. |
| Primary CTA | Ask About This Workshop via WhatsApp. |
| Secondary CTA | Register Interest / Back to workshops section. |
| Content status | Placeholder-safe until real workshops are confirmed. |
| Structure | Detail page, not LMS lesson page. |
| Not allowed | Lesson dashboard, checkout, progress, locked content. |
| SEO | Indexable if workshop is real; noindex if placeholder. |
| Fallback | Full HTML content works without 3D. |

Recommended sections:

1. Workshop hero
2. Who it is for
3. Skills covered
4. Format / level / duration placeholder
5. Mentor/instructor placeholder if available
6. What you will be able to do after
7. FAQ related to the workshop
8. WhatsApp CTA
9. Related workshops, optional

Rules:

- Do not invent workshop facts.
- Unknowns must be marked as pending content confirmation.
- Do not create lesson/module/payment structures.

---

## 9. Optional Page IA

### `/about`

Purpose:

- Explain Mithaq's mission, covenant concept, and philosophy.

Status:

- Deferred unless stakeholder requests.

### `/instructors`

Purpose:

- Full mentor listing.

Status:

- Deferred unless instructor content/photos are ready.

### `/workshops`

Purpose:

- Workshop listing/index.

Status:

- Deferred or conditional depending on number of confirmed workshops.

### `/privacy`

Purpose:

- Privacy policy for data collection.

Status:

- Recommended before public launch if collecting form data.

---

## 10. Content Types

| Content Type | Used On | Fields | Status |
| ------------ | ------- | ------ | ------ |
| Scene content | `/` | scene id, heading, body, CTA, fallback copy | Placeholder/planned |
| Workshop | `/`, `/workshops/[slug]` | title, slug, level, format, skills, description, CTA | Placeholder until confirmed |
| Mentor | `/` and optional `/instructors` | name, role, bio, expertise, image, proof status | Placeholder/pending |
| FAQ item | `/`, `/workshops/[slug]` | question, answer, category | Planned |
| Trust proof | `/` | proof type, value, source, approval status | Pending verification |
| CTA | all routes | label, destination, type, tracking id | Planned |
| Navigation item | header/mobile/footer | label, destination, anchor, visibility | Planned |
| Locale dictionary | all routes | key, ar, en | Required for bilingual MVP |
| Form inquiry | `/register` | name, phone, email, interest, message | Planned |
| Static fallback content | `/` | scene id, text, poster image, alt text | Required later |

---

## 11. Content Type Rules

- Every workshop must have a slug.
- Every workshop detail page must work without 3D.
- Every mentor must be marked as confirmed or placeholder.
- Every trust proof must have a source/approval status.
- Every CTA must have a clear destination.
- Every route must have Arabic and English content keys.
- No critical copy should be stored only inside a 3D texture.
- No fake testimonials or metrics.
- No fake urgency or seat counts.
- Placeholder content must be visibly labeled in internal docs.

---

## 12. Navigation Architecture

### 12.1 Desktop Header

| Nav Item | Destination | Type | Notes |
| -------- | ----------- | ---- | ----- |
| Workshops | `/#workshops` or `/workshops/[slug]` entry points | Anchor/link | Must not imply full catalog if not built. |
| Method | `/#method` | Anchor | Scene 04. |
| Mentors | `/#mentors` | Anchor | Scene 07. |
| FAQ | `/#faq` | Anchor | Scene 09. |
| Register Interest | `/register` | Button | P0 CTA. |
| Language Toggle | `/ar` / `/en` equivalent | Control | Required for bilingual MVP. |

Rules:

- Keep primary nav minimal.
- No mega-menu.
- No LMS/course-dashboard links.

### 12.2 Mobile Navigation

| Item | Destination | Notes |
| ---- | ----------- | ----- |
| Home | `/` | Optional if logo already acts as home. |
| Workshops | `/#workshops` | Anchor. |
| Method | `/#method` | Anchor. |
| Mentors | `/#mentors` | Anchor. |
| FAQ | `/#faq` | Anchor. |
| Register Interest | `/register` | Prominent. |
| WhatsApp | WhatsApp deep link | Prominent. |
| Language Toggle | Arabic/English | Accessible. |

Mobile rules:

- Hamburger or simple full-screen overlay.
- Close button must be visible.
- Keyboard focus must be managed later.
- Tap targets must be at least 44px.
- Do not hide WhatsApp deep link.
- Do not make menu dependent on canvas/WebGL.

### 12.3 Footer / Closing Navigation

| Link | Destination | Priority |
| ---- | ----------- | -------- |
| Register Interest | `/register` | P0 |
| WhatsApp | WhatsApp deep link | P0 |
| Workshops | `/#workshops` | P1 |
| FAQ | `/#faq` | P1 |
| Privacy | `/privacy` if live form exists | P1 |
| Language Toggle | Arabic/English | P0 |

Footer rule:

- Keep footer minimal and premium.
- Avoid footer clutter and platform-style link farms.

---

## 13. CTA Architecture

| CTA Type | Destination | Used On | Priority |
| -------- | ----------- | ------- | -------- |
| WhatsApp primary | WhatsApp deep link | Global, hero, workshops, final CTA | P0 |
| Register Interest | `/register` | Header, hero, final CTA | P0 |
| View Workshop Details | `/workshops/[slug]` | Workshop cards | P0/P1 |
| Ask About This Workshop | WhatsApp prefilled message | Workshop cards/detail page | P0 |
| View Method | `/#method` | Hero/supporting | P1 |
| Back to Home | `/` | Detail/register pages | P1 |

CTA rules:

- Low-pressure only.
- No fake scarcity.
- No aggressive pulsing CTA.
- No "limited seats" unless real and verified.

---

## 14. WhatsApp Conversion Architecture

Use placeholder:

`WHATSAPP_NUMBER_PENDING`

Do not invent the final number.

| Location | WhatsApp CTA Purpose | Message Intent |
| -------- | -------------------- | -------------- |
| Global floating CTA | Fast contact anytime | General inquiry. |
| Hero | Immediate interest | "I want to know more about Mithaq." |
| Workshops section | Workshop-specific inquiry | "I'm interested in this workshop." |
| Workshop detail page | Specific workshop lead | Include workshop slug/title. |
| Final CTA | Conversion close | "I want to register interest." |
| Register page | Alternative to form | "I prefer WhatsApp contact." |

Architecture notes:

- WhatsApp should be visible, not desperate.
- Prefilled messages must be localized later.
- Workshop-specific messages should include confirmed workshop title/slug only.

---

## 15. Inquiry Form Architecture

| Field | Type | Required | Notes |
| ----- | ---- | -------- | ----- |
| Name | Text | Yes | Basic identity field. |
| Phone / WhatsApp | Tel | Yes | Primary contact. |
| Email | Email | No | Optional. |
| Interest area | Select/radio | No | Workshop/general/mentor/institution. |
| Preferred language | Select/radio | No | Arabic/English. |
| Message | Textarea | No | Optional. |

Form rules:

- No account creation.
- No password.
- No payment.
- No complex enrollment.
- No file upload unless later approved.
- Inline success state acceptable.
- Privacy note required before launch.
- Spam protection to be decided later.

---

## 16. Workshop Detail Architecture

| Section | Purpose |
| ------- | ------- |
| Workshop title | Identify workshop. |
| Level | Clarify fit. |
| Format | Online/live/hybrid placeholder. |
| Skills covered | Practical outcomes. |
| Who it is for | Persona fit. |
| What you will learn | Value clarity. |
| Mentor/instructor | Trust if available. |
| FAQ | Objection handling. |
| CTA | WhatsApp / Register interest. |
| Related workshops | Optional. |

Rules:

- Do not create lesson pages.
- Do not create module dashboard.
- Do not create payment checkout.
- Do not fake duration/capacity/pricing.
- If content is unknown, mark as pending.

---

## 17. Bilingual / i18n Architecture

### Option A - Locale Prefix

| Route | Arabic | English |
| ----- | ------ | ------- |
| Home | `/ar` | `/en` |
| Register | `/ar/register` | `/en/register` |
| Workshop detail | `/ar/workshops/[slug]` | `/en/workshops/[slug]` |

### Option B - Default Locale + Prefixed Secondary

| Route | Arabic Default | English |
| ----- | -------------- | ------- |
| Home | `/` | `/en` |
| Register | `/register` | `/en/register` |
| Workshop detail | `/workshops/[slug]` | `/en/workshops/[slug]` |

Recommendation:

**Use Arabic-first content structure and keep bilingual routing explicit. Option B is recommended if Arabic is the default market language; Option A is cleaner if stakeholders want equal locale visibility.**

Final locale decision can remain pending until technical implementation starts.

Required i18n notes:

- Set `dir="rtl"` for Arabic.
- Set `dir="ltr"` for English.
- Use CSS logical properties.
- Do not bake translated text into 3D textures.
- Keep locale dictionaries for all scene content and CTAs.
- Workshop slugs may be English-safe for technical stability, with localized titles in content.
- Meta tags should be localized.
- `hreflang` should be planned later for SEO.

---

## 18. SEO Route Notes

| Route | Indexing Recommendation | SEO Notes |
| ----- | ----------------------- | --------- |
| `/` | Index | Main brand/landing page. |
| `/register` | Index or noindex pending strategy | Could be conversion-only. |
| `/workshops/[slug]` | Index only if real content exists | Noindex if placeholder. |
| `/about` | Future index | If created. |
| `/instructors` | Future index | If created. |
| `/privacy` | Index/noindex depending policy | Required for trust/legal. |

Do not write final meta copy in this task. That belongs to a later SEO/content ticket.

---

## 19. Accessibility IA Notes

- Header nav must be semantic.
- Mobile menu must be keyboard accessible later.
- CTA links must be real links/buttons, not canvas hotspots only.
- FAQ should use semantic accordion structure later.
- Workshop cards must be keyboard reachable later.
- Register form must have labels and error states later.
- Language toggle must announce language clearly.
- Skip-to-content link should be planned.
- Reduced-motion path must not remove content.
- WebGL fallback must preserve all core IA paths.
- Canvas must never be the only navigation path.

---

## 20. Static Fallback IA Notes

For WebGL-disabled/reduced-motion users:

- `/` still includes all 10 sections as editorial content.
- Hero still has headline, support copy, and CTA.
- Workshop section still links to `/workshops/[slug]`.
- FAQ remains accessible.
- Register page remains normal HTML.
- WhatsApp CTA remains visible.
- No IA path should depend on 3D.

---

## 21. Analytics Event Architecture Notes

This is not implementation.

| Event Name | Trigger | Route |
| ---------- | ------- | ----- |
| `cta_whatsapp_click` | WhatsApp CTA clicked | all routes |
| `cta_register_interest_click` | Register Interest clicked | `/`, workshop pages |
| `workshop_detail_click` | Workshop detail link clicked | `/` |
| `workshop_whatsapp_click` | Workshop-specific WhatsApp clicked | `/`, `/workshops/[slug]` |
| `form_submit_attempt` | Register form submit attempted | `/register` |
| `form_submit_success` | Register form submitted successfully | `/register` |
| `language_toggle_click` | User switches language | all routes |
| `faq_open` | FAQ item opened | `/`, workshop pages |
| `reduced_motion_enabled` | Reduced motion path active | all routes |
| `webgl_fallback_rendered` | Static fallback used | `/` |

Do not implement analytics in this task.

---

## 22. Sitemap Table

| Route | Locale Variant | Priority | Page Owner | Content Source | CTA | Status |
| ----- | -------------- | -------- | ---------- | -------------- | --- | ------ |
| `/` | Arabic/English | P0 | UX/Content | Scenes 01-10 | WhatsApp/Register | MVP |
| `/register` | Arabic/English | P0 | UX/Conversion | Form fields | Submit/WhatsApp | MVP |
| `/workshops/[slug]` | Arabic/English | P0/P1 | Content/UX | Workshop content | WhatsApp | MVP/conditional |
| `/about` | Arabic/English | P2 | Content | Brand story | Register/WhatsApp | Deferred |
| `/instructors` | Arabic/English | P2 | Content | Mentor bios | Register/WhatsApp | Deferred |
| `/privacy` | Arabic/English | P1/P2 | Legal/Ops | Privacy policy | N/A | Required before live data collection |
| `/workshops` | Arabic/English | P2 | Content/UX | Workshop index | Workshop CTAs | Deferred/conditional |

---

## 23. IA Guardrail Table

| Keep | Avoid |
| ---- | ----- |
| Portfolio landing architecture | LMS/course dashboard architecture |
| `/`, `/register`, `/workshops/[slug]` as MVP core | Adding every possible page to MVP |
| WhatsApp as primary conversion | Complex application/payment funnel |
| Simple inquiry form | Account creation |
| Bilingual route planning | Arabic as afterthought |
| DOM-first content routes | Canvas-only navigation |
| Workshop detail pages | Lesson/module pages |
| Optional `/about` and `/instructors` | Unapproved scope expansion |
| Static fallback IA | WebGL-dependent content access |
| Verified proof architecture | Fake testimonials/stats |

---

## 24. Final IA Recommendation

| Decision Area | Recommendation |
| ------------- | -------------- |
| MVP route scope | Keep MVP core to `/`, `/register`, and `/workshops/[slug]`. |
| Optional route handling | Document `/about`, `/instructors`, `/workshops`, `/privacy`, `/terms`, `/thank-you`, `/blog`, and `/resources` as deferred/conditional/future. |
| Primary conversion architecture | WhatsApp-first, available globally, in hero, workshops, detail pages, final CTA, and register page. |
| Secondary conversion architecture | Simple inquiry/register interest form at `/register`. |
| Workshop detail route strategy | Use `/workshops/[slug]` for real or placeholder-safe workshop pages; noindex placeholders. |
| Bilingual route strategy | Arabic-first content structure; choose Option B unless stakeholders prefer equal locale prefixes. |
| Navigation model | Minimal anchors plus Register Interest and language toggle; no mega-menu. |
| Footer model | Minimal premium closing navigation with WhatsApp, Register, Workshops, FAQ, Privacy if needed, and language toggle. |
| Static fallback IA | All content paths must work without WebGL; `/` becomes editorial static version. |
| SEO route status | Index `/`; conditionally index `/register`; index workshops only when real; future pages index when approved. |

Final IA position:

Mithaq should remain a premium conversion-focused portfolio/landing experience, not a platform. IA must protect the Covenant Seal narrative, WhatsApp-first conversion, bilingual readiness, accessibility, SEO clarity, and static fallback access while preventing LMS/dashboard scope creep.

---

## 25. Quality Gate

| Gate | Status | Notes |
| ---- | ------ | ----- |
| MVP route scope clear | PASS | `/`, `/register`, `/workshops/[slug]`. |
| Deferred routes labeled | PASS | Optional/deferred table included. |
| Out-of-scope routes documented | PASS | Explicit out-of-scope table included. |
| Navigation architecture defined | PASS | Desktop/mobile/footer included. |
| Mobile navigation addressed | PASS | Mobile rules included. |
| WhatsApp primary conversion represented | PASS | Dedicated architecture included. |
| Register/inquiry form architecture documented | PASS | Fields and rules included. |
| Workshop detail architecture documented | PASS | Sections and rules included. |
| Bilingual/i18n architecture included | PASS | Two route options and recommendation included. |
| Content types documented | PASS | Content type table included. |
| SEO route notes included | PASS | SEO table included. |
| Accessibility IA notes included | PASS | Dedicated section included. |
| Static fallback IA notes included | PASS | Dedicated section included. |
| Analytics event notes included | PASS | Event architecture table included. |
| Avoids LMS/dashboard scope | PASS | Guardrails and out-of-scope routes included. |
| Avoids fake content/proof/urgency | PASS | Content rules and guardrails included. |
| Avoided UI design and implementation | PASS | No UI/routes/code created. |

---

## 26. Acceptance Criteria

| Acceptance Criteria | Status |
| ------------------- | ------ |
| IA document created | PASS |
| MVP core routes defined | PASS |
| Supporting technical routes documented | PASS |
| Deferred/optional routes documented | PASS |
| Out-of-scope routes documented | PASS |
| Page-by-page IA complete | PASS |
| Content types documented | PASS |
| Navigation architecture complete | PASS |
| CTA architecture complete | PASS |
| WhatsApp architecture complete | PASS |
| Inquiry form architecture complete | PASS |
| Workshop detail architecture complete | PASS |
| Bilingual/i18n architecture included | PASS |
| SEO route notes included | PASS |
| Accessibility IA notes included | PASS |
| Static fallback IA included | PASS |
| Sitemap table complete | PASS |
| Final IA recommendation clear | PASS |
| IA guardrail table included | PASS |
| No UI design started | PASS |
| No frontend implementation started | PASS |
| No new roadmap tickets created | PASS |

---

## 27. Final Status

**PASS WITH CONDITIONS - P3.01 complete. Full IA document covers pages, routes, content types, navigation, CTA architecture, WhatsApp/form flows, bilingual/i18n architecture, accessibility, SEO, and fallback IA.**

Final IA remains conditional on final WhatsApp number, final workshop content, final instructor/proof assets, privacy/legal review, and stakeholder approval.
