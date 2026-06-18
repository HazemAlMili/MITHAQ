# Mithaq 10-Scene Scroll Storyflow

**Official Ticket ID:** P3.02  
**Official Ticket Name:** 10-Scene Scroll Storyflow  
**Phase:** Phase 3 - UX / IA / Storyflow Planning  
**Owner:** UX Strategist / Storyflow Lead  
**Status:** PASS WITH CONDITIONS  
**Date:** 2026-06-19  
**Route in Scope:** `/`

---

## 1. Executive Summary

This document defines Mithaq's full 10-scene scroll storyflow for the main landing route `/`.

The storyflow translates the approved IA, opening storyboard, scene composition sketches, 3D art direction, and motion vocabulary into a wireframe-level scroll plan. It assigns scroll ranges, 3D states, DOM content, CTA visibility, transitions, mobile adaptation, reduced-motion equivalents, accessibility notes, performance notes, and bilingual/RTL implications for every scene.

Final storyflow position:

**Use a Seal-led 10-scene scroll journey where Scene 01-02 form the first cinematic vertical-slice priority, Scenes 03-06 convert narrative clarity into workshop interest, Scenes 07-09 build trust and answer objections, and Scene 10 closes with a stable covenant/CTA callback.**

Status is **PASS WITH CONDITIONS** because final scene timing, copy, 3D assets, Arabic/English content, mobile behavior, and production motion still require vertical-slice testing, stakeholder review, and final asset approval.

This is storyflow planning only. No final UI comps, R3F code, GSAP implementation, Lenis setup, production animation, or final copy are created.

---

## 2. Current Mithaq Decisions

| Area | Current Decision |
| --- | --- |
| Product type | Premium bilingual 3D legal academy portfolio / landing experience. |
| Route in scope | `/` main landing route. |
| Core concept | The Covenant Seal. |
| Opening direction | Scroll-Driven Seal-Led Opening. |
| 3D direction | Seal-Led Macro Legal Chamber. |
| Motion direction | Scroll-Led Ceremonial Restraint. |
| Primary conversion | WhatsApp. |
| Secondary conversion | Simple inquiry / Register Interest form. |
| MVP route architecture | `/`, `/register`, `/workshops/[slug]`. |
| Bilingual approach | Arabic and English planned as real localized layouts. |
| Arabic display safety | Tajawal 700 is the safe default; Lemonada remains accent-only pending review. |
| CTA color rule | Filled gold CTA must use near-black text. |
| Gold usage | `gold-dim` is decorative only. |
| Trust/proof rule | No fake proof, testimonials, stats, urgency, countdowns, or seat counters. |
| Platform guardrail | Do not turn workshops into an LMS, dashboard, course catalog, or checkout flow. |
| Feasibility constraint | P1.05 Option C - Vertical Slice Only Until Asset Optimization. |
| Content fallback | Every scene must communicate through DOM-first content if 3D fails. |

---

## 3. Storyflow Principles

| Principle | Meaning |
| --- | --- |
| Scroll tells the story | The user should feel progression, not random sections. |
| DOM-first meaning | All critical content must exist outside canvas. |
| Seal-led continuity | The Seal connects the journey visually and symbolically. |
| Gavel as trigger only | The gavel starts the story but does not dominate it. |
| Conversion never disappears | WhatsApp / Register Interest paths remain accessible. |
| Mobile is shorter | Mobile simplifies motion and reduces 3D dependency. |
| Reduced motion is equivalent | Users who reduce motion get the same content meaning. |
| No false urgency | No fake scarcity, fake deadlines, countdowns, or fake proof. |
| No LMS behavior | Workshops are previews/details, not dashboard/course modules. |
| Bilingual-safe | Arabic/English layouts are planned as separate localized flows. |

---

## 4. Full Scroll Range Map

The baseline range from the ticket is retained. Minor production tuning may happen later after real copy, asset weight, and mobile scroll testing, but the 10-scene order should remain stable.

| Scene | Scene Name | Full Page Scroll Range | Story Role | CTA Mode |
| --- | --- | ---: | --- | --- |
| 01 | Gavel / Seal Opening | 0-10% | Authority and symbolic reveal | CTA by handoff / fallback early |
| 02 | Hero / Mithaq Reveal | 10-22% | Clarify offer and audience | Primary CTA visible |
| 03 | The Gap | 22-37% | Name the study-to-practice problem | Persistent WhatsApp only |
| 04 | The Mithaq Method | 37-50% | Turn confusion into structure | Soft CTA |
| 05 | Training Pillars | 50-62% | Show skill outcomes | View workshops / Register Interest |
| 06 | Workshops & Course Preview | 62-72% | Convert interest into workshop inquiry | Ask About Workshop |
| 07 | Hall of Mentors | 72-82% | Build credibility through people | Optional Register Interest |
| 08 | Trust / Authority / Credibility | 82-88% | Confirm proof, conditions, authority | Optional Register Interest |
| 09 | FAQ | 88-94% | Resolve objections | Ask via WhatsApp / Register |
| 10 | Final CTA / Closing Covenant | 94-100% | Close with Seal callback and action | WhatsApp / Register Interest |

Range recommendation:

