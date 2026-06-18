# Mithaq Conversion Funnel Map

**Official Ticket ID:** P3.03  
**Official Ticket Name:** Conversion Funnel Map  
**Phase:** Phase 3 - UX / IA / Storyflow Planning  
**Owner:** UX Strategist / Conversion Strategist  
**Status:** PASS WITH CONDITIONS  
**Date:** 2026-06-19  
**Scope:** Main route `/` plus MVP conversion routes `/register` and `/workshops/[slug]`

---

## 1. Executive Summary

This document defines Mithaq's official conversion funnel map across the 10-scene landing experience and supporting MVP routes.

The funnel keeps Mithaq premium, calm, and low-pressure:

- **WhatsApp** is the active primary conversion path.
- **Register Interest / inquiry form** is the active secondary conversion path on `/register`.
- **Inquiry** is active through WhatsApp and form-based categories.
- **Waitlist** is mapped only as a future/conditional path until a real waitlist, cohort, capacity, follow-up process, privacy language, and data destination are approved.

Final funnel position:

**Use a WhatsApp-first conversion model with persistent access, contextual workshop inquiries, a simple `/register` form for structured interest, and no active waitlist or urgency language until real operational details exist.**

Status is **PASS WITH CONDITIONS** because final conversion implementation still depends on the final WhatsApp number, form destination, privacy/legal wording, final workshop content, stakeholder approval, and a confirmed waitlist decision.

This is UX/conversion planning only. No CTAs, forms, analytics, backend routes, final copy, or UI comps are implemented.

---

## 2. Current Mithaq Decisions

| Area | Current Decision |
| --- | --- |
| Product type | Premium bilingual 3D legal academy portfolio / landing experience. |
| Not in scope | LMS, student dashboard, booking system, checkout flow, account system, or course platform. |
| Primary conversion | WhatsApp. |
| Secondary conversion | Simple inquiry / Register Interest form. |
| MVP routes | `/`, `/register`, `/workshops/[slug]`. |
| Landing structure | 10-scene scroll storyflow. |
| 3D/UX priority | Scene 01-02 are vertical-slice priority. |
| Workshop behavior | Preview on landing plus `/workshops/[slug]` detail pages. |
| Bilingual planning | Arabic and English labels and flows must be planned separately. |
| Waitlist status | Conditional / not active by default. |
| WhatsApp number | `WHATSAPP_NUMBER_PENDING`. |
| Trust/proof rule | No fake claims, fake testimonials, fake stats, or unsupported authority. |
| Urgency rule | No fake urgency, seat counters, countdowns, or cohort/deadline pressure. |

WhatsApp placeholder:

```text
https://wa.me/WHATSAPP_NUMBER_PENDING
```

Do not replace this placeholder until the final number is provided.

---

## 3. Conversion Principles

| Principle | Meaning |
| --- | --- |
| WhatsApp-first | WhatsApp is the clearest and lowest-friction action. |
| Low-pressure conversion | CTAs should feel premium, helpful, and calm. |
| No fake scarcity | No "limited seats" unless real and verified. |
| Contextual CTAs | CTA must match the scene's user intent. |
| Always-accessible path | A user should never struggle to contact Mithaq. |
| Form as secondary | Form is structured but not the only route. |
| Workshop-specific inquiry | Workshop CTAs should pass workshop context. |
| DOM-first CTAs | CTAs must be real DOM links/buttons. |
| Mobile-first conversion | WhatsApp path must be obvious on phones. |
| Bilingual-safe labels | Arabic/English labels must be planned separately. |
| Track later, not now | Analytics events are planned, not implemented. |

---

## 4. Active vs Conditional Conversion Paths

| Path | MVP Status | Role | Notes |
| --- | --- | --- | --- |
| WhatsApp | Active Primary | Fast contact, workshop questions, mobile conversion. | Uses placeholder number until confirmed. |
| Registration / Register Interest Form | Active Secondary | Structured lead capture on `/register`. | Simple form only; no account or payment. |
| Inquiry | Active Secondary | General questions, suitability questions, institutional questions. | Can happen through WhatsApp or `/register`. |
| Waitlist | Conditional / Future | Only if a real waitlist/cohort/capacity process exists. | Not a live MVP promise. |

