# Mithaq 3D Asset Brief

**Official Ticket ID:** P5.01  
**Official Ticket Name:** 3D Asset Brief  
**Phase:** Phase 5 - 3D Scene Planning & Technical Feasibility  
**Priority:** P0  
**Complexity:** Medium  
**Owner:** 3D Art Director / Technical Art Lead  
**Status:** PASS WITH CONDITIONS  
**Prepared date:** 2026-06-20  

---

## 1. Executive Summary

This document is Mithaq's official 3D asset brief. It defines the required 3D asset set before Blender production begins, including purpose, scene usage, geometry budgets, texture budgets, PBR material direction, export targets, performance constraints, mobile/reduced-motion behavior, fallback equivalents, and QA acceptance criteria.

Primary 3D direction:

**Seal-Led Macro Legal Chamber**

The Seal is the hero object. The gavel is the ceremonial trigger. The desk is the legal stage. Documents, dossiers, particles, and accents support the story only when they improve clarity without competing with DOM content or conversion.

This task is briefing only. It does not create GLB files, Blender files, shaders, R3F implementation, KTX2 conversion, frontend integration, final seal/logo approval, final content, or new roadmap tickets.

---

## 2. Current Mithaq 3D Direction

| Area | Direction |
| --- | --- |
| Product type | Premium 3D legal academy portfolio / landing experience. |
| Core concept | The Covenant Seal. |
| Hero object | Mithaq Seal. |
| Trigger object | Judicial gavel. |
| World | Dark legal chamber, legal desk, parchment, gold/brass, leather, restrained dust. |
| Motion | Scroll-Led Ceremonial Restraint. |
| Content model | DOM-first; canvas is enhancement only. |
| Conversion | WhatsApp primary, `/register` secondary. |
| Mobile | Full 3D not required for all scenes. |
| Fallback | Static fallback preserves meaning. |
| Reduced motion | Static/poster equivalents preserve meaning. |
| Forbidden | Fantasy, magic, cartoon, sci-fi hologram, LMS/dashboard objects, courtroom cliche overload, fake content. |

---

## 3. Delivery Status

| Deliverable | Status | Notes |
| --- | --- | --- |
| 3D asset brief document | PASS | This document is the official P5.01 brief. |
| Asset inventory | PASS | Required asset families 3D-001 through 3D-014 are listed. |
| Polygon/triangle budgets | PASS | Included per asset and globally. |
| Texture budgets | PASS | Included per asset, with P4.06 KTX2 condition carried forward. |
| PBR specs | PASS | Included per asset. |
| Scene mapping | PASS | Scene-to-asset map included. |
| Mobile/fallback behavior | PASS | Included per asset and in global table. |
| Export/naming targets | PASS | Stable output names defined. |
| Blender production | Not started | Correctly out of scope. |
| GLB files | Not created | Correctly out of scope. |
| R3F/shader/frontend implementation | Not started | Correctly out of scope. |

Status remains **PASS WITH CONDITIONS** because final seal/logo approval, KTX2 conversion, Blender production, final texture assignment, shader implementation, R3F integration, mobile validation, and stakeholder approval remain pending.

---

## 4. Primary Asset Inventory

| Asset ID | Asset Name | Priority | Production Ticket | Scenes | Purpose | Output Target |
| --- | --- | --- | --- | --- | --- | --- |
| 3D-001 | Judicial Gavel | P0 | P5.02 | 01, 10 | Ceremonial trigger | `gavel.opt.glb` |
| 3D-002 | Mithaq Seal | P0 | P5.03 | 01, 02, 06, 10 | Hero brand object | `seal.opt.glb` |
| 3D-003 | Legal Desk Environment | P0 | P5.04 | 01, 02, 04, 10 | Core surface/world | `desk.opt.glb` |
| 3D-004 | Leather Writing Pad | P0/P1 | P5.04 | 04, 06, 08 | Legal folio surface | Included in `desk.opt.glb` or `leather-pad.opt.glb` |
| 3D-005 | Floating Documents | P1 | P5.05 | 03, 04 | Gap/method transition | `documents.opt.glb` |
| 3D-006 | Workshop Dossier Cards | P1 | P5.09 | 06 | Workshop atmosphere | `workshop-cards.opt.glb` |
| 3D-007 | Pillar Dossier Accents | P1 | P5.09 or P5.04 | 05 | Pillar atmosphere | Optional or bundled |
| 3D-008 | Ripple / Authority Ring | P0 | P5.06 | 01 | Gavel-to-seal transition | Shader/geometry |
| 3D-009 | Seal Emergence Geometry | P0 | P5.06/P5.03 | 01 | Seal reveal | Shader/geometry |
| 3D-010 | Ambient Dust Particles | P1 | P5.06 | Global | Atmosphere | Points/shader |
| 3D-011 | Mentor Gallery Atmosphere | P2 | Later/Optional | 07 | Authority environment | Static/low-poly accents |
| 3D-012 | Trust Scene Accents | P2 | Later/Optional | 08 | Editorial trust atmosphere | Static/low-poly accents |
| 3D-013 | Final CTA Callback Setup | P0 | P5.02/P5.03/P5.04 | 10 | Closing covenant | Reuse gavel/seal/desk |
| 3D-014 | Static Poster Render Sources | P1 | P4.05/P8.20 handoff | Fallback | Fallback imagery | Render/export references |

---

## 5. Asset-Level Brief Template

Each production asset must use this structure during its later task:

| Field | Required Content |
| --- | --- |
| Asset ID | Stable ID, e.g. `3D-001`. |
| Asset Name | Human-readable asset name. |
| Priority | P0 / P1 / P2. |
| Production Ticket | Later ticket that produces the asset. |
| Scenes Used | All scene appearances. |
| Narrative Purpose | What the asset communicates. |
| Visual Description | Shape, scale, style, proportion, legal tone. |
| Reference Inputs | P4.02, P4.03, P4.05, P4.06, P2.04 references. |
| Geometry Requirements | Triangle budget, LOD, mesh complexity, mobile simplification. |
| UV Requirements | UV unwrap, tiling, atlas, texel density. |
| Texture Budget | Desktop/mobile max sizes, required/optional maps, WebP/KTX2 use. |
| Material / PBR Spec | Base color, roughness, metalness, normal, AO, emissive, transparency. |
| Animation / Rigging Needs | Static/animated, pivot, scroll-driven transform needs. |
| Export Requirements | Format, file name, compression, gltfpack/Meshopt/KTX2 target. |
| Performance Budget | Max compressed size, load priority, lazy loading, mobile exclusion. |
| Fallback Equivalent | Static/non-WebGL replacement. |
| QA Acceptance Criteria | Specific pass/fail checks. |

