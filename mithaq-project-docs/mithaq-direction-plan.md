# MITHAQ — ميثاق
## Premium 3D Legal Academy Website
### Full Strategic, Creative & Implementation Plan

**Version 1.0 — Direction Lock Document**
**Status: Ready for Client Review**

---

## TABLE OF CONTENTS

1. [Executive Summary](#1-executive-summary)
2. [Final Recommended Core Concept](#2-final-recommended-core-concept)
3. [Reference Mix Strategy](#3-reference-mix-strategy)
4. [Creative Direction System](#4-creative-direction-system)
5. [Opening Sequence Direction](#5-opening-sequence-direction)
6. [Scene-by-Scene Website Experience](#6-scene-by-scene-website-experience)
7. [Website Structure / Information Architecture](#7-website-structure--information-architecture)
8. [UX / Conversion Strategy](#8-ux--conversion-strategy)
9. [3D / WebGL Strategy](#9-3d--webgl-strategy)
10. [Technical Stack Recommendation](#10-technical-stack-recommendation)
11. [Accessibility Strategy](#11-accessibility-strategy)
12. [Performance Strategy](#12-performance-strategy)
13. [Open Questions / Client Alignment Questions](#13-open-questions--client-alignment-questions)
14. [Phased Implementation Plan](#14-phased-implementation-plan)
15. [Risks and Mitigation](#15-risks-and-mitigation)
16. [Final Recommendation](#16-final-recommendation)

---

## 1. EXECUTIVE SUMMARY

Mithaq (ميثاق — meaning "covenant" or "charter" in Arabic) is positioned as a premium legal academy bridging the gap between academic legal study and real-world professional readiness. This plan defines the complete strategic, creative, and technical direction for building a cinematic 3D portfolio website that can win clients, drive registrations, and stand apart from every generic course landing page or law firm website in the region.

The plan is built on five principles:

**Authority first.** Every design decision must reinforce that Mithaq is the credible, serious, and premium choice for legal training. No element exists for spectacle alone.

**3D in service of the message.** The WebGL/Three.js layer is narrative infrastructure, not decoration. Every shader, camera move, and particle system exists to communicate something true about Mithaq.

**The word Mithaq means "covenant."** This is not just a brand name — it is the conceptual spine of the entire experience. The site is the covenant between legal study and professional practice, sealed by authority.

**Performance is non-negotiable.** A slow, heavy site kills authority faster than a bad design. Cinematic quality must coexist with sub-2.5s LCP and 50+ FPS on desktop.

**Conversion is the real deliverable.** The most premium site in the world fails if it does not move a visitor toward registration, inquiry, or WhatsApp contact. Every scene must serve the funnel.

The recommended production stack is Next.js + React Three Fiber + Three.js + Drei + GSAP + ScrollTrigger + Lenis + Framer Motion + Zustand, deployed on Vercel. 3D assets are produced in Blender, optimized via gltfpack/Meshopt, and compressed with KTX2.

Total estimated complexity: **High.** This is a 10-phase build requiring Creative Direction, UI/UX, 3D Modeling, WebGL Engineering, and Content Writing working in tight sequence.

---

## 2. FINAL RECOMMENDED CORE CONCEPT

### Concept Name: **"The Covenant Seal"**
### Arabic Anchor: **ميثاق — من الدراسة إلى الاحتراف**
### English Anchor: **"From Legal Study to Professional Readiness"**

---

### The Narrative Logic

The word "Mithaq" — ميثاق — does not just mean "agreement." It means a **binding covenant**. In Islamic and Arabic legal tradition, a mithaq is not a casual contract. It is a solemn, official, sealed commitment between parties.

This gives the entire website a conceptual spine that is not borrowed or invented — it is native to the brand name itself:

> Mithaq makes a covenant with every student: we will transform your legal education into professional readiness.

This covenant is **sealed by the gavel**. The gavel strike in the opening is not decorative — it is the sealing moment. The judge's gavel in a courtroom finalizes and declares. When the gavel strikes on the Mithaq surface, it is not violence — it is **official declaration**.

From the impact, the **Mithaq Seal** is revealed: a circular, calligraphic legal seal carrying the brand name, its values, and the promise. This seal becomes the recurring visual motif throughout the entire site — appearing on section transitions, stamped on workshop cards, embedded in the final CTA.

---

### The Visual World

| Dimension | Direction |
|-----------|-----------|
| **Atmosphere** | Dark judicial chamber. Deep, warm, deliberately unlit at the edges. Premium legal darkness. |
| **Surface** | A formal legal desk surface — dark wenge wood grain, hand-polished. Not marble. Not glass. Wood. |
| **Light Source** | Single directional source, warm amber-gold, entering from upper left. Controlled, deliberate. |
| **Material Palette** | Dark wood, aged leather, brass/gold, parchment cream, black lacquer. Materials that exist in real courtrooms and legal chambers. |
| **Motion Vocabulary** | Slow, decisive, controlled. Nothing bounces. Nothing jiggles. Every motion has weight. |
| **Color Feeling** | Rich darkness with restrained gold. Not neon. Not black-and-white. Expensive warmth in shadow. |

---

### The Three Acts

**Act I — The Covenant Sealed** (Scene 01–02)
The gavel strikes. The seal appears. Mithaq declares its authority.

**Act II — The Knowledge Chamber** (Scene 03–07)
The user enters the chamber. The gap between legal study and professional practice is shown. Mithaq's method, pillars, and workshops are revealed.

**Act III — The Community of Practice** (Scene 08–10)
Mentors, proof, testimonials, and the final call to action. The covenant is offered to the user.

---

## 3. REFERENCE MIX STRATEGY

### How Each Reference Informs Mithaq — Specifically

---

**Reference 1: Oryzo AI**
*What it does:* Builds an entire visual world around one singular 3D object. The object is so close, so detailed, so beautifully lit that it becomes the entire brand proposition.

*What Mithaq borrows:*
- The **macro-proximity approach**: the gavel tip should be close enough that you can see the grain of the wood, the reflection of the desk lamp in the brass band
- The **single-object authority**: in the opening, nothing competes with the gavel. One subject. Total control of attention
- The **lighting philosophy**: a single warm directional light that creates real shadow depth, not ambient fills

*What Mithaq avoids:*
- Oryzo's slight irreverence and product-satire tone
- Any feeling of tech-product pitch (this is legal, not SaaS)
- The synthetic, CGI-render over-sharpness — Mithaq's 3D should feel more organic

---

**Reference 2: KODE Immersive**
*What it does:* Creates the feeling of stepping through a portal into a different world. The hero is not a page — it is an environment.

*What Mithaq borrows:*
- The **spatial sense of entry**: scrolling into Scene 01 should feel like entering a judicial chamber, not loading a website
- **Camera depth cues**: slight perspective shift, subtle depth-of-field, environmental framing that makes the user feel surrounded
- The transition language: the site does not "scroll" between sections — it **advances through chambers**

*What Mithaq avoids:*
- KODE's sci-fi spatial-computing vocabulary (no holographic UI, no AR/VR language)
- Any gaming or XR energy — this is judicial, not immersive tech
- Overusing the "portal" frame to the point it obscures content clarity

---

**Reference 3: Immersive Garden**
*What it does:* Sets the global standard for cinematic scroll choreography. Camera paths, scene transitions, and element reveals feel hand-crafted and authored.

*What Mithaq borrows:*
- **GSAP ScrollTrigger choreography precision**: every scroll increment has a designed output — camera rotation, object opacity, text reveal
- **Scene pacing**: dwell time in each scene feels earned, not rushed. The user is not forced through
- **The craft standard**: if a transition feels accidental or mechanical, it is not at Immersive Garden level. Nothing accidental

*What Mithaq avoids:*
- Over-abstraction where beautiful motion exists without a clear message
- Complexity that slows the site without serving conversion
- Transitions so dramatic they create disorientation

---

**Reference 4: Floema**
*What it does:* Demonstrates that WebGL can be calm, luxurious, and emotionally warm rather than high-energy and technical.

*What Mithaq borrows:*
- The **restraint principle**: a single beautiful shader is more powerful than ten competing effects
- **Material depth over polygonal complexity**: rich PBR materials, subtle subsurface hints, realistic speculars — not geometric complexity
- The **darkness as premium**: deep backgrounds with controlled, warm highlights feel expensive; aggressive lighting feels cheap
- Atmospheric subtlety in idle states: when nothing is animating, the scene still feels alive (subtle ambient particle drift, slow light shimmer)

*What Mithaq avoids:*
- Floema's purely aesthetic, narrative-free moments (Mithaq must always serve a message)
- Being so restrained that content clarity is lost
- The fashion/luxury lifestyle register — Mithaq is legal authority, not perfume

---

**Reference 5: Lenz & Staehelin**
*What it does:* Proves that a premium institutional legal brand can feel authoritative without 3D, purely through typographic hierarchy, structured content, and credibility signals.

*What Mithaq borrows:*
- **Content gravity**: instructor names, firm credentials, and legal background copy must be treated as the most important text on the page — not secondary to visuals
- **Typography as authority signal**: the display face choice must communicate gravitas, not creativity
- **Information hierarchy**: every scene must have a clear primary message. No visual noise competing with the main point
- **Trust architecture**: testimonials, numbers, and institutional associations must feel documented, not designed

*What Mithaq avoids:*
- The static, flat, template quality of a traditional law firm site
- Losing the cinematic/premium digital layer entirely
- The corporate grey palette (Mithaq is dark premium, not institutional beige)

---

### The Synthesis Rule

When any design or technical decision must be made, run it through this filter:

| Question | If Yes | If No |
|----------|--------|-------|
| Does this serve the Mithaq message? | Keep | Remove |
| Does this feel legal and authoritative? | Keep | Reconsider |
| Does this feel premium but not theatrical? | Keep | Tone down |
| Does this support conversion clarity? | Keep | Simplify |
| Does this work on mobile? | Keep | Adapt |

---

## 4. CREATIVE DIRECTION SYSTEM

### 4.1 Color Token System

The palette is derived from three real-world references: **the judicial chamber** (dark wood, candlelit), **the official seal** (gold embossment on dark background), and **aged legal parchment** (warm cream, ink).

| Token | Hex | Role |
|-------|-----|------|
| `--mithaq-void` | `#08070F` | Canvas background, absolute dark |
| `--mithaq-ink` | `#0E0C1A` | Elevated surface, card backgrounds |
| `--mithaq-chamber` | `#161422` | Scene environment, secondary surfaces |
| `--mithaq-wood` | `#1C1510` | Legal desk surface base |
| `--mithaq-seal-gold` | `#C4913A` | Primary accent — seal, gavel brass, dividers |
| `--mithaq-gold-light` | `#E8C97A` | Highlights, hover states, active indicators |
| `--mithaq-gold-dim` | `#8B6420` | Secondary gold, shadows |
| `--mithaq-parchment` | `#F2E8D0` | Primary text on dark backgrounds |
| `--mithaq-parchment-dim` | `#BFB09A` | Body text, secondary copy |
| `--mithaq-trust-navy` | `#1A2540` | Subtle secondary accent — trust signals |
| `--mithaq-red-authority` | `#8B1A1A` | Only for warning/urgency — use sparingly |

**Color philosophy:** 90% of the site lives in dark tones (`void`, `ink`, `chamber`). Gold appears as signal, not background fill. Parchment is for reading; gold is for attention. Never use both on the same element.

---

### 4.2 Typography System

| Role | Font | Weight | Use |
|------|------|--------|-----|
| Display / Hero Headlines | **Cormorant Garamond** | 400 Italic, 600 | H1, hero positioning line, section declarations |
| Authority Subheadings | **Cormorant Garamond** | 700 | Scene titles, mentor names, section anchors |
| Body / Content | **DM Sans** | 300, 400 | All paragraph copy, descriptions, scene body text |
| Labels / Numbers / System | **JetBrains Mono** | 400 | Scene numbers (01–10), statistics, metadata labels |
| Arabic (if required) | **Tajawal** (body), **Lemonada** (display) | 400, 700 | Arabic variant of all copy |

**Typography rules:**
- Cormorant Garamond renders at **minimum 48px display, 32px section-heading** — it earns the stage
- DM Sans body copy: **18px / 1.7 line-height** for reading comfort in dark environments
- Never mix Cormorant and Tajawal on the same line in a bilingual heading — switch the entire element
- Scene numbers in JetBrains Mono at 11px, letter-spacing 0.15em, gold color, above every section heading
- The typeface itself communicates: Cormorant is the voice of legal authority. DM Sans is accessible clarity. The contrast between them is the brand's voice.

---

### 4.3 Motion Vocabulary

| Motion Type | Easing | Duration | Purpose |
|-------------|--------|----------|---------|
| Gavel descent | `power3.in` | 1.2s | Authority, weight, inevitability |
| Gavel strike impact | `power4.out` | 0.05s | Decisive, controlled |
| Ripple expansion | `power2.out` | 1.8s | Controlled spread, not explosion |
| Seal emergence | `circ.out` | 2.0s | Ceremonial, official, deliberate |
| Text reveals (Mithaq hero) | `power2.out` | 0.7s per word | Clear, readable, not theatrical |
| Scene transitions | `power2.inOut` | 0.6s | Smooth, professional |
| Hover states | `power1.out` | 0.2s | Responsive but not eager |
| Scroll camera moves | Custom cubic | Continuous | Fluid, camera-operator quality |
| Reduced motion fallback | `none` (fade only) | 0.4s opacity | Accessible, clean |

**Motion rule:** If a motion exists for more than 1.5 seconds with no new information delivered, cut it. Every frame of motion must earn its place by revealing, transitioning, or punctuating content.

---

### 4.4 Material & Lighting Language

**Lighting setup (Three.js):**
- **Key light:** `DirectionalLight`, warm amber-white (`#F5D87A`), intensity 1.2, positioned upper-left
- **Fill light:** `PointLight`, cool deep blue-purple (`#1A1040`), intensity 0.3, positioned lower-right
- **Rim light:** `PointLight`, gold (`#C49030`), intensity 0.5, positioned directly behind gavel, creating separation from background
- **Ambient:** `AmbientLight`, near-black (`#0A0812`), intensity 0.15 — just enough to not lose geometry in shadow

**Material decisions:**
- Gavel head: `MeshPhysicalMaterial` — dark walnut wood, roughness 0.85, metalness 0, subtle normal map for grain
- Gavel brass band: `MeshPhysicalMaterial` — brushed brass, roughness 0.3, metalness 0.9
- Desk surface: Custom `ShaderMaterial` — dark wenge wood grain, high roughness, adds ripple displacement uniform on impact
- Mithaq Seal: `MeshPhysicalMaterial` with emissive map — gold lines emit slightly after the gavel strike
- Ambient particles: `Points` with custom shader — gold dust, 0.5px, low opacity, slow drift

---

## 5. OPENING SEQUENCE DIRECTION

The opening sequence is the most critical 8 seconds of the entire experience. It must be storyboarded frame-by-frame and engineered precisely. **This is not a loading screen. It is Act I of the Mithaq story.**

---

### 5.1 Sequence Timeline

| Time | What Happens | Technical Layer |
|------|-------------|-----------------|
| 0.0s | Black void. Total darkness. | CSS background, no Canvas yet |
| 0.3s | Canvas mounts. Faint golden atmospheric particles drift. 200 particles, slow, random walks. | R3F Points system |
| 1.0s | Single warm key light slowly fades in, revealing dark desk surface. Grain visible. | DirectionalLight intensity tween |
| 1.8s | Gavel enters frame from upper edge. Slow descent. Single light source creates sharp shadow on desk. | GSAP timeline drives `gavel.position.y` |
| 2.5s | User sees "Skip intro" label appear (10px, JetBrains Mono, gold, 30% opacity, top-right) | DOM element with opacity tween |
| 3.0s | Gavel pauses 2cm above desk surface. Slight pause — the hesitation before authority speaks. | GSAP pause(0.4s) |
| 3.4s | **THE STRIKE.** Single decisive `power4.in` motion, 0.08s duration. No slow-motion. Real weight. | GSAP ultra-short tween |
| 3.5s | Impact frame: particles burst outward (150 gold dust particles, `power3.out` fade). | Instanced mesh burst |
| 3.6s | **Concentric gold ring** expands from impact point on desk surface. Not explosion — a ripple of authority. Shader driven, uniform `uProgress 0→1` over 1.8s. | Custom ShaderMaterial on desk plane |
| 4.0s | From the center of the ripple, **fracture lines** draw outward in 6–8 directional paths. Not cracks — geometric, controlled, almost calligraphic. Gold emission. Shader driven. | Secondary ShaderMaterial layer |
| 5.0s | Fracture lines stop expanding. At their termination points, **circular segments** appear — the beginning of the Mithaq Seal outline being drawn. | GSAP path-draw on 3D ring geometry |
| 5.8s | The Mithaq Seal completes its circular outline. Arabic script inside slowly illuminates (emissive map activation). The seal glows from within. | Emissive intensity tween on seal mesh |
| 6.5s | Camera begins a slow backward pull (z-axis), revealing the full desk surface, the seal, the gavel resting beside it. | GSAP camera.position.z tween |
| 7.0s | **Mithaq wordmark fades in** in Cormorant Garamond, centered above the seal. Simultaneously, Arabic subtitle fades in below: *ميثاق — من الدراسة إلى الاحتراف* | DOM HTML overlay, Framer Motion |
| 7.8s | Sub-headline appears: "Practical legal training for the lawyers the market actually needs." DM Sans, parchment. | Framer Motion staggered reveal |
| 8.2s | Primary CTA button pulses once with a subtle gold ring, then stabilizes. | CSS animation |
| 8.5s | **Intro complete.** Lenis scroll is enabled. ScrollTrigger takes over. The gavel and seal remain in canvas as scene anchors for Scene 02. | Zustand: `openingComplete: true` |

---

### 5.2 Opening Technical Architecture

```
Opening Sequence Controller (GSAP Timeline)
├── Phase 1: Environment reveal (0–1.8s)
│   └── AmbientLight + desk material fade
├── Phase 2: Gavel descent (1.8–3.4s)
│   └── gavel.position.y tween + shadow cast
├── Phase 3: Strike + Impact (3.4–3.6s)
│   └── Ultra-fast position snap + particle burst
├── Phase 4: Ripple + Fracture (3.6–5.0s)
│   └── ShaderMaterial uniforms (uProgress, uFractureProgress)
├── Phase 5: Seal emergence (5.0–5.8s)
│   └── Ring geometry draw + emissive activation
├── Phase 6: Camera pull + hero reveal (5.8–8.5s)
│   └── camera.position tween + DOM overlays (Framer Motion)
└── Phase 7: Handoff (8.5s)
    └── Enable Lenis, initialize ScrollTrigger scenes
```

**Critical constraint:** The opening must be **skippable from 2.5s onwards**. The skip button should jump directly to Scene 02 hero state (camera position pre-set, all DOM content visible, Lenis enabled). Skipping triggers a 0.3s crossfade, not a jarring cut.

**Preload requirement:** The gavel GLB (≤1.5MB compressed) and seal geometry must be fully loaded before the animation begins. Use `useProgress` from `@react-three/drei` to gate the timeline start. Show the atmospheric particles as a loading indicator — they start at 0.3s even before full load, acting as a premium "we're getting ready" signal.

---

## 6. SCENE-BY-SCENE WEBSITE EXPERIENCE

After the opening completes, Lenis takes over smooth scroll. GSAP ScrollTrigger maps scroll progress to scene state via a Zustand store. The R3F canvas persists globally and transitions between scene states.

---

### Scene 01 — Gavel of Authority
**Scroll position:** 0%–10% of total page
**Primary objective:** Establish authority, differentiation, cinematic quality within the first impression
**3D state:** Gavel and seal remain from opening, camera settles
**DOM content:** Minimal — just Mithaq wordmark, tagline, and CTA
**Transition out:** Camera begins a slow forward drift as scroll progresses, seal grows slightly in viewport

---

### Scene 02 — Hero / Mithaq Reveal
**Scroll position:** 10%–22%
**Primary objective:** Immediate clarity — what is Mithaq, who is it for, what does it offer
**Primary headline (Cormorant Garamond, 72px):**
> "Practical Legal Training for the Lawyers the Market Actually Needs."

**Sub-copy (DM Sans 18px):**
> "Mithaq prepares law graduates and early-career lawyers for real practice — not theory. Workshops, training tracks, and mentorship built around what courts, firms, and clients actually demand."

**Primary CTA:** "Register for the Next Workshop →" (gold border button)
**Secondary CTA:** "View Our Tracks" (text link, parchment)
**WhatsApp CTA:** Persistent floating button (bottom-right, WhatsApp green icon, opens link)

**3D state:** Gavel has settled to the side of frame. Seal remains as ambient background element. Warm gold light shifts slightly to illuminate copy area.
**Transition in:** Text elements stagger in from bottom (30px offset, 0.6s each, 0.1s delay between)

---

### Scene 03 — The Gap
**Scroll position:** 22%–37%
**Primary objective:** Show the pain point — the chasm between what law schools teach and what legal practice requires
**Narrative hook:** This is the "problem statement" section. The user must recognize their situation.

**Visual concept:** Floating document fragments — legal notes, academic references, partially-completed forms — drift in a fragmented state around the 3D space. Nothing connects. They float individually, unresolved.

**Headline:** "Four Years of Law School. Zero Days of Real Practice."
**Body copy (abbreviated):** "Law schools teach doctrine. Cases. Theory. What they don't teach: how to write a legal memo that a partner will actually approve. How to structure a client file. How to handle a hearing. How to think like a practitioner."

**3D state:** Gavel has moved off-frame. Floating document meshes (plane geometry with parchment-colored material, slight crumple normal map) rotate slowly in atmospheric space. As scroll progresses into this scene, documents accumulate and orbit a central empty point — reinforcing the "gap" metaphor visually.

**Transition into Scene 04:** Documents begin converging toward a single point as scroll crosses 37%. The convergence is the transition. Mithaq's method is what fills the gap.

---

### Scene 04 — The Mithaq Method
**Scroll position:** 37%–50%
**Primary objective:** Explain how Mithaq bridges the gap — the methodology
**Narrative:** The documents converge into a single structured legal desk. Order replaces chaos.

**Headline:** "The Mithaq Method: Study What Practice Actually Demands"
**Method pillars (4):**
1. Skill-First Curriculum — every session teaches a skill you can use next week
2. Real Scenarios — training cases built from actual legal situations
3. Expert-Led — instructors with active professional careers, not just academic backgrounds
4. Career Integration — from legal writing to LinkedIn to interview preparation

**3D state:** A structured legal desk materializes from the convergence of the fragments. Organized files, a legal notepad, a pen, an official stamp. Clean, ordered, authoritative. This is what Mithaq brings to the chaos.

**Transition mechanism:** Scroll drives a `useTransform` that morphs document positions from chaotic orbits to organized desk positions. No abrupt cut — continuous transformation.

---

### Scene 05 — Training Pillars
**Scroll position:** 50%–62%
**Primary objective:** Present the core Mithaq training tracks clearly, with enough detail to make the user understand what they would get
**Layout:** Five pillars displayed as premium editorial cards — not generic UI cards. More like stamped dossiers or official legal folders.

**The Five Pillars:**

| Pillar | Card Title | Card Description |
|--------|-----------|------------------|
| 01 | Professional Readiness | How to conduct yourself as a legal professional in meetings, correspondence, and firm culture |
| 02 | Legal Research & Opinion | How to structure and write a valid legal opinion from brief to conclusion |
| 03 | Legal Writing & Memo Drafting | Contract memos, correspondence letters, internal memos — the documents that define your professional reputation |
| 04 | Career Infrastructure | CV, LinkedIn profile, interview technique, and firm culture navigation built for law graduates |
| 05 | Practical Legal Mindset | The habits, frameworks, and professional judgment that distinguish practitioners from students |

**Card design:** Dark ink background, gold seal corner mark, Cormorant Garamond title, DM Sans description. When hovered: the card lifts slightly (5px), a subtle gold border illuminates, and a faint stamped-seal watermark becomes visible.

**3D state:** Each card appears in DOM (drei `<Html>` overlay positioned relative to 3D anchor points on the desk). As scroll progresses through this scene, each card reveals sequentially with a 0.15s stagger.

---

### Scene 06 — Workshops & Course Preview
**Scroll position:** 62%–72%
**Primary objective:** Show specific workshops/courses without turning this into a course catalog
**Design rule:** Treat workshops as premium engagements, not products in a shop

**Visual metaphor:** Legal case dossiers — thick folders with the workshop title stamped on the cover. The dossiers are arranged on the desk surface. Picking one up (hover) reveals a preview.

**Workshop card content (structure per card):**
- Workshop title (Cormorant, gold)
- Format: "3-day intensive" / "6-week track" / "Half-day workshop"
- Level: "Graduates" / "Junior Associates" / "Career Changers"
- Core skills covered (3 bullet points, DM Sans 14px)
- "View Details" link (opens a modal or scroll-reveals an expanded state)
- "Register Interest" CTA (gold bordered button)
- Capacity signal: "8 seats remaining" — urgency without desperation

**Important:** Do not show pricing publicly unless the client confirms. Inquiry/WhatsApp flow is preferable for premium positioning.

**3D state:** Dossier-like card objects on the desk surface. Hover interaction uses Raycaster to detect mouse position and lift the hovered card slightly.

---

### Scene 07 — Hall of Mentors
**Scroll position:** 72%–82%
**Primary objective:** Build trust through visible expertise — the instructors are a key purchase signal
**Design rule:** These are not profile cards. They are authority portraits.

**Visual direction:** Full-width editorial mentor gallery. Monochrome portrait with a warm gold tone overlay, slight vignette, their name in Cormorant Garamond below. Professional title beneath. One quoted authority statement from each mentor.

**Per mentor card:**
- Portrait (professional, high-contrast, ideally shot with legal environment background)
- Name (Cormorant Garamond, 28px)
- Current role (DM Sans, 14px, parchment-dim)
- Years of experience (JetBrains Mono, 11px, gold)
- One-sentence authority statement (DM Sans italic, 16px)
- Areas of expertise (2–3 compact tags)

**3D state:** The mentor gallery transitions as a gentle horizontal scroll / camera track. The desk environment persists subtly in the background, anchoring the mentors within the "Mithaq Chamber" world.

---

### Scene 08 — Trust / Authority / Credibility
**Scroll position:** 82%–88%
**Primary objective:** Present proof points that remove doubt and validate the decision to register
**Content types:**
- Total participants trained (number counter, animated on scroll)
- Total workshops delivered
- Satisfaction rate / testimonials
- Institutional affiliations or partner logos (if available)
- Relevant professional certifications of instructors

**Layout:** Three-column trust block. Numbers left column, testimonials center, institutional logos right.

**Testimonial design:** Not a carousel (carousels reduce readability). Two or three testimonials in a fixed grid. Each has: name, university or firm (not full bio), one attributed quote (DM Sans italic 18px), gold quotation mark as a typographic device.

**3D state:** Scene transitions to a clean environment — the desk pulls back, the space opens up. This scene is more "editorial" than immersive, allowing content to breathe.

---

### Scene 09 — FAQ
**Scroll position:** 88%–94%
**Primary objective:** Address the most common objections before they become reasons to leave
**Design:** Clean, semantic `<details>`/`<summary>` accordion. No 3D elements compete here. Typography-only, perfectly readable.

**Required FAQ entries:**
1. Who is Mithaq for?
2. What is the difference between Mithaq and a law school course?
3. Do I receive a certificate?
4. Are workshops online or in-person?
5. How long does each training track take?
6. What is the application / registration process?
7. Can I register for a single workshop instead of a full track?
8. What payment options are available?
9. Are sessions recorded for later viewing?
10. How do I know if a workshop is right for my level?

**Accordion design rule:** Open/close icon is a plus/minus, not a chevron. Gold line above each question. Answer text in DM Sans 16px. Max two-level question hierarchy only — no nested accordions.

**3D state:** Minimal. Ambient particles only. The chamber is calm in this section.

---

### Scene 10 — Final CTA / Closing Covenant
**Scroll position:** 94%–100%
**Primary objective:** Convert. This is the most important 6% of the scroll journey.
**Narrative:** The Mithaq Seal returns, centered, glowing. This is the closing of the covenant.

**Visual:** The gavel and seal from Scene 01 reappear in a callback moment. The camera is further away now — we see the full desk, the seal prominently centered, warm light. A sense of arrival.

**Headline:** "Are You Ready to Practice the Law You Know?"
**Sub-headline:** "Mithaq workshops begin every season. Limited seats. Professional enrollment only."

**CTA options (based on client choice):**
- "Register Now" → Registration form or external link
- "Inquire via WhatsApp" → WhatsApp deep link
- "Join the Waitlist" → Email capture form
- "Speak with Our Team" → Calendar booking link

**Trust reinforcement:** Three micro-trust signals below the CTA (icons + text): "Professional instructors", "Limited cohort sizes", "Certificate of completion"

**Visual close:** After the CTA block, a horizontal gold rule, then the Mithaq wordmark centered, small, and below it: ميثاق © 2024. No footer clutter. Clean close.

---

## 7. WEBSITE STRUCTURE / INFORMATION ARCHITECTURE

### 7.1 Pages Required (MVP)

| Route | Type | Priority |
|-------|------|---------|
| `/` | Main landing experience (10 scenes) | P0 — Core |
| `/workshops/[slug]` | Individual workshop detail page | P1 |
| `/instructors` | Full mentor listing (optional, may be landing-page section only) | P2 |
| `/about` | Mithaq story and mission | P2 |
| `/register` | Registration or inquiry form | P0 |
| `/api/contact` | Server-side form handling | P0 |

### 7.2 Navigation Architecture

**Header navigation:**
- Fixed, transparent over hero, switches to dark fill on scroll past Scene 02
- Left: Mithaq wordmark (SVG, 20px height)
- Right: Text links — Workshops | Method | Mentors | FAQ
- Right-end: "Register" button (gold border)
- Mobile: hamburger → full-screen overlay nav

**Navigation behavior:**
- No mega-menus. Four links maximum in primary nav.
- "Workshops" scrolls to Scene 06 OR links to `/workshops`
- "Register" always opens registration flow regardless of scroll position
- Arabic/English toggle (if bilingual)

### 7.3 URL Structure

```
mithaq.com/               — Main landing experience
mithaq.com/workshops/     — Workshop index (listing of all workshops)
mithaq.com/workshops/legal-memo-writing/   — Individual workshop
mithaq.com/register/      — Registration / inquiry form
mithaq.com/about/         — Brand story
mithaq.com/ar/            — Arabic root (if i18n)
```

### 7.4 i18n Architecture (if Arabic required)

Use Next.js built-in i18n routing:
```js
// next.config.js
i18n: {
  locales: ['en', 'ar'],
  defaultLocale: 'en',   // or 'ar' if Arabic-first
}
```

Set `dir="rtl"` on `<html>` for Arabic. Use CSS logical properties (`margin-inline-start` not `margin-left`) throughout. Separate Arabic font loading, activated by locale. The Three.js canvas is not affected by text direction — only DOM elements need RTL treatment.

---

## 8. UX / CONVERSION STRATEGY

### 8.1 The Conversion Funnel

```
AWARENESS (Scene 01–02)
→ "This is premium. This is different. I want to know more."
→ KPI: Scroll depth past 22%

UNDERSTANDING (Scene 03–05)
→ "This solves my exact problem. I recognize myself in this."
→ KPI: Scroll depth past 50%, time-on-site > 90s

INTEREST (Scene 06–07)
→ "There is a specific workshop I want. These instructors are credible."
→ KPI: Workshop card hover/click, Instructor section engagement

INTENT (Scene 08–09)
→ "I have answered my objections. I am close to deciding."
→ KPI: FAQ interaction, Trust section view

CONVERSION (Scene 10 + persistent CTAs)
→ "I am registering / contacting / joining the waitlist."
→ KPI: CTA click, WhatsApp contact, form submit
```

### 8.2 CTA Hierarchy

**Priority 1 (always visible):**
- WhatsApp floating button (bottom-right, always in viewport)
- This is the lowest friction conversion path — one tap

**Priority 2 (scene-specific):**
- "Register for the Next Workshop" in Scene 02 and Scene 10
- This is the primary conversion action

**Priority 3 (secondary):**
- "View Our Tracks" in Scene 02
- "Register Interest" on workshop cards (Scene 06)

**Priority 4 (supporting):**
- "Join Waitlist" for workshops with limited availability
- "Speak with Our Team" for institutional/corporate inquiries

### 8.3 Friction Reduction Principles

1. **Never require a full registration form as the first step.** WhatsApp or a 3-field form (Name, Email, Workshop interest) is the MVP conversion.
2. **Workshop cards must have an inquiry CTA**, not just a "details" link. The path from interest to contact must be ≤2 taps.
3. **The FAQ must answer the question "how do I register?"** explicitly. Users who find the FAQ are close to converting — do not lose them to confusion.
4. **Social proof must be above the fold on mobile.** On small screens, Scene 07 (mentors) and key trust numbers should appear earlier in the flow than on desktop.

### 8.4 Mobile-Specific UX Adjustments

- Scene 01 (Opening): 4s maximum, auto-complete on mobile, no manual "skip" needed
- Scene 03 (Gap): Floating documents reduced to 3 elements maximum
- Scene 05 (Pillars): Horizontal scroll between cards (native touch scroll, no custom scroll library)
- Scene 06 (Workshops): Stacked cards, one per row, clear tap targets
- Scene 07 (Mentors): Horizontal swipe gallery
- Scene 10 (CTA): WhatsApp CTA at 100% width button, first in CTA stack

---

## 9. 3D / WebGL STRATEGY

### 9.1 Global Canvas Architecture

One persistent `<Canvas>` mounted at the root layout level. All scenes share the same WebGL context. Scene components mount/unmount via conditional rendering driven by Zustand scroll state.

```tsx
// app/layout.tsx
export default function RootLayout({ children }) {
  return (
    <html>
      <body>
        <MithaqCanvas />          {/* Persistent, full-viewport R3F canvas */}
        <main>{children}</main>   {/* DOM content overlaid via CSS */}
      </body>
    </html>
  );
}

// components/canvas/MithaqCanvas.tsx
export function MithaqCanvas() {
  return (
    <Canvas
      gl={{ antialias: true, alpha: false }}
      camera={{ fov: 45, near: 0.1, far: 100 }}
      dpr={[1, 1.5]}           // Cap DPR at 1.5 for performance
      style={{ position: 'fixed', inset: 0, zIndex: 0 }}
    >
      <Suspense fallback={null}>
        <SceneManager />
        <PerformanceMonitor />   // From drei
        <PostProcessing />       // Conditional on device tier
      </Suspense>
    </Canvas>
  );
}
```

### 9.2 Scene Manager

```tsx
function SceneManager() {
  const { activeScene, openingComplete } = useMithaqStore();

  return (
    <>
      {!openingComplete && <OpeningSequence />}
      {openingComplete && (
        <>
          <Scene01Gavel visible={activeScene <= 1} />
          <Scene02Hero visible={activeScene === 2} />
          <Scene03Gap visible={activeScene === 3} />
          <Scene04Method visible={activeScene === 4} />
          <Scene05Pillars visible={activeScene === 5} />
          {/* Scenes 06–10: lazy loaded */}
          <Suspense fallback={null}>
            <LazyScenes activeScene={activeScene} />
          </Suspense>
        </>
      )}
      <SharedEnvironment />  {/* Persists across all scenes */}
    </>
  );
}
```

### 9.3 Zustand Store Architecture

```typescript
// lib/store/mithaq-store.ts
interface MithaqStore {
  // Scene State
  activeScene: number;       // 0–10
  sceneProgress: number;     // 0–1 progress within current scene
  scrollProgress: number;    // Global scroll 0–1

  // Opening Sequence
  openingComplete: boolean;
  openingProgress: number;   // 0–1
  gavelStruck: boolean;
  sealRevealed: boolean;

  // Loading
  criticalAssetsLoaded: boolean;
  loadingProgress: number;   // 0–100

  // Accessibility
  reducedMotion: boolean;
  webGLAvailable: boolean;
  deviceTier: 'high' | 'mid' | 'low';

  // UI
  navOpen: boolean;
  activeModal: string | null;
  language: 'en' | 'ar';

  // Conversion
  ctaSource: string | null;  // Track which CTA was clicked

  // Actions
  setActiveScene: (n: number) => void;
  setScrollProgress: (n: number) => void;
  completeOpening: () => void;
  setGavelStruck: (v: boolean) => void;
  setDeviceTier: (t: DeviceTier) => void;
  openModal: (id: string) => void;
  closeModal: () => void;
  setLanguage: (l: Language) => void;
  skipOpening: () => void;
}
```

### 9.4 Gavel Opening Shaders

**Ripple ShaderMaterial (desk surface):**
```glsl
// ripple.frag
uniform float uProgress;     // 0 → 1 over 1.8s
uniform vec2 uImpactPoint;   // UV coords of gavel tip contact
uniform vec3 uGoldColor;     // #C4913A

varying vec2 vUv;

void main() {
  float dist = distance(vUv, uImpactPoint);
  
  // Ring expansion: leading edge at uProgress, 0.05 width
  float ring = smoothstep(uProgress - 0.05, uProgress, dist)
             - smoothstep(uProgress, uProgress + 0.02, dist);
  
  // Echo ring: 0.3 behind
  float echo = smoothstep(uProgress - 0.35, uProgress - 0.3, dist)
             - smoothstep(uProgress - 0.3, uProgress - 0.25, dist);
  echo *= 0.3; // 30% intensity of primary ring
  
  // Fade total progress toward edges of UVs
  float edgeFade = 1.0 - smoothstep(0.4, 0.5, dist);
  float totalFade = 1.0 - smoothstep(0.85, 1.0, uProgress);

  float intensity = (ring + echo) * edgeFade * totalFade;
  gl_FragColor = vec4(uGoldColor, intensity);
}
```

**Fracture Lines ShaderMaterial:**
The fracture lines use a custom Voronoi-seeded distance field, constrained to 6-8 directional paths (pre-authored, not random) so they read as deliberate legal-document-like rays, not chaotic cracks. Each line has an anisotropic glow using a Gaussian along the perpendicular axis.

### 9.5 3D Asset Pipeline

| Asset | Polygon Budget | Texture Budget | Format |
|-------|--------------|----------------|--------|
| Judicial gavel | ≤ 8,000 tris | 2K PBR set (color, normal, roughness) | GLB, Meshopt |
| Mithaq Seal (3D) | ≤ 3,000 tris | 1K (gold metal) | GLB, Meshopt |
| Legal desk | ≤ 5,000 tris | 2K (wood grain) | GLB, Meshopt |
| Floating documents (Scene 03) | ≤ 500 tris each × 8 | Shared atlas | GLB |
| Organized desk (Scene 04) | ≤ 10,000 tris total | 2K shared | GLB, Meshopt |
| Workshop dossiers (Scene 06) | ≤ 2,000 tris each × 6 | Shared | GLB |
| **Total desktop budget** | — | **≤ 8MB uncompressed textures** | **KTX2 compressed → ≤ 2.5MB** |
| **Mobile assets** | 50% reduced | 1K or shared atlas | GLB, simplified |

**Blender production notes:**
- Bake all indirect lighting into texture maps — no real-time global illumination
- Use only one environment map (HDRI) for reflections — shared across all scenes
- Apply Meshopt compression via `gltfpack -i model.glb -o model-opt.glb -cc`
- Convert all textures to KTX2 with Basis Universal supercompression

### 9.6 Post-Processing (Conditional by Device Tier)

```tsx
function PostProcessing() {
  const { deviceTier } = useMithaqStore();

  return (
    <EffectComposer multisampling={deviceTier === 'high' ? 4 : 0}>
      {deviceTier !== 'low' && (
        <Bloom
          intensity={0.4}
          threshold={0.8}
          luminanceSmoothing={0.9}
        />
      )}
      {deviceTier === 'high' && (
        <Vignette eskil={false} offset={0.3} darkness={0.7} />
      )}
    </EffectComposer>
  );
}
```

**Device tier detection:**
```typescript
export function detectDeviceTier(): DeviceTier {
  const gl = document.createElement('canvas').getContext('webgl2');
  if (!gl) return 'low';

  const renderer = gl.getParameter(gl.RENDERER);
  const isMobile = /Mobile|Android/.test(navigator.userAgent);
  const cores = navigator.hardwareConcurrency ?? 2;
  const memory = (navigator as any).deviceMemory ?? 2;

  if (isMobile && memory < 4) return 'low';
  if (isMobile || cores < 4) return 'mid';
  return 'high';
}
```

---

## 10. TECHNICAL STACK RECOMMENDATION

### Definitive Stack

| Layer | Technology | Version | Rationale |
|-------|-----------|---------|-----------|
| **Framework** | Next.js | 14 (App Router) | SSR for SEO, ISR for workshop pages, optimal Vercel deployment |
| **React** | React | 18 | Concurrent features, Suspense for async 3D loading |
| **3D Engine** | Three.js | r165+ | Full control over WebGL, no abstraction ceiling |
| **R3F** | @react-three/fiber | 8.x | React reconciler for Three.js — cleaner component model |
| **Helpers** | @react-three/drei | 9.x | Camera, Html overlay, Environment, useProgress, Bounds |
| **Post-FX** | @react-three/postprocessing | 2.x | Bloom, Vignette, conditional on device tier |
| **Animation** | GSAP + ScrollTrigger | 3.x | Cinematic timelines, scroll choreography |
| **Smooth Scroll** | Lenis | 1.x | Best-in-class smooth scroll, GSAP integration |
| **UI Transitions** | Framer Motion | 11.x | DOM overlay reveals, page transitions |
| **State** | Zustand | 4.x | Minimal, performant, no Context overhead |
| **Styling** | Tailwind CSS + CSS vars | 3.x | Utility classes + design token custom properties |
| **Language** | TypeScript | 5.x | Type safety across store, components, shaders |
| **3D Authoring** | Blender | 4.x | Full control, GLB/glTF export |
| **Optimization** | gltfpack / Meshopt | Latest | GLB compression |
| **Textures** | KTX2 / Basis Universal | — | Compressed GPU textures |
| **Deployment** | Vercel | — | Next.js native, edge network, CDN, preview URLs |
| **Dev Tools** | Leva (dev only) | — | Runtime 3D parameter tuning |
| **QA** | Lighthouse CI + Axe | — | Automated performance + accessibility gates |
| **Monitoring** | Sentry + Vercel Analytics | — | Error tracking + performance insights |

### What to Avoid

| Technology | Reason to Avoid |
|-----------|-----------------|
| Spline | No shader control, performance ceiling, export limitations |
| A-Frame / Babylon.js | Wrong abstraction level for this use case |
| React Spring for 3D | Use GSAP instead — better control for cinematic timelines |
| CSS-only animations for 3D | They can't interact with WebGL state |
| Webpack bundle without analysis | Always bundle-analyze before production |

---

## 11. ACCESSIBILITY STRATEGY

Accessibility is not optional. It is a quality gate. A site that cannot be navigated without a mouse fails professionally, regardless of how impressive the 3D is.

### 11.1 Core Requirements

| Requirement | Implementation |
|-------------|---------------|
| **Semantic HTML** | All scenes have underlying HTML sections with proper heading hierarchy (h1 → h6). The canvas is decorative aria-hidden. |
| **Screen reader content** | All important text in DOM, not canvas-only. The 3D is purely visual; all narrative is in HTML. |
| **Keyboard navigation** | Tab order follows visual order. No keyboard traps. Modal closes on Escape. |
| **Visible focus states** | Custom focus ring: 2px solid `--mithaq-seal-gold`, 2px offset. Never `outline: none`. |
| **Reduced motion** | Full reduced-motion mode activated by `prefers-reduced-motion: reduce`. |
| **WebGL fallback** | If WebGL unavailable: static poster image + full editorial layout. Same content, no canvas. |
| **Color contrast** | Parchment `#F2E8D0` on Void `#08070F`: contrast ratio 15.8:1 (AAA). Gold `#C4913A` on Void: 5.1:1 (AA). All body text passes AA. |
| **RTL support** | Full RTL layout for Arabic using CSS logical properties and `dir="rtl"` on `<html>`. |
| **Preloader time limit** | No loading screen blocks interaction for more than 5 seconds. Core text and CTA visible immediately. |
| **Form accessibility** | All form inputs have associated labels, not just placeholder text. Error states use both color and text. |
| **FAQ accordion** | Uses native `<details>`/`<summary>` or correct ARIA `role="region"`, `aria-expanded`. |

### 11.2 Reduced Motion Mode

```tsx
// hooks/useReducedMotion.ts
export function useReducedMotion() {
  const mediaQuery = window.matchMedia('(prefers-reduced-motion: reduce)');
  return mediaQuery.matches;
}

// In components:
const reducedMotion = useReducedMotion();

if (reducedMotion) {
  // Skip GSAP timeline, use instant state
  gsap.set(elements, { opacity: 1 });
} else {
  // Full cinematic timeline
  gsap.from(elements, { opacity: 0, y: 30, duration: 0.6 });
}
```

**Reduced motion experience replacement:**
- Opening sequence: Show static Mithaq wordmark + seal illustration (SVG) with a 0.4s fade-in
- Gavel: Static hero image of gavel on desk surface (Blender render exported as WebP)
- Scroll parallax: Disabled entirely
- Scene transitions: Simple opacity fades between sections
- All content fully accessible and readable in this mode

### 11.3 WebGL Fallback

```tsx
// components/canvas/WebGLFallback.tsx
export function WebGLFallback() {
  return (
    <div aria-label="Mithaq legal academy website" className="fallback-layout">
      <img
        src="/hero-static.webp"
        alt="Mithaq — Legal Training Academy"
        loading="eager"
      />
      {/* Full editorial layout of all 10 scenes as a normal webpage */}
    </div>
  );
}

// WebGL detection
const webGLAvailable = (() => {
  try {
    const canvas = document.createElement('canvas');
    return !!(canvas.getContext('webgl2') || canvas.getContext('webgl'));
  } catch {
    return false;
  }
})();
```

---

## 12. PERFORMANCE STRATEGY

### 12.1 Performance Budgets

| Metric | Target | Hard Maximum |
|--------|--------|-------------|
| LCP (Largest Contentful Paint) | < 2.0s | < 2.5s |
| INP (Interaction to Next Paint) | < 100ms | < 200ms |
| CLS (Cumulative Layout Shift) | < 0.05 | < 0.1 |
| FID / Total Blocking Time | < 50ms | < 200ms |
| Desktop FPS | 60 FPS | 45 FPS min |
| Mobile FPS | 45 FPS | 30 FPS min |
| Initial JS (pre-3D) | < 250 KB compressed | < 350 KB |
| Full page (first load) | < 700 KB compressed | < 900 KB |
| Hero GLB (desktop) | < 1.2 MB compressed | < 1.5 MB |
| Hero GLB (mobile) | < 600 KB compressed | < 700 KB |
| Texture payload desktop | < 2 MB total | < 3 MB |
| Texture payload mobile | < 800 KB total | < 1 MB |
| Web Font payload | < 80 KB (WOFF2) | < 100 KB |

### 12.2 Loading Strategy

**Phase 1 — Instant (< 1s):**
- HTML shell, Mithaq wordmark (SVG inline), body font (DM Sans 400 woff2)
- Hero text and primary CTA in DOM
- WhatsApp button functional
- Canvas element mounted but transparent

**Phase 2 — Progressive (1–3s):**
- Scene 01 GLB + desk texture (hero assets only, ≤ 1.5MB)
- Opening sequence begins when hero assets loaded
- `useProgress` drives the ambient particle system as visual "loading signal"
- Cormorant Garamond font loads (only 2 weights needed)

**Phase 3 — Lazy (post-opening, on demand):**
- Scenes 03–10 GLB assets loaded only as user scrolls within 1 scroll-screen distance
- Intersection Observer triggers loading before the scene is visible

```tsx
// Scene lazy loading pattern
function LazyScene({ sceneId, children }) {
  const [shouldLoad, setShouldLoad] = useState(false);
  const ref = useRef();

  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => { if (entry.isIntersecting) setShouldLoad(true); },
      { rootMargin: '100%' } // Load 1 viewport ahead
    );
    if (ref.current) observer.observe(ref.current);
    return () => observer.disconnect();
  }, []);

  return (
    <div ref={ref}>
      {shouldLoad ? (
        <Suspense fallback={<SceneSkeleton />}>
          {children}
        </Suspense>
      ) : <SceneSkeleton />}
    </div>
  );
}
```

### 12.3 Render Optimization

- `dpr={[1, 1.5]}` on Canvas — cap DPR. A 4K screen at full DPR is 16x more pixels than 1080p. Do not render them.
- `frameloop="demand"` after the opening sequence completes — only re-render when scroll state changes
- Pause render loop when tab is not visible: `document.addEventListener('visibilitychange', ...)`
- Use `instancedMesh` for floating document particles and desk particles — 200 particles as 200 draw calls kills mobile, 200 as one instanced mesh is fine
- Avoid real-time shadows — bake them into textures in Blender
- Avoid post-processing on mobile (`deviceTier === 'low'` or `'mid'`)
- Limit `MeshPhysicalMaterial` to 2–3 objects maximum (gavel, seal) — it is expensive

### 12.4 Asset Optimization Pipeline

```bash
# Step 1: Export GLB from Blender (apply modifiers, no animation baked unless needed)
# Step 2: Optimize with gltfpack
gltfpack -i gavel.glb -o gavel.opt.glb -cc -tc

# Step 3: Convert textures to KTX2
toktx --t2 --bcmp gavel-color.ktx2 gavel-color.png
toktx --t2 --bcmp gavel-normal.ktx2 gavel-normal.png

# Step 4: Verify final sizes
ls -lh *.glb *.ktx2

# Step 5: Add to Vercel CDN cache headers
# vercel.json: "Cache-Control": "public, max-age=31536000, immutable"
```

### 12.5 Vercel Configuration

```json
{
  "headers": [
    {
      "source": "/_next/static/(.*)",
      "headers": [
        { "key": "Cache-Control", "value": "public, max-age=31536000, immutable" }
      ]
    },
    {
      "source": "/models/(.*)",
      "headers": [
        { "key": "Cache-Control", "value": "public, max-age=31536000, immutable" }
      ]
    }
  ]
}
```

---

## 13. OPEN QUESTIONS / CLIENT ALIGNMENT QUESTIONS

Each question includes its reasoning and a clear recommendation. The client should answer these before development begins.

---

**Q1: Should the opening be the gavel strike, or should we explore a seal-based opening instead?**

*Why it matters:* The gavel is a universal symbol of legal authority but can edge into cliché if not executed with craft. The Mithaq Seal is more unique, directly tied to the brand name, and carries the "covenant" metaphor more precisely.

*Recommendation:* **Keep the gavel as the opening act**, but make the Seal the reveal and the hero of Act I. The gavel is a narrative trigger. The Seal is the brand. This structure earns both the authority of the gavel and the uniqueness of the Mithaq identity.

---

**Q2: What is the exact primary conversion action — registration form, WhatsApp, inquiry, or waitlist?**

*Why it matters:* The entire Scene 10 and all persistent CTAs are built around this. Getting it wrong means a beautiful site with a confusing purchase path.

*Recommendation:* **WhatsApp as the primary (lowest friction) + a simple 3-field form as secondary.** WhatsApp feels personal and accessible. The form captures structured lead data. Do not force a complex application form before trust is established.

---

**Q3: Will the site be Arabic-first, English-first, or bilingual?**

*Why it matters:* Arabic-first requires RTL as the default layout. The typography system, spacing, component structure, and navigation all change significantly. This decision affects Phase 2 onwards.

*Recommendation:* If the primary audience is Arabic-speaking students in the region (likely), **build Arabic-first as the primary experience**. English can be a secondary locale. This is more respectful of the audience and ensures the Arabic typography is not an afterthought.

---

**Q4: Do we have professional instructor photography?**

*Why it matters:* Scene 07 (Hall of Mentors) is one of the most trust-building moments. If instructor photos are unprofessional, the entire credibility architecture collapses. Generic stock photos or low-quality selfies will undermine the premium positioning more than almost any design failure.

*Recommendation:* **Schedule a professional photoshoot before development.** Monochrome with a warm gold overlay is the design direction — this requires clean, well-lit portraits with neutral or architectural backgrounds. Budget for this as a non-negotiable production item.

---

**Q5: Should the 3D visual world be realistic, symbolic, or abstract?**

*Why it matters:* This determines the entire Blender production approach and the rendering cost. Realistic PBR assets take 3–5x longer to produce and optimize than symbolic/low-poly assets.

*Recommendation:* **Symbolic realism** — objects should be recognizably legal (gavel, desk, seal, documents) but rendered with enough artistic control that they feel intentional, not photographic. This is the Floema/Oryzo approach: real enough to understand, crafted enough to be premium.

---

**Q6: What workshops and courses exist today, and which will be launched in the future?**

*Why it matters:* Scene 06 (Workshops Preview) must have real content to design around. Placeholder cards will be replaced but their count and format determine the layout.

*Recommendation:* Provide a content inventory of at least **3–5 confirmed workshops with titles, format, level, and key skills** before Scene 06 design begins. A workshop listing with real content communicates authority far more than beautifully designed empty cards.

---

**Q7: How long should the opening intro run before the user can fully use the site?**

*Why it matters:* Every second a user cannot scroll is friction. Premium does not mean slow. An intro that runs beyond 5–6 seconds without the ability to skip will cost conversions.

*Recommendation:* **8 seconds maximum before Lenis enables. Skip available from 2.5 seconds. On mobile, reduce to 5 seconds maximum with auto-complete.** This is stated in Section 5 — confirm the client agrees with this constraint.

---

**Q8: Should optional sound design be included?**

*Why it matters:* A subtle sound on gavel strike could dramatically elevate the impact moment. However, unexpected audio on a professional website is almost universally disliked and can embarrass users in shared environments.

*Recommendation:* **Optional sound, off by default.** A small audio toggle (speaker icon, top-right) gives users who want the premium audio experience the option. The gavel strike audio should be a deep, resonant, wooden thud — not dramatic or cinematic. Users who never activate audio lose nothing critical.

---

**Q9: Should instructor pages exist as separate routes, or is Scene 07 sufficient?**

*Why it matters:* SEO value of individual instructor pages can be significant, and deep-linking to a specific instructor can be a referral path.

*Recommendation:* **MVP: Scene 07 on the landing page with brief cards is sufficient.** Post-launch: Add `/instructors/[slug]` with full bios, linked publications, and credentials. Build the card component to be reusable for both contexts.

---

**Q10: What testimonials, numbers, and proof points are available?**

*Why it matters:* Scene 08 (Trust/Authority) is only as strong as its actual proof. "Trusted by legal professionals" with no evidence is a red flag, not a trust signal.

*Recommendation:* Provide at minimum: **3 genuine testimonials (with consent to publish), 2–3 quantitative proof points (participants trained, workshop hours delivered, satisfaction rate), and any institutional affiliations or press mentions**. If these do not exist yet, design Scene 08 to be forward-compatible — structured to add proof as the academy grows.

---

**Q11: Should workshops open in modals or dedicated pages?**

*Why it matters:* Modals keep the user in the immersive experience but limit SEO and shareability. Separate pages allow deep-linking and SEO optimization but break the flow.

*Recommendation:* **Hybrid.** On the landing page, a modal preview with key details and CTA is sufficient. Each workshop also has a canonical `/workshops/[slug]` page for SEO, direct linking, and full detail view. The landing page modal contains a "Full Details" link to the dedicated page.

---

**Q12: What is the client's timeline and budget for this project?**

*Why it matters:* The plan as designed is a Phase 0–10 build that could take 10–16 weeks for one full-stack team (creative + dev + 3D). An abbreviated timeline will require scope reduction.

*Recommendation:* If timeline is under 8 weeks, prioritize Scenes 01, 02, 05, 06, 07, and 10 (the highest-conversion scenes) and deliver the others as static editorial sections. The 3D can be added progressively in Phase 2 of the project.

---

**Q13: What must be avoided to maintain legal and professional credibility?**

*Why it matters:* The design and copy must not make claims the academy cannot support, use imagery that feels generic or stock, or adopt a tone that is either too casual or too self-promotional.

*Recommendation:* Define a content governance checklist: no unverified claims ("best legal training in the region"), no stock photography of courtrooms or robed judges, no copy that sounds like a law firm advertising pitch. Every claim must be backed by something real.

---

**Q14: Will there be a registration deadline or seasonal cohort model?**

*Why it matters:* A cohort model (seasonal registration) adds natural urgency to the conversion path and makes "limited seats" messaging feel authentic, not artificial.

*Recommendation:* If workshops run in cohorts, display the next cohort start date prominently in Scene 10 and in the Hero CTA. Countdown timers can be appropriate here if the deadline is genuine.

---

**Q15: What pages beyond the main landing are in scope for Phase 1?**

*Why it matters:* Additional pages multiply design, content, and development time significantly.

*Recommendation:* **Phase 1 scope: landing page + `/register` form + `/workshops/[slug]` template.** Everything else (About, Blog, Archive, Arabic locale) is Phase 2.

---

## 14. PHASED IMPLEMENTATION PLAN

---

### Phase 0 — Project Alignment & Input Collection

**Goal:** Gather all client inputs, confirm direction, align on scope and timeline before any production work begins.

| Task | Description | Deliverable | Priority | Complexity |
|------|-------------|-------------|----------|------------|
| **P0.01** Creative Brief Finalization | Confirm all brand details, target audience, tone, legal claim boundaries, and any existing brand guidelines. | Signed creative brief document | P0 | Low |
| **P0.02** Content Asset Inventory | Collect all existing: logo files (SVG/AI), instructor photos (or confirm photoshoot required), testimonials, workshop descriptions, proof points. Identify all gaps. | Content inventory spreadsheet | P0 | Low |
| **P0.03** Technical Environment Survey | Confirm hosting preference, domain status, existing Next.js codebase (if any), email/form infrastructure, WhatsApp number, analytics requirements. | Technical environment checklist | P0 | Low |
| **P0.04** Direction Lock Sign-off | Client reviews and approves this document (or revised version). No production begins without signed direction lock. | Signed direction lock document | P0 | Low |
| **P0.05** Timeline & Budget Confirmation | Confirm weeks available, developer hours, 3D production budget, photography budget, and milestone schedule. | Signed project schedule | P0 | Low |
| **P0.06** Open Questions Resolution | Work through the 15 questions in Section 13. Get definitive answers in writing. | Q&A resolution log | P0 | Low |

---

### Phase 1 — Research Synthesis & Direction Lock

**Goal:** Ensure the creative team fully understands the references, the audience, and the competitive context before designing anything.

| Task | Description | Deliverable | Priority | Complexity |
|------|-------------|-------------|----------|------------|
| **P1.01** Reference Website Analysis | Deep-dive into all five reference sites (Oryzo, KODE, Immersive Garden, Floema, Lenz & Staehelin). Extract specific techniques with screenshots, timing notes, and source-inspection notes. | Reference analysis report | P0 | Medium |
| **P1.02** Legal Education Competitor Audit | Review 5–8 regional legal education websites (law school continuing education, legal training firms, bar association courses). Document what they all have in common — these are exactly what Mithaq must not look like. | Competitor audit report | P0 | Medium |
| **P1.03** Target Audience Profile | Define 2–3 specific user personas: law graduate job-seeking, junior associate seeking skills, career-changer from adjacent field. Understand what each persona cares about, fears, and needs to see to convert. | Audience persona document | P0 | Medium |
| **P1.04** Device & Browser Target Matrix | Confirm primary browsers (likely Chrome/Safari mobile + Chrome desktop), OS distribution, and expected device quality range for the target audience (typically mid-tier Android + iPhone). This determines 3D performance targets. | Device matrix + performance calibration | P0 | Low |
| **P1.05** 3D Feasibility Benchmark | Build a minimal R3F prototype to validate that the target hero GLB loads and renders at acceptable performance on target mid-tier devices. Run on BrowserStack if physical devices unavailable. | Performance benchmark report | P0 | Medium |

---

### Phase 2 — Creative Concept Development

**Goal:** Define the complete visual, atmospheric, and motion identity of Mithaq before any development begins.

| Task | Description | Deliverable | Priority | Complexity |
|------|-------------|-------------|----------|------------|
| **P2.01** Dark Premium Moodboard | Curate 20–30 reference images covering: dark judicial interiors, legal desk photography, premium editorial design, gold embossing, seal design, cinematic legal film stills (tasteful). No horror, no cheesy legal clipart. | Figma moodboard | P0 | Low |
| **P2.02** Color Token System | Finalize all color tokens from Section 4.1. Generate contrast ratio table. Create dark and light test swatches. Validate all text passes AA contrast on primary backgrounds. | Color token file (Figma + CSS vars) | P0 | Low |
| **P2.03** Typography Specimen | Create a type specimen showing Cormorant Garamond at all used sizes and weights, DM Sans at all body/label sizes, JetBrains Mono for labels. Test Arabic pairing (Tajawal + Lemonada). Confirm web font WOFF2 loading sizes. | Typography specimen PDF | P0 | Low |
| **P2.04** 3D Art Direction Moodboard | Curate 15–20 references specifically for the 3D direction: gavel renders, judicial chamber environments, dark desk compositions, seal textures. Notes on camera angles, lighting, and material direction. | 3D art direction moodboard | P0 | Low |
| **P2.05** Opening Sequence Storyboard | Frame-by-frame storyboard of the 8.5-second opening sequence from Section 5. Each frame should show: what is in viewport, camera angle, which elements are visible, timing note. Minimum 12 frames. | Illustrated storyboard (Figma or drawn) | P0 | Medium |
| **P2.06** Scene Composition Sketches | Quick thumbnail composition sketches for Scenes 01–10. Not full designs — just layout direction, 3D element placement, and primary copy placement. | Scene thumbnail sketches × 10 | P0 | Medium |
| **P2.07** Motion Vocabulary Reference | Collect 5–8 motion references from reference sites that represent the desired easing and timing language. Create an annotated GSAP easing reference list. | Motion vocabulary reference doc | P1 | Low |

---

### Phase 3 — UX / IA / Storyflow Planning

**Goal:** Define the complete scroll experience, conversion path, and mobile UX before any visual design.

| Task | Description | Deliverable | Priority | Complexity |
|------|-------------|-------------|----------|------------|
| **P3.01** Information Architecture | Full IA document: all pages, routes, content types, and navigation. Include the i18n architecture if Arabic is in scope. | IA document | P0 | Low |
| **P3.02** 10-Scene Scroll Storyflow | Wireframe-level representation of the entire scroll experience. For each scene: scroll % trigger, 3D state, DOM content, primary CTA present. | Storyflow wireframe (Figma) | P0 | Medium |
| **P3.03** Conversion Funnel Map | Map the four conversion paths (WhatsApp, registration form, waitlist, inquiry) through each scene. Identify where each path is visible and accessible. | Conversion funnel map | P0 | Low |
| **P3.04** Mobile UX Adaptation Plan | For every scene, define the mobile-specific adaptation. Identify which 3D scenes are simplified, which are replaced with static, and which are fully removed on mobile. | Mobile UX adaptation document | P0 | Medium |
| **P3.05** Accessibility Requirements Specification | Document all accessibility requirements (from Section 11) in a testable format. For each requirement, include: expected behavior, test method, and pass/fail criteria. | Accessibility specification | P1 | Medium |
| **P3.06** Content Priority Matrix | For every scene, define: primary message (one sentence), primary CTA, secondary copy, and optional enrichment. This ensures that even if 3D is not rendered, the page communicates correctly. | Content priority matrix | P0 | Low |

---

### Phase 4 — Visual System & Art Direction

**Goal:** Produce the complete design system and scene-level visual compositions in Figma.

| Task | Description | Deliverable | Priority | Complexity |
|------|-------------|-------------|----------|------------|
| **P4.01** Design System Foundation | Build Figma component library: color tokens, type styles, spacing scale, icon set, button variants, card components, accordion, form inputs, navigation. | Figma design system | P0 | High |
| **P4.02** Scene-Level Visual Comps | Full-fidelity Figma compositions for each of the 10 scenes in desktop (1440px) and mobile (390px). These are the design contract for frontend implementation. | 20 Figma compositions (10 scenes × 2 breakpoints) | P0 | Very High |
| **P4.03** Opening Sequence Frame Comps | Keyframe compositions (at least 6) for the opening sequence showing exact visual state at key moments. Engineers reference these for R3F implementation. | 6+ opening keyframe comps | P0 | High |
| **P4.04** UI Micro-interaction Specs | Document all hover states, focus states, active states, loading states, and transition animations for every interactive element. | Micro-interaction spec document | P1 | Medium |
| **P4.05** Static Fallback Layout | Full editorial layout for users without WebGL — same 10 scenes as standard editorial content with hero static imagery. This must be beautiful, not a degraded fallback. | Static fallback Figma comp | P1 | High |
| **P4.06** Dark Texture & Material Library | Create or source: dark wood grain texture, aged parchment texture, gold foil texture, leather grain texture. These are used both in 3D materials and as CSS background textures in some sections. | Optimized texture library (WebP + KTX2) | P1 | Medium |

---

### Phase 5 — 3D Scene Planning & Technical Feasibility

**Goal:** Define all 3D assets required, produce them in Blender, and validate performance before full implementation.

| Task | Description | Deliverable | Priority | Complexity |
|------|-------------|-------------|----------|------------|
| **P5.01** 3D Asset Brief | Complete brief for every 3D asset: object description, reference images, polygon budget, texture budget, material spec (PBR inputs), and which scene it appears in. | 3D asset brief document | P0 | Medium |
| **P5.02** Gavel Model Production | Model, UV-unwrap, texture (PBR), and optimize the judicial gavel in Blender. Export as GLB. Optimize with gltfpack. Target: ≤ 1.2 MB compressed. | gavel.opt.glb | P0 | High |
| **P5.03** Mithaq Seal Model Production | Create the Mithaq Seal as a 3D circular embossed object in Blender. Design the seal itself (circular, calligraphic ميثاق, scales motif). | seal.opt.glb | P0 | High |
| **P5.04** Legal Desk Environment | Model the dark desk surface, desk edge, leather writing pad. Keep polygon count low — this is a background surface, not a hero object. | desk.opt.glb | P0 | High |
| **P5.05** Floating Documents (Scene 03) | 8 paper plane geometries with crumple normal maps, very low poly. These need to orbit in space — keep them under 500 tris each. | documents.opt.glb | P1 | Medium |
| **P5.06** Shader Development | Build and test all custom ShaderMaterials: ripple (Section 9.4), fracture lines, seal emergence, atmospheric particles. Test each in isolation in an R3F sandbox before integration. | Shader sandbox + shader files | P0 | Very High |
| **P5.07** R3F Architecture Proof of Concept | Build the full `MithaqCanvas`, `SceneManager`, and `Zustand` store skeleton without final assets. Validate that the architecture handles scene switching, scroll mapping, and reduced motion correctly. | R3F PoC codebase | P0 | High |
| **P5.08** Mobile Performance Audit | Run the Scene 01 GLB + shader on target mid-tier Android device (or BrowserStack equivalent). Measure FPS, memory usage, and load time. If below target, simplify assets. | Mobile performance report | P0 | High |
| **P5.09** Workshop Dossier 3D Cards | Simple 3D card/folder objects for Scene 06. 2,000 tris each maximum. These are for visual atmosphere only — real content in HTML overlay. | workshop-cards.opt.glb | P1 | Medium |

---

### Phase 6 — Content & Conversion Planning

**Goal:** Produce all copy, CTAs, and content assets needed for the 10 scenes. Content must be written, reviewed, and approved before implementation.

| Task | Description | Deliverable | Priority | Complexity |
|------|-------------|-------------|----------|------------|
| **P6.01** Hero Positioning Copy | Write, test, and finalize the hero headline, sub-headline, and CTA for Scene 02. A/B test 2–3 variants if possible. | Approved hero copy | P0 | Medium |
| **P6.02** Scene-by-Scene Copy | Write all copy for Scenes 01–10. Each scene needs: headline, body (max 80 words), CTA label, and any label/metadata text. | Copy deck document (all 10 scenes) | P0 | High |
| **P6.03** Arabic Translation / Localization | If Arabic locale is in scope, translate all approved copy into Arabic by a professional legal-sector translator (not general translator). Legal terminology must be precise. | Arabic copy deck | P0 | High |
| **P6.04** FAQ Copy | Write 10–15 FAQ entries answering real user questions. Tone: professional, direct, not corporate. | FAQ content | P0 | Medium |
| **P6.05** Workshop Card Content | For each workshop: title, format, level, 3 skill bullets, capacity, and CTA. Must be confirmed real workshops. | Workshop content cards | P0 | Medium |
| **P6.06** Instructor Bios | For each instructor: name, current role, 2-sentence bio, authority statement (one sentence), areas of expertise (tags). | Instructor content | P0 | Medium |
| **P6.07** SEO Meta Copy | Write title tags, meta descriptions, and OG content for all pages in scope. Legal education keywords research required. | SEO meta content | P1 | Low |
| **P6.08** Proof Points Collection | Collect and verify all numbers, testimonials, and institutional affiliations for Scene 08. Get written consent for testimonial publication. | Verified proof points | P0 | Medium |

---

### Phase 7 — Prototype Planning & Client Validation

**Goal:** Build an interactive prototype of the opening sequence and hero scene for client validation before full implementation.

| Task | Description | Deliverable | Priority | Complexity |
|------|-------------|-------------|----------|------------|
| **P7.01** Opening Sequence Prototype | R3F implementation of the gavel opening (Scenes 01) using placeholder/simple geometry if final assets are not ready. Test the full 8.5s timeline. | Interactive prototype | P0 | Very High |
| **P7.02** Hero Scene Prototype | Scene 02 with all DOM content, CTA, and typography in place. The hero represents the "above the fold" moment that most users will judge the site on. | Hero scene prototype | P0 | High |
| **P7.03** Scroll Choreography Prototype | Implement Lenis + GSAP ScrollTrigger for the first 3 scenes. Validate that scroll feels right, not sluggish or over-smooth. | Scroll choreography demo | P0 | High |
| **P7.04** Reduced Motion Prototype | Show the static fallback version of Scenes 01–02. Client must approve this version — it will be seen by a meaningful percentage of users. | Reduced motion demo | P1 | Medium |
| **P7.05** Mobile Prototype | Responsive version of Scenes 01–02 on mobile screen sizes. Confirm simplified 3D, typography scale, and CTA placement. | Mobile prototype | P0 | High |
| **P7.06** Client Prototype Review Session | Present the prototype to the client. Document all feedback in writing. Get sign-off before Phase 8 begins. | Signed prototype approval | P0 | Low |

---

### Phase 8 — Frontend Architecture & Full Implementation

**Goal:** Build the complete production website from approved designs and prototypes.

| Task | Description | Deliverable | Priority | Complexity |
|------|-------------|-------------|----------|------------|
| **P8.01** Next.js Project Setup | Initialize Next.js 14 (App Router), configure TypeScript, Tailwind CSS, import design tokens as CSS vars, set up ESLint + Prettier + Husky. | Production repository | P0 | Medium |
| **P8.02** Design System Implementation | Implement all design tokens (colors, type scale, spacing) in CSS custom properties. Build base component set: Button, Card, Accordion, Form Input, Nav. | Component library | P0 | High |
| **P8.03** Zustand Store + Hooks | Implement the full Zustand store from Section 9.3. Build all custom hooks: `useScrollProgress`, `useSceneProgress`, `useReducedMotion`, `useWebGLSupport`, `useDeviceTier`. | Store + hooks | P0 | Medium |
| **P8.04** Lenis + GSAP Integration | Set up Lenis smooth scroll, integrate with GSAP ticker, initialize ScrollTrigger. Create the global scroll progress tracker that feeds Zustand. | Scroll infrastructure | P0 | High |
| **P8.05** Global R3F Canvas | Build `MithaqCanvas`, `SceneManager`, `SharedEnvironment`, and `PostProcessing` from Section 9.1. Validate WebGL fallback. | Canvas architecture | P0 | High |
| **P8.06** Opening Sequence (Scene 01) | Full production implementation of the gavel opening with all shaders, particles, seal reveal, camera animation, and skip functionality. | Scene 01 production | P0 | Very High |
| **P8.07** Scene 02 — Hero | Hero scene with full DOM content, CTAs, typography, and background 3D state. | Scene 02 production | P0 | High |
| **P8.08** Scene 03 — The Gap | Floating documents system, DOM copy, transition into Scene 04. | Scene 03 production | P1 | High |
| **P8.09** Scene 04 — Mithaq Method | Desk materialization from document convergence, DOM content. | Scene 04 production | P1 | High |
| **P8.10** Scene 05 — Training Pillars | Premium card components, staggered reveal, DOM content for all 5 pillars. | Scene 05 production | P0 | Medium |
| **P8.11** Scene 06 — Workshops Preview | Workshop card system, modal implementation, Raycaster hover for 3D cards. | Scene 06 production | P0 | High |
| **P8.12** Scene 07 — Hall of Mentors | Mentor gallery, portrait treatment (CSS filter for monochrome + gold tone), card design. | Scene 07 production | P0 | Medium |
| **P8.13** Scene 08 — Trust & Credibility | Number counter animation, testimonial layout, proof point display. | Scene 08 production | P1 | Medium |
| **P8.14** Scene 09 — FAQ | Semantic accordion, keyboard navigation, ARIA implementation. | Scene 09 production | P0 | Low |
| **P8.15** Scene 10 — Final CTA | Seal/gavel callback, final CTA layout, all conversion paths (WhatsApp, form, waitlist). | Scene 10 production | P0 | Medium |
| **P8.16** Navigation & Header | Fixed nav with scroll state, mobile hamburger, language toggle, "Register" CTA. | Navigation production | P0 | Medium |
| **P8.17** Reduced Motion Mode | Full implementation of the static fallback experience. Test with OS-level reduced motion enabled. | Reduced motion complete | P0 | Medium |
| **P8.18** Arabic / RTL Support | If in scope: next.config.js i18n, `dir="rtl"`, CSS logical properties throughout, Arabic font loading, Arabic copy integration. | RTL implementation | P1 | High |
| **P8.19** Mobile Optimization Pass | Simplify or disable 3D on mobile where performance requires it. Verify all tap targets ≥ 44px. Verify text scales correctly. | Mobile polish | P0 | High |
| **P8.20** Static / WebGL Fallback | Full static fallback experience for WebGL-unavailable devices. Full editorial layout with hero poster. | Static fallback complete | P0 | Medium |

---

### Phase 9 — Accessibility, Performance & QA

**Goal:** Validate that the site meets all accessibility, performance, and quality requirements before launch.

| Task | Description | Deliverable | Priority | Complexity |
|------|-------------|-------------|----------|------------|
| **P9.01** Axe DevTools Audit | Run automated accessibility audit across all scenes. Zero critical violations permitted. Document all warnings and confirm intentional exceptions. | Axe audit report | P0 | Medium |
| **P9.02** Keyboard Navigation QA | Manually tab through the entire page. Every interactive element must be reachable and operable. Document and fix any keyboard traps or skip-focus issues. | QA report + fixes | P0 | Medium |
| **P9.03** Screen Reader QA | Test with VoiceOver (Safari/macOS) and NVDA (Windows/Chrome). Confirm that all semantic content is read in correct order and all interactive elements are announced correctly. | Screen reader QA report | P0 | Medium |
| **P9.04** Reduced Motion QA | Enable `prefers-reduced-motion: reduce` in OS settings. Confirm that the static fallback experience loads instead of all animations. | Reduced motion QA pass | P0 | Low |
| **P9.05** Lighthouse CI Setup | Configure Lighthouse CI to run on every pull request. Set budget gates: LCP < 2.5s, INP < 200ms, CLS < 0.1, Accessibility ≥ 95, Best Practices = 100. Fail builds that miss budgets. | Lighthouse CI pipeline | P0 | Medium |
| **P9.06** WebPageTest Audit | Run WebPageTest from target geographic region (ideally Cairo if regional audience). Confirm real-world LCP < 2.5s. Film strip review to ensure content appears early. | WebPageTest report | P0 | Low |
| **P9.07** Cross-Browser QA | Test in: Chrome latest, Safari 16+, Firefox latest, Samsung Internet (for Android market). Document and fix any rendering issues. | Cross-browser QA matrix | P0 | Medium |
| **P9.08** Mobile Device QA | Test on: iPhone 14 (Safari), iPhone 11 (Safari), Samsung Galaxy S21 (Chrome), Xiaomi mid-tier device (Chrome). 3D must maintain ≥ 30 FPS on mid-tier. | Mobile QA report | P0 | High |
| **P9.09** Performance Optimization Pass | After QA identifies performance gaps, implement fixes: further GLB optimization, texture compression, render loop optimizations, Suspense boundary improvements. | Optimization pass documentation | P0 | High |
| **P9.10** Content Final Review | Client reviews all live copy, instructor content, workshop content, and proof points in staging environment. Final approval before launch. | Signed content approval | P0 | Low |
| **P9.11** SEO Technical Audit | Confirm: canonical tags, meta titles/descriptions, OG images, robots.txt, sitemap.xml, structured data (Schema.org/EducationalOrganization), no broken links. | SEO technical audit | P1 | Medium |

---

### Phase 10 — Deployment & Launch

**Goal:** Deploy to production, configure monitoring, and manage the launch.

| Task | Description | Deliverable | Priority | Complexity |
|------|-------------|-------------|----------|------------|
| **P10.01** Vercel Production Setup | Configure production Vercel project: production domain, environment variables, build settings, cache headers (Section 12.5). | Production Vercel project | P0 | Low |
| **P10.02** CDN & Asset Configuration | Confirm all GLB and KTX2 assets are served with `Cache-Control: immutable`. Set up Vercel CDN headers for all `/models` and `/textures` paths. | CDN configuration | P0 | Low |
| **P10.03** Analytics Integration | Configure Vercel Analytics (or Google Analytics 4 if required). Set up custom events: `gavel_strike_complete`, `opening_skipped`, `cta_click`, `workshop_card_hover`, `whatsapp_click`. | Analytics live | P0 | Medium |
| **P10.04** Sentry Integration | Configure Sentry for runtime error tracking. Ensure canvas errors and shader compilation failures are caught and reported. | Sentry live | P1 | Low |
| **P10.05** Soft Launch (Stakeholder Review) | Deploy to production URL. Share with client and 3–5 internal stakeholders for a 48-hour review period. Collect final feedback. | Stakeholder review session | P0 | Low |
| **P10.06** Final Fixes & Polish | Address all stakeholder feedback from soft launch. Prioritize: copy edits, mobile issues, conversion path clarity. | Final fix list completed | P0 | Medium |
| **P10.07** Go-Live | Remove any maintenance mode, confirm DNS propagation, activate monitoring, and notify team. | Site live on production | P0 | Low |
| **P10.08** Post-Launch Monitoring (Week 1) | Monitor Sentry for errors, Vercel Analytics for performance regressions, and analytics for conversion funnel health. Address any critical issues within 24 hours. | Week-1 monitoring report | P0 | Low |

---

## 15. RISKS AND MITIGATION

| # | Risk | Why It Matters | Severity | Mitigation |
|---|------|---------------|----------|-----------|
| R01 | **Gavel opening feels violent or clichéd** | The opening is the make-or-break first impression. If it reads as aggressive, theatrical, or like a movie trailer, the legal authority frame is broken immediately. | Critical | Follow the storyboard timing precisely. The strike must be 0.08s maximum. No dramatic music without audio-off by default. Test with non-team viewers before client demo. |
| R02 | **Site becomes too game-like** | WebGL experiences risk sliding into gaming energy — interaction-first, narrative-second. If users are playing with the site rather than learning about Mithaq, conversion suffers. | High | Every scene must have visible DOM content and a clear primary message. 3D is never interactive for its own sake. No click-to-spin, no drag-to-explore without a purpose. |
| R03 | **Legal authority diluted by visual spectacle** | Too much visual effect can make Mithaq feel like a design studio or tech startup rather than a legal training institution. The 3D must serve the message, not compete with it. | High | Enforce the "does this serve the Mithaq message?" filter for every effect added. When in doubt, remove the effect. Copy and mentor credibility are more powerful trust signals than shaders. |
| R04 | **3D performance too heavy on target devices** | If the site runs at 15 FPS on a mid-tier Android phone, it communicates cheapness more than any design choice. The audience (law graduates, junior associates) likely has a mixed device profile. | Critical | Mandatory performance audit in Phase 5.08 before full implementation. Device tier detection in Phase 8.03. Mobile-simplified GLB assets. Never skip this. |
| R05 | **Mobile experience becomes weak or broken** | Mobile-first users (likely majority for this audience) get a broken or degraded experience. Most students browse on their phones, not workstations. | High | Phase 3.04 Mobile UX Adaptation Plan is mandatory, not optional. Every scene must have a tested mobile state. Phase 9.08 (device QA) is non-negotiable. |
| R06 | **Content hierarchy becomes unclear** | When 3D, motion, and copy compete for attention, none wins. The user ends up confused rather than informed. | High | Content Priority Matrix (Phase 3.06) defines the primary message for every scene. If the DOM content is unclear without the 3D, the scene has failed. |
| R07 | **Accessibility ignored under time pressure** | Accessibility is often cut when timelines tighten. This produces a site that fails professionally and, in some regions, legally. It also cuts out a meaningful percentage of potential users. | High | Axe CI gates (Phase 9.05) make accessibility failures block deployment. This cannot be deferred. It is a technical constraint, not a nice-to-have. |
| R08 | **Arabic / RTL typography breaks layout** | Mixing Cormorant Garamond (Latin) with Arabic fonts in RTL context without careful CSS logical property implementation produces broken layouts and misaligned elements. | Medium | Use CSS logical properties (`padding-inline`, `margin-block-start`) from day one. Test RTL in Phase 8.18 with a native Arabic reader, not just a text direction toggle. |
| R09 | **Conversion path unclear** | The most premium site fails if users cannot figure out how to register or contact Mithaq within 30 seconds. Cinematic experiences create distraction risk. | Critical | WhatsApp floating button is always visible. Primary CTA visible in Scene 02 (above the fold). FAQ answers "how do I register" explicitly. Conduct user testing in Phase 7.06 with target-audience members. |
| R10 | **Project scope expands without budget** | Without a locked Phase 1 scope, additional scenes, pages, features, and content requests push timelines and blow budgets. | High | Direction lock (Phase 0.04) defines exact scope. Every change request after sign-off is a formal scope addition with time and cost impact documented. |
| R11 | **Preloader blocks user entry** | A loading screen that runs longer than 5s before any content is visible creates abandonment, especially on mobile with slower connections. | High | Core text and CTA must be in DOM immediately. The canvas loads progressively. The atmospheric particles serve as a premium "loading indicator" so users feel progress. Implement and test under throttled (3G) network conditions. |
| R12 | **Site looks like a law firm instead of an academy** | Institutional typography and dark colors, if applied without the cinematic 3D layer, produce a law firm website, not a legal academy. The "expensive but also living" quality is critical. | Medium | Cormorant Garamond must appear alongside DM Sans, not alone. The scene numbering (01, 02…) communicates curriculum/program, not institution. Instructor section must feel like faculty, not partners. |
| R13 | **Poor instructor photography undermines credibility** | Scene 07 is a major trust-builder. Unprofessional headshots (phone selfies, uncontrolled backgrounds, bad lighting) will undermine all the premium design work around them. | High | Professional photography is a project deliverable, not optional. Include in client brief (Phase 0.02). Define the shot style brief using the dark-monochrome-gold direction. Block Scene 07 design on photo delivery. |
| R14 | **Shader compilation errors on certain GPU/driver combinations** | Custom GLSL can fail silently or crash on older mobile GPUs, leaving a black canvas or incorrect rendering. | Medium | Sentry integration (Phase 10.04) catches runtime shader errors. All shaders must have try/catch around shader compilation and fall back to a simpler material if compilation fails. |

---

## 16. FINAL RECOMMENDATION

Mithaq has a genuinely exceptional brief. The word "Mithaq" — covenant, charter, binding commitment — gives this project a conceptual foundation that most web projects never have. The name itself contains the story.

The recommended direction is **"The Covenant Seal"**: an experience that opens with the authority of the gavel strike and closes with the offering of the covenant — Mithaq's commitment to bridge legal study and professional readiness. The seal is not decoration. It is the brand's promise, made physical.

This plan is achievable, ambitious, and appropriate for the stated goal: to impress a serious client while remaining conversion-focused, accessible, and production-ready.

**Three principles to protect through every phase:**

1. **Authority before spectacle.** If the 3D is ever competing with the message, simplify the 3D, not the message. Mithaq's credibility comes from its instructors, its method, and its positioning — not from its shaders.

2. **Accessible by architecture, not afterthought.** The semantic HTML layer is the real content. The WebGL canvas is the cinematic atmosphere. One must be able to function without the other.

3. **Conversion is the measure of success.** A Mithaq website that earns Awwwards recognition but generates zero registrations has failed. Every beautiful decision must be justified by its service to the user's journey toward enrollment.

If these three principles are held to throughout all 10 phases, Mithaq will deliver a site that is genuinely rare in the legal education space — and entirely possible to build with the recommended stack and the plan documented here.

---

*Document prepared for: Mithaq Legal Academy*
*Status: Direction Lock — Ready for Client Alignment*
*Version: 1.0*
*Next step: Phase 0 kickoff — confirm open questions and begin asset inventory*

---