Waitlist activation requires:

- Real waitlist exists.
- Real cohort or launch schedule exists.
- Real follow-up process exists.
- Data destination is confirmed.
- Privacy/legal language is ready.

Until then, waitlist remains:

```text
Future / Conditional Path
```

---

## 5. Funnel Stage Model

| Funnel Stage | Scenes | Visitor State | Primary Goal |
| --- | --- | --- | --- |
| Awareness | Scene 01-02 | "This feels premium and serious." | Establish authority and clarity. |
| Problem Recognition | Scene 03 | "This gap applies to me." | Make pain visible. |
| Solution Understanding | Scene 04-05 | "Mithaq has a practical method." | Explain method and pillars. |
| Offer Interest | Scene 06 | "Which workshop fits me?" | Drive workshop-specific action. |
| Trust Building | Scene 07-08 | "Can I trust who is behind this?" | Build confidence without fake proof. |
| Objection Handling | Scene 09 | "What do I still need to know?" | Remove friction. |
| Conversion | Scene 10 + persistent CTAs | "I'm ready to ask/register." | WhatsApp or form action. |

---

## 6. Persona-to-Conversion Map

| Persona | Likely Primary Path | Secondary Path | Best CTA Moment | Main Objection Before Conversion |
| --- | --- | --- | --- | --- |
| Law Graduate / Job-Seeking Fresh Graduate | WhatsApp / Register Interest | Workshop detail | Scene 05-06 / Scene 10 | "Is this useful for starting my career?" |
| Junior Lawyer / Trainee Lawyer | Workshop-specific WhatsApp | Workshop detail page | Scene 06 | "Is this practical enough for real work?" |
| Career-Changer / Adjacent Professional | Inquiry form / WhatsApp | Register Interest | Scene 04-05 / Scene 09 | "Is this suitable for my level?" |

| Persona | Needed Proof Before Action | Recommended CTA Tone |
| --- | --- | --- |
| Law Graduate | Practical outcomes, level clarity, mentor credibility. | Supportive and confidence-building. |
| Junior Lawyer | Real practice relevance and instructor credibility. | Direct and practical. |
| Career-Changer | Level fit, prerequisites, clarity, no intimidation. | Clear and reassuring. |

Persona conversion guidance:

- Law graduates need low-pressure language and reassurance that asking does not mean a hard commitment.
- Junior lawyers need workshop-specific context and practical relevance.
- Career-changers need suitability language and a safe inquiry route before registering.

---

## 7. Four Conversion Paths

### 7.1 Path A - WhatsApp

| Field | Direction |
| --- | --- |
| Status | Active MVP Primary |
| Purpose | Fastest contact path; best for mobile users, workshop-specific questions, and users who prefer not to fill a form. |
| Required behavior | Global/persistent access after safe point; visible in Hero, Workshops, FAQ, and Final CTA. |
| Workshop behavior | Use workshop-specific prefill intent where title/slug is confirmed. |
| Accessibility | Real link/button, clear Arabic/English accessible label, not canvas-only. |
| Technical placeholder | `https://wa.me/WHATSAPP_NUMBER_PENDING` |

### 7.2 Path B - Registration / Register Interest Form

| Field | Direction |
| --- | --- |
| Status | Active MVP Secondary |
| Purpose | Structured lead capture for users who prefer a form. |
| Route | `/register` |
| Required behavior | Header CTA, hero CTA, final CTA, and workshop detail secondary CTA may link to `/register`. |
| Form style | Simple and low-friction. |
| Avoid | Account creation, payment, course dashboard, long application flow. |

### 7.3 Path C - Waitlist

| Field | Direction |
| --- | --- |
| Status | Conditional / Future |
| Purpose | Only useful if Mithaq has real cohorts, launch dates, or capacity model. |
| Current rule | Do not promote waitlist as an active MVP CTA. |
| Required mapping | Document future locations, but mark inactive/conditional. |
| Avoid | Fake scarcity, implied limited seats, unsupported launch promises. |

