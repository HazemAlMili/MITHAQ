# Mithaq Open Questions Resolution Log

**Official Ticket ID:** P0.06  
**Official Ticket Name:** Open Questions Resolution  
**Phase:** Phase 0, Project Alignment & Input Collection  
**Priority:** P0  
**Final Status:** PASS WITH CONDITIONS  
**Prepared date:** 2026-06-17  
**Decision source:** Internal project-owner / acting client decision-maker

---

## 1. Executive Summary

The 15 open questions from the Mithaq direction plan have been answered internally by the project owner / acting client decision-maker.

These answers are treated as the temporary approved direction until future stakeholder changes are introduced.

Current result:

**PASS WITH CONDITIONS.**

Phase 1 research and planning may begin under the constraints documented below.

Production is still not fully authorized. Final UI production, final 3D production, final frontend implementation, production copy, and legal/compliance-sensitive claims remain conditional until the remaining Phase 0 blockers are resolved or consciously accepted as assumptions.

No new roadmap tickets are created. All decisions remain inside official P0.06.

---

## 2. Current Phase 0 Status

### Completed / Drafted Outputs

- P0.01 direction/creative foundation has been drafted.
- P0.02 asset/content inventory has been drafted.
- Supporting brand/content request materials exist.
- Language/RTL recommendation exists as supporting decision material.
- Technical checklist exists.
- Timeline/budget checklist exists.
- Direction sign-off document exists.
- P0.06 open questions now have internal project-owner answers.

### Remaining Production Conditions

- P0.03 remains QA blocked until technical answers/access are provided.
- P0.04 remains QA blocked until formal direction sign-off is documented.
- P0.05 remains QA blocked until timeline, budget, resources, and review windows are confirmed.
- Brand assets are still missing.
- Content assets are still missing or placeholder-only.
- Contact/conversion assets are still missing.
- Legal/compliance guidance still needs final confirmation.

---

## 3. Q&A Resolution Log

