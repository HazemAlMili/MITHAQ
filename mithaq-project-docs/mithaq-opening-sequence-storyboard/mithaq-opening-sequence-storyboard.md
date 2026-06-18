# Mithaq Opening Sequence Storyboard

**Official Ticket ID:** P2.05  
**Official Ticket Name:** Opening Sequence Storyboard  
**Phase:** Phase 2 - Creative Concept Development  
**Priority:** P0  
**Complexity:** Medium  
**Owner:** Creative Director / Motion Director  
**Status:** PASS WITH CONDITIONS  
**Prepared date:** 2026-06-18  

---

## 1. Executive Summary

This document translates Mithaq's approved opening concept into a scroll-driven storyboard:

**judicial gavel trigger -> Mithaq Seal reveal -> usable hero handoff.**

The storyboard uses the original 8.5-second cinematic beat order as a timing reference, but the user controls progression through scroll. The sequence is not a fixed trailer intro and must not trap the user.

Final storyboard direction:

**Scroll-Driven Seal-Led Opening**

This means:

- The user enters a dark judicial atmosphere.
- The desk is revealed first.
- The gavel enters as a ceremonial trigger.
- The strike activates a controlled ripple.
- The ripple draws the Mithaq Seal.
- The Seal becomes the visual hero.
- The camera pulls back into the hero state.
- Bilingual identity and WhatsApp CTA appear.
- The sequence hands off naturally to Scene 02.

This ticket does not create final UI screens, final 3D assets, final shaders, R3F implementation, GSAP implementation, production animation, or production sound.

Status is **PASS WITH CONDITIONS** because final animation remains dependent on final brand assets, final seal approval, shader feasibility, asset optimization, mobile validation, and stakeholder review.

---

## 2. Current Mithaq Decisions

- Mithaq is a premium bilingual 3D legal academy portfolio / landing experience.
- Core concept: The Covenant Seal.
- The Seal is the hero.
- The gavel is the ceremonial trigger, not the brand hero.
- Opening direction: scroll-driven gavel trigger into Mithaq Seal reveal.
- P2.04 3D direction: Option D - Seal-Led Macro Legal Chamber.
- P2.01 visual direction: Option D - Hybrid Direction.
- P2.03 typography condition: Tajawal 700 is the safe Arabic display default; Lemonada is accent-only.
- P2.02 color condition: filled gold CTAs use near-black text; white on gold is not allowed.
- P1.05 feasibility condition: Vertical Slice Only Until Asset Optimization.
- Sound effects are approved only if controlled, optional/user-safe, and professional.
- Reduced motion and WebGL/static fallback are mandatory.
- DOM-first content must remain accessible independently from canvas.

---

## 3. Storyboard Adaptation: Timed Plan To Scroll-Driven Opening

Original narrative order retained:

1. Black void
2. Ambient particles
3. Warm light reveals desk
4. Gavel enters
5. Gavel pauses
6. Gavel strikes
7. Ripple expands
8. Controlled gold lines draw
9. Mithaq Seal outline appears
10. Seal completes
11. Camera reveals desk/seal/gavel composition
12. Wordmark / bilingual positioning appears
13. CTA stabilizes
14. Handoff to Scene 02 / Hero state

Scroll translation:

| Scroll Progress | Narrative Beat |
| --------------: | -------------- |
| 0-5% | Darkness / entry |
| 5-12% | Particles and desk reveal |
| 12-24% | Gavel enters frame |
| 24-32% | Gavel pause / authority tension |
| 32-36% | Gavel strike |
| 36-48% | Ripple and controlled lines |
| 48-62% | Seal outline forms |
| 62-74% | Seal completes and glows subtly |
| 74-86% | Camera pulls back / composition opens |
| 86-94% | Wordmark + bilingual subtitle reveal |
| 94-100% | CTA appears / handoff to hero state |

Storyboard rule:

The animation responds to scroll progress. It must feel like a user-led ceremonial reveal, not a forced loading sequence.

---

## 4. Frame-By-Frame Storyboard

### F01 - Black Judicial Void