Potential future locations:

| Location | Future Waitlist Use |
| --- | --- |
| Scene 06 | Join waitlist for a specific workshop. |
| `/workshops/[slug]` | Join waitlist if workshop is not currently open. |
| Scene 10 | Join future cohort waitlist. |
| `/register` | Select "Waitlist" as interest type only if approved. |

### 7.4 Path D - Inquiry

| Field | Direction |
| --- | --- |
| Status | Active MVP Secondary |
| Purpose | General questions, institution/company inquiries, mentor/workshop questions, career-fit questions. |
| Entry points | WhatsApp, `/register` form, workshop-specific WhatsApp, future inquiry category in form. |
| Required behavior | Low-friction; do not force users into "registration" if they only want to ask. |
| CTA tone | Helpful and consultative. |

---

## 8. Scene-by-Scene Funnel Map

| Scene | Funnel Stage | WhatsApp Path | Register Form Path | Waitlist Path | Inquiry Path | CTA Priority | Accessibility Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 01 - Opening | Awareness | Available by handoff/fallback. | Available by handoff. | Hidden/Inactive. | Hidden/Inactive. | Low/Medium | CTA must not be canvas-only. |
| 02 - Hero | Awareness | Visible. | Visible. | Hidden/Inactive. | Secondary. | High | Real links/buttons. |
| 03 - The Gap | Problem Recognition | Persistent only. | Not primary. | Hidden/Inactive. | Soft only. | Low | Do not interrupt story. |
| 04 - Method | Solution Understanding | Persistent. | Soft. | Hidden/Inactive. | Soft. | Medium | Link text clear. |
| 05 - Pillars | Solution Understanding | Visible. | Visible/soft. | Hidden/Inactive. | Soft. | Medium/High | Cards keyboard reachable later. |
| 06 - Workshops | Offer Interest | Strong, workshop-specific. | Secondary. | Conditional future only. | Strong. | Highest | CTA per card accessible. |
| 07 - Mentors | Trust Building | Persistent/soft. | Optional. | Hidden/Inactive. | Optional. | Medium | No fake credentials. |
| 08 - Trust | Trust Building | Persistent/soft. | Optional. | Hidden/Inactive. | Optional. | Medium | No fake proof. |
| 09 - FAQ | Objection Handling | Visible. | Visible. | Hidden/Inactive. | Visible. | High | FAQ + CTA keyboard accessible later. |
| 10 - Final CTA | Conversion | Primary. | Primary/secondary. | Conditional only. | Secondary. | Highest | CTA visible without animation. |

---

## 9. Scene-Specific Conversion Notes

### Scene 01 - Opening

Conversion intent:

- Do not sell too early.
- Allow CTA by handoff.
- In fallback/reduced-motion, CTA should appear earlier.

| CTA | Status |
| --- | --- |
| WhatsApp | Visible by end / persistent after safe point. |
| Register Interest | Visible by end or Scene 02. |
| Waitlist | Not visible. |
| Inquiry | Not visible or soft only. |

### Scene 02 - Hero

Conversion intent:

- First clear conversion moment.
- Visitor understands what Mithaq is and can act immediately.

| CTA | Status |
| --- | --- |
| WhatsApp | Primary or co-primary. |
| Register Interest | Primary or secondary. |
| Waitlist | Not active. |
| Inquiry | Secondary wording possible. |

### Scene 03 - The Gap

Conversion intent:

- Build recognition, not pressure.
- Keep persistent WhatsApp available but avoid aggressive CTAs.

| CTA | Status |
| --- | --- |
| WhatsApp | Persistent only. |
| Register Interest | Not primary. |
| Waitlist | Hidden. |
| Inquiry | Optional soft "ask if this fits you" style later. |

### Scene 04 - Method

Conversion intent:

- Move from problem to solution.
- Soft CTA acceptable.

