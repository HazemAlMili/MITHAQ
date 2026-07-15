# MITHAQ — Execution Instructions

## 1. How to Use This File

Read this file first for every future Mithaq task.

Do not read the full `mithaq-project-docs/` tree by default. It is large, repetitive, and includes historical drafts, validation artifacts, captures, sandboxes, and superseded planning material. Use Section 14 to choose the smallest set of extra files for the task in front of you.

When older documents conflict with this file, prefer this file unless a newer approved ticket output exists. Do not assume a condition is resolved without source evidence. If a client input is still marked missing, treat it as missing.

Source priority:

```text
Latest approved ticket output
→ Latest completion report
→ Phase-level locked specification
→ Direction Lock
→ Older planning documents
```

Preserve all existing documentation and assets. Do not move, delete, rename, archive, or overwrite prior outputs unless a future ticket explicitly asks for that.

## 2. Project Identity and Scope

Mithaq / ميثاق is a premium bilingual legal academy portfolio and landing experience. It presents practical legal training for professional readiness, especially for law graduates, junior lawyers, and early-career legal professionals.

Current positioning:

```text
Practical Legal Training for Professional Readiness
```

Primary conversion: WhatsApp inquiry.  
Secondary conversion: simple three-field inquiry/register-interest form.  
Confirmed MVP routes: `/`, `/register`, and `/workshops/[slug]` as a template-only route until workshop content is verified.

Mithaq is not:

- an LMS
- a dashboard
- a course marketplace
- a law firm website
- a payment, booking, cohort, or seat-count platform
- a source of legal advice
- a site that may use unsupported proof, urgency, credentials, certificates, outcomes, testimonials, or partner claims

## 3. Locked Creative Direction

Core concept: **The Covenant Seal**.

The gavel is the ceremonial trigger. The Seal is the brand hero and recurring motif. The experience should feel like symbolic realism inside a dark judicial chamber: dark wood, leather, parchment, muted brass/gold, warm directional light, and restrained cinematic presence.

Creative rules:

- Authority before spectacle.
- 3D serves content and conversion.
- The Seal leads the brand story; the gavel must not become the hero.
- Motion is slow, weighted, controlled, and decisive.
- Avoid bounce, jiggle, neon, sci-fi holograms, horror lighting, explosions, fantasy magic, game-like UI, and decorative interaction without purpose.
- DOM content and CTAs must carry the meaning even when WebGL, motion, hover, audio, or shaders are unavailable.

## 4. Scene 01–10 Map

| Scene | Name | Purpose | Primary Content Source | Main 3D / Visual Responsibility | Current Readiness |
| --- | --- | --- | --- | --- | --- |
| 01 | Gavel Seal Opening | Establish Mithaq's identity and ceremonial tone. | `mithaq-project-docs/mithaq-scene-copy/scene-copy-master.md` | Gavel descent/strike, ripple, Seal reveal setup. | Visual/keyframe planning exists; mobile must use lightweight/static path. |
| 02 | Hero / Mithaq Reveal | Explain what Mithaq is, who it serves, and the next action. | `mithaq-project-docs/mithaq-hero-positioning-copy/approved-hero-copy.md` | Seal as hero anchor with readable DOM overlay. | Recommended for client approval, not final client-approved. |
| 03 | The Gap | Show the gap between academic legal education and professional expectations. | `mithaq-project-docs/mithaq-scene-copy/scene-copy-master.md` | Floating legal/academic document fragments. | Copy and documents asset exist with conditions. |
| 04 | The Mithaq Method | Explain how Mithaq turns knowledge into practical capability. | `mithaq-project-docs/mithaq-scene-copy/scene-copy-master.md` | Organized legal desk/method transition. | Safe method copy exists; practitioner wording depends on instructor approval. |
| 05 | Training Pillars | Define capability areas developed through training. | `mithaq-project-docs/mithaq-scene-copy/scene-copy-master.md` | Five capability/pillar visual system. | Source copy exists; no workshop mapping is public-ready. |
| 06 | Workshops Preview | Introduce training engagements without inventing workshop content. | `mithaq-project-docs/mithaq-workshop-content/workshop-content-master.md` | Workshop dossier assets as atmospheric 3D support. | No confirmed public workshop inventory; schema only. |
| 07 | Hall of Mentors | Establish instructor credibility without invented bios or credentials. | `mithaq-project-docs/mithaq-instructor-content/instructor-content-master.md` | Mentor/professional presence placeholders. | No confirmed instructor inventory, portraits, credentials, or consent; schema only. |
| 08 | Trust & Credibility | Support confidence through verified proof or honest pre-launch trust state. | `mithaq-project-docs/mithaq-proof-points/publishable-proof-copy.md` | Proof cards/logos/counters only after verification. | No verified publishable proof; use pre-launch trust state. |
| 09 | FAQ | Resolve practical objections before contact. | `mithaq-project-docs/mithaq-faq-copy/faq-copy-master.md` | FAQ visual/supporting scene only. | FAQ structure complete; operational answers conditioned on client input. |
| 10 | Final CTA | Convert interest into WhatsApp or register-interest action. | `mithaq-project-docs/mithaq-scene-copy/scene-copy-master.md` | Final Seal/gavel covenant callback. | Copy exists; final WhatsApp number, form destination, and legal language pending. |