Keep the baseline allocation. Scene 03 receives the longest range because the problem recognition beat needs breathing room and should not feel like a throwaway section. Scene 08 and Scene 09 remain shorter because they are editorial/supporting beats and should not overtake the conversion path.

---

## 5. Scene 01 Storyflow - Gavel / Seal Opening

| Field | Required Answer |
| --- | --- |
| Full page scroll range | 0-10% |
| Scene objective | Establish premium legal authority and reveal the Mithaq Seal. |
| User question answered | "Is this serious, premium, and worth my attention?" |
| Primary narrative beat | The judicial world appears, the gavel triggers the covenant moment, and the Seal becomes the central motif. |
| 3D state at entry | Dark judicial void; low warm light; no readable brand yet. |
| 3D state during scene | Desk reveals, gavel enters as ceremonial trigger, controlled contact creates ripple, Seal outline emerges. |
| 3D state at exit | Seal is stable and centered; gavel rests as secondary callback. |
| DOM content visible | Mithaq identity, test tagline, short positioning line, CTA by handoff. |
| Primary CTA present? | Yes, by end of scene; visible early in fallback. |
| CTA type | WhatsApp / Register Interest |
| Secondary CTA | None or subtle continue cue if usability testing supports it. |
| Transition in | Page loads into darkness with immediate semantic fallback content available in DOM. |
| Transition out | Seal stabilizes into Scene 02 hero anchor; brand copy becomes fully readable. |
| Mobile adaptation | Shortened seal reveal or static poster; CTA appears earlier. |
| Reduced-motion equivalent | Static seal/desk poster with brand and CTA fade-in. |
| Accessibility note | Do not require canvas or scroll animation to identify Mithaq or reach CTA. |
| Performance note | Highest 3D complexity; first vertical-slice priority; must have static fallback. |
| Bilingual/RTL note | Arabic/English brand lines must be DOM text; no baked text inside canvas. |

Low-fidelity wireframe:

```text
+------------------------------------------------------+
| SCENE 01 / 0-10%                                     |
| [3D CANVAS: dark desk, centered seal reveal]         |
|                                                      |
|              [MITHAQ SEAL CENTER]                    |
|        [gavel secondary / lower side]                |
|                                                      |
| [DOM HANDOFF ZONE: brand, test tagline, CTA]         |
| [Primary: WhatsApp/Register Interest]                |
| Fallback: static seal poster + visible CTA           |
+------------------------------------------------------+
```

---

## 6. Scene 02 Storyflow - Hero / Mithaq Reveal

| Field | Required Answer |
| --- | --- |
| Full page scroll range | 10-22% |
| Scene objective | Clarify what Mithaq is, who it serves, and why it matters. |
| User question answered | "What is Mithaq, and is it for me?" |
| Primary narrative beat | The symbolic reveal becomes a clear legal academy positioning statement. |
| 3D state at entry | Stable Seal and secondary gavel inherited from Scene 01. |
| 3D state during scene | Seal becomes atmospheric anchor; camera settles; desk/chamber depth stays calm. |
| 3D state at exit | Camera prepares for document fragmentation and problem recognition. |
| DOM content visible | Hero headline, supporting copy, primary CTA, secondary CTA. |
| Primary CTA present? | Yes |
| CTA type | WhatsApp / Register Interest |
| Secondary CTA | View training pillars / workshops |
| Transition in | Seal stabilizes and hero text becomes dominant over motion. |
| Transition out | Hero promise fades into problem state; chamber darkens slightly. |
| Mobile adaptation | Text-first layout; 3D becomes background poster or reduced scene. |
| Reduced-motion equivalent | Static hero with Seal artwork/poster and immediate CTA visibility. |
| Accessibility note | Headline and CTAs should appear early in DOM order; no scroll trap. |
| Performance note | Do not let WebGL block LCP, CTA, or readable content. |
| Bilingual/RTL note | Arabic and English should use localized composition, not forced line mixing. |

Low-fidelity wireframe:

```text
+------------------------------------------------------+
| SCENE 02 / 10-22%                                    |
| [3D: seal as background/side anchor]                 |
|                                                      |
| [DOM TEXT COLUMN]              [SEAL ATMOSPHERE]     |
| [Hero headline]                                      |
| [Support copy]                                       |
| [Primary CTA] [Secondary CTA]                        |
|                                                      |
| Mobile: text first, seal poster behind/below         |
+------------------------------------------------------+
```

---

## 7. Scene 03 Storyflow - The Gap

| Field | Required Answer |
| --- | --- |
| Full page scroll range | 22-37% |
| Scene objective | Help users recognize the gap between legal study and real practice. |
| User question answered | "Why do I still feel unready?" |
| Primary narrative beat | Ordered promise gives way to fragmented legal documents, showing practical uncertainty. |
| 3D state at entry | Seal/desk atmosphere shifts toward scattered documents. |
| 3D state during scene | Memos, legal notes, forms, and folders drift around a protected text area. |
| 3D state at exit | Documents begin converging toward order. |
| DOM content visible | Problem headline and short explanatory copy. |
| Primary CTA present? | No primary scene CTA; persistent WhatsApp remains available. |
| CTA type | Persistent WhatsApp only |
| Secondary CTA | Optional continue cue. |
| Transition in | Chamber darkens slightly; documents fragment from the hero world. |
| Transition out | Document drift slows and begins aligning into a method structure. |
| Mobile adaptation | Static or limited document collage; no crowded floating objects. |
| Reduced-motion equivalent | Static fragmented document layout with problem copy. |
| Accessibility note | Problem content must not be obscured by canvas objects. |
| Performance note | Cap document mesh count; no essential text in textures. |
| Bilingual/RTL note | Arabic problem heading needs wider line room and line/block reveal only. |