| CTA | Status |
| --- | --- |
| WhatsApp | Persistent. |
| Register Interest | Soft. |
| Waitlist | Hidden. |
| Inquiry | Soft. |

### Scene 05 - Training Pillars

Conversion intent:

- User starts choosing relevance.
- CTA can guide toward workshops.

| CTA | Status |
| --- | --- |
| WhatsApp | Visible. |
| Register Interest | Secondary. |
| Waitlist | Hidden. |
| Inquiry | Soft. |
| View Workshops | Strong internal CTA. |

### Scene 06 - Workshops

Conversion intent:

- Highest workshop-specific conversion scene.
- Each workshop card must support WhatsApp and detail view.

| CTA | Status |
| --- | --- |
| WhatsApp | Strong, workshop-specific. |
| Register Interest | Secondary. |
| Waitlist | Conditional future only. |
| Inquiry | Strong. |
| View Details | Strong. |

### Scene 07 - Hall of Mentors

Conversion intent:

- Trust reinforcement.
- CTA should be calm and optional.

| CTA | Status |
| --- | --- |
| WhatsApp | Persistent/soft. |
| Register Interest | Optional. |
| Waitlist | Hidden. |
| Inquiry | Optional. |

### Scene 08 - Trust / Credibility

Conversion intent:

- Reassure without fake claims.
- CTA should not depend on fake proof.

| CTA | Status |
| --- | --- |
| WhatsApp | Persistent/soft. |
| Register Interest | Optional. |
| Waitlist | Hidden. |
| Inquiry | Optional. |

### Scene 09 - FAQ

Conversion intent:

- Remove final objections.
- CTA should be clearly visible after questions.

| CTA | Status |
| --- | --- |
| WhatsApp | Visible. |
| Register Interest | Visible. |
| Waitlist | Hidden. |
| Inquiry | Visible. |

### Scene 10 - Final CTA

Conversion intent:

- Main closing action.
- WhatsApp and Register Interest must be unmistakable.
- Waitlist only appears if real.

| CTA | Status |
| --- | --- |
| WhatsApp | Primary. |
| Register Interest | Primary/secondary. |
| Waitlist | Conditional only. |
| Inquiry | Secondary. |

---

## 10. CTA Visibility Map

| Location | WhatsApp | Register Form | Waitlist | Inquiry |
| --- | --- | --- | --- | --- |
| Header desktop | Visible or CTA slot. | Visible or CTA slot. | Hidden. | Indirect through WhatsApp/register. |
| Header mobile | Visible in menu and/or floating CTA. | Visible in menu. | Hidden. | Indirect through WhatsApp/register. |
| Floating CTA | WhatsApp primary. | Not floating by default. | Hidden. | General WhatsApp inquiry. |
| Scene 01 | By handoff / fallback early. | By handoff or Scene 02. | Hidden. | Hidden/soft only. |
| Scene 02 | Visible. | Visible. | Hidden. | Secondary. |
| Scene 03 | Persistent only. | Not primary. | Hidden. | Soft only. |
| Scene 04 | Persistent. | Soft. | Hidden. | Soft. |
| Scene 05 | Visible. | Secondary. | Hidden. | Soft. |
| Scene 06 | Strong per workshop. | Secondary. | Conditional future only. | Strong. |
| Scene 07 | Persistent/soft. | Optional. | Hidden. | Optional. |
| Scene 08 | Persistent/soft. | Optional. | Hidden. | Optional. |
| Scene 09 | Visible. | Visible. | Hidden. | Visible. |
| Scene 10 | Primary. | Primary/secondary. | Conditional only. | Secondary. |
| `/register` | Secondary alternative. | Primary form submit. | Conditional field only. | Primary/secondary depending category. |
| `/workshops/[slug]` | Primary workshop CTA. | Secondary. | Conditional if real. | Workshop question. |
| Footer | Visible. | Visible. | Hidden. | Visible through form/WhatsApp. |
| Static fallback | Visible. | Visible at key points. | Hidden. | Visible through WhatsApp/register. |

---