Official scroll map from P5.07:

```text
01: 0.00–0.10
02: 0.10–0.22
03: 0.22–0.37
04: 0.37–0.50
05: 0.50–0.62
06: 0.62–0.72
07: 0.72–0.82
08: 0.82–0.88
09: 0.88–0.94
10: 0.94–1.00
```

Do not renumber, merge, or add scenes without a new approved roadmap decision.

## 5. UX and Conversion Rules

- WhatsApp is the primary conversion path.
- The secondary path is a short three-field inquiry/register-interest form.
- Use “Ask About...” or “Register Interest” language until registration availability is confirmed.
- Do not use “Register Now,” countdowns, seat counters, fake urgency, payment flows, booking flows, or cohort/deadline logic.
- Content must remain understandable without WebGL, motion, hover, sound, or scroll choreography.
- No forced long preloader. Users must be able to access meaningful content and CTAs in fallback modes.
- Workshop details, mentor details, FAQ answers, proof, and conversion copy must be semantic HTML in production, not baked into GLB/canvas assets.
- Keep first-contact forms simple. Do not add complex qualification flows unless a future ticket approves them.

## 6. Visual, 3D, and Motion Rules

Approved visual language:

- dark legal chamber / dark desk
- dark wenge/walnut wood
- aged dark leather
- parchment paper
- muted brass/gold: `#C4913A`, highlight `#E8C97A`, shadow `#8B6420`
- warm key light from upper-left
- restrained rim/highlight treatment

3D and motion status:

- Gavel: produced as a real Blender/GLB asset; ceremonial trigger only.
- Seal: produced as a real Blender/GLB asset; primary hero object, pending final wordmark/calligraphy/stakeholder approval.
- Desk: produced as a separate dark legal desk environment; stage only, not hero.
- Floating documents: produced as eight separate lightweight document assets; Scene 03 only unless future scope says otherwise.
- Shaders: isolated sandbox exists for ripple, controlled fracture lines, Seal emergence, and atmospheric particles. No production integration has started.
- Workshop dossiers: produced as lightweight Scene 06 atmospheric assets. They do not contain real workshop content.

Asset reuse rules:

- Keep assets independently addressable.
- Use shared materials and instancing where practical.
- Do not bake workshop, instructor, CTA, certificate, legal, or proof text into GLBs.
- Do not import all Phase 5 assets into mobile by default.
- Do not increase particles, post-processing, shader effects, or camera choreography until the mobile performance limitation is resolved.

Reference reports are listed in Sections 12 and 18.

## 7. Technical Architecture

P5.07 validates an isolated Vite + React + TypeScript + Three.js + React Three Fiber + Drei + Zustand proof of concept.

Locked architecture direction:

- persistent full-viewport `MithaqCanvas`
- `SceneManager` switches scene modules without remounting the whole canvas
- Zustand store skeleton with `activeScene`, `scrollProgress`, `sceneProgress`, opening state, loading placeholders, reduced motion, WebGL availability, device tier, language, nav/modal, and CTA source
- global scroll progress and scene-local progress from the official scene map
- reduced-motion detection and manual override
- WebGL/WebGL2 fallback detection
- device-tier detection affecting DPR and optional post-processing
- `PostProcessingGate` must disable expensive effects for low tier and reduced motion

Current PoC status: PASS WITH CONDITIONS. It mounted the canvas, rendered all 10 proxies, passed build, produced captures, and had no runtime console errors in local Chromium headless validation.