Low-fidelity wireframe:

```text
+------------------------------------------------------+
| SCENE 03 / 22-37%                                    |
| [3D: sparse document fragments around edges]         |
|                                                      |
|      [PROTECTED DOM TEXT ZONE]                       |
|      [Problem headline]                              |
|      [Short body copy]                               |
|                                                      |
| [Persistent WhatsApp available globally]             |
| Fallback: static document collage                    |
+------------------------------------------------------+
```

---

## 8. Scene 04 Storyflow - The Mithaq Method

| Field | Required Answer |
| --- | --- |
| Full page scroll range | 37-50% |
| Scene objective | Show how Mithaq organizes confusion into practical training. |
| User question answered | "How does Mithaq solve this?" |
| Primary narrative beat | Fragmentation becomes order: documents align into a practical method. |
| 3D state at entry | Documents converging from Scene 03. |
| 3D state during scene | Ordered desk/method structure appears; Seal remains a subtle authority motif. |
| 3D state at exit | Method objects prepare the transition into training pillars. |
| DOM content visible | Method headline plus 3-4 practical method principles. |
| Primary CTA present? | Soft/secondary only |
| CTA type | View pillars / continue |
| Secondary CTA | Optional "View Training Pillars". |
| Transition in | Documents align; visual chaos resolves into method. |
| Transition out | Ordered objects become anchors for pillar cards/dossiers. |
| Mobile adaptation | Static ordered method blocks. |
| Reduced-motion equivalent | Ordered desk poster plus method list. |
| Accessibility note | Method principles should be semantic list items. |
| Performance note | Medium 3D at most; avoid expensive morphs. |
| Bilingual/RTL note | Arabic principles may need more vertical spacing and shorter line lengths. |

Low-fidelity wireframe:

```text
+------------------------------------------------------+
| SCENE 04 / 37-50%                                    |
| [3D: ordered desk, aligned papers, seal accent]      |
|                                                      |
| [Method headline]                                    |
| [Principle 01] [Principle 02]                        |
| [Principle 03] [Principle 04 optional]               |
| [Soft CTA: View Training Pillars]                    |
|                                                      |
| Fallback: static ordered method section              |
+------------------------------------------------------+
```

---

## 9. Scene 05 Storyflow - Training Pillars

| Field | Required Answer |
| --- | --- |
| Full page scroll range | 50-62% |
| Scene objective | Present the five training pillars clearly. |
| User question answered | "What skills will I actually gain?" |
| Primary narrative beat | The Mithaq method becomes five practical skill pillars. |
| 3D state at entry | Dossier/card anchors appear from ordered desk world. |
| 3D state during scene | Five pillar cards/dossiers reveal with restrained motion. |
| 3D state at exit | Pillars guide users toward workshop previews. |
| DOM content visible | Five pillar cards with short practical explanations. |
| Primary CTA present? | Yes or soft CTA |
| CTA type | View Workshops / Register Interest |
| Secondary CTA | Persistent WhatsApp |
| Transition in | Method objects become dossier/card anchors. |
| Transition out | Pillar dossiers become workshop dossier previews. |
| Mobile adaptation | Vertical stacked cards; no hover-only behavior. |
| Reduced-motion equivalent | Static pillar card list. |
| Accessibility note | Cards should be real DOM content with headings and readable order. |
| Performance note | DOM cards preferred; avoid heavy 3D cards. |
| Bilingual/RTL note | Arabic card body expansion must be expected and accommodated. |

Approved placeholder pillars:

1. Legal Research
2. Legal Writing
3. Professional Readiness
4. Career Infrastructure
5. Practical Legal Mindset

Low-fidelity wireframe:

```text
+------------------------------------------------------+
| SCENE 05 / 50-62%                                    |
| [3D: subtle dossier anchors / seal motif]            |
|                                                      |
| [Training Pillars headline]                          |
| [Card 01] [Card 02] [Card 03]                        |
| [Card 04] [Card 05]                                  |
|                                                      |
| [CTA: View Workshops] [Register Interest]            |
| Mobile: single-column stack                          |
+------------------------------------------------------+
```

---

## 10. Scene 06 Storyflow - Workshops & Course Preview