## 11. WhatsApp Conversion Map

| WhatsApp Entry Point | User Intent | Suggested Prefill Intent | Required Context |
| --- | --- | --- | --- |
| Header / floating CTA | General inquiry. | "I want to know more about Mithaq." | Locale. |
| Hero CTA | Brand interest. | "I'm interested in Mithaq training." | Locale. |
| Pillars CTA | Skill interest. | "I want to know which track fits me." | Selected pillar if applicable. |
| Workshop card CTA | Workshop-specific. | "I'm interested in [Workshop Title]." | Workshop title/slug. |
| Workshop detail CTA | Workshop-specific. | "I want details about [Workshop Title]." | Workshop title/slug. |
| FAQ CTA | Objection/question. | "I have a question about Mithaq." | Locale. |
| Final CTA | Register interest. | "I want to register interest in Mithaq." | Locale. |
| Register page alternative | Prefer WhatsApp. | "I prefer to continue through WhatsApp." | Locale. |

Important:

- These are message intents, not final approved copy.
- Use `WHATSAPP_NUMBER_PENDING` until the final number is supplied.
- Workshop-specific messages must include only confirmed workshop titles/slugs.
- WhatsApp links must remain reachable without WebGL.

---

## 12. Registration Form Funnel Map

| Step | User Action | UX Requirement | Risk |
| ---: | --- | --- | --- |
| 1 | Click Register Interest. | Clear route to `/register`. | CTA ambiguity. |
| 2 | Read short intro. | Explain low-friction inquiry. | Feels like full enrollment. |
| 3 | Fill required fields. | Name + phone only required. | Too many fields. |
| 4 | Optional interest area. | Workshop/general/mentor/institution. | Confusing taxonomy. |
| 5 | Submit. | Clear success state. | No confirmation. |
| 6 | Follow-up path. | WhatsApp alternative remains visible. | User waits without clarity. |

Required form fields:

| Field | Required | Notes |
| --- | --- | --- |
| Name | Yes | Simple. |
| Phone / WhatsApp | Yes | Primary contact. |
| Email | No | Optional. |
| Interest area | No | Dropdown/radio. |
| Preferred language | No | Arabic/English. |
| Message | No | Optional. |

Form rules:

- Do not implement the form in this task.
- Do not decide backend destination unless already confirmed.
- Do not imply payment, account creation, or enrollment.
- Keep the form useful for both registration interest and inquiries.

---

## 13. Inquiry Funnel Map

| Inquiry Type | Best Entry Point | Destination |
| --- | --- | --- |
| General Mithaq question | Header / Hero / FAQ | WhatsApp or `/register`. |
| Workshop question | Scene 06 / workshop page | Workshop-specific WhatsApp. |
| Suitability question | Scene 04 / FAQ | WhatsApp. |
| Mentor/instructor question | Scene 07 | WhatsApp or form. |
| Institutional/corporate inquiry | `/register` form | Form. |
| Technical/contact issue | Footer/register page | Form/WhatsApp. |

Inquiry rules:

- Inquiry must not force the user into "registration."
- "Ask" language is allowed and often better than commitment-heavy language.
- Workshop inquiries should carry workshop context.
- Institutional/corporate inquiries should be possible without adding a separate MVP route.

---

## 14. Waitlist Conditional Map

| Waitlist Location | Current MVP Status | Activation Condition |
| --- | --- | --- |
| Scene 06 workshop card | Hidden | Real waitlist/workshop capacity approved. |
| `/workshops/[slug]` | Hidden/conditional | Workshop closed or future cohort confirmed. |
| Scene 10 final CTA | Hidden/conditional | Real cohort schedule exists. |
| `/register` form field | Optional/conditional | Admissions process needs waitlist category. |

Warning:

**Do not use waitlist language as a fake scarcity mechanism.** A waitlist is only acceptable when it reflects a real operational process.

---

## 15. Workshop Conversion Map