| Field | Direction |
| ----- | --------- |
| Scroll progress | 0-5% |
| Equivalent time beat | 0.0s |
| Viewport description | Deep near-black judicial void; no object claims attention yet. |
| Camera angle | No visible object; camera feels present but hidden in darkness. |
| Visible 3D elements | None, or canvas visually quiet. |
| DOM elements | None visible yet, or loading-safe semantic hero content available off-canvas/for fallback only. |
| Motion note | Very subtle fade from black as scroll begins. |
| Lighting note | Ambient nearly zero; no gold yet. |
| Sound note | Silent. |
| Accessibility note | Essential content must exist in DOM for fallback; no meaning depends on this blank visual. |
| Mobile note | Same or shortened; do not waste vertical scroll on empty darkness. |
| Performance note | Canvas may initialize quietly; DOM must not wait for heavy assets. |
| Purpose | Establish seriousness and controlled entry. |

Visual annotation:

- Composition: empty center, deep negative space.
- Camera: hidden, static, no drama.
- Depth: no readable foreground/midground/background yet.
- Light: almost none.
- Material: none visible.
- Text/CTA: not visible.

### F02 - Atmospheric Dust Appears

| Field | Direction |
| ----- | --------- |
| Scroll progress | 5-12% |
| Equivalent time beat | 0.3s |
| Viewport description | Faint gold dust appears in dark space. |
| Camera angle | Static or very slow push. |
| Visible 3D elements | Sparse ambient dust only. |
| DOM elements | No main copy. |
| Motion note | Dust drifts slowly and irregularly. |
| Lighting note | Tiny warm particles only; no spectacle. |
| Sound note | Silent or near-silent room tone only if later approved. |
| Accessibility note | Particles are decorative and can be removed. |
| Mobile note | Reduce particle count drastically or disable. |
| Performance note | Use capped particle count; avoid transparent overdraw. |
| Purpose | Suggest atmosphere without revealing the message too early. |

Visual annotation:

- Composition: particles in upper-left light path.
- Camera: slight push, no rotation.
- Depth: particles hint at air volume.
- Material: dust/foil motes only.

### F03 - Desk Surface Revealed

| Field | Direction |
| ----- | --------- |
| Scroll progress | 12-18% |
| Equivalent time beat | 1.0s |
| Viewport description | Dark wood desk surface emerges from shadow. |
| Camera angle | Macro, shallow low angle, close to desk plane. |
| Visible 3D elements | Desk plane/surface. |
| DOM elements | None. |
| Motion note | Warm light grazes surface as scroll advances. |
| Lighting note | Key light begins from upper-left. |
| Sound note | Silent. |
| Accessibility note | Decorative reveal; fallback poster can show desk already visible. |
| Mobile note | Use simpler desk plane/material; no detailed dynamic shadow required. |
| Performance note | One optimized plane/material; avoid large uncompressed textures. |
| Purpose | Establish the legal stage. |

Visual annotation:

- Composition: desk surface occupies lower frame.
- Camera: low macro angle.
- Depth: foreground grain, dark background.
- Material: dark walnut/wenge-like wood.

### F04 - Gavel Enters Frame

| Field | Direction |
| ----- | --------- |
| Scroll progress | 18-24% |
| Equivalent time beat | 1.8s |
| Viewport description | Gavel descends into partial view; head/handle enter from top or side. |
| Camera angle | Macro close-up, not aggressive. |
| Visible 3D elements | Gavel head/handle, desk. |
| DOM elements | None. |
| Motion note | Controlled weighted descent. |
| Lighting note | Gavel catches warm rim/highlight; brass band glints subtly. |
| Sound note | Optional subtle wood/air movement later; no whoosh. |
| Accessibility note | Motion is decorative; reduced motion uses static gavel/desk composition. |
| Mobile note | Shorten travel distance and reduce rotation. |
| Performance note | Gavel geometry must be budget-aware and optimized. |
| Purpose | Introduce the authority trigger. |

Visual annotation:

- Composition: gavel enters off-center, leaving center for future seal.
- Camera: tight but not threatening.
- Depth: gavel foreground, desk midground.
- Material: dark wood and muted brass.

### F05 - Gavel Suspended Before Impact

