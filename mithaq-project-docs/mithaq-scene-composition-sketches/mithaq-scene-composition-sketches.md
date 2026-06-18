# Mithaq Scene Composition Sketches

**Official Ticket ID:** P2.06  
**Official Ticket Name:** Scene Composition Sketches  
**Phase:** Phase 2 - Creative Concept Development  
**Priority:** P0  
**Complexity:** Medium  
**Owner:** Creative Director / UI Art Director  
**Status:** PASS WITH CONDITIONS  
**Prepared date:** 2026-06-18  

---

## 1. Executive Summary

This document defines quick thumbnail composition sketches for the 10 Mithaq landing experience scenes.

These are directional layout sketches only. They define:

- 3D element placement
- Text placement
- CTA placement
- Visual hierarchy
- Negative space
- Scroll transition direction
- Mobile simplification
- Reduced-motion/static fallback
- Bilingual composition considerations
- Performance complexity

Final recommendation:

**Proceed with a Seal-led composition system where Scenes 01-02 prove the cinematic vertical slice, Scene 10 protects conversion clarity, and the remaining scenes stay editorial/static-first until content and asset readiness improve.**

Status is **PASS WITH CONDITIONS** because final layouts still depend on final content, official brand assets, final seal approval, workshop/mentor/trust material, stakeholder review, UX storyflow, and vertical-slice validation.

No final UI screens, final Figma comps, design system, 3D assets, production copy, frontend implementation, or new roadmap tickets were created.

---

## 2. Current Mithaq Decisions

- Mithaq is a premium bilingual 3D legal academy portfolio / landing experience.
- Mithaq is not an LMS, dashboard, booking system, payment system, course-management system, or operational platform.
- Core concept: The Covenant Seal.
- 3D direction: Option D - Seal-Led Macro Legal Chamber.
- Opening direction: Scroll-Driven Seal-Led Opening.
- The gavel is the ceremonial trigger.
- The Mithaq Seal is the visual hero and recurring motif.
- Primary conversion: WhatsApp.
- Secondary conversion: simple inquiry form.
- MVP planning is bilingual.
- Arabic and English must be planned as real layouts.
- Tajawal 700 is the safe Arabic display default.
- Lemonada is accent-only pending review.
- P2.02 color tokens remain candidate tokens.
- Filled gold CTAs must use near-black text.
- `gold-dim` is decorative only.
- Red is not body text on dark backgrounds.
- Delivery approach: Vertical Slice First.
- P1.05 feasibility decision: Option C - Vertical Slice Only Until Asset Optimization.
- Production-grade 3D complexity is not approved yet.
- Mobile simplification and static fallback are mandatory.
- No fake urgency, fake proof, countdowns, seat counters, or unsupported claims.

---

## 3. Sketching Method

Format used:

- Markdown thumbnail sketches with labeled grayscale-style blocks.
- One sketch per official landing scene.
- Per-scene annotation tables.
- Per-scene bilingual layout notes.

Sketch rules:

- These are not final layouts.
- These are not polished UI comps.
- Blocks show placement, hierarchy, and scroll behavior only.
- All text is placeholder-safe and not final website copy.
- 3D zones are conceptual; no 3D assets are produced.

Legend:

```text
[3D]   = conceptual WebGL/static visual zone
[TXT]  = DOM copy zone
[CTA]  = WhatsApp/form/detail action zone
[NAV]  = optional page/navigation context
[SAFE] = protected negative space / readability zone
```

---

## 4. Scene 01 Sketch + Notes - Gavel / Seal Opening

```text
------------------------------------------------
|                  DARK VOID                   |
|                                              |
|             [3D SEAL FORMING]                |
|                                              |
|       gavel secondary after trigger          |
|                                              |
|                    [SAFE]                    |
|             brand/CTA appear at handoff      |
------------------------------------------------
```

| Field | Direction |
| ----- | --------- |
| Scene number | 01 |
| Scene name | Gavel / Seal Opening |
| Scene objective | Establish premium legal authority and reveal the Mithaq Seal. |
| Primary message | The covenant begins through a ceremonial legal signal. |
| 3D element placement | Seal centered; gavel enters as trigger and rests secondary/side after impact. |
| Text placement | Minimal/delayed; brand identity appears near final handoff only. |
| CTA placement | At handoff or always available in fallback/mobile. |
| Visual hierarchy | 1. Darkness, 2. gavel trigger, 3. Seal reveal, 4. brand/CTA. |
| Negative space | Large dark space around centered seal; no copy competing during reveal. |
| Scroll transition | Entry from black into desk/gavel/seal; exits into hero composition. |
| Bilingual note | Brand identity appears as separate Arabic and English DOM elements; no mixed line. |
| Mobile note | Shorter/simplified seal reveal; CTA available earlier. |
| Reduced-motion note | Static seal/desk poster plus fade-in brand/CTA. |
| Performance note | High desktop vertical-slice candidate only; particles and shader effects capped. |
| Sketch reference | Markdown thumbnail above. |