---

## 6. 3D-001 Judicial Gavel Brief

| Field | Specification |
| --- | --- |
| Asset ID | 3D-001 |
| Asset Name | Judicial Gavel |
| Priority | P0 |
| Production Ticket | P5.02 - Gavel Model Production |
| Scenes Used | Scene 01 opening/gavel strike; Scene 10 final CTA callback |
| Narrative Purpose | The gavel is the ceremonial trigger that declares the covenant and initiates the Seal reveal. It must never become the brand hero. |

### Visual Description

A premium judicial gavel with dark walnut/wenge wood and restrained brass banding. The form should feel formal, weighty, and realistic. It should not look cartoonish, oversized, plastic, decorative, or violent. The head and handle should read clearly in macro close-up, with enough bevel to catch warm light.

### Reference Inputs

- P4.03 KF03-KF05 for descent, strike, and contact framing.
- P4.02 Scene 01 and Scene 10 comps for placement.
- P4.06 dark wood and gold foil/brass material direction.
- P2.04 3D art direction for gavel role and anti-patterns.

### Geometry Requirements

| Requirement | Target |
| --- | ---: |
| Triangle budget | 8k-18k tris before compression |
| Hero close-up allowance | Detail concentrated on head/handle silhouette |
| Mobile LOD | 4k-8k tris if separate LOD is created |
| Bevels | Enough to catch light, not excessive |
| Pivot | Set for descent/strike animation |
| Contact point | Bottom contact point clearly defined |
| Avoided details | Cracks, smash debris, excessive decorative engraving |

### UV Requirements

| Requirement | Direction |
| --- | --- |
| UV unwrap | Required for wood grain direction and brass bands. |
| Texture repetition | Wood can tile along handle; avoid visible seam in close-up. |
| Atlas | Optional; separate wood/brass materials acceptable. |
| Texel density | Highest near gavel head and visible handle. |

### Texture Budget

| Map | Target |
| --- | --- |
| Base color | 1024px desktop, 512px mobile |
| Normal | 1024px if grain detail needed |
| Roughness | 512-1024px |
| Brass band map | Material values or small map |
| AO | Optional 512px |
| KTX2 | Required later if texture maps are used; pending from P4.06 |

### Material / PBR Spec

| Part | Direction |
| --- | --- |
| Wood | Dark wood, high roughness, subtle grain |
| Brass | Muted brass/gold, high metalness, controlled roughness |
| Contact edge | Slight wear acceptable, not distressed |
| Emissive | None |
| Transparency | None |

### Animation / Rigging Needs

| Need | Direction |
| --- | --- |
| Animation | Scroll-driven descent and short contact. |
| Pivot | Near natural rotation/handle control point for strike. |
| Transform | Must support macro suspended state and resting callback state. |
| Rigging | No skeletal rig required; transform animation only. |

### Export Requirements

| Field | Requirement |
| --- | --- |
| Output | `gavel.opt.glb` |
| Optional mobile | `gavel.mobile.opt.glb` |
| Compression target | <= 1.2 MB compressed |
| Optimizer | gltfpack/Meshopt later |
| Export format | GLB 2.0 |
| Textures | External vs embedded decision documented in P5.02 |
| Orientation | Blender-to-Three.js consistent |
| Scale | Realistic relative to desk/seal |

### Performance Budget

| Field | Target |
| --- | --- |
| Load priority | Critical for opening WebGL path |
| Lazy-load | Not lazy for desktop opening; can be skipped for mobile/static |
| Mobile exclusion | Static poster allowed |
| Max compressed size | <= 1.2 MB |

### Fallback Equivalent

Static seal/desk hero poster or final CTA static image from P4.05.

### QA Acceptance Criteria

- Gavel reads as a premium legal object.
- Gavel does not dominate the completed Seal state.
- Gavel supports close-up opening frames.
- Pivot supports strike animation.
- Compressed file target is respected.
- No unnecessary geometry hidden from camera.
- Material matches P4.06 dark wood/brass direction.
- No violent smash language in shape or animation support.

---

## 7. 3D-002 Mithaq Seal Brief

| Field | Specification |
| --- | --- |
| Asset ID | 3D-002 |
| Asset Name | Mithaq Seal |
| Priority | P0 |
| Production Ticket | P5.03 - Mithaq Seal Model Production |
| Scenes Used | Scene 01, Scene 02, Scene 06, Scene 10, static fallback poster source |
| Narrative Purpose | The Seal is the core brand object and physical representation of the covenant. It is the hero object of the entire experience. |

### Visual Description

A circular embossed legal seal carrying the Arabic word `ميثاق` with restrained legal/covenant motifs. It should feel official, ceremonial, premium, culturally appropriate, and readable. It must not look like a fantasy medallion, wedding wax seal, generic law-firm icon, or religious ornament overload.

### Reference Inputs

- P4.03 KF06-KF08 for reveal, completion, and CTA handoff.
- P4.02 Scenes 01, 02, 06, 10 for recurring motif placement.
- P4.05 static fallback hero/final CTA poster needs.
- P4.06 gold foil/brass material family.
- P2.04 seal/stamp/embossed mark direction.

### Geometry Requirements

| Requirement | Target |
| --- | ---: |
| Triangle budget | 12k-30k tris before compression |
| Mobile LOD | 6k-12k tris |
| Emboss depth | Visible but not exaggerated |
| Separate parts | Rim / inner detail / Arabic mark can be separate meshes |
| Animation support | Reveal/draw/emissive activation possible |
| Avoided details | Dense unreadable ornament, fantasy spikes, fake institutional symbols |

### UV Requirements

| Requirement | Direction |
| --- | --- |
| UV unwrap | Required if texture maps are used. |
| Tiling | Not required for main seal face; material noise may tile subtly. |
| Atlas | Optional for rim/inner mark/face. |
| Texel density | Highest on Arabic mark, rim, and front face. |

### Texture Budget