| Field | Required Answer |
| --- | --- |
| Full page scroll range | 62-72% |
| Scene objective | Let users find a relevant workshop path without making this an LMS. |
| User question answered | "Which workshop should I ask about?" |
| Primary narrative beat | Skill pillars become practical workshop dossiers. |
| 3D state at entry | Workshop dossiers appear on desk. |
| 3D state during scene | Workshop preview cards appear as DOM content; 3D supports atmosphere only. |
| 3D state at exit | Cards recede and mentor/trust context opens. |
| DOM content visible | Workshop cards with title, level, skill bullets, and CTA. |
| Primary CTA present? | Yes |
| CTA type | Ask About This Workshop via WhatsApp |
| Secondary CTA | View Details `/workshops/[slug]` |
| Transition in | Pillar cards transform conceptually into workshop previews. |
| Transition out | Workshop interest transitions toward mentor credibility. |
| Mobile adaptation | Stacked cards with at least 44px tap targets. |
| Reduced-motion equivalent | Static workshop list/grid. |
| Accessibility note | Workshop CTAs must be links/buttons with clear labels. |
| Performance note | Avoid Raycaster dependency in MVP; DOM cards first. |
| Bilingual/RTL note | Arabic titles and CTA labels must wrap safely inside cards. |

Rules:

- No pricing unless confirmed.
- No fake capacity.
- No countdown.
- No fake cohort/deadline.
- No dashboard/course catalog behavior.

Low-fidelity wireframe:

```text
+------------------------------------------------------+
| SCENE 06 / 62-72%                                    |
| [3D: desk/dossier atmosphere behind DOM cards]       |
|                                                      |
| [Workshops headline]                                 |
| [Workshop Card: title, level, skills, CTA]           |
| [Workshop Card: title, level, skills, CTA]           |
| [Workshop Card: placeholder-safe if content pending] |
|                                                      |
| [CTA per card: Ask via WhatsApp] [View Details]      |
+------------------------------------------------------+
```

---

## 11. Scene 07 Storyflow - Hall of Mentors

| Field | Required Answer |
| --- | --- |
| Full page scroll range | 72-82% |
| Scene objective | Build credibility through mentor presence without inventing credentials. |
| User question answered | "Who is behind this, and can I trust them?" |
| Primary narrative beat | The offer becomes human and guided, not anonymous. |
| 3D state at entry | Workshop cards clear into a calmer chamber/gallery atmosphere. |
| 3D state during scene | Low 3D atmosphere, subtle Seal/chamber depth; mentor cards remain DOM. |
| 3D state at exit | Mentor credibility leads into proof/authority section. |
| DOM content visible | Mentor placeholders or verified mentor cards: name, role, short bio/photo if approved. |
| Primary CTA present? | Optional |
| CTA type | Register Interest / WhatsApp if appropriate |
| Secondary CTA | Ask about mentors / persistent WhatsApp. |
| Transition in | Workshop interest opens into guidance/people. |
| Transition out | People/trust cues lead into credibility/proof structure. |
| Mobile adaptation | Stacked mentor cards; image placeholders only if real assets missing. |
| Reduced-motion equivalent | Static mentor grid/list. |
| Accessibility note | Do not use image-only mentor names; all credentials must be DOM text. |
| Performance note | Optimize images later; placeholders until photos are confirmed. |
| Bilingual/RTL note | Arabic role titles may need extra line height and no cramped card layout. |

Low-fidelity wireframe:

```text
+------------------------------------------------------+
| SCENE 07 / 72-82%                                    |
| [3D: subdued chamber/seal atmosphere]                |
|                                                      |
| [Hall of Mentors headline]                           |
| [Mentor Card] [Mentor Card] [Mentor Card]            |
| [Role / short verified bio or placeholder note]      |
|                                                      |
| [Optional CTA: Register Interest]                    |
| No invented credentials                              |
+------------------------------------------------------+
```

---

## 12. Scene 08 Storyflow - Trust / Authority / Credibility

| Field | Required Answer |
| --- | --- |
| Full page scroll range | 82-88% |
| Scene objective | Show credibility and authority only through verified material. |
| User question answered | "Why should I trust Mithaq?" |
| Primary narrative beat | Proof is editorial, restrained, and honest. |
| 3D state at entry | Mentor atmosphere resolves into minimal legal/trust backdrop. |
| 3D state during scene | Minimal/static 3D; Seal may appear as watermark/motif only. |
| 3D state at exit | Trust blocks clear into FAQ. |
| DOM content visible | Verified proof blocks, institutional notes, methodology credibility, or placeholder-safe structure. |
| Primary CTA present? | Optional |
| CTA type | Register Interest / WhatsApp if proof supports conversion. |
| Secondary CTA | None or persistent WhatsApp. |
| Transition in | Mentor trust becomes broader institutional credibility. |
| Transition out | Proof leads into user questions and objections. |
| Mobile adaptation | Single-column proof blocks. |
| Reduced-motion equivalent | Static editorial proof section. |
| Accessibility note | No fake statistics; no proof as decorative image text. |
| Performance note | Low/static; avoid adding heavy 3D here. |
| Bilingual/RTL note | Arabic proof copy needs clarity, not overly small metadata. |

Low-fidelity wireframe:

```text
+------------------------------------------------------+
| SCENE 08 / 82-88%                                    |
| [Minimal 3D/static chamber atmosphere]               |
|                                                      |
| [Trust / Authority headline]                         |
| [Verified proof block or placeholder-safe note]      |
| [Verified proof block or methodology note]           |
| [Verified proof block if available]                  |
|                                                      |
| [Optional CTA] [Persistent WhatsApp]                 |
+------------------------------------------------------+
```