Production constraints:

- Final Next.js architecture is still pending.
- Production routing is not implemented.
- Production Lenis/ScrollTrigger integration is not implemented.
- Production GLB and shader integration are not implemented.
- The isolated P5.07 build warned about a large Three/R3F/Drei chunk: `993.17 kB / gzip 274.63 kB`. Phase 8 must plan dynamic imports, route-level splitting, manual chunks, and asset loading strategy.

## 8. Mobile, Performance, and Fallback Rules

P5.08 mobile audit status: **FAIL**.

Do not miss this: real-asset mobile WebGL readiness is not approved.

P5.08 verdict:

- Representative Scene 01 real-asset WebGL workload failed the hard mobile floor in local mobile emulation / SwiftShader-like headless conditions.
- Mid-tier mobile emulation averaged `18.26–20.73 FPS`; verdict FAIL.
- Low-tier mobile emulation averaged `13.94–30.17 FPS`; overall verdict FAIL despite one passing run.
- Reduced-motion real-asset path averaged `12.15–14.66 FPS`; verdict FAIL.
- WebGL fallback path reached `60.00 FPS`; verdict PASS.
- Optimized gavel + Seal + desk GLB payload is small, approximately `161 KB`; the problem is runtime/rendering stability, not GLB file size.
- Physical-device validation remains unavailable.

Mobile rules:

- Use fallback/static/lightweight opening on mobile until a simpler Scene 01 workload passes a new audit on real devices.
- WebGL fallback is mandatory.
- Reduced motion must avoid expensive hidden workloads; do not keep real-asset rendering running invisibly.
- Do not treat emulator/headless data as physical-device approval.
- Do not increase mobile 3D complexity, particles, post-processing, shader effects, or camera choreography before re-audit.
- Low-tier mobile may use static poster imagery, DOM-first content, or very lightweight proxy states.

P5.09 dossier mobile note: mobile-light dossier assets passed isolated sandbox checks, but they are not approved for the complete mobile runtime because P5.08 failed.

## 9. Accessibility and RTL Rules

Accessibility requirements:

- Main meaning must be semantic DOM content.
- Canvas objects are decorative/symbolic unless explicitly paired with accessible DOM text.
- CTAs must be keyboard accessible and visible in fallback modes.
- Use visible focus states.
- No essential information may require hover, 3D, animation, counters, or audio.
- Reduced-motion mode must keep content equivalent and avoid rapid transitions, flashing, or hidden heavy work.
- WebGL fallback must provide the active scene context and CTA access.

RTL / Arabic requirements:

- Arabic pages/components must use `dir="rtl"` where appropriate.
- Use CSS logical properties: `margin-inline`, `padding-inline`, `inset-inline`, `text-align: start`.
- Avoid hard-coded left/right layout assumptions.
- Keep Arabic and English as separate localizable strings.
- Watch mixed-direction text for numbers, Latin route segments, `WebGL`, `RTL`, WhatsApp, and placeholders.
- Arabic should read naturally, not as literal English translation.

## 10. Approved Content Sources

Do not duplicate detailed copy in implementation tickets. Read the relevant source file.

Critical orientation copy:

- English hero eyebrow: `Mithaq Legal Academy`
- English hero headline: `Practical Legal Training for Professional Readiness`
- English hero CTA: `Ask About Mithaq Workshops`
- English secondary CTA: `Discover the Mithaq Method`
- Arabic brand: `ميثاق`
- Primary WhatsApp destination remains `WHATSAPP_NUMBER_PENDING`.

Source-of-truth files:

| Content Area | Source File |
| --- | --- |
| Hero English/Arabic package | `mithaq-project-docs/mithaq-hero-positioning-copy/approved-hero-copy.md` |
| Scene 01–10 English source copy | `mithaq-project-docs/mithaq-scene-copy/scene-copy-master.md` |
| English mobile variants | `mithaq-project-docs/mithaq-scene-copy/mobile-copy-variants.md` |
| Scene copy dependencies | `mithaq-project-docs/mithaq-scene-copy/content-dependency-register.md` |
| Arabic localization | `mithaq-project-docs/mithaq-arabic-localization/arabic-scene-copy-master.md` |
| Arabic mobile variants | `mithaq-project-docs/mithaq-arabic-localization/arabic-mobile-variants.md` |
| Arabic glossary | `mithaq-project-docs/mithaq-arabic-localization/localization-glossary.md` |
| FAQ copy | `mithaq-project-docs/mithaq-faq-copy/faq-copy-master.md` |
| Workshop content schema | `mithaq-project-docs/mithaq-workshop-content/workshop-content-master.md` |
| Instructor content schema | `mithaq-project-docs/mithaq-instructor-content/instructor-content-master.md` |
| SEO metadata | `mithaq-project-docs/mithaq-seo-copy/seo-meta-master.md` |
| Dynamic metadata templates | `mithaq-project-docs/mithaq-seo-copy/dynamic-metadata-templates.md` |
| Proof / pre-launch trust state | `mithaq-project-docs/mithaq-proof-points/publishable-proof-copy.md` |

## 11. Workshop, Instructor, FAQ, Proof, and SEO Status

Workshops:

- No confirmed public workshop inventory exists.
- P6.05 produced taxonomy, schema, conversion copy patterns, and one internal non-publishable template.
- No workshop cards may publish without verified title, audience, level, skills, format, duration, language, certificate policy, pricing/inquiry status, availability, and instructor relation.

Instructors:

- No confirmed instructor profiles, bios, portraits, credentials, expertise, quotes, or publication consent exist.
- P6.06 produced schema and dependency tracking only.
- Do not create mentor cards, names, roles, years of experience, expertise tags, or portraits until verified.

FAQ:

- P6.04 produced bilingual FAQ content.
- Some audience/positioning answers are ready for client approval.
- Operational answers remain conditioned on workshop format, duration, certificate, recordings, single-workshop policy, WhatsApp number, and form destination.

Proof:

- No verified publishable proof exists.
- Scene 08 uses `Pre-Launch Trust State — No Public Proof Available` from P6.08.
- Do not publish counters, testimonials, ratings, logos, affiliations, certificates, accreditations, “trusted by,” “leading,” or “proven” claims.

SEO:

- `/` and `/register` metadata are prepared for client review.
- `/workshops/[slug]` is template-only and must remain `noindex` until verified workshop content exists.
- `/about`, `/instructors`, `/workshops`, `/privacy`, and other routes are deferred or not approved.
- Do not implement `Review`, `AggregateRating`, `Event`, `Offer`, `CourseInstance`, `Course`, or `Person` schema until required verified content exists.

## 12. Asset Inventory and Approval Status

| Asset | Phase | Location | Status | Production Limitation |
| --- | --- | --- | --- | --- |
| Gavel | P5.02 | `mithaq-project-docs/mithaq-gavel-model-production/` | PASS WITH CONDITIONS | Blender/GLB exists; optimized via Blender Draco because `gltfpack` unavailable; stakeholder art approval, R3F import, mobile LOD, real-device validation pending. |
| Mithaq Seal | P5.03 | `mithaq-project-docs/mithaq-seal-model-production/` | PASS WITH CONDITIONS | Real Seal asset exists; Arabic text uses workaround; final calligraphy/wordmark/stakeholder approval, R3F import, mobile validation pending. |
| Legal desk | P5.04 | `mithaq-project-docs/mithaq-desk-environment-production/` | PASS WITH CONDITIONS | Desk GLB exists; material approval, KTX2, ripple shader validation, R3F import, real-device validation pending. |
| Floating documents | P5.05 | `mithaq-project-docs/mithaq-floating-documents-production/` | PASS WITH CONDITIONS | Eight assets exist; orbit/convergence behavior and R3F import pending. |
| Shader sandbox | P5.06 | `mithaq-project-docs/mithaq-shader-development/` | PASS WITH CONDITIONS | Shaders compile in sandbox; production integration, mobile profiling, and final performance validation pending. |
| R3F architecture PoC | P5.07 | `mithaq-project-docs/mithaq-r3f-architecture-poc/` | PASS WITH CONDITIONS | Persistent-canvas architecture validated; final Next.js architecture, production code splitting, GLB/shader integration, browser/mobile validation pending. |
| Mobile performance audit | P5.08 | `mithaq-project-docs/mithaq-mobile-performance-audit/` | FAIL | Real-asset mobile WebGL path failed; fallback passed. Mobile WebGL readiness not approved. |
| Workshop dossiers | P5.09 | `mithaq-project-docs/mithaq-workshop-dossier-assets/` | PASS WITH CONDITIONS | Desktop/mobile-light GLBs exist; isolated validation only; final Seal artwork, KTX2, real-device validation, production Scene 06 integration pending. |
| Texture/material references | P4.06 | `mithaq-project-docs/mithaq-dark-texture-material-library/` | PASS WITH CONDITIONS | Material direction exists; final texture pipeline/KTX2 still conditional. |
| Static/fallback references | Phase 4/P5.08 | `mithaq-project-docs/mithaq-static-fallback-layout/`; `mithaq-project-docs/mithaq-mobile-performance-audit/` | Required fallback path | Must be used for mobile/low-tier/reduced-motion until WebGL path passes. |