| Map | Target |
| --- | --- |
| Base color | 1024px |
| Roughness | 1024px |
| Metalness | 512-1024px |
| Normal | 1024px if emboss needs map support |
| AO | Optional 512px |
| Emissive | Optional reveal-only mask |
| KTX2 | Required later for WebGL optimization; pending from P4.06 |

### Material / PBR Spec

| Material | Direction |
| --- | --- |
| Base metal | Muted gold/brass |
| Roughness | Not mirror chrome; medium-low to medium |
| Metalness | High but controlled |
| Emissive | Very subtle, reveal-only; no magic glow |
| Edge wear | Optional, subtle |
| Transparency | None |

### Animation / Rigging Needs

| Need | Direction |
| --- | --- |
| Animation | Seal outline/draw/reveal and settle. |
| Pivot | Centered for scale/rotation/pullback framing. |
| Transform | Must work centered and as background anchor. |
| Rigging | No skeletal rig; reveal may use shader/mesh segmentation. |

### Export Requirements

| Field | Requirement |
| --- | --- |
| Output | `seal.opt.glb` |
| Optional mobile | `seal.mobile.opt.glb` |
| Compression target | <= 1.5 MB preferred |
| Optimizer | gltfpack/Meshopt later |
| Export format | GLB 2.0 |
| Variant | Desktop + optional mobile LOD |
| Texture assignment | KTX2-ready later |

### Performance Budget

| Field | Target |
| --- | --- |
| Load priority | Critical hero/brand object |
| Lazy-load | Not for desktop opening/hero; reusable later |
| Mobile exclusion | Mobile can use simplified model or static poster |
| Max compressed size | <= 1.5 MB preferred |

### Fallback Equivalent

Static seal poster used in fallback hero and final CTA.

### QA Acceptance Criteria

- Seal is clearly the hero object.
- Arabic `ميثاق` remains legible.
- Seal feels official, not magical/fantasy.
- Gold is muted and premium.
- Works in Scene 01/02/06/10.
- Can be reused as small card seal/accent if needed.
- Does not rely on fake institutional symbols.

---

## 8. 3D-003 Legal Desk Environment Brief

| Field | Specification |
| --- | --- |
| Asset ID | 3D-003 |
| Asset Name | Legal Desk Environment |
| Priority | P0 |
| Production Ticket | P5.04 - Legal Desk Environment |
| Scenes Used | Scene 01, Scene 02, Scene 04, Scene 06, Scene 10 |
| Narrative Purpose | The desk is the physical world of Mithaq: legal seriousness, order, documents, training, and authority. |

### Visual Description

A dark legal desk surface with enough edge depth to ground macro camera moves. It may include a leather pad and minimal low-poly desk accessories, but the desk must remain a stage, not a hero. It should feel like a premium legal workspace, not a generic table or cluttered law office.

### Reference Inputs

- P4.03 KF02-KF08 for desk reveal and camera role.
- P4.02 Scene 01/02/04/10 canvas zones.
- P4.05 static desk hero/final CTA layout.
- P4.06 wood and leather materials.

### Geometry Requirements

| Requirement | Target |
| --- | ---: |
| Triangle budget | 2k-8k tris |
| Desk plane | Low-poly, material-driven |
| Edge detail | Enough for camera depth |
| Leather pad | Simple beveled plane or separate asset 3D-004 |
| Accessories | Optional and minimal |
| Mobile | Static/poster preferred |

### UV Requirements

| Requirement | Direction |
| --- | --- |
| UV unwrap | Required for wood grain direction. |
| Tiling | Wood texture may tile across broad surface. |
| Atlas | Optional if bundled with leather pad/accessories. |
| Texel density | Surface close-up must avoid blurry grain. |

### Texture Budget

| Map | Target |
| --- | --- |
| Wood base | 1024px |
| Wood normal | 1024px optional |
| Wood roughness | 512-1024px |
| Leather base | 1024px if pad bundled |
| Leather normal | 512-1024px |
| KTX2 | Required later if used in WebGL; pending from P4.06 |

### Material / PBR Spec

| Part | Direction |
| --- | --- |
| Desk | Dark wenge/walnut, high roughness |
| Leather pad | Dark leather, subtle grain |
| Edge | Slight warm light catch |
| Dust/marks | Very subtle, not dirty |
| Emissive | None |
| Transparency | None |

### Animation / Rigging Needs

| Need | Direction |
| --- | --- |
| Animation | Mostly static; supports camera reveal/pullback. |
| Pivot | Centered or world-aligned for placement. |
| Transform | Stable surface for gavel, seal, documents. |
| Rigging | None. |

### Export Requirements

| Field | Requirement |
| --- | --- |
| Output | `desk.opt.glb` |
| Optional mobile | `desk.mobile.opt.glb` |
| Compression target | <= 1.5 MB compressed if possible |
| Optimizer | gltfpack/Meshopt |
| Export format | GLB 2.0 |
| Materials | Uses P4.06 wood/leather direction |

### Performance Budget

| Field | Target |
| --- | --- |
| Load priority | Critical/light for opening world |
| Lazy-load | Critical subset only; accessories lazy/optional |
| Mobile exclusion | Static/poster allowed |
| Max compressed size | <= 1.5 MB preferred |

### Fallback Equivalent

Static dark desk hero/background image.

### QA Acceptance Criteria

- Desk supports Scene 01 opening camera.
- Desk does not look like a generic table.
- Leather pad, if included, feels professional/legal.
- Surface can hold documents/dossiers.
- Low geometry, material-led.
- Does not compete with Seal or copy.

---

## 9. 3D-004 Leather Writing Pad Brief

| Field | Specification |
| --- | --- |
| Asset ID | 3D-004 |
| Asset Name | Leather Writing Pad |
| Priority | P0/P1 |
| Production Ticket | P5.04 - Legal Desk Environment |
| Scenes Used | Scene 04, Scene 06, Scene 08 |
| Narrative Purpose | Provides legal folio/writing-pad tactility and a premium surface for method, workshop, and trust sections. |

### Visual Description

A dark leather writing pad or legal folio surface, rectangular with subtle beveling and fine grain. It must feel professional and legal, not fashion-luxury, reptile skin, glossy plastic, or decorative excess.

### Reference Inputs