| Field | Direction |
| ----- | --------- |
| Scroll progress | 24-32% |
| Equivalent time beat | 3.0s |
| Viewport description | Gavel pauses just above desk. |
| Camera angle | Tight side/macro view. |
| Visible 3D elements | Gavel, shadow, desk. |
| DOM elements | Optional minimal "Scroll to continue" only if testing proves useful; not mandatory. |
| Motion note | Almost still; slight micro-motion only. |
| Lighting note | Shadow deepens below gavel. |
| Sound note | Silence before contact. |
| Accessibility note | Avoid requiring users to understand pause as instruction. |
| Mobile note | Reduce pause length; no scroll trap feeling. |
| Performance note | Avoid expensive real-time contact shadows on low-tier devices. |
| Purpose | Create anticipation without theatrical drama. |

Visual annotation:

- Composition: gavel close but center remains reserved.
- Depth: contact point implied, background dark.
- Light: warm key, low ambient.

### F06 - The Strike

| Field | Direction |
| ----- | --------- |
| Scroll progress | 32-36% |
| Equivalent time beat | 3.4s |
| Viewport description | Gavel touches desk with a short ceremonial contact. |
| Camera angle | Controlled close-up. |
| Visible 3D elements | Gavel impact point, desk. |
| DOM elements | None. |
| Motion note | Short decisive impact. |
| Lighting note | Tiny gold accent at contact point. |
| Sound note | Deep, short, restrained wooden/brass resonance if audio is enabled. |
| Accessibility note | Sound is optional and never required for meaning. |
| Mobile note | Can be a small transform/fade or skipped in reduced mobile mode. |
| Performance note | No impact physics simulation required; keyframe only. |
| Purpose | Ceremonial declaration, not violence. |

Visual annotation:

- Composition: impact point visible but not explosive.
- Motion: one controlled contact.
- Avoid: no smash, shockwave explosion, cracked glass, horror, or action-trailer slow motion.

### F07 - Ripple Of Authority

| Field | Direction |
| ----- | --------- |
| Scroll progress | 36-44% |
| Equivalent time beat | 3.6s |
| Viewport description | Controlled concentric gold ripple expands across desk. |
| Camera angle | Close-up following ripple. |
| Visible 3D elements | Desk, ripple, gavel partially visible. |
| DOM elements | None. |
| Motion note | Smooth outward ripple. |
| Lighting note | Gold line catches surface, very restrained. |
| Sound note | Short resonance tail, then silence. |
| Accessibility note | Reduced motion uses static subtle gold line or fade. |
| Mobile note | Use one ring or CSS/static equivalent; reduce shader complexity. |
| Performance note | Avoid expensive fragment shader; provide fallback material/poster. |
| Purpose | Show authority spreading from the strike. |

Visual annotation:

- Composition: ripple leads eye toward seal center.
- Depth: desk surface becomes active stage.
- Material: gold on dark wood, not neon.

### F08 - Controlled Gold Lines Draw

| Field | Direction |
| ----- | --------- |
| Scroll progress | 44-52% |
| Equivalent time beat | 4.0s |
| Viewport description | Geometric controlled gold lines begin forming. |
| Camera angle | Slight pullback. |
| Visible 3D elements | Ripple, gold line paths, desk. |
| DOM elements | None. |
| Motion note | Lines draw outward, calligraphic but structured. |
| Lighting note | Lines glow subtly; not magical. |
| Sound note | Silent. |
| Accessibility note | Line drawing is decorative; seal state can appear directly in fallback. |
| Mobile note | Reduce line count and draw duration. |
| Performance note | Avoid many animated curves; use simple mesh/path or texture mask. |
| Purpose | Transition from gavel impact to covenant seal. |

Visual annotation:

- Composition: paths start clarifying a circular structure.
- Camera: pullback enough to understand formation.
- Material: muted gold linework.

### F09 - Seal Outline Begins

| Field | Direction |
| ----- | --------- |
| Scroll progress | 52-62% |
| Equivalent time beat | 5.0s |
| Viewport description | Circular seal outline forms around center. |
| Camera angle | Pullback enough to read circular shape. |
| Visible 3D elements | Seal outline, desk, gavel secondary. |
| DOM elements | None. |
| Motion note | Ring/path draws around center. |
| Lighting note | Seal catches muted gold. |
| Sound note | Silent. |
| Accessibility note | No critical text inside seal; DOM text appears later. |
| Mobile note | Use simplified ring/emboss reveal. |
| Performance note | Keep seal geometry low-poly enough for vertical slice. |
| Purpose | Introduce Mithaq's true hero. |