| Workshop Touchpoint | CTA | Destination | Notes |
| --- | --- | --- | --- |
| Scene 05 pillar | View workshops. | Scene 06 anchor. | Internal navigation. |
| Scene 06 workshop card | Ask About This Workshop. | WhatsApp. | Include workshop title/slug. |
| Scene 06 workshop card | View Details. | `/workshops/[slug]`. | Detail page. |
| `/workshops/[slug]` hero | Ask About This Workshop. | WhatsApp. | Primary. |
| `/workshops/[slug]` body | Register Interest. | `/register`. | Secondary. |
| `/workshops/[slug]` FAQ | Ask a Question. | WhatsApp. | Objection handling. |
| Related workshops | View Details. | `/workshops/[slug]`. | Optional. |

Workshop conversion rules:

- No course checkout.
- No module dashboard.
- No fake pricing.
- No fake date/capacity.
- No "enroll now" unless a real enrollment process exists.
- Workshop detail pages should support inquiry, not become a course platform.

---

## 16. Route-Level Conversion Map

| Route | Primary Conversion | Secondary Conversion | Conditional Conversion |
| --- | --- | --- | --- |
| `/` | WhatsApp / Register Interest. | Workshop detail. | Waitlist hidden. |
| `/register` | Submit inquiry/register interest form. | WhatsApp. | Waitlist field conditional. |
| `/workshops/[slug]` | Workshop-specific WhatsApp. | Register Interest. | Waitlist if workshop closed/approved. |

Optional/deferred routes:

| Route | Conversion Role |
| --- | --- |
| `/about` | Trust support, register/WhatsApp CTA. |
| `/instructors` | Mentor trust, register/WhatsApp CTA. |
| `/privacy` | Trust/legal support, no conversion focus. |
| `/workshops` | Workshop discovery if later approved. |

---

## 17. Mobile Conversion Map

| Mobile Location | Conversion Requirement |
| --- | --- |
| Header | WhatsApp/Register accessible in menu. |
| Floating CTA | WhatsApp visible without blocking content. |
| Scene 02 | CTA above or near first screen. |
| Scene 06 | Workshop card CTAs large enough. |
| Scene 09 | CTA after FAQ and persistent WhatsApp. |
| Scene 10 | CTA immediately after headline. |
| `/register` | Simple form, minimal typing. |
| `/workshops/[slug]` | Sticky or repeated workshop CTA if not intrusive. |

Mobile rules:

- Minimum tap target: 44px.
- No hover-only conversion.
- No CTA hidden behind 3D.
- No long pinned scroll blocking CTA access.
- WhatsApp CTA should be easy to reach.
- Forms must not feel long.
- Arabic CTA labels must not overflow.

---

## 18. Reduced-Motion / Static Conversion Map

| Area | Standard Experience | Reduced-Motion / Static Conversion |
| --- | --- | --- |
| Opening | CTA appears by scene handoff. | CTA visible early with static poster. |
| Hero | Animated reveal. | CTA visible with static content. |
| Workshops | Dossier/card reveal. | Static cards with same CTAs. |
| Mentors | Gallery reveal. | Static mentor cards + optional CTA. |
| Trust | Subtle proof reveal. | Static proof blocks. |
| FAQ | Accordion animation. | Native/instant accordion. |
| Final CTA | Seal callback. | Static closing CTA. |

Rule:

Reduced-motion or WebGL-disabled users must receive the same conversion opportunities.

---

## 19. Bilingual CTA Map

These labels are candidates only and require final copy/tone review.

| CTA Intent | Arabic Label Candidate | English Label Candidate | Notes |
| --- | --- | --- | --- |
| WhatsApp general | تواصل عبر واتساب | Contact on WhatsApp | Needs final tone review. |
| Register interest | سجّل اهتمامك | Register Interest | Low-pressure. |
| Ask about workshop | اسأل عن هذه الورشة | Ask About This Workshop | Workshop-specific. |
| View details | اعرف تفاصيل الورشة | View Workshop Details | Detail page. |
| General inquiry | أرسل استفسارك | Send an Inquiry | Form/inquiry. |
| Continue to FAQ | اعرف الإجابات | View FAQ | Optional. |
| Back to home | العودة للرئيسية | Back to Home | Supporting route. |