---

## 13. Scene 09 Storyflow - FAQ

| Field | Required Answer |
| --- | --- |
| Full page scroll range | 88-94% |
| Scene objective | Resolve practical objections before final conversion. |
| User question answered | "What else do I need to know before asking or registering?" |
| Primary narrative beat | The experience pauses motion and gives clear answers. |
| 3D state at entry | Minimal or no 3D; editorial reading state. |
| 3D state during scene | Static/no canvas dependency; FAQ is semantic DOM. |
| 3D state at exit | FAQ clears into final seal callback. |
| DOM content visible | FAQ questions/answers with honest placeholder-safe content. |
| Primary CTA present? | Yes, but not aggressive. |
| CTA type | Ask via WhatsApp |
| Secondary CTA | Register Interest |
| Transition in | Trust blocks clear into structured questions. |
| Transition out | FAQ closes into final Seal/CTA world. |
| Mobile adaptation | Native/semantic accordion; minimal or instant motion. |
| Reduced-motion equivalent | Instant/native accordion. |
| Accessibility note | Use accessible accordion pattern later; focus order follows DOM. |
| Performance note | No heavy 3D; protect readability. |
| Bilingual/RTL note | Arabic questions may wrap longer; allow generous accordion height. |

Low-fidelity wireframe:

```text
+------------------------------------------------------+
| SCENE 09 / 88-94%                                    |
| [No/minimal 3D: reading-first section]               |
|                                                      |
| [FAQ headline]                                       |
| [Question 01 v] [Answer text]                        |
| [Question 02 v]                                      |
| [Question 03 v]                                      |
|                                                      |
| [CTA: Ask via WhatsApp] [Register Interest]          |
+------------------------------------------------------+
```

---

## 14. Scene 10 Storyflow - Final CTA / Closing Covenant

| Field | Required Answer |
| --- | --- |
| Full page scroll range | 94-100% |
| Scene objective | Close the journey with a calm, premium action point. |
| User question answered | "What should I do next?" |
| Primary narrative beat | The Seal returns as a covenant callback, now tied to user action. |
| 3D state at entry | FAQ clears; Seal/desk callback reappears. |
| 3D state during scene | Seal centered or near-centered; gavel secondary; warm desk/chamber closure. |
| 3D state at exit | Static final covenant poster with CTA. |
| DOM content visible | Final headline, supporting line, WhatsApp CTA, Register Interest CTA, optional workshop link. |
| Primary CTA present? | Yes |
| CTA type | WhatsApp / Register Interest |
| Secondary CTA | View workshop details / workshop section. |
| Transition in | FAQ clears into Seal callback. |
| Transition out | End state remains stable; no timed disappearance. |
| Mobile adaptation | CTA-first closing section; static seal/desk poster. |
| Reduced-motion equivalent | Static final poster with immediate CTA visibility. |
| Accessibility note | CTA remains keyboard-accessible and visible; no motion-required close. |
| Performance note | Low/medium 3D; static fallback acceptable and likely preferred on weak devices. |
| Bilingual/RTL note | Arabic CTA block may use different composition; do not force English layout. |

Low-fidelity wireframe:

```text
+------------------------------------------------------+
| SCENE 10 / 94-100%                                   |
| [3D/static: centered seal, desk callback]            |
|                                                      |
|             [FINAL HEADLINE]                         |
|             [Support copy]                           |
|             [WhatsApp CTA] [Register Interest]       |
|             [Optional: View workshop details]        |
|                                                      |
| End state: stable, no disappearing CTA               |
+------------------------------------------------------+
```

---

## 15. Scene Transition Map

| Transition | UX Meaning | Motion Direction | Avoid |
| --- | --- | --- | --- |
| 01 -> 02 | Symbol becomes brand clarity. | Seal stabilizes; text appears. | Jarring cut or delayed CTA. |
| 02 -> 03 | Promise meets problem. | Chamber darkens; documents fragment. | Confusing jump or horror mood. |
| 03 -> 04 | Chaos becomes method. | Documents converge into order. | Overcomplex morph. |
| 04 -> 05 | Method becomes pillars. | Ordered desk reveals cards/dossiers. | Dashboard feel. |
| 05 -> 06 | Pillars become workshops. | Dossiers become workshop previews. | Course catalog overload. |
| 06 -> 07 | Offer becomes trust. | Cards clear; mentor gallery appears. | Random section cut. |
| 07 -> 08 | People become proof. | Mentor credibility leads to proof structure. | Fake authority. |
| 08 -> 09 | Proof leads to answers. | Trust blocks clear into FAQ. | Heavy animation in reading section. |
| 09 -> 10 | Objections lead to action. | FAQ clears to final Seal callback. | CTA delay or overdramatic zoom. |

---

## 16. CTA Visibility Map