Annotation:

| Area | Decision |
| ---- | -------- |
| Primary focal point | Mithaq Seal forming at center. |
| Secondary focal point | Gavel after trigger, off-center. |
| Text zone | Delayed lower/side safe zone at handoff. |
| CTA zone | Appears at bottom/side after reveal or early in fallback. |
| 3D zone | Full viewport, but content remains DOM-first. |
| Scroll entry | Black void and dust. |
| Scroll exit | Stable hero handoff. |
| Mobile adaptation | Condensed reveal, reduced particles. |
| Reduced-motion equivalent | Static premium poster and fade. |

Bilingual check:

| Language Question | Answer |
| ----------------- | ------ |
| Does Arabic/English appear together or through language toggle? | Prefer language-specific layout; optional brand pairing at handoff. |
| If together, where does secondary language appear? | Smaller support line below primary identity, separate element. |
| Does Arabic get enough line-height and width? | Yes; avoid cramped seal-side overlay. |
| Is any text baked into 3D? | No. |
| How does CTA text fit in Arabic and English? | CTA uses DOM button; Arabic/English labels tested separately. |

---

## 5. Scene 02 Sketch + Notes - Hero / Mithaq Reveal

```text
------------------------------------------------
| [TXT: headline/body]          [3D SEAL]       |
| [TXT: positioning]             behind/side    |
| [CTA: WhatsApp] [form/detail]                 |
|                                                |
|         gavel secondary / desk atmosphere      |
------------------------------------------------
```

| Field | Direction |
| ----- | --------- |
| Scene number | 02 |
| Scene name | Hero / Mithaq Reveal |
| Scene objective | Clarify what Mithaq is and why it matters. |
| Primary message | Practical legal training that moves learners toward professional readiness. |
| 3D element placement | Seal behind or beside copy; gavel secondary; desk/chamber atmosphere. |
| Text placement | Strong editorial block in protected column. |
| CTA placement | Primary WhatsApp CTA prominent; secondary form/detail link nearby. |
| Visual hierarchy | 1. Headline, 2. Seal atmosphere, 3. CTA, 4. support copy. |
| Negative space | Protected text column; 3D never crosses copy contrast zone. |
| Scroll transition | Receives stable state from Scene 01; exits into problem/gap scroll. |
| Bilingual note | Prefer localized hero layouts; Arabic and English not forced together. |
| Mobile note | Text first; 3D becomes reduced/poster background; CTA above fold. |
| Reduced-motion note | Static hero with same semantic content. |
| Performance note | High priority for vertical slice; 3D lazy/conditional after DOM content. |
| Sketch reference | Markdown thumbnail above. |

Annotation:

| Area | Decision |
| ---- | -------- |
| Primary focal point | Readable headline/value proposition. |
| Secondary focal point | Seal as atmospheric anchor. |
| Text zone | Left/start column on desktop; top stack on mobile. |
| CTA zone | Directly under supporting copy. |
| 3D zone | Right/end or background, constrained by overlay. |
| Scroll entry | From completed opening seal. |
| Scroll exit | Copy fades/scrolls into problem framing. |
| Mobile adaptation | DOM-first stack, shorter visual. |
| Reduced-motion equivalent | Static seal/desk background. |

Bilingual check:

| Language Question | Answer |
| ----------------- | ------ |
| Does Arabic/English appear together or through language toggle? | Language toggle/localized layout preferred. |
| If together, where does secondary language appear? | Beneath primary headline as smaller support only. |
| Does Arabic get enough line-height and width? | Yes; Arabic hero may use wider/top-first block. |
| Is any text baked into 3D? | No. |
| How does CTA text fit in Arabic and English? | CTA container must fit longer Arabic labels without shrinking below 44px height. |

---

## 6. Scene 03 Sketch + Notes - The Gap

```text
------------------------------------------------
| [3D: fragmented docs orbit/field]   [TXT]     |
| papers around empty center          gap copy  |
|                                      [soft]   |
|                                      continue |
------------------------------------------------
```