Bilingual rules:

- Arabic/English labels are candidates only.
- Do not animate Arabic letter-by-letter later.
- Ensure labels fit mobile.
- Keep CTA tone low-pressure and premium.
- Do not mix Arabic and English in the same animated text line.
- CTA accessible labels should be localized, not machine-translated at the last minute.

---

## 20. Analytics Event Planning

No analytics are implemented in this task. These event names are planning references for later technical implementation.

| Event Name | Trigger | Route/Scene | Conversion Path |
| --- | --- | --- | --- |
| `cta_whatsapp_click` | General WhatsApp clicked. | All | WhatsApp |
| `cta_hero_whatsapp_click` | Hero WhatsApp clicked. | Scene 02 | WhatsApp |
| `cta_final_whatsapp_click` | Final CTA WhatsApp clicked. | Scene 10 | WhatsApp |
| `cta_register_interest_click` | Register Interest clicked. | All relevant | Registration |
| `workshop_detail_click` | View Details clicked. | Scene 06 | Workshop |
| `workshop_whatsapp_click` | Workshop WhatsApp clicked. | Scene 06 / workshop pages | WhatsApp |
| `form_submit_attempt` | Form submit attempted. | `/register` | Registration/Inquiry |
| `form_submit_success` | Form success. | `/register` | Registration/Inquiry |
| `form_submit_error` | Form error. | `/register` | Registration/Inquiry |
| `faq_cta_click` | CTA clicked after FAQ. | Scene 09 | Inquiry |
| `language_toggle_click` | Language changed. | All | Bilingual |
| `waitlist_interest_click` | Waitlist clicked. | Conditional only | Waitlist |
| `webgl_fallback_cta_click` | CTA clicked in fallback. | `/` | Fallback conversion |
| `reduced_motion_cta_click` | CTA clicked in reduced-motion path. | `/` | Accessibility |

Analytics rules:

- Do not track until privacy/legal guidance and analytics stack are confirmed.
- Event names may change during technical implementation.
- Do not collect sensitive data beyond what is required for conversion.
- Locale should be tracked as context later if privacy guidance allows it.

---

## 21. Conversion Risk Map

| Risk | Why It Matters | Mitigation |
| --- | --- | --- |
| CTA only appears at the end | Users may leave before converting. | Persistent WhatsApp + Hero CTA. |
| Too many CTA types | Confusion. | Prioritize WhatsApp + Register. |
| Waitlist implies fake scarcity | Trust damage. | Keep conditional until real. |
| Form feels like enrollment system | LMS confusion. | Simple inquiry/register interest form. |
| Workshop cards feel like course marketplace | Wrong positioning. | Premium dossier style, no checkout. |
| WhatsApp number missing | Cannot implement final CTA. | Keep placeholder until confirmed. |
| Mobile CTA hidden | Conversion loss. | Mobile sticky/floating CTA plan. |
| Canvas-only CTA | Accessibility failure. | DOM links/buttons only. |
| Arabic CTA overflow | Broken mobile UX. | Test Arabic labels. |
| Fake proof near CTA | Credibility risk. | Only verified trust/proof. |

---

## 22. Conversion Guardrail Table

| Keep | Avoid |
| --- | --- |
| WhatsApp as primary conversion. | Complex enrollment funnel. |
| Simple `/register` form. | Account creation. |
| Workshop-specific inquiry. | Course checkout/payment flow. |
| Low-pressure CTA language. | Fake urgency. |
| Conditional waitlist only. | Fake waitlist/scarcity. |
| DOM links/buttons. | Canvas-only CTAs. |
| CTA access across scenes. | CTA only at final scene. |
| Mobile-visible WhatsApp. | Desktop-only conversion thinking. |
| Arabic/English CTA planning. | Arabic labels as afterthought. |
| Verified proof near CTA. | Fake testimonials/stats. |

---

## 23. Final Funnel Recommendation