- P4.06 dark leather material.
- P4.02 Scenes 04, 06, 08.
- P4.05 fallback method/workshop/trust editorial surfaces.

### Geometry Requirements

| Requirement | Target |
| --- | ---: |
| Triangle budget | 500-2k tris |
| Shape | Beveled rectangular pad/folio |
| Detail | Material-driven grain; minimal geometry |
| Mobile LOD | Can be removed or baked into poster |
| Bundling | May be included in `desk.opt.glb` |

### UV Requirements

| Requirement | Direction |
| --- | --- |
| UV unwrap | Required if textured. |
| Tiling | Leather can tile subtly. |
| Atlas | Bundle with desk if efficient. |
| Texel density | Moderate; close-up only if used in Scene 04/06. |

### Texture Budget

| Map | Target |
| --- | --- |
| Base color | 512-1024px |
| Normal | 512px optional |
| Roughness | 512px |
| AO | Optional |
| KTX2 | Required later if map is used; pending from P4.06 |

### Material / PBR Spec

| Property | Direction |
| --- | --- |
| Base color | Near-black brown leather |
| Roughness | High |
| Metalness | 0 |
| Normal | Subtle grain |
| Emissive | None |
| Transparency | None |

### Animation / Rigging Needs

Static. No rigging. Must support documents/dossiers above it if composition requires.

### Export Requirements

| Field | Requirement |
| --- | --- |
| Output | Included in `desk.opt.glb` preferred, or `leather-pad.opt.glb` if separate |
| Compression target | <= 200 KB if separate |
| Optimizer | gltfpack/Meshopt |
| Export format | GLB 2.0 |

### Performance Budget

Low. Remove from mobile or bake into static poster if not essential.

### Fallback Equivalent

Static dark leather/panel texture in fallback section backgrounds.

### QA Acceptance Criteria

- Reads as legal writing pad/folio.
- Does not distract from content.
- Grain is subtle and not noisy.
- Works under documents/cards.
- Can be removed on mobile without meaning loss.

---

## 10. 3D-005 Floating Documents Brief

| Field | Specification |
| --- | --- |
| Asset ID | 3D-005 |
| Asset Name | Floating Legal Documents |
| Priority | P1 |
| Production Ticket | P5.05 - Floating Documents |
| Scenes Used | Scene 03, Scene 04 transition |
| Narrative Purpose | Represents the gap between academic legal knowledge and practical readiness, then organizes into method/order. |

### Visual Description

A small set of low-poly parchment-like legal pages, slightly bent or softly crumpled. They should look like legal documents but must not contain readable fake legal text. Abstract line marks are acceptable.

### Reference Inputs

- P4.02 Scene 03 document fragments.
- P4.05 fragmented document poster.
- P4.06 parchment material.
- P3.02 storyflow for gap-to-method transition.

### Geometry Requirements

| Requirement | Target |
| --- | ---: |
| Count | 8 document geometries |
| Triangle budget | Under 500 tris each |
| Shape | Slight bend/crumple |
| Variants | 3-4 silhouettes minimum |
| Animation | Must float/orbit/align |
| Mobile | Static/minimal collage |

### UV Requirements

| Requirement | Direction |
| --- | --- |
| UV unwrap | Required for parchment texture. |
| Tiling | Parchment can tile or use shared atlas. |
| Atlas | Preferred for all paper variants. |
| Texel density | Moderate; no readable text required. |

### Texture Budget

| Map | Target |
| --- | --- |
| Parchment base | 512-1024px |
| Normal/crumple | 512px optional |
| Opacity | Avoid; only if torn edges are essential |
| Roughness | 512px optional |
| KTX2 | Required later if used in WebGL; pending from P4.06 |

### Material / PBR Spec

| Part | Direction |
| --- | --- |
| Paper | Warm parchment, not dirty |
| Text marks | Abstract lines only, no fake legal text |
| Roughness | High |
| Metalness | 0 |
| Transparency | Avoid if possible for performance |
| Emissive | None |

### Animation / Rigging Needs

Transform animation only. Each document needs a stable origin for drift/alignment. No skeletal rig.

### Export Requirements

| Field | Requirement |
| --- | --- |
| Output | `documents.opt.glb` |
| Optional mobile | `documents.mobile.opt.glb` or none |
| Compression target | <= 500 KB compressed preferred |
| Count | 8 papers |
| Optimizer | gltfpack/Meshopt |
| Instancing | Consider if possible later |

### Performance Budget

Lazy-load before Scene 03. Mobile should use static collage or DOM/static poster.

### Fallback Equivalent

Static fragmented document poster from P4.05.

### QA Acceptance Criteria

- 8 low-poly document geometries exist.
- Under 500 tris each.
- They read as legal papers.
- No fake legal copy is readable.
- They can animate without heavy cost.
- Mobile can replace with static collage.

---

## 11. 3D-006 Workshop Dossier Cards Brief

| Field | Specification |
| --- | --- |
| Asset ID | 3D-006 |
| Asset Name | Workshop Dossier 3D Cards |
| Priority | P1 |
| Production Ticket | P5.09 - Workshop Dossier 3D Cards |
| Scenes Used | Scene 06 |
| Narrative Purpose | Creates premium physical framing for workshops without turning the site into an LMS or course marketplace. |

### Visual Description

Simple legal folder/card objects with subtle thickness, stamped seal accents, parchment/dark leather material options, and no final text baked into textures. The cards are atmospheric; DOM cards and CTAs remain the source of truth.

### Reference Inputs

- P4.02 Scene 06 workshop preview.
- P4.05 workshop dossier static fallback cards.
- P4.06 parchment, leather, and gold foil materials.
- P3.03 conversion funnel for workshop inquiry.

### Geometry Requirements

| Requirement | Target |
| --- | ---: |
| Triangle budget | <= 2,000 tris each |
| Count | 3-5 cards/dossiers |
| Shape | Folder/card/dossier silhouette |
| Text | No baked final text |
| Interaction | Optional hover lift; DOM holds real content |
| Mobile | DOM cards/static only |

### UV Requirements

| Requirement | Direction |
| --- | --- |
| UV unwrap | Required if textured. |
| Tiling | Parchment/leather can tile subtly. |
| Atlas | Preferred across card set. |
| Texel density | Moderate; seal/stamp accents need clarity. |

### Texture Budget