| Field | Direction |
| ----- | --------- |
| Scene number | 03 |
| Scene name | The Gap |
| Scene objective | Show that academic legal study does not equal practical readiness. |
| Primary message | Knowing the law is not the same as being ready to practice it. |
| 3D element placement | Floating documents around an empty center/side field. |
| Text placement | Clear editorial block opposite document field. |
| CTA placement | Usually none; optional soft continue cue. |
| Visual hierarchy | 1. Gap copy, 2. controlled document fragmentation, 3. empty center. |
| Negative space | Text side stays clean; document field does not cross copy. |
| Scroll transition | Exits hero into fragmented documents; exits into organized method. |
| Bilingual note | Problem statement needs native Arabic phrasing, not literal translation. |
| Mobile note | Max 3 document elements or static collage; copy first. |
| Reduced-motion note | Static fragmented document poster. |
| Performance note | Medium later; avoid many transparent paper meshes. |
| Sketch reference | Markdown thumbnail above. |

Annotation:

| Area | Decision |
| ---- | -------- |
| Primary focal point | Problem headline/copy. |
| Secondary focal point | Fragmented legal papers. |
| Text zone | Right/end column desktop; first stack mobile. |
| CTA zone | Optional subtle continue cue only. |
| 3D zone | Side field or behind negative center. |
| Scroll entry | Hero seal recedes; documents emerge. |
| Scroll exit | Documents begin organizing. |
| Mobile adaptation | Static 2-3 paper shapes. |
| Reduced-motion equivalent | Static collage. |

Bilingual check:

| Language Question | Answer |
| ----------------- | ------ |
| Does Arabic/English appear together or through language toggle? | Localized layout preferred. |
| If together, where does secondary language appear? | Not recommended here; the emotional message should be native. |
| Does Arabic get enough line-height and width? | Yes; avoid narrow Arabic problem statement. |
| Is any text baked into 3D? | No; papers may have abstract marks only. |
| How does CTA text fit in Arabic and English? | No main CTA expected. |

---

## 7. Scene 04 Sketch + Notes - The Mithaq Method

```text
------------------------------------------------
| [TXT: Method explanation]                      |
| [soft CTA]                                     |
|                                                |
|       [3D: documents align into desk system]   |
|       [ordered files / seal mark / pen]        |
------------------------------------------------
```

| Field | Direction |
| ----- | --------- |
| Scene number | 04 |
| Scene name | The Mithaq Method |
| Scene objective | Show how Mithaq turns confusion into practical structure. |
| Primary message | Mithaq organizes legal learning around practical professional outputs. |
| 3D element placement | Ordered desk/object arrangement center/lower field. |
| Text placement | Editorial method block above/side. |
| CTA placement | Optional "View Training Pillars" soft CTA. |
| Visual hierarchy | 1. Method headline, 2. ordered desk system, 3. soft CTA. |
| Negative space | Balanced split; enough breathing room around method copy. |
| Scroll transition | Documents from Scene 03 converge into order. |
| Bilingual note | Arabic method copy may need more vertical space; keep layout flexible. |
| Mobile note | Static before/after or vertical method blocks. |
| Reduced-motion note | Documents already organized; no morph required. |
| Performance note | P2/static-first; avoid complicated morph animations early. |
| Sketch reference | Markdown thumbnail above. |

Annotation:

| Area | Decision |
| ---- | -------- |
| Primary focal point | Method copy. |
| Secondary focal point | Ordered documents/dossier system. |
| Text zone | Top/start editorial block. |
| CTA zone | Small text link below method copy. |
| 3D zone | Lower/center desk arrangement. |
| Scroll entry | Fragmentation becomes structure. |
| Scroll exit | Structure becomes pillar dossiers. |
| Mobile adaptation | Vertical blocks. |
| Reduced-motion equivalent | Static organized desk. |

Bilingual check:

| Language Question | Answer |
| ----------------- | ------ |
| Does Arabic/English appear together or through language toggle? | Localized layout preferred. |
| If together, where does secondary language appear? | Short support line only. |
| Does Arabic get enough line-height and width? | Yes; method block may become full-width. |
| Is any text baked into 3D? | No. |
| How does CTA text fit in Arabic and English? | Soft CTA must wrap naturally, not mono/uppercase. |

---

## 8. Scene 05 Sketch + Notes - Training Pillars

```text
------------------------------------------------
| [TXT: Training Pillars intro]                  |
|                                                |
| [CARD 1] [CARD 2] [CARD 3]                    |
| [CARD 4] [CARD 5]        [3D dossier accent]  |
|                                                |
| [soft link: workshops / interest]              |
------------------------------------------------
```