| Q# | Topic | Final Answer | Status | Impact | Blocker? | Owner | Required Action |
| -- | ----- | ------------ | ------ | ------ | -------- | ----- | --------------- |
| Q1 | Opening direction | Use the judicial gavel as the opening trigger, then reveal the Mithaq Seal. The gavel is not the hero; the Seal is the hero. | Approved | 3D, Motion, Storyboard | No | Creative Director / 3D Lead | Build future opening concepts around gavel-trigger to seal-reveal logic |
| Q2 | Primary conversion action | WhatsApp is the primary conversion action. | Approved | UX, CTA, Tracking | Conditional | Product Lead / Admissions | Final WhatsApp number still needed before implementation |
| Q3 | Language direction | Full bilingual direction is approved. Arabic and English should both be planned for the MVP. | Approved with scope impact | UX, Copy, RTL, LTR, SEO, Frontend | Conditional | Product Lead / Arabic Copywriter / Frontend Lead | Build bilingual architecture from the beginning; Arabic remains visually prioritized but English is included in MVP planning |
| Q4 | Instructor photography | Use placeholders for now. Final mentor section can be designed around placeholder logic until real photos are available. | Approved with conditions | Design, Content, Trust | No for prototype / Yes for final polish | Content Lead / UI Designer | Use premium placeholders only; do not pretend placeholders are final instructor photography |
| Q5 | 3D visual world | Symbolic realism is approved. Legal objects should be recognizable but artistically controlled and premium. | Approved | 3D, Art Direction, Performance | No | Creative Director / 3D Lead | Continue with gavel, seal, desk, documents, and legal chamber language |
| Q6 | Workshops/courses | Use 3-5 temporary workshop placeholders based on Mithaq pillars: Legal Research, Legal Writing, Professional Readiness, Career Infrastructure, Practical Legal Mindset. | Approved with conditions | Content, UX, Workshops Section | No for prototype / Yes for final content | Content Lead / UX Strategist | Mark all workshop content as placeholder until final workshop details are confirmed |
| Q7 | Opening duration | The opening scene should complete through scroll, not as a fixed timed intro. The user controls progression by scrolling. | Approved with design change | Motion, UX, GSAP, ScrollTrigger | No | Creative Director / UX Strategist / Frontend Lead | Replace fixed 8-second intro logic with scroll-driven cinematic sequence; keep fallback and skip behavior if needed |
| Q8 | Sound design | Sound effects are approved. | Approved with accessibility condition | UX, Audio, Accessibility | No | Creative Director / Motion Designer | Add sound effects as optional/user-controlled; no loud or unexpected autoplay |
| Q9 | Instructor pages | MVP uses Scene 07 only. Separate instructor pages are not required in MVP. | Approved | IA, Scope | No | Product Lead / UX Strategist | Keep instructor pages for Phase 2 if needed |
| Q10 | Testimonials/proof | If proof points are unavailable, Scene 08 should be forward-compatible and ready to receive testimonials/numbers later, with no fake claims. | Approved | Trust, Content, Legal | No | Content Lead / Legal Reviewer | Build trust section structure without inventing testimonials, metrics, or affiliations |
| Q11 | Workshop modal/pages | Hybrid is approved: modal preview inside the landing page + dedicated workshop detail pages. | Approved | UX, IA, SEO | No | Product Lead / UX Strategist / Frontend Lead | Keep workshop detail pages informational only, not a full course system |
| Q12 | Timeline/budget | Vertical Slice First is approved. | Approved | Scope, Timeline, Budget | No | Project Manager / Product Lead | First prove opening/hero/core scroll/CTA experience before full production expansion |
| Q13 | Legal/credibility boundaries | Use strict credibility governance. Avoid unsupported claims, exaggerated promises, fake authority, direct job guarantees, or wording that sounds like legal advice. | Approved | Copy, Legal, Trust | No | Content Lead / Legal Reviewer | All claims must be supportable; use premium, restrained, credible language |
| Q14 | Cohort/deadline model | No cohort system, deadline system, booking system, or seat-count system in MVP. This is a portfolio/landing experience, not an operational registration system. | Approved | Scope, CTA, Content | No | Product Lead / Admissions | Use general interest/WhatsApp inquiry language; avoid countdowns, seat counters, fake urgency, or system-like registration flows |
| Q15 | Pages in Phase 1 | Approved Phase 1 page scope: `/`, `/register`, `/workshops/[slug]`. Other pages remain Phase 2 unless specifically needed. | Approved | IA, Frontend, SEO | No | Product Lead / Technical Lead | Keep MVP focused and avoid expanding into LMS/system structure |

---

## 4. The 15 Questions, Recommendations, and Final Answers

### Q1 - Opening Direction

**Question:** Should the opening be the gavel strike, or should we explore a seal-based opening instead?

**Plan recommendation:** Keep the gavel as the opening act, but make the Mithaq Seal the reveal and the hero of Act I.

**Final answer:** Use the judicial gavel as the opening trigger, then reveal the Mithaq Seal. The gavel is not the hero; the Seal is the hero.

**Status:** Approved.

**Impact:** 3D, motion, storyboard.

**Blocker:** No.

**Required action:** Build all future opening concepts around gavel-trigger to seal-reveal logic.

---

### Q2 - Primary Conversion Action

**Question:** What is the exact primary conversion action: registration form, WhatsApp, inquiry, or waitlist?

**Plan recommendation:** WhatsApp as primary + simple 3-field form as secondary.

**Final answer:** WhatsApp is the primary conversion action.

**Status:** Approved.

**Impact:** UX, CTA, tracking.

**Blocker:** Conditional.

**Required action:** Final WhatsApp number is still needed before implementation.

---

### Q3 - Language Direction

**Question:** Will the site be Arabic-first, English-first, or bilingual?

**Plan recommendation:** If the primary audience is Arabic-speaking students in the region, build Arabic-first as the primary experience. English can be secondary.

**Final answer:** Full bilingual direction is approved. Arabic and English should both be planned for the MVP.

**Status:** Approved with scope impact.

**Impact:** UX, copy, RTL, LTR, SEO, frontend.

**Blocker:** Conditional.

**Required action:** Build bilingual architecture from the beginning. Arabic remains visually prioritized, but English must be included in MVP planning.