Key asset metrics:

- Gavel optimized GLB: `89,480 bytes`; `15,084` triangles.
- Seal optimized GLB: `57,588 bytes`; `8,578` triangles.
- Desk optimized GLB: `14,228 bytes`; `1,040` triangles.
- Floating documents optimized GLB: `28,652 bytes`; `760` triangles.
- Workshop dossier desktop optimized GLB: `17,544 bytes`; `1,480` triangles.
- Workshop dossier mobile optimized GLB: `8,304 bytes`; `420` triangles.

Small file sizes do not override the P5.08 runtime failure.

## 13. Global Do / Do Not

Do:

- Use verified sources.
- Preserve Scene 01–10 numbering.
- Keep content semantic and accessible.
- Measure before optimizing.
- Build mobile and fallback paths intentionally.
- Respect bilingual parity.
- Keep tickets context-friendly.
- List created and modified files.
- Stay within the active roadmap ticket.
- Preserve prior evidence, reports, and assets.

Do not:

- Invent content, workshops, instructors, proof, dates, prices, capacity, certificates, accreditations, testimonials, or outcomes.
- Start later tickets.
- Rewrite locked direction without approval.
- Add routes or features outside scope.
- Treat placeholders as live content.
- Hide performance problems.
- Claim mobile readiness without physical-device evidence.
- Read the entire documentation tree unnecessarily.
- Delete previous evidence.
- Modify production or PoC code during planning/content tasks.

## 14. Required Reading by Task Type

Copy task:

- `MITHAQ-INSTRUCTIONS.md`
- Relevant content master from Section 10
- Relevant dependency register

Arabic / localization task:

- `MITHAQ-INSTRUCTIONS.md`
- `mithaq-project-docs/mithaq-arabic-localization/localization-glossary.md`
- Relevant English source master
- Relevant Arabic handoff file

3D asset task:

- `MITHAQ-INSTRUCTIONS.md`
- Relevant asset report/handoff in Section 12
- `mithaq-project-docs/mithaq-3d-asset-brief/`
- `mithaq-project-docs/mithaq-mobile-performance-audit/reports/final-mobile-performance-report.md`

Scene implementation:

- `MITHAQ-INSTRUCTIONS.md`
- The scene's content source from Section 4
- Relevant visual/asset source from Section 12
- `mithaq-project-docs/mithaq-r3f-architecture-poc/reports/r3f-handoff-notes.md`
- `mithaq-project-docs/mithaq-mobile-performance-audit/reports/final-mobile-performance-report.md`

Mobile/performance task:

- `MITHAQ-INSTRUCTIONS.md`
- `mithaq-project-docs/mithaq-mobile-performance-audit/reports/final-mobile-performance-report.md`
- `mithaq-project-docs/mithaq-mobile-performance-audit/data/performance-summary.csv`
- Relevant lightweight asset handoff

SEO task:

- `MITHAQ-INSTRUCTIONS.md`
- `mithaq-project-docs/mithaq-seo-copy/seo-meta-master.md`
- `mithaq-project-docs/mithaq-seo-copy/indexing-and-schema-register.md`
- Current route/content readiness from Sections 10 and 11

Proof/trust task:

- `MITHAQ-INSTRUCTIONS.md`
- `mithaq-project-docs/mithaq-proof-points/proof-point-register.md`
- `mithaq-project-docs/mithaq-proof-points/proof-dependency-register.md`
- Source evidence supplied by the client, if any

Workshop content task:

- `MITHAQ-INSTRUCTIONS.md`
- `mithaq-project-docs/mithaq-workshop-content/workshop-content-master.md`
- `mithaq-project-docs/mithaq-workshop-content/workshop-dependency-register.md`
- New verified client workshop inventory, if supplied