| Field | Direction |
| ----- | --------- |
| Scene number | 05 |
| Scene name | Training Pillars |
| Scene objective | Present five Mithaq pillar placeholders clearly and practically. |
| Primary message | Training is structured around practical legal capabilities. |
| 3D element placement | Dossier/file anchors around or over desk, not inside card meaning. |
| Text placement | Pillar cards in readable DOM layout. |
| CTA placement | Soft link to workshops or interest. |
| Visual hierarchy | 1. Pillar intro, 2. five cards, 3. dossier atmosphere, 4. soft CTA. |
| Negative space | Cards breathe; no dense catalog grid. |
| Scroll transition | Ordered method becomes five professional dossiers. |
| Bilingual note | Cards need enough width for Arabic titles and line-height. |
| Mobile note | Vertical stack preferred; horizontal swipe only if clearly accessible. |
| Reduced-motion note | Static cards with subtle fade. |
| Performance note | Low/static; DOM carries all meaning. |
| Sketch reference | Markdown thumbnail above. |

Approved placeholder pillars:

1. Legal Research
2. Legal Writing
3. Professional Readiness
4. Career Infrastructure
5. Practical Legal Mindset

Annotation:

| Area | Decision |
| ---- | -------- |
| Primary focal point | Pillar card group. |
| Secondary focal point | Dossier/seal accents. |
| Text zone | Cards and intro copy in DOM. |
| CTA zone | Soft link after card group. |
| 3D zone | Decorative dossier/desk support only. |
| Scroll entry | Method framework resolves into pillars. |
| Scroll exit | Pillars lead to workshops. |
| Mobile adaptation | Single-column card stack. |
| Reduced-motion equivalent | Static cards. |

Bilingual check:

| Language Question | Answer |
| ----------------- | ------ |
| Does Arabic/English appear together or through language toggle? | Localized card set preferred. |
| If together, where does secondary language appear? | Avoid full bilingual per card unless needed. |
| Does Arabic get enough line-height and width? | Yes; card min-width/stack must support Arabic. |
| Is any text baked into 3D? | No. |
| How does CTA text fit in Arabic and English? | Soft CTA remains sentence-case DOM text. |

---

## 9. Scene 06 Sketch + Notes - Workshops & Course Preview

```text
------------------------------------------------
| [TXT: Workshops intro]        [3D dossier pile]|
|                                                |
| [WORKSHOP CARD] [WORKSHOP CARD] [WORKSHOP]    |
|  title/level/skills/format                     |
|  [Ask About] [View Details]                    |
------------------------------------------------
```

| Field | Direction |
| ----- | --------- |
| Scene number | 06 |
| Scene name | Workshops & Course Preview |
| Scene objective | Show workshop placeholders as premium engagements and route users to WhatsApp/details. |
| Primary message | Explore practical workshops and ask about the right next step. |
| 3D element placement | Dossier objects on desk; DOM cards overlay/nearby. |
| Text placement | Workshop title, level, skills, format placeholders in cards. |
| CTA placement | "Ask About This Workshop" and "View Details" per card. |
| Visual hierarchy | 1. Workshop card title, 2. format/skills, 3. CTA pair, 4. dossier atmosphere. |
| Negative space | Clear card rhythm; no catalog density. |
| Scroll transition | Pillar cards become workshop dossiers. |
| Bilingual note | Arabic card text likely longer; avoid three-column lock on smaller widths. |
| Mobile note | Stacked cards, large tap targets, no hover-only details. |
| Reduced-motion note | Static card grid/list. |
| Performance note | Medium later; keep 3D dossier decorative and optional. |
| Sketch reference | Markdown thumbnail above. |

Annotation:

| Area | Decision |
| ---- | -------- |
| Primary focal point | Workshop cards. |
| Secondary focal point | Dossier desk objects. |
| Text zone | DOM cards. |
| CTA zone | Inside each card, clearly tappable. |
| 3D zone | Background/side dossier pile. |
| Scroll entry | From training pillars. |
| Scroll exit | Toward mentor authority. |
| Mobile adaptation | Stacked cards with 44px+ CTAs. |
| Reduced-motion equivalent | Static grid/list. |

Bilingual check:

| Language Question | Answer |
| ----------------- | ------ |
| Does Arabic/English appear together or through language toggle? | Localized workshop cards preferred. |
| If together, where does secondary language appear? | Secondary language can be a small subtitle only if content is approved. |
| Does Arabic get enough line-height and width? | Yes; stack at tablet/mobile sizes. |
| Is any text baked into 3D? | No. |
| How does CTA text fit in Arabic and English? | Buttons must support longer Arabic labels without shrinking. |

---

## 10. Scene 07 Sketch + Notes - Hall of Mentors

```text
------------------------------------------------
| [TXT: Hall of Mentors intro]                   |
|                                                |
| [PORTRAIT] [PORTRAIT] [PORTRAIT]              |
| name/title/bio placeholders in DOM             |
|                                                |
| [optional soft CTA]       subtle chamber/desk  |
------------------------------------------------
```