Visual annotation:

- Composition: seal takes central position.
- Depth: gavel recedes.
- Material: brass/gold relief begins.

### F10 - Mithaq Seal Completes

| Field | Direction |
| ----- | --------- |
| Scroll progress | 62-74% |
| Equivalent time beat | 5.8s |
| Viewport description | Seal fully visible and subtly illuminated. |
| Camera angle | Centered ceremonial composition. |
| Visible 3D elements | Seal, gavel resting secondary, desk. |
| DOM elements | No long copy yet. |
| Motion note | Seal settles; minor light catch or low emissive activation. |
| Lighting note | Restrained seal highlight; gold catches light more than glows. |
| Sound note | Optional soft low metallic/paper resonance. |
| Accessibility note | Seal is motif; meaningful identity text still appears in DOM. |
| Mobile note | Static or very simple seal fade is acceptable. |
| Performance note | Avoid heavy bevels, excessive glow, and dense Arabic geometry. |
| Purpose | Brand promise becomes physical. |

Visual annotation:

- Composition: seal is hero at center.
- Camera: stable, ceremonial.
- Material: muted brass/gold, embossed relief.

### F11 - Camera Pullback / Legal Chamber Opens

| Field | Direction |
| ----- | --------- |
| Scroll progress | 74-84% |
| Equivalent time beat | 6.5s |
| Viewport description | Wider desk/chamber composition appears. |
| Camera angle | Slow pullback from macro to hero framing. |
| Visible 3D elements | Seal center, gavel side, desk surface, ambient particles, implied chamber depth. |
| DOM elements | Wordmark not yet visible or faint. |
| Motion note | Camera opens space around seal. |
| Lighting note | Warm key stabilizes; background remains dark. |
| Sound note | Silent. |
| Accessibility note | Reduced motion removes camera pullback and uses static composition. |
| Mobile note | Smaller pullback distance; avoid long pinned scroll. |
| Performance note | Implied chamber depth, not full courtroom model. |
| Purpose | Prepare for hero message and CTA. |

Visual annotation:

- Composition: seal central, gavel side, copy-safe negative space.
- Depth: foreground desk, midground seal, background chamber shadow.

### F12 - Wordmark + Bilingual Identity Reveal

| Field | Direction |
| ----- | --------- |
| Scroll progress | 84-92% |
| Equivalent time beat | 7.0s |
| Viewport description | Mithaq wordmark and bilingual identity appear. |
| Camera angle | Stable hero framing. |
| Visible 3D elements | Seal remains central or slightly behind/near text; gavel secondary. |
| DOM elements | Mithaq / Arabic identity as separate elements, bilingual tagline placeholder. |
| Motion note | Text fades/slides softly. |
| Lighting note | Content readability protected by overlay/negative space. |
| Sound note | No sound required. |
| Accessibility note | Text is DOM, selectable, localizable, and not canvas-only. |
| Mobile note | Arabic and English should stack or use localized layout; no mixed line. |
| Performance note | Text renders independently of 3D load. |
| Purpose | Move from cinematic symbol to clear brand recognition. |

Visual annotation:

- Composition: DOM text occupies protected negative space.
- Text: Arabic and English separate elements.
- Typography: Tajawal 700 for Arabic display unless later approved otherwise.

### F13 - CTA Appears

| Field | Direction |
| ----- | --------- |
| Scroll progress | 92-98% |
| Equivalent time beat | 8.2s |
| Viewport description | Primary WhatsApp CTA appears. |
| Camera angle | Stable. |
| Visible 3D elements | Seal/gavel become background atmosphere. |
| DOM elements | Primary CTA, optional secondary form/detail link. |
| Motion note | CTA appears with restrained gold accent. |
| Lighting note | CTA contrast follows P2.02. |
| Sound note | No attention-grabbing sound. |
| Accessibility note | CTA is keyboard reachable and visible without canvas. |
| Mobile note | CTA appears early enough and remains reachable; no hover-only behavior. |
| Performance note | CTA must not wait for final 3D asset completion. |
| Purpose | Convert attention into action. |

Visual annotation:

- CTA: outline gold preferred; filled gold must use near-black text.
- Composition: 3D supports conversion, does not obscure it.