| Scene | Persistent WhatsApp | Primary CTA | Secondary CTA | Notes |
| --- | --- | --- | --- | --- |
| 01 | Yes after safe point / always in fallback | Register/WhatsApp by handoff | None | Fallback should expose CTA early. |
| 02 | Yes | Register Interest / WhatsApp | View pillars/workshops | Primary CTA above fold. |
| 03 | Yes | No | Continue cue optional | Do not over-convert during problem recognition. |
| 04 | Yes | Soft only | View pillars | Keeps narrative moving without pressure. |
| 05 | Yes | View Workshops / Register Interest | WhatsApp | First skill-based conversion point. |
| 06 | Yes | Ask About Workshop | View Details | Highest workshop-specific conversion point. |
| 07 | Yes | Optional Register Interest | Ask about mentors | Use only if mentor content is credible. |
| 08 | Yes | Optional Register Interest | None | No fake proof-driven pressure. |
| 09 | Yes | Ask via WhatsApp | Register Interest | FAQ should resolve and convert gently. |
| 10 | Yes | WhatsApp / Register Interest | View workshop details | Final stable close; CTA never disappears. |

CTA rules:

- Do not hide all conversion paths until Scene 10.
- Do not pulse WhatsApp aggressively.
- Do not create fake urgency around registration.
- Filled gold CTAs use near-black text.
- Gold-dim remains decorative only.

---

## 17. 3D State Timeline

| Scene | 3D State | Complexity | Fallback |
| --- | --- | --- | --- |
| 01 | Gavel/Seal opening. | High | Static seal/desk poster. |
| 02 | Seal hero anchor. | High/Medium | Static hero poster. |
| 03 | Fragmented documents. | Medium | Static document collage. |
| 04 | Documents align into method desk. | Medium | Static ordered desk. |
| 05 | Dossier/card anchors. | Low/Medium | DOM cards only. |
| 06 | Workshop dossiers. | Medium | DOM workshop cards. |
| 07 | Chamber/portrait atmosphere. | Low | DOM mentor cards. |
| 08 | Minimal atmosphere. | Low/static | Editorial proof blocks. |
| 09 | None/minimal. | Static | Semantic FAQ. |
| 10 | Seal callback. | Low/Medium | Static final poster. |

3D priority rule:

**Only Scene 01-02 should be treated as first vertical-slice heavy 3D.** Scenes 05-10 should lean DOM/editorial unless later mobile and performance validation supports more 3D.

---

## 18. DOM Content Timeline

| Scene | DOM Must Include | Canvas May Support |
| --- | --- | --- |
| 01 | Brand identity, tagline, CTA by handoff. | Opening symbolism. |
| 02 | Hero headline, body, CTA. | Seal atmosphere. |
| 03 | Problem headline/body. | Document metaphor. |
| 04 | Method headline/principles. | Ordered desk metaphor. |
| 05 | Five pillar cards. | Dossier atmosphere. |
| 06 | Workshop cards and CTAs. | Dossier objects. |
| 07 | Mentor cards/placeholders. | Chamber atmosphere. |
| 08 | Trust/proof structure. | Minimal atmosphere. |
| 09 | FAQ accordion. | None/minimal. |
| 10 | Final headline, support copy, CTA. | Seal callback. |

DOM-first rule:

If canvas fails, the DOM content must still communicate the page and preserve conversion access.

---

## 19. Trigger Map

| Trigger Point | Action | Scene |
| ---: | --- | --- |
| 0% | Scene 01 starts; dark void and accessible fallback content are present. | 01 |
| 5% | Opening desk/gavel reveal progresses; CTA must be available in fallback. | 01 |
| 10% | Hero state begins; Seal stabilizes. | 02 |
| 22% | Gap documents enter; problem section begins. | 03 |
| 37% | Documents begin convergence into method. | 04 |
| 50% | Pillar dossiers/cards reveal. | 05 |
| 62% | Workshop dossier preview begins. | 06 |
| 72% | Mentor gallery appears. | 07 |
| 82% | Trust/authority section begins. | 08 |
| 88% | FAQ section begins. | 09 |
| 94% | Final CTA seal callback begins. | 10 |
| 100% | Closing covenant complete; CTA remains stable. | 10 |

---

## 20. Bilingual / RTL Storyflow Notes

Global rules:

- Arabic and English should use localized layout behavior, not forced side-by-side everywhere.
- Use `dir="rtl"` for Arabic and `dir="ltr"` for English.
- Scene headlines must have enough width in Arabic.
- Arabic animation should use line/block reveal, not letter-by-letter.
- CTA labels must be tested in Arabic and English.
- Workshop cards must allow Arabic text expansion.
- FAQ questions must allow longer Arabic wrapping.
- Do not bake Arabic/English text into 3D textures.
- Language toggle must be accessible from header/mobile nav.
- Final storyflow must work in both language directions.
- Respect Tajawal 700 as Arabic display default; Lemonada remains accent-only pending review.