| Field | Direction |
| ----- | --------- |
| Scene number | 07 |
| Scene name | Hall of Mentors |
| Scene objective | Build trust through mentor presence, even with placeholders. |
| Primary message | Mentor credibility will anchor practical training once approved content exists. |
| 3D element placement | Subtle chamber/desk atmosphere behind portraits. |
| Text placement | Mentor name/title/bio placeholders in DOM. |
| CTA placement | Optional "Ask about mentors/training" soft CTA. |
| Visual hierarchy | 1. Mentor portraits/cards, 2. mentor title/bio, 3. atmosphere, 4. soft CTA. |
| Negative space | Portraits feel editorial, not crowded business cards. |
| Scroll transition | Workshop interest moves into human authority. |
| Bilingual note | Names/titles may be original-language; bios localized if approved. |
| Mobile note | Swipe gallery or stacked editorial cards, not tiny grid. |
| Reduced-motion note | Static portrait grid. |
| Performance note | Low/static; no fake portraits or credentials. |
| Sketch reference | Markdown thumbnail above. |

Annotation:

| Area | Decision |
| ---- | -------- |
| Primary focal point | Mentor portrait/card area. |
| Secondary focal point | Mentor credentials placeholders. |
| Text zone | Below/alongside portraits. |
| CTA zone | Optional after card group. |
| 3D zone | Background atmosphere only. |
| Scroll entry | From workshop section. |
| Scroll exit | Toward trust/proof structure. |
| Mobile adaptation | Stacked/swipe editorial cards. |
| Reduced-motion equivalent | Static grid. |

Bilingual check:

| Language Question | Answer |
| ----------------- | ------ |
| Does Arabic/English appear together or through language toggle? | Localized layout; original names may appear consistently. |
| If together, where does secondary language appear? | Under title/bio as secondary metadata only if approved. |
| Does Arabic get enough line-height and width? | Yes; mentor bios need readable line-height. |
| Is any text baked into 3D? | No. |
| How does CTA text fit in Arabic and English? | Optional CTA must remain tappable and concise. |

---

## 11. Scene 08 Sketch + Notes - Trust / Authority / Credibility

```text
------------------------------------------------
| [TXT: Trust intro]                             |
|                                                |
| [FUTURE PROOF SLOT] [FUTURE PROOF SLOT]       |
| [TESTIMONIAL SLOT]  [INSTITUTION SLOT]        |
|                                                |
| [soft CTA if appropriate]                      |
------------------------------------------------
```

| Field | Direction |
| ----- | --------- |
| Scene number | 08 |
| Scene name | Trust / Authority / Credibility |
| Scene objective | Create forward-compatible trust structure without fake proof. |
| Primary message | Verified proof will appear only when approved. |
| 3D element placement | Minimal; small seal/divider or none. |
| Text placement | Trust/proof grid with empty/future slots. |
| CTA placement | Soft CTA after trust if appropriate. |
| Visual hierarchy | 1. Trust framing, 2. verified/future proof slots, 3. CTA. |
| Negative space | High readability, low visual noise. |
| Scroll transition | Mentor credibility widens into proof/trust. |
| Bilingual note | Trust claims require language-specific legal review. |
| Mobile note | Single-column proof blocks. |
| Reduced-motion note | Static editorial section. |
| Performance note | Low/static; no carousel dependency. |
| Sketch reference | Markdown thumbnail above. |

Annotation:

| Area | Decision |
| ---- | -------- |
| Primary focal point | Trust/proof structure. |
| Secondary focal point | Seal/divider accent. |
| Text zone | Full-width or centered editorial grid. |
| CTA zone | Bottom soft CTA if appropriate. |
| 3D zone | Minimal/ambient only. |
| Scroll entry | From mentor section. |
| Scroll exit | Toward FAQ clarity. |
| Mobile adaptation | Single-column slots. |
| Reduced-motion equivalent | Same static section. |

Bilingual check:

| Language Question | Answer |
| ----------------- | ------ |
| Does Arabic/English appear together or through language toggle? | Localized trust section preferred. |
| If together, where does secondary language appear? | Not recommended for legal/proof claims. |
| Does Arabic get enough line-height and width? | Yes; proof cards must not compress Arabic. |
| Is any text baked into 3D? | No. |
| How does CTA text fit in Arabic and English? | Soft CTA only after proof, not pressure-based. |

---

## 12. Scene 09 Sketch + Notes - FAQ

```text
------------------------------------------------
| [TXT: FAQ heading]                             |
|                                                |
| [FAQ Q accordion row]                          |
| [FAQ Q accordion row]                          |
| [FAQ Q accordion row]                          |
| [FAQ Q accordion row]                          |
|                                                |
| [WhatsApp/help CTA]                            |
------------------------------------------------
```