| Map | Target |
| --- | --- |
| Base color | 512-1024px |
| Normal | 512px optional |
| Roughness | 512px |
| Seal/stamp | Geometry, decal, or material accent |
| KTX2 | Required later if textured; pending from P4.06 |

### Material / PBR Spec

| Part | Direction |
| --- | --- |
| Card body | Aged parchment or dark leather |
| Stamp/accent | Muted gold/brass |
| Roughness | Medium-high for paper/leather; controlled for gold |
| Metalness | 0 for card body; high for gold stamp |
| Emissive | None |
| Transparency | Avoid |

### Animation / Rigging Needs

Static or transform-only gentle entrance. No 3D flip card. No raycaster-only CTA.

### Export Requirements

| Field | Requirement |
| --- | --- |
| Output | `workshop-cards.opt.glb` |
| Optional mobile | None preferred; DOM/static |
| Compression target | <= 1 MB preferred |
| Interaction | Raycaster optional; DOM CTA required |
| Optimizer | gltfpack/Meshopt |

### Performance Budget

Lazy-load before Scene 06. Do not load in initial hero critical subset.

### Fallback Equivalent

DOM workshop cards from P4.05.

### QA Acceptance Criteria

- Dossiers feel premium and legal.
- They do not look like course marketplace cards.
- No fake workshop facts are baked in.
- DOM remains source of truth.
- Mobile can remove 3D entirely.

---

## 12. 3D-007 Pillar Dossier Accents Brief

| Field | Specification |
| --- | --- |
| Asset ID | 3D-007 |
| Asset Name | Pillar Dossier Accents |
| Priority | P1 |
| Production Ticket | P5.09 or P5.04 |
| Scenes Used | Scene 05 |
| Narrative Purpose | Adds subtle physicality to the five training pillars without creating a course-module dashboard. |

### Visual Description

Small dossier tabs, stamped marks, file edges, or thin layered cards used behind/near pillar content. These should be accents only, not primary interactive cards. Real pillar text remains DOM.

### Reference Inputs

- P4.02 Scene 05 pillar comps.
- P4.05 five pillar fallback cards.
- P4.06 parchment/gold/dark panel materials.

### Geometry Requirements

| Requirement | Target |
| --- | ---: |
| Triangle budget | <= 500-1,500 tris per accent set |
| Count | 5 accent objects or one grouped set |
| Shape | Dossier tabs, stamped files, thin card edges |
| Mobile | Remove/static |
| Avoided details | Module grids, badges, fake course icons |

### UV Requirements

Simple unwrap or shared atlas. Tiling acceptable. No baked pillar text.

### Texture Budget

| Map | Target |
| --- | --- |
| Base color | 512px |
| Roughness | 512px optional |
| Gold accent | Material value or small map |
| KTX2 | Pending if textured |

### Material / PBR Spec

Parchment/dark panel body with optional muted gold seal/stamp accent. High roughness, low glare, no emissive.

### Animation / Rigging Needs

Static or gentle entrance only. No hover-only information.

### Export Requirements

Optional bundled output in `workshop-cards.opt.glb`, `desk.opt.glb`, or a separate `pillar-accents.opt.glb` if justified. Keep separate only if it benefits lazy loading.

### Performance Budget

Low priority. Can be removed from mobile and reduced-motion.

### Fallback Equivalent

DOM pillar cards from P4.05.

### QA Acceptance Criteria

- Supports pillar atmosphere without LMS feeling.
- Text is not baked into 3D.
- Can be removed without meaning loss.
- No fake module counts, badges, or course-dashboard visuals.

---

## 13. 3D-008 Ripple / Authority Ring Brief

| Field | Specification |
| --- | --- |
| Asset ID | 3D-008 |
| Asset Name | Ripple / Authority Ring |
| Priority | P0 |
| Production Ticket | P5.06 - Shader Development |
| Scenes Used | Scene 01 |
| Narrative Purpose | Converts the gavel contact into a controlled authority signal that bridges to the Seal reveal. |

### Visual Description

A restrained concentric gold/brass ring or line pattern expanding across the desk from the gavel contact point. It must feel official and structured, not explosive, magical, sci-fi, or game-like.

### Reference Inputs

- P4.03 KF04-KF06.
- P2.07 motion vocabulary.
- P4.06 gold foil material direction.

### Geometry Requirements

| Requirement | Target |
| --- | ---: |
| Geometry | Plane/ring/line geometry or shader on desk |
| Triangle budget | <= 1k tris if mesh-based |
| Shader budget | Lightweight; isolated test required later |
| Mobile | Simplified/disabled |
| Avoided details | Shockwaves, explosions, cracked desk, magic sparks |

### UV Requirements

Only if texture mask is used. Procedural geometry preferred if simpler.

### Texture Budget

512px mask optional. KTX2 pending if texture-based. No large animated texture sequences.

### Material / PBR Spec

Muted gold/brass line, low opacity, controlled roughness/emissive if any. Emissive must be subtle and reveal-only.

### Animation / Rigging Needs

Scroll-driven expansion from contact point. No bounce. No autonomous loop.

### Export Requirements

May be shader/geometry rather than GLB. If geometry exported, name `authority-ring.opt.glb`. If shader-only, document in P5.06.

### Performance Budget

Critical for opening only if WebGL path active. Must have static fallback. Disable or simplify on mobile.

### Fallback Equivalent

Static completed seal/desk poster.

### QA Acceptance Criteria

- Reads as official authority ring.
- Not explosion/magic/sci-fi.
- Lightweight enough for opening vertical slice.
- Can be disabled without losing content meaning.

---

## 14. 3D-009 Seal Emergence Geometry Brief

| Field | Specification |
| --- | --- |
| Asset ID | 3D-009 |
| Asset Name | Seal Emergence Geometry |
| Priority | P0 |
| Production Ticket | P5.06/P5.03 |
| Scenes Used | Scene 01 |
| Narrative Purpose | Forms the Seal outline and transitions the user's attention from the gavel trigger to the Seal hero. |

### Visual Description

Controlled ring segments, line paths, or reveal masks that draw/resolve into the completed Seal. The effect should feel ceremonial and precise, not magical or decorative noise.

### Reference Inputs

- P4.03 KF06-KF07.
- P2.05 opening storyboard.
- P2.07 motion vocabulary.
- P4.06 gold foil material.