Instructor content task:

- `MITHAQ-INSTRUCTIONS.md`
- `mithaq-project-docs/mithaq-instructor-content/instructor-content-master.md`
- `mithaq-project-docs/mithaq-instructor-content/instructor-dependency-register.md`
- New verified instructor profiles/consent, if supplied

QA task:

- `MITHAQ-INSTRUCTIONS.md`
- Relevant acceptance criteria from the active ticket
- Latest build, validation, or source evidence for the scope being checked

## 15. Current Roadmap Status

| Phase / Ticket | Status | Notes |
| --- | --- | --- |
| P0 foundations | Completed with conditions | Core decisions recorded; many client inputs remain open. |
| P1 research/audience | Completed with conditions | Audience and competitor direction available. |
| P2 creative concept | Completed with conditions | Covenant Seal, opening, motion, and 3D direction locked but asset approvals remain. |
| P3 UX/conversion planning | Completed with conditions | IA, storyflow, mobile UX, accessibility, and content priority available. |
| P4 visual system/art direction | Completed with conditions | Design system, comps, opening frames, materials, micro-interactions, fallback plans available. |
| P5.01–P5.07 | PASS WITH CONDITIONS | Assets, shaders, and R3F architecture PoC exist; production integration pending. |
| P5.08 | FAIL | Real-asset mobile runtime failed; fallback path passed. |
| P5.09 | PASS WITH CONDITIONS | Dossier assets exist; isolated only, not mobile-runtime approved. |
| P6.01–P6.08 | PASS WITH CONDITIONS | Content packages exist; major client inputs still missing. |
| P6.09 | Completed by this file | Phase 6 planning lock source of truth created. |
| Phase 7 | Not started | Next official step is P7.01. |

Phase 6 planning is locked to the decisions and conditions in this file. Do not create P7.01 here.

## 16. Open Dependencies and Client Inputs

| Dependency | Affected Scenes / Tasks |
| --- | --- |
| Final brand/logo/Seal approval | Scenes 01, 02, 08, 10; Seal asset; SEO OG image |
| WhatsApp number and response owner | Scenes 02, 06, 09, 10; `/register`; all CTAs |
| Form destination, privacy, consent language | Scenes 02, 10; `/register`; data collection |
| Confirmed workshop inventory | Scene 06; `/workshops/[slug]`; FAQ; SEO; proof |
| Workshop format, duration, price, recording, capacity, level, language, location | Scene 06; FAQ; SEO templates |
| Certificate/accreditation policy and wording | Scenes 06, 08, 09; SEO/schema; proof |
| Instructor profiles, roles, bios, expertise, credentials | Scenes 04, 07, 08; instructor schema |
| Instructor portraits and publication consent | Scene 07; future Person schema |
| Testimonial consent and source wording | Scene 08; proof; SEO/review restrictions |
| Verified proof points and calculation records | Scene 08; schema; trust modules |
| Partner/sponsor/logo permissions | Scene 08; SEO/social proof |
| Domain, canonical, locale, and hreflang strategy | SEO; routing; metadata |
| Final OG image | SEO/social sharing |
| Physical-device access | Mobile validation; P5.08 re-audit; Phase 7/8 decisions |
| KTX2 / texture pipeline and gltfpack availability | 3D asset production/integration |
| Hosting and production access | Deployment and production QA |

## 17. Superseded Guidance

Old Guidance: Scene 08 headline and evidence slots could imply verified evidence modules.  
Source: `mithaq-project-docs/mithaq-scene-copy/scene-copy-master.md`  
Superseded By: P6.08 proof audit.  
Current Decision: No publishable proof exists; use `Pre-Launch Trust State — No Public Proof Available` until verified proof and approvals exist.

Old Guidance: Conceptual workshop examples or training pillars could become workshop cards.  
Source: Older planning and pillar materials.  
Superseded By: P6.05 Workshop Card Content.  
Current Decision: No confirmed workshop inventory; only internal non-publishable schema exists.

Old Guidance: Conceptual instructor/mentor section could imply public profiles.  
Source: Older Scene 07 planning.  
Superseded By: P6.06 Instructor Bios.  
Current Decision: No public instructor profiles, portraits, credentials, or consent exist.