| Field | Direction |
| ----- | --------- |
| Scene number | 09 |
| Scene name | FAQ |
| Scene objective | Answer objections clearly before conversion. |
| Primary message | Clear answers before asking the user to inquire. |
| 3D element placement | Ambient only or none. |
| Text placement | FAQ accordion full-width or centered column. |
| CTA placement | WhatsApp/help CTA near bottom. |
| Visual hierarchy | 1. FAQ heading, 2. readable questions, 3. answers, 4. help CTA. |
| Negative space | Strong reading rhythm; no visual clutter. |
| Scroll transition | Trust section resolves into practical clarity. |
| Bilingual note | FAQ must be native Arabic/English, not literal translation. |
| Mobile note | Large tap targets, vertical accordion. |
| Reduced-motion note | Same static accordion. |
| Performance note | Static recommended; semantic DOM priority. |
| Sketch reference | Markdown thumbnail above. |

Annotation:

| Area | Decision |
| ---- | -------- |
| Primary focal point | FAQ questions. |
| Secondary focal point | Help CTA. |
| Text zone | Center/full-width reading column. |
| CTA zone | Bottom of FAQ. |
| 3D zone | None or tiny ambient seal mark. |
| Scroll entry | From trust proof. |
| Scroll exit | Final CTA. |
| Mobile adaptation | Full-width accordion rows. |
| Reduced-motion equivalent | Same static content. |

Bilingual check:

| Language Question | Answer |
| ----------------- | ------ |
| Does Arabic/English appear together or through language toggle? | Language-specific FAQ preferred. |
| If together, where does secondary language appear? | Avoid together; too dense. |
| Does Arabic get enough line-height and width? | Yes; FAQ answers require generous line-height. |
| Is any text baked into 3D? | No. |
| How does CTA text fit in Arabic and English? | Help CTA remains clear and reachable. |

---

## 13. Scene 10 Sketch + Notes - Final CTA / Closing Covenant

```text
------------------------------------------------
|                  [3D SEAL]                    |
|             desk + gavel secondary            |
|                                                |
|        [TXT: Closing headline/support]         |
|        [CTA: WhatsApp primary] [form link]     |
|                                                |
|             [small brand close]                |
------------------------------------------------
```

| Field | Direction |
| ----- | --------- |
| Scene number | 10 |
| Scene name | Final CTA / Closing Covenant |
| Scene objective | Convert the user through a calm premium closing moment. |
| Primary message | Take the next step by contacting Mithaq through WhatsApp or inquiry. |
| 3D element placement | Seal centered, desk full composition, gavel secondary. |
| Text placement | Closing headline and concise support copy centered or protected below seal. |
| CTA placement | Primary WhatsApp CTA large/prominent; secondary inquiry/form link nearby. |
| Visual hierarchy | 1. Seal callback, 2. closing headline, 3. WhatsApp CTA, 4. small brand close. |
| Negative space | Ceremonial centered composition; no footer clutter. |
| Scroll transition | FAQ clarity resolves into final covenant/CTA. |
| Bilingual note | Localized final CTA; Arabic and English not crammed together. |
| Mobile note | CTA first or immediately after headline; seal may become poster. |
| Reduced-motion note | Static seal/desk closing poster. |
| Performance note | Low/static unless final slice approves 3D callback. |
| Sketch reference | Markdown thumbnail above. |

Annotation:

| Area | Decision |
| ---- | -------- |
| Primary focal point | WhatsApp CTA after seal callback. |
| Secondary focal point | Seal centered. |
| Text zone | Centered beneath/near seal. |
| CTA zone | Large central button group. |
| 3D zone | Background/center seal and desk. |
| Scroll entry | From FAQ. |
| Scroll exit | Footer/brand close. |
| Mobile adaptation | CTA immediately after headline. |
| Reduced-motion equivalent | Static poster. |

Bilingual check:

| Language Question | Answer |
| ----------------- | ------ |
| Does Arabic/English appear together or through language toggle? | Localized layout preferred. |
| If together, where does secondary language appear? | Secondary line under primary only if approved. |
| Does Arabic get enough line-height and width? | Yes; centered Arabic must not be too narrow. |
| Is any text baked into 3D? | No. |
| How does CTA text fit in Arabic and English? | Primary CTA must fit both languages; near-black text if filled gold. |

---

## 14. Bilingual Composition Notes

Global bilingual recommendations:

- Default to language-specific localized layouts.
- Use language toggle rather than showing full Arabic and full English everywhere.
- Keep Arabic and English elements separate.
- Use Tajawal 700 for Arabic display unless later review changes it.
- Lemonada remains accent-only and should not define core layout.
- Do not bake translated text into 3D textures.
- CTA labels must be tested in Arabic and English.
- Arabic paragraphs and cards require more line-height and flexible width.

High-risk bilingual scenes:

| Scene | Bilingual Risk | Composition Response |
| ----- | -------------- | -------------------- |
| 01 | Brand identity over 3D could become canvas-only. | DOM identity only; separate Arabic/English elements. |
| 02 | Hero could become crowded if both languages show fully. | Localized layout preferred. |
| 06 | Workshop cards may overflow in Arabic. | Stack cards earlier; flexible CTA widths. |
| 07 | Mentor titles/bios may vary by language. | DOM cards with adjustable height. |
| 09 | FAQ becomes dense if bilingual on same page section. | Language-specific FAQ. |
| 10 | Closing CTA must be clear in both languages. | Localized CTA and no text in 3D. |

---

## 15. Mobile Composition Table

| Scene | Desktop Composition | Mobile Composition |
| ----- | ------------------- | ------------------ |
| 01 | Full-viewport seal/gavel reveal. | Short reveal, reduced particles, CTA/fallback available early. |
| 02 | Split hero: copy column + seal atmosphere. | Text first, seal/poster behind or below, CTA above fold. |
| 03 | Documents field opposite copy. | Copy first, max 3 paper elements/static collage. |
| 04 | Method copy plus ordered desk system. | Vertical method blocks, static ordered desk. |
| 05 | Five dossier/cards in breathable grid. | Single-column stack or accessible swipe. |
| 06 | Workshop cards with dossier atmosphere. | Stacked cards, 44px+ tap targets, no hover-only details. |
| 07 | Editorial mentor card grid. | Stacked or swipe portrait cards, no tiny business-card grid. |
| 08 | Trust/proof grid. | Single-column proof slots, clearly pending if empty. |
| 09 | Center/full FAQ column. | Full-width accordion rows with large tap targets. |
| 10 | Centered seal + closing CTA. | Headline then CTA quickly; seal as static poster or small motif. |

---

## 16. Reduced-Motion / Static Fallback Table

| Scene | Full Motion Concept | Reduced-Motion / Static Equivalent |
| ----- | ------------------- | ---------------------------------- |
| 01 | Scroll-driven gavel trigger and seal reveal. | Static seal/desk poster; brand/CTA fade in. |
| 02 | Seal atmosphere behind hero. | Static hero background/poster with DOM content. |
| 03 | Floating fragmented documents. | Static fragmented document collage. |
| 04 | Documents converge into method structure. | Documents already organized. |
| 05 | Dossier/cards may fade/slide. | Static card grid/stack. |
| 06 | Dossier objects support workshop cards. | Static workshop card grid/list. |
| 07 | Portraits may reveal with subtle motion. | Static portrait/editorial cards. |
| 08 | Proof blocks reveal in rhythm. | Static editorial proof structure. |
| 09 | FAQ accordion interaction only. | Same semantic accordion; no motion dependency. |
| 10 | Seal callback and CTA reveal. | Static seal/desk closing poster; CTA visible. |

Every scene must communicate the same meaning without WebGL or animation.

---

## 17. Performance Composition Table

| Scene | Planned 3D Complexity | Mobile Complexity | Performance Note |
| ----- | --------------------- | ----------------- | ---------------- |
| 01 | High | Medium/static fallback | Vertical-slice candidate; optimize gavel/seal/particles before expansion. |
| 02 | High | Low/static fallback | DOM hero and CTA render before heavy 3D. |
| 03 | Medium | Low/static | Limit document count and transparency. |
| 04 | Low/Medium | Low/static | Avoid morphing complexity in early slice. |
| 05 | Low/static | Static | DOM cards carry meaning. |
| 06 | Medium later | Low/static | Dossier 3D optional; cards DOM-first. |
| 07 | Low/static | Static | Portrait/content section; no heavy 3D needed. |
| 08 | Static recommended | Static | Trust section should not depend on 3D. |
| 09 | Static recommended | Static | FAQ is semantic reading content. |
| 10 | Low/static | Static | Seal callback can be poster unless 3D budget allows. |

P1.05 rule:

**Vertical Slice Only Until Asset Optimization.**

Do not make all 10 scenes heavy 3D.

---

## 18. Vertical Slice Priority