| Decision Area | Recommendation |
| --- | --- |
| Primary conversion path | WhatsApp. |
| Secondary conversion path | `/register` inquiry/register interest form. |
| Inquiry handling | WhatsApp + form categories. |
| Waitlist handling | Conditional/future only. |
| Workshop conversion | Workshop-specific WhatsApp + detail page. |
| Header CTA | Register Interest + WhatsApp accessible. |
| Mobile CTA | WhatsApp prominent, form secondary. |
| Final CTA | WhatsApp primary, Register Interest secondary. |
| Analytics planning | Event names documented, implementation later. |
| Production blockers | WhatsApp number, form destination, privacy/legal text. |

Final recommendation:

**Proceed with a WhatsApp-first, low-pressure conversion funnel. Keep Register Interest as the structured secondary path, allow inquiry through both WhatsApp and form categories, map waitlist only as future/conditional, and ensure every CTA remains DOM-based, bilingual-safe, mobile-visible, and accessible in static/reduced-motion modes.**

---

## 24. Quality Gate

| Gate | Status | Notes |
| --- | --- | --- |
| All four official conversion paths mapped | PASS | WhatsApp, registration form, waitlist, and inquiry included. |
| WhatsApp marked as primary | PASS | Active MVP Primary. |
| Registration form mapped as secondary | PASS | `/register` funnel included. |
| Inquiry mapped clearly | PASS | Inquiry categories and destinations included. |
| Waitlist marked conditional unless real | PASS | Hidden/conditional throughout. |
| Every scene included | PASS | Scenes 01-10 covered. |
| CTA visibility shown per scene | PASS | Scene and location maps included. |
| Workshop-specific conversion mapped | PASS | Scene 06 and workshop detail path included. |
| Route-level conversions mapped | PASS | `/`, `/register`, `/workshops/[slug]`. |
| Mobile conversion rules included | PASS | Dedicated table and rules. |
| Reduced-motion/static conversion rules included | PASS | Dedicated table. |
| Bilingual CTA candidates included | PASS | Arabic/English candidate labels included. |
| Analytics event names planned | PASS | Event planning table included. |
| Conversion risks documented | PASS | Risk table included. |
| Fake urgency avoided | PASS | Waitlist and urgency guardrails included. |
| LMS/dashboard behavior avoided | PASS | Route and workshop rules prevent platform drift. |
| Avoided implementation | PASS | No links, forms, analytics, backend, or UI comps implemented. |
| Avoided new roadmap tickets | PASS | No new tickets created. |

---

## 25. Acceptance Criteria

| Acceptance Criteria | Status |
| --- | --- |
| Conversion funnel map document created | PASS |
| WhatsApp path mapped | PASS |
| Registration form path mapped | PASS |
| Waitlist path mapped as conditional unless approved | PASS |
| Inquiry path mapped | PASS |
| All 10 scenes included | PASS |
| CTA visibility map complete | PASS |
| WhatsApp conversion map complete | PASS |
| Registration form funnel map complete | PASS |
| Inquiry funnel map complete | PASS |
| Waitlist conditional map complete | PASS |
| Workshop conversion map complete | PASS |
| Route-level conversion map complete | PASS |
| Mobile conversion map complete | PASS |
| Reduced-motion/static conversion map complete | PASS |
| Bilingual CTA map included | PASS |
| Analytics event planning included | PASS |
| Conversion risk map included | PASS |
| Final funnel recommendation clear | PASS |
| Conversion guardrail table included | PASS |
| No UI comps created | PASS |
| No frontend implementation started | PASS |
| No form/backend implementation started | PASS |
| No analytics code added | PASS |
| No new roadmap tickets created | PASS |

---

## 26. Final Status

**PASS WITH CONDITIONS - P3.03 complete. Four conversion paths are mapped across all scenes/routes with CTA visibility, mobile, fallback, bilingual, analytics, and risk notes.**

Final funnel remains conditional on final WhatsApp number, form destination, privacy/legal wording, final workshop content, stakeholder approval, and a confirmed waitlist decision.