---

### Q4 - Instructor Photography

**Question:** Do we have professional instructor photography?

**Plan recommendation:** Schedule a professional photoshoot before development if current photos are not premium enough.

**Final answer:** Use placeholders for now. Final mentor section can be designed around placeholder logic until real photos are available.

**Status:** Approved with conditions.

**Impact:** Design, content, trust.

**Blocker:** No for prototype / yes for final polish.

**Required action:** Use premium placeholders only. Do not pretend placeholders are final instructor photography.

---

### Q5 - 3D Visual World Style

**Question:** Should the 3D visual world be realistic, symbolic, or abstract?

**Plan recommendation:** Symbolic realism. Objects should be recognizably legal, but artistically controlled and premium.

**Final answer:** Symbolic realism is approved. Legal objects should be recognizable but artistically controlled and premium.

**Status:** Approved.

**Impact:** 3D, art direction, performance.

**Blocker:** No.

**Required action:** Continue with gavel, seal, desk, documents, and legal chamber language.

---

### Q6 - Workshops / Courses Inventory

**Question:** What workshops and courses exist today, and which will be launched in the future?

**Plan recommendation:** Provide at least 3-5 confirmed workshops with titles, format, level, and key skills before Scene 06 design begins.

**Final answer:** Use 3-5 temporary workshop placeholders based on Mithaq pillars: Legal Research, Legal Writing, Professional Readiness, Career Infrastructure, Practical Legal Mindset.

**Status:** Approved with conditions.

**Impact:** Content, UX, workshops section.

**Blocker:** No for prototype / yes for final content.

**Required action:** Mark all workshop content as placeholder until final workshop details are confirmed.

---

### Q7 - Opening Intro Duration

**Question:** How long should the opening intro run before the user can fully use the site?

**Plan recommendation:** 8 seconds maximum before Lenis enables. Skip available from 2.5 seconds. On mobile, reduce to 5 seconds maximum with auto-complete.

**Final answer:** The opening scene should complete through scroll, not as a fixed timed intro. The user controls progression by scrolling.

**Status:** Approved with design change.

**Impact:** Motion, UX, GSAP, ScrollTrigger.

**Blocker:** No.

**Required action:** Replace fixed 8-second intro logic with a scroll-driven cinematic opening sequence. Still include fallback and skip behavior if needed.

---

### Q8 - Optional Sound Design

**Question:** Should optional sound design be included?

**Plan recommendation:** Optional sound, off by default. User-controlled audio toggle only.

**Final answer:** Sound effects are approved.

**Status:** Approved with accessibility condition.

**Impact:** UX, audio, accessibility.

**Blocker:** No.

**Required action:** Add sound effects as optional/user-controlled. Do not autoplay loud or unexpected audio. Default should be muted or activated by user interaction.

---

### Q9 - Instructor Pages

**Question:** Should instructor pages exist as separate routes, or is Scene 07 sufficient?

**Plan recommendation:** MVP: Scene 07 on landing page is sufficient. Post-launch: add `/instructors/[slug]`.

**Final answer:** MVP uses Scene 07 only. Separate instructor pages are not required in MVP.

**Status:** Approved.

**Impact:** IA, scope.

**Blocker:** No.

**Required action:** Keep instructor pages for Phase 2 if needed.

---

### Q10 - Testimonials / Numbers / Proof Points

**Question:** What testimonials, numbers, and proof points are available?

**Plan recommendation:** Provide at minimum 3 genuine testimonials with consent, 2-3 quantitative proof points, and institutional affiliations or press mentions if available. If unavailable, design Scene 08 to be forward-compatible.

**Final answer:** If proof points are unavailable, Scene 08 should be forward-compatible and ready to receive testimonials/numbers later, with no fake claims.

**Status:** Approved.

**Impact:** Trust, content, legal.

**Blocker:** No.

**Required action:** Build trust section structure without inventing testimonials, metrics, or affiliations.

---

### Q11 - Workshop Detail Behavior

**Question:** Should workshops open in modals or dedicated pages?

**Plan recommendation:** Hybrid. Landing page uses modal preview. Each workshop also has canonical `/workshops/[slug]` page.