### Geometry Requirements

| Requirement | Target |
| --- | ---: |
| Geometry | Ring segments, line paths, or reveal masks |
| Triangle budget | <= 2k tris if mesh-based, excluding final seal |
| Shader budget | Lightweight and isolated later |
| Mobile | Static completed seal preferred |
| Avoided details | Sparkles, fantasy glow, unreadable calligraphy animation |

### UV Requirements

Depends on reveal method. If using masks, keep masks 512-1024px max.

### Texture Budget

| Map | Target |
| --- | --- |
| Reveal mask | 512-1024px optional |
| Emissive mask | 512px optional |
| KTX2 | Pending if texture-based |

### Material / PBR Spec

Muted gold/brass, subtle reveal light, no glow flood. Emissive optional and minimal.

### Animation / Rigging Needs

Scroll-driven draw/reveal. Must align with final `seal.opt.glb`. No letter-by-letter Arabic animation.

### Export Requirements

May be integrated with `seal.opt.glb` or shader-only in P5.06. If separate mesh, use `seal-emergence.opt.glb`.

### Performance Budget

Critical opening effect, but must be removable for reduced motion and mobile.

### Fallback Equivalent

Static completed Seal.

### QA Acceptance Criteria

- Seal becomes hero by completion.
- Transition clearly moves attention from gavel to Seal.
- No magic/fantasy/sci-fi feel.
- Reduced-motion equivalent is static completed Seal.

---

## 15. 3D-010 Ambient Dust Particles Brief

| Field | Specification |
| --- | --- |
| Asset ID | 3D-010 |
| Asset Name | Ambient Dust Particles |
| Priority | P1 |
| Production Ticket | P5.06 |
| Scenes Used | Global, especially Scenes 01, 02, 10 |
| Narrative Purpose | Adds quiet premium atmosphere and depth to the legal chamber without becoming spectacle. |

### Visual Description

Sparse warm dust/particle motes in directional light. Low opacity, slow motion, no sparkle/magic. Particles should be barely noticed but felt.

### Reference Inputs

- P4.03 KF01-KF08 atmosphere.
- P2.07 ambient motion guidance.
- P2.04 lighting/camera mood.

### Geometry Requirements

| Requirement | Target |
| --- | ---: |
| Geometry | Points or instanced sprites |
| Desktop count | 100-250 particles |
| Mobile count | Reduced or disabled |
| Reduced motion | Disabled |
| Avoided details | Glitter, magic sparkle, dense fog |

### UV Requirements

Optional small sprite texture. Avoid large transparent textures.

### Texture Budget

Tiny sprite/mask 128-256px if needed. KTX2 not required unless part of WebGL optimization pipeline.

### Material / PBR Spec

Low opacity warm parchment/gold tint, additive only if very restrained. Depth sorting must not create artifacts over text.

### Animation / Rigging Needs

Slow ambient drift using `sine.inOut` style motion. Disable in reduced motion.

### Export Requirements

Shader/points system, not necessarily GLB. If sprite texture exists, use stable texture naming later.

### Performance Budget

Optional. Disable if FPS drops. Never critical to content.

### Fallback Equivalent

None required; static texture/poster handles atmosphere.

### QA Acceptance Criteria

- Subtle and premium.
- No sparkle/magic.
- Does not hurt FPS.
- Disabled in reduced motion.
- Does not obscure DOM text.

---

## 16. Optional Accent Assets Brief

### 16.1 3D-011 Mentor Gallery Atmosphere

| Field | Specification |
| --- | --- |
| Priority | P2 |
| Scenes | Scene 07 |
| Purpose | Add subtle authority environment around mentor section if needed. |
| Possible Assets | Low-poly frames, desk shadow, archive shelf silhouette, seal watermark plane. |
| Triangle Budget | <= 1k-3k tris total if used. |
| Texture Budget | 512px max, preferably CSS/static only. |
| Material | Dark panel/wood/gold accent, no portrait fabrication. |
| Mobile | Static cards only. |
| Fallback | Mentor cards from P4.05. |
| QA | No fake mentor identities or credentials. |

### 16.2 3D-012 Trust Scene Accents

| Field | Specification |
| --- | --- |
| Priority | P2 |
| Scenes | Scene 08 |
| Purpose | Support trust/authority without fake proof. |
| Possible Assets | Seal watermark plane, stamped document edge, gold rule, archive tag. |
| Triangle Budget | <= 1k tris total if used. |
| Texture Budget | 512px max. |
| Material | Muted gold/parchment/dark panel. |
| Mobile | Static blocks. |
| Fallback | Trust blocks from P4.05. |
| QA | No fake stats, logos, testimonials, or institutional claims. |

### 16.3 3D-013 Final CTA Callback Setup

| Field | Specification |
| --- | --- |
| Priority | P0 |
| Scenes | Scene 10 |
| Purpose | Reuses Seal, gavel, and desk for closing covenant. |
| Assets | `seal.opt.glb`, `gavel.opt.glb`, `desk.opt.glb`. |
| New Geometry | None unless final layout requires small gold rule/particle field. |
| Budget | Reuse existing loaded assets; avoid new heavy downloads. |
| Mobile | Static final seal CTA poster. |
| Fallback | P4.05 final CTA poster. |
| QA | Conversion CTAs remain DOM and visible. |

### 16.4 3D-014 Static Poster Render Sources

| Field | Specification |
| --- | --- |
| Priority | P1 |
| Scenes | Static fallback / reduced motion / WebGL failure |
| Purpose | Provide render-source compositions for non-WebGL fallback imagery. |
| Assets | Seal/desk/gavel/documents/dossiers as static renders once models exist. |
| Output | WebP/AVIF poster sources later, not in P5.01. |
| Budget | Optimize for LCP; do not use huge posters. |
| Mobile | Cropped/mobile poster variants required later. |
| Fallback | Current P4.05 HTML placeholders until final renders exist. |
| QA | No text baked into posters if it should be DOM. |

### 16.5 Optional Stamps / Paper Clips / Pen / Archive Elements

| Field | Specification |
| --- | --- |
| Priority | P2 |
| Scenes | 04, 06, 08 if needed |
| Purpose | Legal desk atmosphere only. |
| Triangle Budget | <= 500-1,500 tris per object; <= 3k total visible optional set. |
| Texture Budget | 512px max or material values only. |
| Material | Brass, dark metal, parchment, dark wood; restrained. |
| Mobile | Exclude. |
| Fallback | Static poster/card texture. |
| QA | Must not create clutter or generic stock legal desk. |