### F14 - Hero Handoff State

| Field | Direction |
| ----- | --------- |
| Scroll progress | 98-100% |
| Equivalent time beat | 8.5s |
| Viewport description | Opening resolves into usable hero state. |
| Camera angle | Stable final composition. |
| Visible 3D elements | Seal anchor, gavel secondary, desk/chamber atmosphere. |
| DOM elements | Hero message + CTA visible. |
| Motion note | Scroll continues naturally into next section. |
| Lighting note | Balanced readability and atmosphere. |
| Sound note | No looping sound. |
| Accessibility note | User is not trapped; content flow continues. |
| Mobile note | Handoff may arrive sooner; no long pinned intro. |
| Performance note | If 3D underperforms, switch to static fallback at or before this state. |
| Purpose | Handoff from opening into Scene 02 without trapping the user. |

Visual annotation:

- Composition: seal is still the motif; page is now usable.
- Text/CTA: visible, semantic, accessible.

### F15 - Reduced Motion Equivalent

| Field | Direction |
| ----- | --------- |
| Scroll progress | Applies to full opening |
| Equivalent time beat | Fallback equivalent |
| Viewport description | Static premium seal/desk poster appears with subtle fades only. |
| Camera angle | No camera movement. |
| Visible 3D elements | Static seal/desk/gavel composition, or non-WebGL image fallback. |
| DOM elements | Brand identity and CTA visible early. |
| Motion note | No gavel impact, no ripple animation, no pullback. |
| Lighting note | Precomposed premium lighting. |
| Sound note | No required sound. |
| Accessibility note | `prefers-reduced-motion` gets static/fade version automatically. |
| Mobile note | Same behavior can be used on low-tier devices. |
| Performance note | Avoid canvas entirely if needed. |
| Purpose | Preserve meaning without motion. |

### F16 - Mobile Simplified Equivalent

| Field | Direction |
| ----- | --------- |
| Scroll progress | Condensed 0-100% path |
| Equivalent time beat | Mobile fallback equivalent |
| Viewport description | Shorter desk -> gavel cue -> seal reveal -> CTA path. |
| Camera angle | Minimal depth changes; tighter composition. |
| Visible 3D elements | Simplified gavel, seal, desk; fewer/no particles. |
| DOM elements | CTA visible early; bilingual text wraps safely. |
| Motion note | Reduced object travel, fewer line effects. |
| Lighting note | Simple warm key, no complex shadows. |
| Sound note | Optional only; likely off by default. |
| Accessibility note | No hover interactions; all controls tappable. |
| Mobile note | Avoid long pinned scroll and oversized headlines. |
| Performance note | Static fallback if FPS or memory is poor. |
| Purpose | Keep mobile premium without forcing desktop animation complexity. |

---

## 5. Full Frame Table