**Final answer:** Hybrid is approved: modal preview inside the landing page + dedicated workshop detail pages.

**Status:** Approved.

**Impact:** UX, IA, SEO.

**Blocker:** No.

**Required action:** Keep workshop detail pages informational only, not a full course system.

---

### Q12 - Timeline and Budget

**Question:** What is the client's timeline and budget for this project?

**Plan recommendation:** If timeline is under 8 weeks, prioritize Scenes 01, 02, 05, 06, 07, and 10 and deliver others as static editorial sections.

**Final answer:** Vertical Slice First is approved.

**Status:** Approved.

**Impact:** Scope, timeline, budget.

**Blocker:** No.

**Required action:** First prove opening/hero/core scroll/CTA experience before full production expansion.

---

### Q13 - Credibility / Legal Claim Boundaries

**Question:** What must be avoided to maintain legal and professional credibility?

**Plan recommendation:** Define a content governance checklist: no unverified "best legal training" claims, no stock courtroom cliches, no law-firm advertising tone, and every claim must be backed by something real.

**Final answer:** Use strict credibility governance. Avoid unsupported claims, exaggerated promises, fake authority, direct job guarantees, or any wording that sounds like legal advice.

**Status:** Approved.

**Impact:** Copy, legal, trust.

**Blocker:** No.

**Required action:** All claims must be supportable. Use premium, restrained, credible language.

---

### Q14 - Registration Deadline / Cohort Model

**Question:** Will there be a registration deadline or seasonal cohort model?

**Plan recommendation:** If workshops run in cohorts, display next cohort start date prominently in Scene 10 and Hero CTA. Countdown timers only if the deadline is genuine.

**Final answer:** No cohort system, deadline system, booking system, or seat-count system in MVP. This is a portfolio/landing experience, not an operational registration system.

**Status:** Approved.

**Impact:** Scope, CTA, content.

**Blocker:** No.

**Required action:** Use general interest/WhatsApp inquiry language. Avoid countdowns, seat counters, fake urgency, or system-like registration flows.

---

### Q15 - Pages Beyond Main Landing

**Question:** What pages beyond the main landing are in scope for Phase 1?

**Plan recommendation:** Phase 1 scope: landing page, `/register` form, and `/workshops/[slug]` template. Everything else is Phase 2.

**Final answer:** Approved Phase 1 page scope: `/`, `/register`, `/workshops/[slug]`. Other pages remain Phase 2 unless specifically needed.

**Status:** Approved.

**Impact:** IA, frontend, SEO.

**Blocker:** No.

**Required action:** Keep MVP focused and avoid expanding into LMS/system structure.

---

## 5. Final Decisions Summary

Approved core decisions:

- Opening direction: gavel trigger to Mithaq Seal reveal.
- Primary conversion: WhatsApp.
- Language direction: bilingual MVP.
- 3D style: symbolic realism.
- Workshop content: temporary placeholders based on Mithaq pillars.
- Opening behavior: scroll-driven, not fixed-time intro.
- Sound design: included, but controlled and accessible.
- Mentor section: Scene 07 only in MVP.
- Trust section: forward-compatible, no fake proof.
- Workshop details: hybrid modal + detail page.
- Delivery approach: Vertical Slice First.
- Legal credibility: strict, no unsupported claims.
- Cohort/deadline logic: excluded from MVP.
- Phase 1 pages: `/`, `/register`, `/workshops/[slug]`.

---

## 6. Important Conditions

### 6.1 Bilingual Scope Condition

The project is now bilingual for MVP planning.

This affects:

- Copywriting
- Translation
- RTL/LTR layout
- Typography
- Navigation
- Forms
- SEO metadata
- URL strategy
- QA

The team must not treat English as a future-only afterthought.

Required direction:

- Arabic-first visual and content priority.
- English equivalent content included.
- RTL and LTR support planned from the beginning.
- No final copy implementation until both languages are approved.

### 6.2 Scroll-Driven Opening Condition

The opening should not be a fixed 8-second intro.

Updated direction:

- The gavel/seal opening should progress with scroll.
- The user should feel they are entering the legal chamber through movement.
- The opening must still feel cinematic and controlled.
- Reduced-motion users must get a static/fade fallback.
- Mobile should simplify the motion if performance requires it.

This changes the motion logic from timed intro sequence to scroll-controlled cinematic opening sequence.

### 6.3 Sound Effects Condition

Sound effects are approved, but must follow professional website rules:

- No aggressive autoplay.
- No loud unexpected sound.
- Sound should be off by default or activated after user interaction.
- Add a visible mute/unmute control if sound exists.
- The gavel impact sound must be restrained, deep, premium, and realistic.
- Sound must not be required to understand the experience.

### 6.4 Portfolio / Landing Scope Condition

Mithaq is not an operational system.

The site must not become:

- LMS
- Booking system
- Payment system
- Student dashboard
- Admin panel
- Course progress system
- Seat management system
- Cohort management platform

The website remains:

**Premium bilingual 3D legal academy portfolio / landing experience.**

---

## 7. Remaining Production Conditions

Before UI production, 3D production, or frontend implementation begins, the following must still be confirmed or intentionally treated as placeholders:

- Final logo files.
- Final wordmark files.
- Final seal approval.
- Final WhatsApp number.
- Final form destination.
- Final bilingual copy.
- Final workshop details.
- Final instructor details/photos.
- Final proof points if available.
- Domain / hosting / repo decisions.
- Timeline / budget / resources.

---

## 8. Deferred Items

| Item | Related Question | Status | Notes |
| ---- | ---------------- | ------ | ----- |
| Full instructor pages | Q9 | Deferred to Phase 2 unless specifically needed | Scene 07 is the MVP mentor surface |
| Extra pages beyond `/`, `/register`, `/workshops/[slug]` | Q15 | Deferred to Phase 2 unless specifically needed | Avoid scope expansion |
| Operational registration system | Q14 | Excluded from MVP | No booking, seat, payment, cohort, or dashboard system |
| Final proof/testimonials | Q10 | Add when available | Do not invent proof |
| Real workshop content | Q6 | Required before final content | Placeholders allowed for planning/prototype only |
| Final instructor photography | Q4 | Required for final polish | Premium placeholders allowed for prototype |

---

## 9. Phase 1 Readiness Assessment

Current status:

**PASS WITH CONDITIONS - Phase 1 research and planning may begin under constraints.**

Reason:

- The 15 open questions now have internal project-owner answers.
- Strategic direction is clear enough for research/planning.
- Vertical Slice First is approved as the delivery approach.
- Production blockers remain visible and unresolved.

Phase 1 may begin only for:

- Research synthesis.
- Planning.
- Storyflow exploration.
- Placeholder-safe UX thinking.
- Bilingual information architecture planning.
- Technical feasibility planning.

Phase 1 must not begin as:

- Final UI production.
- Final 3D production.
- Final seal production.
- Frontend implementation.
- Production copywriting.
- Legal/compliance-sensitive claims.

---

## 10. Final Q&A Resolution Status

**PASS WITH CONDITIONS.**

P0.06 is complete enough for limited non-production Phase 1 work.

All 15 open questions have been answered internally by the acting project-owner/client decision-maker.

Production remains conditional until assets, technical environment, final content, timeline/budget/resources, and formal sign-off items are ready.

No production work is authorized by this document.

---

## 11. Approval / Signature Section

| Sign-off Item | Decision |
| ------------- | -------- |
| All 15 questions resolved? | Yes, internally by acting project-owner/client decision-maker |
| Phase 1 readiness | PASS WITH CONDITIONS |
| Approved by | Acting project-owner / client decision-maker |
| Approval date | 2026-06-17 |
| Conditions | Production remains blocked until listed assets, content, technical, and budget items are ready |
| Deferred items accepted? | Yes, as documented |
| Remaining blockers accepted? | Accepted as production conditions, not resolved blockers |

Client / Project Owner Signature:

```text
Name:
Role:
Signature / Written Approval:
Date:
```

Project Manager Signature:

```text
Name:
Role:
Signature / Written Approval:
Date:
```