---

## 17. Scene-to-Asset Map

| Scene | Required Assets | Optional Assets | Mobile Treatment | Static Fallback |
| --- | --- | --- | --- | --- |
| 01 Opening | Gavel, Seal, Desk, Ripple, Dust | Fracture/line accents only if restrained | Simplified/static | Static seal/desk poster |
| 02 Hero | Seal, Desk, Dust | Gavel side state | Seal poster/static | Hero static poster |
| 03 Gap | Floating Documents | Dust | Static/minimal collage | Fragmented document poster |
| 04 Method | Desk, Documents, Leather Pad | Pen/stamp | Static method blocks | Ordered desk poster |
| 05 Pillars | Pillar dossier accents | Seal stamp decals | DOM/static | Pillar cards |
| 06 Workshops | Workshop Dossiers, Seal accents | Desk/leather | DOM/static | Workshop cards |
| 07 Mentors | Atmosphere only | Portrait frames, archive silhouette | Static cards | Mentor cards |
| 08 Trust | Minimal accents | Seal watermark | Static | Trust blocks |
| 09 FAQ | None | Ambient texture only | None | FAQ |
| 10 Final CTA | Seal, Gavel, Desk | Gold rule/particles | Static/light | Final seal CTA poster |

---

## 18. Global Asset Budget

| Category | Target |
| --- | ---: |
| Initial hero 3D critical subset | <= 2.5 MB compressed preferred |
| Gavel compressed | <= 1.2 MB |
| Seal compressed | <= 1.5 MB preferred |
| Desk compressed | <= 1.5 MB preferred |
| Documents compressed | <= 500 KB preferred |
| Workshop cards compressed | <= 1 MB preferred |
| Total 3D loaded after interaction | <= 6-8 MB |
| Desktop texture max | 1024-2048px only if justified |
| Mobile texture max | 512-1024px |
| Desktop FPS target | 55-60 FPS |
| Mobile FPS target | 30-45 FPS |
| LCP target | <= 2.5s on good connection |
| INP target | <= 200ms |
| CLS target | <= 0.1 |

Budget rule:

The opening vertical slice must prove performance before approving full 3D complexity across scenes.

---

## 19. Material Library Integration Notes

Use P4.06 texture/material library:

[P4.06 README](D:/Clinets/MITHAQ/MITHAQ/mithaq-project-docs/mithaq-dark-texture-material-library/README.md:1)

| Asset | Material Family |
| --- | --- |
| Gavel wood | Dark wood |
| Gavel brass | Gold/brass foil direction |
| Seal | Gold foil / brass |
| Desk | Dark wood |
| Leather pad | Dark leather |
| Documents | Aged parchment |
| Workshop dossiers | Aged parchment + leather + gold stamp |
| Pillar cards | Parchment/dark panel + gold seal accent |
| Trust accents | Gold foil / seal watermark |

Current P4.06 condition:

- WebP textures complete.
- KTX2 conversion pending because no local KTX2/Basis encoder was available.
- Do not claim final KTX2 readiness until real `.ktx2` files are produced.

---

## 20. Export & Naming Requirements

Required final production asset names:

```txt
gavel.opt.glb
seal.opt.glb
desk.opt.glb
documents.opt.glb
workshop-cards.opt.glb
```

Optional/derived mobile names:

```txt
gavel.mobile.opt.glb
seal.mobile.opt.glb
desk.mobile.opt.glb
documents.mobile.opt.glb
workshop-cards.mobile.opt.glb
```

Optional accent names, only if justified later:

```txt
leather-pad.opt.glb
pillar-accents.opt.glb
authority-ring.opt.glb
seal-emergence.opt.glb
```

Do not use:

```txt
final.glb
gavel2.glb
new-seal.glb
test-export.glb
model-ok.glb
```

Recommended future asset path:

```txt
/public/assets/models/mithaq/
```

Do not move or wire files into production paths in P5.01.

---

## 21. Blender Production Requirements

| Requirement | Rule |
| --- | --- |
| Scale | Consistent scene scale across all assets. |
| Origin/pivot | Set intentionally for animation. |
| Transforms | Apply transforms before export. |
| Naming | Mesh/material names clean and stable. |
| UVs | No overlapping UVs unless intentional tiling/atlas decision. |
| Materials | PBR-compatible. |
| Hidden geometry | Remove before export. |
| Normals | Clean normals, no artifacts. |
| LOD | Create mobile LOD where needed. |
| Export | GLB 2.0. |
| Optimization | gltfpack/Meshopt later. |
| Texture formats | WebP for static/CSS; KTX2 for WebGL after conversion. |

---

## 22. Performance / Loading Strategy

| Asset | Load Priority | Notes |
| --- | --- | --- |
| Seal | Critical | Hero/brand object. |
| Gavel | Critical for opening | Can use static fallback if delayed. |
| Desk | Critical/light | Foundation surface. |
| Ripple shader | Critical for opening if WebGL path | Static completed seal fallback required. |
| Documents | Lazy-load before Scene 03 | Static collage on mobile. |
| Workshop cards | Lazy-load before Scene 06 | DOM cards are primary. |
| Mentor atmosphere | Optional/lazy/static | Avoid if it adds clutter. |
| Trust accents | Optional/static | No fake proof. |
| Dust particles | Optional | Disable/reduce on mobile. |

Rules:

- HTML/DOM content loads first.
- 3D enhances after.
- Static poster can show while GLB loads.
- Non-hero assets lazy-load.
- Mobile can skip non-critical 3D.
- CTAs never wait for canvas.

---

## 23. Mobile / Reduced-Motion Rules

| Asset | Mobile Rule | Reduced Motion Rule |
| --- | --- | --- |
| Gavel | Simplified/static | Static hero poster |
| Seal | Simplified/poster | Static completed seal |
| Desk | Static/poster | Static |
| Documents | Static collage | Static collage |
| Workshop Dossiers | Removed/static accent | DOM cards |
| Pillar Accents | Removed/static | DOM cards |
| Dust | Reduced/disabled | Disabled |
| Ripple | Simplified/disabled | Disabled |
| Seal Emergence | Static completed seal | Static completed seal |
| Mentor Atmosphere | Static cards | Static cards |
| Trust Accents | Static blocks | Static blocks |