| Frame | Scroll % | Equivalent Time Beat | Visual State | Camera | 3D Elements | DOM Elements | Motion | Sound | Mobile/Fallback |
| ----- | -------: | -------------------: | ------------ | ------ | ----------- | ------------ | ------ | ----- | --------------- |
| F01 | 0-5% | 0.0s | Black judicial void | Hidden/static | None | None visible | Fade from black | Silent | Shorten or skip empty time |
| F02 | 5-12% | 0.3s | Faint dust | Static/slow push | Sparse particles | None | Slow drift | Silent/room tone | Reduce or disable particles |
| F03 | 12-18% | 1.0s | Desk emerges | Macro shallow angle | Desk surface | None | Light reveal | Silent | Simple desk plane/poster |
| F04 | 18-24% | 1.8s | Gavel enters | Macro close-up | Gavel, desk | None | Weighted descent | Optional subtle wood air | Shorter travel |
| F05 | 24-32% | 3.0s | Gavel suspended | Tight side macro | Gavel, shadow, desk | Optional scroll cue | Micro-motion | Silence | Reduce pause |
| F06 | 32-36% | 3.4s | Strike | Controlled close-up | Impact point | None | Short contact | Deep restrained hit | Keyframe or skip |
| F07 | 36-44% | 3.6s | Ripple expands | Close follow | Desk, ripple, gavel | None | Smooth ring | Short tail | One ring/static line |
| F08 | 44-52% | 4.0s | Gold lines draw | Slight pullback | Gold paths, desk | None | Structured draw | Silent | Fewer lines |
| F09 | 52-62% | 5.0s | Seal outline | Pullback | Seal outline, desk, gavel | None | Ring draws | Silent | Simplified ring |
| F10 | 62-74% | 5.8s | Seal completes | Centered ceremonial | Seal, gavel, desk | None | Seal settles | Optional subtle resonance | Static/fade seal |
| F11 | 74-84% | 6.5s | Chamber opens | Slow pullback | Seal, desk, gavel, particles | Faint wordmark optional | Camera opens | Silent | Minimal pullback |
| F12 | 84-92% | 7.0s | Identity reveal | Stable hero | Seal background | Wordmark + bilingual identity | Soft text reveal | None required | Stack/localize text |
| F13 | 92-98% | 8.2s | CTA appears | Stable | Seal/gavel atmosphere | WhatsApp CTA + optional secondary | Restrained CTA fade | None | CTA early/reachable |
| F14 | 98-100% | 8.5s | Hero handoff | Stable | Seal anchor, gavel secondary | Hero message + CTA | Natural scroll continues | No loop | Static fallback if needed |
| F15 | Reduced motion | N/A | Static poster | No movement | Static seal/desk | Text + CTA visible early | Fade only | No sound | Preferred reduced path |
| F16 | Mobile simplified | N/A | Condensed reveal | Minimal movement | Simplified scene | Text + CTA early | Short path | Optional/off | Avoid long pinned intro |

---

## 6. Camera Direction Notes

| Beat | Camera Direction | Avoid |
| ---- | ---------------- | ----- |
| Entry | Slow reveal from darkness. | Immediate full scene exposure. |
| Desk reveal | Macro / shallow angle. | Generic flat top-down stock view. |
| Gavel descent | Close but not aggressive. | Smash framing. |
| Strike | Short controlled focus. | Violent action framing. |
| Ripple | Slight follow/pullback. | Chaotic shake. |
| Seal reveal | Centered ceremonial composition. | Random floating object. |
| Hero handoff | Calm pullback. | Overdramatic zoom. |

Camera rules:

- Camera movement is scroll-led, not timed autoplay.
- The gavel gets a close-up only for the trigger moment.
- The seal receives the centered hero composition.
- Mobile reduces camera travel and depth changes.

---

## 7. Lighting Direction Notes

| Beat | Lighting Direction | Avoid |
| ---- | ------------------ | ----- |
| Entry | Near-black, very low ambient. | Horror black crush that hides fallback meaning. |
| Dust | Tiny warm glints in air path. | Sparkle/magic effect. |
| Desk reveal | Warm key from upper-left grazes wood. | Overexposed desk or bright office light. |
| Gavel | Warm rim on brass and wood edge. | Shiny fake gold or plastic highlights. |
| Strike | Tiny gold contact accent. | Explosion/shockwave. |
| Ripple/lines | Muted gold line on desk. | Neon glow. |
| Seal | Highlight through bevel/emboss, not self-glow. | Magic emblem glow. |
| Handoff | Balanced readability with dark atmosphere. | Text over unreadable canvas. |

---

## 8. Sound Direction Notes

Sound must be optional or user-safe. It must never be required for meaning.

| Frame | Sound Direction | Trigger | Notes |
| ----- | --------------- | ------- | ----- |
| F01-F05 | Silent or near-silent room tone | User-controlled / muted | Do not autoplay loudly. |
| F06 | Deep short gavel resonance | User interaction / enabled audio | Restrained, no explosion. |
| F07 | Resonance tail | If sound enabled | Short fade. |
| F10 | Subtle seal resonance | Optional | No magic sparkle. |
| F13 | No attention-grabbing sound | N/A | CTA should not feel game-like. |

Sound anti-rules:

- No trailer booms.
- No whoosh-heavy object motion.
- No horror drone.
- No looping ambience required.
- No game-like CTA sound.

---

## 9. DOM / CTA Notes

- The opening can be cinematic, but the site must become usable quickly.
- DOM hero content and CTA must be available independently from the canvas.
- CTA appears by F13 and remains visible in F14.
- Primary conversion remains WhatsApp.
- Secondary conversion can remain a simple form/detail link if needed.
- Filled gold CTA must use near-black text, never white.
- No fake urgency, countdown, seat counter, or deadline pressure.
- Critical text must not be baked into 3D textures or canvas.