| Scene | Arabic/RTL Concern | English/LTR Concern | Storyflow Decision |
| --- | --- | --- | --- |
| 01 | Arabic wordmark/tagline may need different width and line height. | English headline can sit compactly beside Seal. | Keep brand text as DOM; allow localized handoff composition. |
| 02 | Arabic hero headline may wrap into more lines. | English hero can use more editorial whitespace. | Text-first localized hero; do not force identical column widths. |
| 03 | Arabic problem copy needs protected reading zone. | English can use shorter lines. | Use large clear DOM zone; fragments stay away from text. |
| 04 | Arabic method principles need generous line height. | English principles can be compact. | Use flexible list/card heights. |
| 05 | Arabic pillar titles and explanations expand. | English cards may appear visually shorter. | Card layout must equalize by content structure, not fixed height. |
| 06 | Arabic workshop titles/CTAs may wrap. | English CTA labels are shorter. | Test card width and 44px tap targets in both languages. |
| 07 | Arabic role titles may need more vertical space. | English mentor metadata can be smaller. | Avoid cramped mentor card layout. |
| 08 | Arabic proof/legal wording may be longer. | English proof blocks can be terse. | Use editorial stacked blocks, not dense columns. |
| 09 | Arabic FAQ questions may be long. | English accordion labels shorter. | Accordion supports multi-line questions. |
| 10 | Arabic CTA composition may need headline-first flow. | English CTA can sit beside Seal. | CTA-first localized closing; no same-line language mixing. |

---

## 21. Mobile Storyflow Notes

| Scene | Desktop Storyflow | Mobile Storyflow |
| --- | --- | --- |
| 01 | Full scroll-driven opening. | Shortened opening/static fallback option. |
| 02 | 3D + copy composition. | Text-first, seal poster/low 3D. |
| 03 | Floating documents. | Static/limited document collage. |
| 04 | Document convergence. | Static ordered method blocks. |
| 05 | Dossier/card reveal. | Vertical pillar stack. |
| 06 | Workshop dossiers/cards. | Stacked workshop cards. |
| 07 | Mentor gallery. | Stacked/swipe-safe mentor cards. |
| 08 | Proof/trust grid. | Single-column proof blocks. |
| 09 | FAQ accordion. | Native/semantic accordion. |
| 10 | Seal callback. | CTA-first closing section. |

Mobile rules:

- Do not create long pinned scroll experiences on mobile unless tested.
- Do not hide CTA behind motion.
- Do not require WebGL for understanding.
- Keep tap targets at least 44px.
- Avoid hover-only states.
- Reduce particles and camera motion.
- Make WhatsApp CTA easy to reach.
- If FPS drops, disable non-essential motion and 3D support.

---

## 22. Reduced-Motion / Static Storyflow

| Scene | Standard Storyflow | Reduced-Motion Equivalent |
| --- | --- | --- |
| 01 | Scroll-driven gavel/seal reveal. | Static seal/desk poster + fade-in brand/CTA. |
| 02 | Seal anchor + text reveal. | Static hero content. |
| 03 | Floating documents. | Static document collage. |
| 04 | Documents align. | Static method layout. |
| 05 | Pillar cards stagger. | Static cards. |
| 06 | Workshop dossier reveal. | Static card grid/list. |
| 07 | Mentor gallery motion. | Static mentor cards. |
| 08 | Trust block reveal. | Static trust section. |
| 09 | FAQ accordion. | Instant/native accordion. |
| 10 | Seal callback reveal. | Static closing CTA. |

Reduced-motion rule:

Reduced-motion users must not lose content, CTA access, orientation, or the meaning of the Covenant Seal journey.

---

## 23. Accessibility Storyflow Notes

- Plan a skip-to-content link before the cinematic opening.
- Each scene should be a semantic section with a meaningful heading.
- CTA elements must be real links/buttons, not canvas hotspots.
- FAQ must use accessible accordion patterns during implementation.
- Scroll-driven content must not create keyboard traps or scroll traps.
- Canvas must not contain the only meaningful text.
- Reduced motion must not remove content.
- Focus order should follow DOM order, not visual animation order.
- Language toggle must announce current language.
- WhatsApp link must have a clear accessible label.
- Static fallback must be equivalent in meaning.
- No critical copy should be baked into 3D textures or images.
- All cards and accordions should be navigable by keyboard when implemented.

---

## 24. Performance Storyflow Notes

| Scene | Performance Risk | Storyflow Mitigation |
| --- | --- | --- |
| 01 | Heavy opening assets. | Placeholder/optimized assets, fallback poster, vertical-slice test. |
| 02 | Canvas blocking content. | DOM-first content and CTA; lazy/non-blocking 3D where possible. |
| 03 | Too many document meshes. | Cap meshes; static collage fallback. |
| 04 | Expensive morph/convergence. | Use simplified alignment transition. |
| 05 | Heavy card overlays. | DOM cards; 3D only as atmosphere. |
| 06 | Raycaster/dossier complexity. | DOM cards first; no interactive 3D dependency. |
| 07 | Portrait/gallery load. | Optimized images/placeholders; defer non-critical assets. |
| 08 | Fake/unknown proof and unnecessary effects. | Editorial placeholder structure; low/static motion. |
| 09 | FAQ readability. | No heavy 3D. |
| 10 | CTA hidden by effect. | CTA visible immediately; static fallback. |

Performance principles:

- Scene 01-02 are the first vertical-slice priority.
- Scene 01 has the highest 3D complexity.
- Scene 02 must protect LCP and CTA visibility.
- Scenes 05-10 should lean DOM/editorial unless later approved.
- Do not make every scene heavy WebGL.
- Lazy-load non-critical 3D objects.
- Keep text independent from canvas.
- Mobile may use static fallback earlier.
- No performance claim is final until vertical-slice testing.