Mobile rule:

Mobile conversion safety is more important than preserving desktop 3D choreography.

---

## 24. Accessibility / DOM-First Rules

- No content is baked only into 3D textures.
- Workshop titles live in DOM, not 3D.
- CTA buttons live in DOM.
- Seal/gavel are decorative/symbolic, not required to understand copy.
- If canvas fails, static fallback communicates the same message.
- Screen readers should not be forced through canvas internals.
- 3D assets must not obscure text/CTA zones.
- Mobile users must not need raycaster interaction to convert.
- Arabic and English meaningful text must remain accessible DOM text.
- If the Seal includes Arabic marks, the same meaning must also exist in DOM where needed.

---

## 25. Reference Board / Source Notes

Accepted internal references:

| Source | Use |
| --- | --- |
| [P4.02 Scene-Level Visual Comps](D:/Clinets/MITHAQ/MITHAQ/mithaq-project-docs/mithaq-scene-level-visual-comps/mithaq-scene-level-visual-comps.md:1) | Scene composition, DOM/canvas zones, 10-scene visual role. |
| [P4.03 Opening Sequence Frame Comps](D:/Clinets/MITHAQ/MITHAQ/mithaq-project-docs/mithaq-opening-sequence-frame-comps/mithaq-opening-sequence-frame-comps.md:1) | Opening keyframes, gavel/Seal/desk timing and framing. |
| [P4.05 Static Fallback Layout](D:/Clinets/MITHAQ/MITHAQ/mithaq-project-docs/mithaq-static-fallback-layout/mithaq-static-fallback-layout.md:1) | Static fallback equivalents and poster needs. |
| [P4.06 Material Library](D:/Clinets/MITHAQ/MITHAQ/mithaq-project-docs/mithaq-dark-texture-material-library/README.md:1) | Texture/material direction and KTX2 condition. |
| P2.04 3D Art Direction Moodboard | Seal-led macro legal chamber direction and anti-patterns. |

External image references are not added in P5.01. If later asset-production tickets add external imagery, each source must document URL, license, commercial-use status, attribution requirements, and no watermarks/unclear copyright.

---

## 26. QA Checklist

| Check | Status | Notes |
| --- | --- | --- |
| All required 3D assets listed | PASS | 3D-001 through 3D-014 included. |
| Every asset has scene mapping | PASS | Asset sections and scene map included. |
| Every asset has narrative purpose | PASS | Included per asset. |
| Every asset has visual description | PASS | Included per asset. |
| Polygon/triangle budgets included | PASS | Included per asset and global budget. |
| Texture budgets included | PASS | Included per asset. |
| Material/PBR specs included | PASS | Included per asset. |
| Export targets included | PASS | Required names and optional names included. |
| Fallback equivalents included | PASS | Included per asset. |
| Mobile/reduced-motion rules included | PASS | Included per asset and global table. |
| Shader-driven assets briefed | PASS | 3D-008, 3D-009, 3D-010 included. |
| Global asset budget included | PASS | Section 18. |
| Material library integration documented | PASS | Section 19. |
| KTX2 pending condition carried forward | PASS | P4.06 condition documented. |
| Blender production rules documented | PASS | Section 21. |
| Loading strategy documented | PASS | Section 22. |
| Accessibility/DOM-first rules included | PASS | Section 24. |
| Reference sources documented | PASS | Section 25. |
| Avoided GLB production | PASS | No GLB files created. |
| Avoided implementation | PASS | No R3F/shader/frontend work. |
| Avoided new roadmap tickets | PASS | No new tickets created. |

---

## 27. Final Recommendation

Proceed into Phase 5 production using this order:

1. P5.02 gavel model, because it drives the opening trigger.
2. P5.03 Seal model, because it is the hero and must be reviewed carefully.
3. P5.04 desk environment, because it anchors every macro composition.
4. P5.05 documents, only after the opening vertical slice budget remains safe.
5. P5.06 ripple/seal emergence/dust shader tests, isolated before production integration.
6. P5.09 workshop/dossier accents only if performance and content readiness support them.

Production posture:

- Build the opening vertical slice first.
- Keep P0 assets optimized and reusable.
- Use DOM content and static fallback as the source of meaning.
- Do not allow optional 3D accents to delay conversion or accessibility.

---

## 28. Acceptance Criteria

| Acceptance Criteria | Status |
| --- | --- |
| 3D asset brief document created | PASS |
| Every required 3D asset listed | PASS |
| Every asset has object description | PASS |
| Every asset has scene mapping | PASS |
| Every asset has narrative purpose | PASS |
| Every asset has polygon/triangle budget | PASS |
| Every asset has texture budget | PASS |
| Every asset has PBR material spec | PASS |
| Every asset has export requirements | PASS |
| Every asset has performance budget | PASS |
| Every asset has mobile/reduced-motion behavior | PASS |
| Every asset has fallback equivalent | PASS |
| Shader-driven assets briefed | PASS |
| Scene-to-asset map complete | PASS |
| Global asset budget included | PASS |
| Material library mapping included | PASS |
| KTX2 pending condition from P4.06 carried forward honestly | PASS |
| Blender production requirements documented | PASS |
| Loading strategy documented | PASS |
| Accessibility/DOM-first rules documented | PASS |
| Reference/source notes included | PASS |
| No GLB production started | PASS |
| No Blender production files created | PASS |
| No R3F implementation started | PASS |
| No shader implementation started | PASS |
| No frontend implementation started | PASS |
| No new roadmap tickets created | PASS |

---

## 29. Final Status

**PASS WITH CONDITIONS - P5.01 complete. All 3D assets are fully briefed with descriptions, scene mapping, reference inputs, polygon budgets, texture budgets, PBR specs, export targets, mobile/fallback rules, performance budgets, loading strategy, Blender requirements, DOM-first accessibility rules, and QA criteria.**

Conditions remaining:

- Final seal/logo design is pending.
- KTX2 conversion remains pending from P4.06.
- Blender production has not started.
- Final texture assignment is pending.
- Shader implementation is pending.
- R3F integration is pending.
- Final mobile device validation is pending.
- Stakeholder approval is pending.