---

## 10. Bilingual / RTL Notes

- Arabic and English are separate DOM elements.
- Do not mix Arabic and English fonts on one line.
- Use Tajawal 700 for Arabic display unless later review approves otherwise.
- Lemonada remains accent-only pending review and should not be used for critical hero identity in this storyboard.
- Arabic and English layouts may differ for final composition.
- Mobile text wrapping must be tested separately for Arabic and English.
- The seal may contain Arabic later only if official wordmark/seal approval confirms legibility.
- Meaningful text must remain in DOM even if the seal includes text-like marks.

---

## 11. Reduced Motion Storyboard

| Standard Frame | Reduced Motion Equivalent |
| -------------- | ------------------------- |
| Gavel descent | Static gavel/desk composition. |
| Strike | No impact animation. |
| Ripple | Static subtle gold line or fade. |
| Seal reveal | Seal visible via fade. |
| Camera pullback | No camera movement. |
| CTA reveal | Simple fade-in. |

Reduced-motion requirements:

- Skip gavel impact motion.
- Show static premium seal/desk poster.
- Fade in brand identity and CTA.
- Keep all essential text in DOM.
- Avoid camera movement.
- Avoid scroll-trapping.
- Keep WhatsApp CTA accessible.
- Avoid required sound.
- Preserve the same content meaning.

---

## 12. Mobile Storyboard Notes

| Beat | Desktop Direction | Mobile Direction |
| ---- | ----------------- | ---------------- |
| Entry | Near-black scroll entry. | Shorter entry; avoid empty scroll delay. |
| Desk reveal | Macro desk surface with warm key. | Simple desk plane or static poster; minimal shadow. |
| Gavel | Weighted close descent. | Shorter transform; fewer rotations. |
| Strike | Controlled close contact. | Optional micro-motion or skipped if reduced. |
| Ripple | Concentric gold ripple and line paths. | One ring or static/fade line. |
| Seal | Centered embossed reveal. | Simplified seal geometry/material; static fallback allowed. |
| Hero text | Bilingual identity appears after seal. | Stack/localize text; prevent cropped headings. |
| CTA | WhatsApp CTA appears at handoff. | CTA visible earlier and reachable; no hover dependency. |

Mobile rules:

- Reduce particles.
- Reduce camera distance changes.
- Keep CTA reachable.
- Avoid long pinned scroll sections.
- Avoid hover-only behavior.
- Allow static fallback if FPS is poor.
- Keep bilingual text wrapping safe.
- Avoid oversized English/Arabic headings that crop.

---

## 13. Performance / Feasibility Notes

P1.05 constraint:

**Vertical Slice Only Until Asset Optimization.**

| Risk | Storyboard Guardrail |
| ---- | -------------------- |
| Heavy seal/gavel assets | Use budget-aware silhouettes and simplified forms. |
| Mobile FPS drops | Simplified scene / static fallback. |
| Scroll trap | Keep short scroll range and clear progress. |
| Long load | DOM hero and CTA available independently. |
| Shader failure | Static gold lines / fallback poster. |
| Bilingual text overflow | Separate layout notes for Arabic/English. |
| Particle overdraw | Cap particles and disable on mobile/reduced motion. |
| Canvas-only meaning | Keep text, CTA, and labels in DOM. |

Additional feasibility notes:

- Final assets are not available yet.
- Use placeholder seal/gavel until final assets.
- Full shader complexity is not approved until vertical-slice validation.
- Text and CTA render before heavy 3D.
- No production-grade 3D is authorized by this storyboard alone.

---

## 14. Anti-Patterns To Avoid

| Anti-Pattern | Why It Hurts Mithaq | Replacement |
| ------------ | ------------------- | ----------- |
| Fixed cinematic trailer intro | Feels trapped and ignores scroll decision. | Scroll-driven ceremonial reveal. |
| Gavel as brand hero | Generic legal cliche. | Seal as hero, gavel as trigger. |
| Violent smash | Aggressive and theatrical. | Short controlled contact. |
| Explosion/shockwave | Game/trailer tone. | Controlled gold ripple. |
| Canvas-only text | Accessibility and SEO failure. | DOM-first identity and CTA. |
| Autoplay dramatic audio | Unsafe and intrusive. | Optional restrained sound. |
| Mandatory camera movement | Bad for reduced motion. | Static/fade fallback. |
| Full heavy desktop animation on mobile | Performance risk. | Mobile simplification. |
| Mixed Arabic/English on one line | Weak bilingual maturity. | Separate localized elements. |
| Horror darkness | Wrong emotional tone. | Premium judicial darkness. |