Old Guidance: Mobile WebGL could proceed from lightweight asset sizes alone.  
Source: Pre-P5.08 feasibility assumptions.  
Superseded By: P5.08 Mobile Performance Audit.  
Current Decision: Real-asset mobile runtime failed; fallback/static/lightweight path is mandatory until re-audit.

Old Guidance: `/workshops/[slug]` could be treated as a publishable page.  
Source: IA and SEO route planning.  
Superseded By: P6.05 and P6.07.  
Current Decision: Route remains template-only and `noindex` until workshop inventory is verified.

Old Guidance: Instructor pages or `/instructors` route could be prepared as public metadata.  
Source: Early IA considerations.  
Superseded By: P0.06, P6.06, and P6.07.  
Current Decision: Instructor pages are deferred/not approved; no Person schema until verified profiles and consent exist.

Old Guidance: Registration could imply booking, payment, seats, cohort, or deadline.  
Source: Early conversion options.  
Superseded By: P0.06 conversion decisions and P6 copy.  
Current Decision: WhatsApp inquiry is primary; simple register-interest form is secondary; no operational registration system in MVP.

## 18. Source Reference Index

| Topic | Authoritative File | Use When |
| --- | --- | --- |
| Open decisions and credibility boundaries | `mithaq-project-docs/mithaq-open-questions/mithaq-open-questions-resolution-log.md` | Checking locked strategic decisions or unresolved client inputs. |
| Content/asset gaps | `mithaq-project-docs/mithaq-content-assets/11-audit-report/mithaq-content-assets-gap-report.md` | Verifying missing content, proof, workshops, instructors, and compliance items. |
| Hero copy | `mithaq-project-docs/mithaq-hero-positioning-copy/approved-hero-copy.md` | Implementing or reviewing Scene 02. |
| Scene copy | `mithaq-project-docs/mithaq-scene-copy/scene-copy-master.md` | Implementing/reviewing English Scene 01–10 copy. |
| Arabic localization | `mithaq-project-docs/mithaq-arabic-localization/arabic-scene-copy-master.md` | Implementing/reviewing Arabic copy. |
| Arabic terminology | `mithaq-project-docs/mithaq-arabic-localization/localization-glossary.md` | Choosing Arabic terms. |
| FAQ | `mithaq-project-docs/mithaq-faq-copy/faq-copy-master.md` | Implementing/reviewing Scene 09. |
| Workshop content | `mithaq-project-docs/mithaq-workshop-content/workshop-content-master.md` | Handling Scene 06 content schema. |
| Instructor content | `mithaq-project-docs/mithaq-instructor-content/instructor-content-master.md` | Handling Scene 07 content schema. |
| SEO | `mithaq-project-docs/mithaq-seo-copy/seo-meta-master.md` | Metadata copy/spec work. |
| Schema/indexing | `mithaq-project-docs/mithaq-seo-copy/indexing-and-schema-register.md` | Route and schema readiness. |
| Proof/trust | `mithaq-project-docs/mithaq-proof-points/publishable-proof-copy.md` | Scene 08 current public-safe state. |
| Gavel | `mithaq-project-docs/mithaq-gavel-model-production/gavel-r3f-handoff-notes.md` | Gavel import/animation handoff. |
| Seal | `mithaq-project-docs/mithaq-seal-model-production/reports/seal-r3f-handoff-notes.md` | Seal import/reveal handoff. |
| Desk | `mithaq-project-docs/mithaq-desk-environment-production/reports/desk-r3f-handoff-notes.md` | Desk import/ripple anchor handoff. |
| Floating documents | `mithaq-project-docs/mithaq-floating-documents-production/reports/documents-r3f-handoff-notes.md` | Scene 03 document behavior handoff. |
| Shaders | `mithaq-project-docs/mithaq-shader-development/reports/shader-r3f-handoff-notes.md` | Shader integration planning. |
| R3F architecture | `mithaq-project-docs/mithaq-r3f-architecture-poc/reports/r3f-handoff-notes.md` | Scene implementation architecture. |
| Mobile performance | `mithaq-project-docs/mithaq-mobile-performance-audit/reports/final-mobile-performance-report.md` | Any mobile/WebGL decision. |
| Workshop dossiers | `mithaq-project-docs/mithaq-workshop-dossier-assets/reports/dossier-handoff-notes.md` | Scene 06 dossier asset use. |