| Priority | Scenes | Reason |
| -------- | ------ | ------ |
| P0 | Scene 01 + Scene 02 | Opening/hero proof of concept. |
| P0 | Scene 10 | Conversion destination clarity. |
| P1 | Scene 03 | First problem transition. |
| P1 | Scene 05/06 | Training/workshop clarity. |
| P1 | Scene 07 | Trust/mentor credibility. |
| P2 | Scene 04/08/09 | Can remain editorial/static in early slice. |

Final priority:

1. Prove Scene 01/02 cinematic-to-readable handoff.
2. Prove Scene 10 WhatsApp conversion clarity.
3. Add Scene 03/05/06 content clarity.
4. Keep Scene 04/08/09 mostly editorial/static until final content exists.

---

## 19. Scene Composition Guardrails

| Keep | Avoid |
| ---- | ----- |
| Seal-led compositions | Gavel-dominated brand world |
| DOM-first text placement | Canvas-only messaging |
| Clear WhatsApp CTA zones | Hidden CTA at end only |
| Premium legal negative space | Busy course catalog layout |
| Bilingual layout flexibility | English-only sketch assumptions |
| Mobile-first CTA safety | Desktop-only visual thinking |
| Static fallback per scene | 3D-dependent meaning |
| Vertical Slice prioritization | Heavy 3D in all 10 scenes |
| Trust without fake proof | Invented testimonials/stats |
| Workshop placeholders marked safe | Fake real course content |

Additional anti-patterns:

- No LMS/dashboard composition.
- No fake urgency.
- No invented mentor credentials.
- No unsupported certificates, accreditations, results, stats, or testimonials.
- No final copy claims in sketches.

---

## 20. Quality Gate

| Gate | Status | Notes |
| ---- | ------ | ----- |
| Exactly 10 scene sketches | PASS | Scenes 01-10 included. |
| Each sketch includes 3D placement | PASS | Per-scene field table included. |
| Each sketch includes text placement | PASS | Per-scene field table included. |
| CTA placement included where relevant | PASS | CTA field included for all scenes. |
| Visual hierarchy included | PASS | Per-scene hierarchy documented. |
| Mobile notes included | PASS | Per-scene notes plus mobile table. |
| Reduced-motion/static fallback notes included | PASS | Per-scene notes plus fallback table. |
| Bilingual notes included | PASS | Per-scene checks plus global section. |
| Avoided final UI polish | PASS | Markdown thumbnail sketches only. |
| Respects Seal-led 3D direction | PASS | Seal is motif/hero throughout. |
| Respects Vertical Slice First | PASS | Priority and performance table included. |
| Performance complexity levels included | PASS | Scene complexity table included. |
| Fake proof/urgency avoided | PASS | Guardrails documented. |
| Supporting outputs kept inside P2.06 | PASS | Single document, no new ticket. |
| Avoided new roadmap tickets | PASS | No roadmap ticket created. |

---

## 21. Acceptance Criteria

| Acceptance Criteria | Status |
| ------------------- | ------ |
| Scene 01 thumbnail sketch created | PASS |
| Scene 02 thumbnail sketch created | PASS |
| Scene 03 thumbnail sketch created | PASS |
| Scene 04 thumbnail sketch created | PASS |
| Scene 05 thumbnail sketch created | PASS |
| Scene 06 thumbnail sketch created | PASS |
| Scene 07 thumbnail sketch created | PASS |
| Scene 08 thumbnail sketch created | PASS |
| Scene 09 thumbnail sketch created | PASS |
| Scene 10 thumbnail sketch created | PASS |
| Every sketch includes layout direction | PASS |
| Every sketch includes 3D element placement | PASS |
| Every sketch includes primary copy placement | PASS |
| CTA placement included where relevant | PASS |
| Mobile adaptation documented | PASS |
| Reduced-motion/static fallback documented | PASS |
| Bilingual considerations documented | PASS |
| Performance complexity documented | PASS |
| Vertical Slice priority documented | PASS |
| Scene composition guardrail table included | PASS |
| No final UI screens created | PASS |
| No 3D assets created | PASS |
| No frontend implementation started | PASS |
| No new roadmap tickets created | PASS |

---

## 22. Final Recommendation

**PASS WITH CONDITIONS - P2.06 complete. 10 scene thumbnail sketches created with layout, 3D, copy, CTA, mobile, fallback, bilingual, and performance notes.**

Final scene layouts remain conditional on:

- Final brand assets and wordmarks.
- Final Mithaq Seal approval.
- Final Arabic/English content.
- Workshop details.
- Mentor content and approved portraits.
- Verified trust/proof assets.
- Legal/compliance review.
- UX storyflow validation.
- Vertical-slice performance validation.

Recommended next posture:

Use these sketches as low-fidelity composition guidance for UX/storyflow and later visual comps. Do not treat them as final UI layouts or production-ready designs.