---

## 15. Opening Storyboard Guardrail Table

| Keep | Avoid |
| ---- | ----- |
| Scroll-driven ceremonial reveal | Fixed cinematic trailer intro |
| Seal as hero | Gavel as brand hero |
| Controlled gavel trigger | Violent smash |
| Gold ripple of authority | Explosion/shockwave |
| DOM-first CTA | Canvas-only text |
| Optional/user-safe sound | Autoplay dramatic audio |
| Reduced-motion fallback | Mandatory camera movement |
| Mobile simplification | Full heavy desktop animation on mobile |
| Bilingual text as separate elements | Mixed Arabic/English on one line |

---

## 16. Final Storyboard Direction

Selected direction:

**Scroll-Driven Seal-Led Opening**

This is the correct direction because:

- It preserves the gavel trigger into Mithaq Seal reveal.
- It keeps the Seal as the hero.
- It respects the approved scroll-driven opening.
- It avoids a fixed trailer intro.
- It supports DOM-first conversion and accessibility.
- It gives mobile and reduced-motion users a premium fallback.
- It remains compatible with P1.05's vertical-slice constraints.

Final creative sentence:

The user scrolls into a dark legal chamber, watches the desk and gavel emerge with controlled weight, sees a restrained strike activate a gold ripple, and arrives at the Mithaq Seal as the stable hero motif before the bilingual identity and WhatsApp CTA appear.

---

## 17. Quality Gate

| Gate | Status | Notes |
| ---- | ------ | ----- |
| At least 12 frames | PASS | 16 frames included. |
| Frames clearly scroll-driven | PASS | Scroll progress mapped per frame. |
| Gavel trigger -> seal reveal preserved | PASS | Core sequence maintained. |
| Seal clearly hero | PASS | Seal dominates F09-F14. |
| Gavel secondary | PASS | Gavel is trigger/callback only. |
| Camera angles documented | PASS | Per-frame and camera table included. |
| Visible elements documented per frame | PASS | Each frame includes visible 3D elements. |
| DOM/CTA elements documented | PASS | F12-F14 and DOM notes included. |
| Lighting notes included | PASS | Per-frame and lighting table included. |
| Sound notes included | PASS | Per-frame and sound table included. |
| Reduced-motion notes included | PASS | F15 and dedicated section. |
| Mobile notes included | PASS | F16 and mobile table. |
| Performance constraints included | PASS | P1.05 guardrails included. |
| Avoided final UI design | PASS | No UI screens created. |
| Avoided final 3D production | PASS | No models, shaders, or animation created. |
| Avoided new roadmap tickets | PASS | No extra tickets created. |

---

## 18. Acceptance Criteria

| Acceptance Criteria | Status |
| ------------------- | ------ |
| Opening storyboard is created | PASS |
| Minimum 12 frames included | PASS |
| Scroll progress mapped to every frame | PASS |
| Equivalent original time beats documented | PASS |
| Each frame includes viewport, camera, visible elements, motion, lighting, DOM, sound, accessibility, mobile, and performance notes | PASS |
| Reduced-motion version documented | PASS |
| Mobile simplified version documented | PASS |
| Sound direction documented | PASS |
| Bilingual/RTL notes documented | PASS |
| Final storyboard direction selected | PASS |
| Storyboard guardrail table included | PASS |
| No final UI screens created | PASS |
| No final 3D assets created | PASS |
| No shaders implemented | PASS |
| No frontend implementation started | PASS |
| No new roadmap tickets created | PASS |

---

## 19. Final Status

**PASS WITH CONDITIONS - P2.05 complete. Storyboard has 16 frames and a clear scroll-driven opening direction.**

Final animation remains conditional on final assets, shader feasibility, mobile validation, stakeholder review, and vertical-slice performance testing.