---

## 25. Storyflow Guardrail Table

| Keep | Avoid |
| --- | --- |
| 10-scene scroll journey. | Random disconnected sections. |
| Scene 01-02 as vertical-slice priority. | Heavy 3D in all 10 scenes. |
| Seal-led continuity. | Gavel dominating every scene. |
| DOM-first content. | Canvas-only messaging. |
| Persistent WhatsApp access. | CTA only at the end. |
| Clear scroll ranges. | Ambiguous motion triggers. |
| Static fallback per scene. | 3D-dependent meaning. |
| Mobile-shortened flow. | Desktop choreography forced on phones. |
| Arabic/English localized flow. | English-only storyflow assumptions. |
| Verified trust/proof only. | Fake testimonials, fake stats, fake urgency. |

---

## 26. Final Storyflow Recommendation

| Decision Area | Recommendation |
| --- | --- |
| Full-page scene order | Keep the 10-scene order exactly as planned. |
| Scroll range allocation | Keep baseline ranges; only tune after copy/asset/mobile testing. |
| Highest-priority vertical slice scenes | Scene 01 and Scene 02. |
| Heavy 3D scenes | Scene 01 high; Scene 02 high/medium; Scene 10 low/medium callback. |
| DOM-first scenes | Scenes 03-10, with especially strong DOM reliance in Scenes 05-09. |
| CTA visibility model | Persistent WhatsApp plus visible major CTAs in Scenes 02, 05, 06, 09, and 10. |
| Mobile simplification model | Shortened opening, reduced camera/particles, stacked cards, static/low 3D fallback. |
| Reduced-motion model | Static poster/DOM equivalent for every scene; no meaning lost. |
| Bilingual storyflow model | Localized Arabic/English flows with `dir` support and no mixed-font same-line animation. |
| Production risk level | Medium: concept is clear, but final scroll timing depends on copy, assets, mobile validation, and vertical-slice performance. |

Final recommendation:

**Proceed with the 10-scene storyflow as the main landing route plan, but treat Scene 01-02 as the only heavy 3D vertical-slice priority until final assets and mobile performance are validated. Keep every other scene readable, semantic, bilingual-safe, and conversion-ready without relying on WebGL.**

---

## 27. Quality Gate

| Gate | Status | Notes |
| --- | --- | --- |
| All 10 scenes included | PASS | Scenes 01-10 documented. |
| Every scene has scroll range | PASS | Full-page ranges included. |
| Every scene defines 3D state | PASS | Entry/during/exit state included per scene. |
| Every scene defines DOM content | PASS | DOM content visible field included per scene. |
| Every scene defines primary CTA presence | PASS | CTA presence and type included. |
| Every scene defines transition in/out | PASS | Per-scene fields plus transition map. |
| Every scene includes mobile notes | PASS | Per-scene notes and mobile table. |
| Every scene includes reduced-motion/fallback notes | PASS | Per-scene notes and static storyflow table. |
| Every scene includes bilingual/RTL notes | PASS | Per-scene notes and bilingual table. |
| CTA visibility map complete | PASS | Scenes 01-10 covered. |
| 3D state timeline complete | PASS | Scenes 01-10 covered. |
| DOM content timeline complete | PASS | Scenes 01-10 covered. |
| Transition map complete | PASS | All scene-to-scene transitions included. |
| Storyflow low-fidelity, not final UI | PASS | ASCII wireframes only; no visual comps. |
| Avoided implementation | PASS | No GSAP, Lenis, R3F, or frontend code created. |
| Avoided new roadmap tickets | PASS | No new tickets created. |

---

## 28. Acceptance Criteria

| Acceptance Criteria | Status |
| --- | --- |
| Storyflow document created | PASS |
| 10 scenes included | PASS |
| Scroll % range assigned to every scene | PASS |
| 3D state documented for every scene | PASS |
| DOM content documented for every scene | PASS |
| Primary CTA presence documented for every scene | PASS |
| Scene transition map documented | PASS |
| CTA visibility map documented | PASS |
| 3D state timeline documented | PASS |
| DOM content timeline documented | PASS |
| Bilingual/RTL storyflow notes included | PASS |
| Mobile storyflow notes included | PASS |
| Reduced-motion/static storyflow included | PASS |
| Accessibility storyflow notes included | PASS |
| Performance storyflow notes included | PASS |
| Storyflow guardrail table included | PASS |
| Wireframe-level representation exists for all scenes | PASS |
| No final UI comps created | PASS |
| No frontend implementation started | PASS |
| No new roadmap tickets created | PASS |

---

## 29. Final Status

**PASS WITH CONDITIONS - P3.02 complete. Full 10-scene scroll storyflow is documented with scroll ranges, 3D states, DOM content, CTA presence, transitions, mobile, fallback, bilingual, accessibility, and performance notes.**

Final storyflow remains conditional on final copy, final 3D assets, final workshop/mentor/trust content, stakeholder review, mobile validation, reduced-motion QA, and vertical-slice performance testing.
