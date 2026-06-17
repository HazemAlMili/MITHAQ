# Mithaq Reference Website Analysis Report

**Official Ticket ID:** P1.01  
**Official Ticket Name:** Reference Website Analysis  
**Phase:** Phase 1, Research Synthesis & Direction Lock  
**Priority:** P0  
**Status:** Complete with documented screenshot persistence limitation  
**Prepared date:** 2026-06-17  

---

## 1. Executive Summary

This report analyzes the five approved references for Mithaq:

1. Oryzo AI: https://oryzo.ai/
2. KODE Immersive: https://kodeimmersive.com/
3. Immersive Garden: https://immersive-g.com/
4. Floema: https://floema.com/
5. Lenz & Staehelin: https://www.lenzstaehelin.com/

All five references were live-inspected in the browser. The analysis focuses only on patterns useful to Mithaq as a premium bilingual 3D legal academy portfolio / landing experience.

Key research outcome:

- Oryzo AI supports object-led storytelling and macro symbolic product focus.
- KODE Immersive supports spatial entry, sound-control patterns, and "entering a world" pacing.
- Immersive Garden supports authored scroll choreography and premium case-study rhythm.
- Floema supports restrained premium editorial structure, material clarity, and product/category hierarchy.
- Lenz & Staehelin supports legal authority, multilingual institutional structure, and trust-through-content hierarchy.

Screenshot note:

Browser screenshots were attempted, but the browser runtime denied file writes to both the workspace and temp directories. Screenshot annotations are included in this report as required fallback notes. No screenshots are falsely claimed as saved artifacts.

---

## 2. Research Context

This task is research and analysis only. It does not start UI design, 3D modeling, frontend implementation, Figma work, or roadmap expansion.

The purpose is to extract reusable patterns for Mithaq:

- Premium atmosphere
- Scroll-driven cinematic pacing
- Symbolic 3D storytelling
- Bilingual / RTL-safe layout thinking
- Trust and legal authority
- Accessibility and performance guardrails

---

## 3. Current Mithaq Decisions from P0.06

| Decision Area | Locked Direction |
| ------------- | ---------------- |
| Site type | Premium bilingual 3D legal academy portfolio / landing experience |
| Not in scope | LMS, dashboard, booking system, payment system, course platform |
| Opening | Gavel trigger to Mithaq Seal reveal |
| Hero object | Seal is the hero; gavel is the trigger |
| Opening behavior | Scroll-driven, not fixed-time intro |
| Primary conversion | WhatsApp |
| Language | Bilingual MVP planning; Arabic visually prioritized |
| 3D style | Symbolic realism |
| Sound | Approved, but optional/user-controlled |
| Workshop behavior | Hybrid modal preview + `/workshops/[slug]` |
| Delivery | Vertical Slice First |
| Trust section | Forward-compatible if proof points are missing |
| Urgency | No fake urgency, countdowns, seat systems, or cohort/deadline model |
| Phase 1 pages | `/`, `/register`, `/workshops/[slug]` |

---

## 4. Reference 1 Analysis - Oryzo AI

### 4.1 First Impression

| Item | Notes |
| ---- | ----- |
| First 5-second impression | A highly polished, object-led AI/product satire experience with one central object and bold editorial copy. |
| Primary emotional effect | Premium craft mixed with playful absurdity. |
| Clarity level | Visually clear, conceptually playful; the product story is intentionally ironic. |
| Premium signals | Macro object focus, high-detail product framing, controlled typography, rich interaction density. |
| Risk if copied blindly | Mithaq would become too playful or product-satirical. |
| Mithaq takeaway | Use one symbolic object as the narrative anchor, but remove the satire and keep legal seriousness. |

### 4.2 Visual Direction

| Visual Element | Observed Pattern | Mithaq Use | Mithaq Avoid |
| -------------- | ---------------- | ---------- | ------------ |
| Color | Strong product contrast with clean editorial sections. | Use contrast to isolate the seal/gavel moment. | Avoid bright product-launch energy. |
| Lighting | Product-focused highlight treatment. | Use warm, controlled legal-chamber lighting. | Avoid commercial gadget lighting. |
| Materials | Object detail is important; surfaces support the product. | Make gavel/desk/seal material quality visible. | Avoid making material realism the whole message. |
| Typography | Big, confident, often humorous product copy. | Use typographic confidence for hero/section declarations. | Avoid joke-copy and meme energy. |
| Layout | Alternates object focus with editorial content. | Use object-to-content rhythm for seal to sections. | Avoid excessive novelty blocks. |
| Trust signals | Links to paper, model, code, studio, policies; intentionally over-engineered proof tone. | Use real proof and source links only where meaningful. | Avoid fake or parody credibility. |

### 4.3 Motion & Scroll Behavior

| Motion Pattern | Description | Timing / Feeling | Mithaq Relevance |
| -------------- | ----------- | ---------------- | ---------------- |
| Scroll behavior | Content appears structured by product moments and sections. | Playful, energetic, object-led. | Useful for anchoring scroll to symbolic object beats. |
| Scene transitions | Transitions support object/content reveals. | Crafted, not generic. | Use controlled transitions from gavel to seal to content. |
| Camera movement | Central object implies product-stage camera logic. | Product-macro feeling. | Adapt to legal seal macro details. |
| Text reveal | Bold and readable. | Fast editorial confidence. | Mithaq should slow this down and make it ceremonial. |
| Sound / audio | No confirmed audio observed in source inspection. | Not a primary lesson. | Mithaq sound should be optional and restrained. |
| Motion risks | Playfulness may overpower message. | Energetic. | Mithaq must stay calm and authoritative. |

### 4.4 3D / WebGL / Technical Observations

| Technical / 3D Element | Observation | Mithaq Relevance |
| ---------------------- | ----------- | ---------------- |
| Central 3D object | Appears object-led; page contains 6 canvases. | Supports one-symbol strategy: gavel trigger, seal hero. |
| Canvas / WebGL usage | Multiple canvases observed. Exact library not confirmed. |
| Scroll-to-3D mapping | Observed behavior suggests object moments tied to page progression. | Useful for scroll-driven opening. |
| Asset loading | Uses `_astro` CSS and many images/pictures. | Shows static assets can coexist with canvas. |
| Mobile behavior | Mobile screenshot could not be persisted; mobile-specific inspection not completed due write failure. | Must be tested later. |
| Fallback behavior | Cannot confirm. | Mithaq must implement explicit fallback. |
| Performance risk | Multiple canvas elements and rich visuals can become heavy. | Use one shared canvas where possible. |

### 4.5 Content / Trust Structure

| Trust Pattern | Observed Use | Mithaq Application |
| ------------- | ------------ | ------------------ |
| Authority copy | Exaggerated, intentionally funny authority language. | Use serious authority language, not parody. |
| Names / people | Studio attribution visible. | Use mentor names only when real and approved. |
| Proof / numbers | Technical links and mock-science framing. | Use real proof only. |
| Institutional tone | Not institutional; product-satire. | Avoid as tone reference. |
| CTA clarity | Navigation links and contact paths visible. | Keep WhatsApp/register interest visible. |
| Content hierarchy | Strong section hierarchy. | Use this confidence with legal restraint. |

### 4.6 Accessibility & Performance Notes

| Area | Observation | Mithaq Requirement |
| ---- | ----------- | ------------------ |
| Reduced motion | Cannot confirm. | Required for Mithaq. |
| Keyboard access | Not fully tested. | All CTAs and nav must be keyboard accessible. |
| Text readability | Strong large copy. | Maintain readable DOM text in Arabic/English. |
| Mobile experience | Not fully captured. | Mobile must simplify 3D. |
| Loading / performance | Multiple canvases/assets imply performance risk. | Use budgets and fallbacks. |
| Audio control | No confirmed audio. | Mithaq audio must be user-controlled. |
| Fallback | Cannot confirm. | Required. |

---

## 5. Reference 2 Analysis - KODE Immersive

### 5.1 First Impression

| Item | Notes |
| ---- | ----- |
| First 5-second impression | A portal-like immersive world with explicit sound state and "enter" language. |
| Primary emotional effect | Spatial entry, tech-enabled wonder, cinematic immersion. |
| Clarity level | Atmospheric first, then service/content clarity. |
| Premium signals | Dark immersive atmosphere, sound controls, spatial copy, controlled nav, contact access. |
| Risk if copied blindly | Mithaq could become too XR/gaming/tech agency. |
| Mithaq takeaway | Borrow "entering a world" mechanics and sound-control discipline, not the tech-world vocabulary. |

### 5.2 Visual Direction

| Visual Element | Observed Pattern | Mithaq Use | Mithaq Avoid |
| -------------- | ---------------- | ---------- | ------------ |
| Color | Dark immersive palette. | Use dark legal chamber atmosphere. | Avoid sci-fi darkness. |
| Lighting | Spatial/cinematic. | Translate to warm legal chamber light. | Avoid XR/neon cues. |
| Materials | More atmospheric than material-specific. | Use for chamber depth, not object materials. | Avoid vague digital fog. |
| Typography | Large uppercase navigation/content labels. | Use crisp bilingual labels. | Avoid all-caps English dependency for Arabic. |
| Layout | Entry-screen feeling with scroll prompt. | Use as model for scroll-driven entry. | Avoid trapping users before CTA. |
| Trust signals | Team names, contact, office details, service sections. | Use real mentor/team/trust details. | Avoid agency-sales tone. |

### 5.3 Motion & Scroll Behavior

| Motion Pattern | Description | Timing / Feeling | Mithaq Relevance |
| -------------- | ----------- | ---------------- | ---------------- |
| Scroll behavior | Explicit "scroll for more" entry; immersive section flow. | User-controlled, spatial. | Strong reference for scroll-driven opening. |
| Scene transitions | Appears to move through immersive content states. | Cinematic. | Use for chamber progression. |
| Camera movement | Observed canvases suggest moving/interactive scene layers. | Spatial and depth-driven. | Useful for gavel-to-seal camera path. |
| Text reveal | Big statements unfold after immersive entry. | Dramatic but readable. | Use slower, authoritative reveals. |
| Sound / audio | Source hints include `AudioButton`; visible text includes "SOUND OFF". | Directly useful. | Mithaq should default muted and expose control. |
| Motion risks | Tech spectacle can overshadow content. | High-energy immersive. | Mithaq must keep CTA/content accessible. |

### 5.4 3D / WebGL / Technical Observations

| Technical / 3D Element | Observation | Mithaq Relevance |
| ---------------------- | ----------- | ---------------- |
| Central 3D object | More environmental than single-object. | Use only the spatial-entry lesson. |
| Canvas / WebGL usage | 11 canvases observed. | Mithaq should avoid unnecessary multiple canvases. |
| Scroll-to-3D mapping | Observed page text and canvases suggest scroll/scene progression. | Useful for scroll-driven legal chamber. |
| Asset loading | Nuxt build; CSS includes MouseTrail and AudioButton components; GTM present. | Shows sound/control components can be first-class UI. |
| Mobile behavior | Not persisted; requires later testing. | Mithaq mobile should simplify scene progression. |
| Fallback behavior | Cannot confirm. | Mithaq must define fallback. |
| Performance risk | Many canvases/audio/mouse trail imply heavy interaction risk. | Keep vertical slice lean. |

### 5.5 Content / Trust Structure

| Trust Pattern | Observed Use | Mithaq Application |
| ------------- | ------------ | ------------------ |
| Authority copy | "We see no limit..." experiential agency positioning. | Use confidence but legal-specific clarity. |
| Names / people | CEO/head of immersive named. | Use mentor names and roles when approved. |
| Proof / numbers | Less number-driven; more capability-driven. | Mithaq needs proof only if real. |
| Institutional tone | Creative studio tone. | Avoid for legal academy body copy. |
| CTA clarity | Contact and visit links are available. | Keep WhatsApp CTA visible during cinematic flow. |
| Content hierarchy | Big hero, services, team/contact. | Useful for converting immersive entry into clear sections. |

### 5.6 Accessibility & Performance Notes

| Area | Observation | Mithaq Requirement |
| ---- | ----------- | ------------------ |
| Reduced motion | Cannot confirm. | Required. |
| Keyboard access | Not fully tested. | Sound/nav/CTA must be keyboard accessible. |
| Text readability | Big text is readable but atmospheric density is high. | Avoid overlay conflicts. |
| Mobile experience | Requires later verification. | Simplify motion and avoid scroll traps. |
| Loading / performance | Multiple canvas/audio hints create risk. | Budget canvas and assets. |
| Audio control | Visible "SOUND OFF" and AudioButton asset observed. | Use visible mute/unmute control; muted by default. |
| Fallback | Cannot confirm. | Required. |

---

## 6. Reference 3 Analysis - Immersive Garden

### 6.1 First Impression

| Item | Notes |
| ---- | ----- |
| First 5-second impression | A refined digital-experience studio with project-led, scrollable premium case-study rhythm. |
| Primary emotional effect | Polished, curated, quietly confident. |
| Clarity level | Clear studio positioning and project browsing. |
| Premium signals | Smooth portfolio cadence, high-quality project thumbnails, understated typography. |
| Risk if copied blindly | Mithaq could become a design studio portfolio rather than a legal academy. |
| Mithaq takeaway | Borrow scroll choreography, section pacing, and project-card craft. |

### 6.2 Visual Direction

| Visual Element | Observed Pattern | Mithaq Use | Mithaq Avoid |
| -------------- | ---------------- | ---------- | ------------ |
| Color | Clean premium agency palette with project imagery. | Use restrained palette and visual rhythm. | Avoid making Mithaq look like an agency. |
| Lighting | Project-dependent. | Use equivalent polish in legal chamber scene. | Avoid inconsistent visual worlds. |
| Materials | Imagery/project-case-driven. | Translate to workshop/mentor cards. | Avoid scattered visual themes. |
| Typography | Clean, editorial, spacious. | Use for bilingual information hierarchy. | Avoid English-only microtype sizing. |
| Layout | Strong project grid/list hierarchy. | Adapt to workshops and mentors. | Avoid overloading every section with cards. |
| Trust signals | Client/project portfolio acts as proof. | Use real workshops/mentors/proof when available. |

### 6.3 Motion & Scroll Behavior

| Motion Pattern | Description | Timing / Feeling | Mithaq Relevance |
| -------------- | ----------- | ---------------- | ---------------- |
| Scroll behavior | Project browsing and reveal sequence; 2 canvases observed. | Authored but navigable. | Useful for non-trapping scroll. |
| Scene transitions | Smooth project-to-project rhythm. | Premium polish. | Good model for section transitions. |
| Camera movement | Not confirmed as object camera; canvas exists. | Subtle digital layer. | Use minimal camera movement for clarity. |
| Text reveal | Clean hierarchy, not overly theatrical. | Directly relevant. | Use for legal content readability. |
| Sound / audio | No audio observed. | Not relevant. | Sound should not imitate agency sites. |
| Motion risks | Portfolio motion may be too decorative if copied. | Controlled. | Tie all Mithaq motion to message. |

### 6.4 3D / WebGL / Technical Observations

| Technical / 3D Element | Observation | Mithaq Relevance |
| ---------------------- | ----------- | ---------------- |
| Central 3D object | No single central object observed from DOM. | Mithaq should keep its own seal/gavel object logic. |
| Canvas / WebGL usage | 2 canvases observed. | Supports restrained canvas use. |
| Scroll-to-3D mapping | Likely present in visual layer, but exact mapping not confirmed. | Use as pacing reference, not implementation proof. |
| Asset loading | Project links and many images; GTM present. | Use progressive/lazy content strategy. |
| Mobile behavior | Not persisted; needs later test. | Layout must handle bilingual content. |
| Fallback behavior | Cannot confirm. | Required. |
| Performance risk | Many images/project assets. | Optimize image/video/poster loading. |

### 6.5 Content / Trust Structure

| Trust Pattern | Observed Use | Mithaq Application |
| ------------- | ------------ | ------------------ |
| Authority copy | Short positioning line: innovative digital experiences studio. | Short, confident Mithaq positioning. |
| Names / people | Portfolio/client work more important than staff. | For Mithaq, mentors should be more visible. |
| Proof / numbers | Project/client breadth acts as proof. | Use real workshop/proof content only. |
| Institutional tone | Creative industry tone. | Adapt hierarchy, not voice. |
| CTA clarity | Project exploration CTA. | Workshop details + WhatsApp CTA must be clearer. |
| Content hierarchy | Strong project titles and descriptions. | Use for workshop previews and trust blocks. |

### 6.6 Accessibility & Performance Notes

| Area | Observation | Mithaq Requirement |
| ---- | ----------- | ------------------ |
| Reduced motion | Cannot confirm. | Required. |
| Keyboard access | Not fully tested. | Required for nav/cards/modals. |
| Text readability | Good hierarchy in inspected text. | Maintain in Arabic and English. |
| Mobile experience | Requires later verification. | Use content-first responsive design. |
| Loading / performance | Many images and project assets. | Lazy load non-critical assets. |
| Audio control | No audio observed. | Mithaq audio must be optional. |
| Fallback | Cannot confirm. | Required. |

---

## 7. Reference 4 Analysis - Floema

### 7.1 First Impression

| Item | Notes |
| ---- | ----- |
| First 5-second impression | A premium product/category site with calm editorial language and strong material/product hierarchy. |
| Primary emotional effect | Durable, crafted, sustainable, calm. |
| Clarity level | Clear category and product purpose. |
| Premium signals | Large calm hero, structured categories, product imagery, sustainability/person proof. |
| Risk if copied blindly | Mithaq could become too lifestyle/product-catalog-like. |
| Mithaq takeaway | Borrow calm editorial hierarchy and structured category rhythm. |

### 7.2 Visual Direction

| Visual Element | Observed Pattern | Mithaq Use | Mithaq Avoid |
| -------------- | ---------------- | ---------- | ------------ |
| Color | Natural/product-led palette. | Use restraint and warmth. | Avoid outdoor/lifestyle cues. |
| Lighting | Product/material clarity. | Translate to desk, paper, seal materials. | Avoid bright catalog look. |
| Materials | Durable products and sustainability language. | Use material authenticity for legal objects. | Avoid catalog-like product grid dominance. |
| Typography | Calm editorial/product labels. | Useful for bilingual section structure. | Avoid small labels that break in Arabic. |
| Layout | Clear category list and product/news sections. | Use for workshops/tracks. | Avoid e-commerce feel. |
| Trust signals | Founder quote, sustainability, legal links, catalogs. | Use mentor/proof/FAQ equivalents. |

### 7.3 Motion & Scroll Behavior

| Motion Pattern | Description | Timing / Feeling | Mithaq Relevance |
| -------------- | ----------- | ---------------- | ---------------- |
| Scroll behavior | Standard scroll with polished reveals/category progression. | Calm, non-trapping. | Good model for middle sections after opening. |
| Scene transitions | Editorial/content transitions rather than cinematic scenes. | Smooth, practical. | Useful for static/simplified sections. |
| Camera movement | No canvas observed. | Not relevant. | Mithaq can use static fallback/editorial sections similarly. |
| Text reveal | Clear category sequencing. | Strong for workshops/pillars. | Keep Arabic length in mind. |
| Sound / audio | No sound observed. | Not relevant. | Mithaq sound should stay only in opening if used. |
| Motion risks | Product catalog feel. | Low. | Avoid turning workshops into products for sale. |

### 7.4 3D / WebGL / Technical Observations

| Technical / 3D Element | Observation | Mithaq Relevance |
| ---------------------- | ----------- | ---------------- |
| Central 3D object | No canvas observed. | Useful as static editorial fallback model. |
| Canvas / WebGL usage | 0 canvases observed. | Shows premium can exist without WebGL in every section. |
| Scroll-to-3D mapping | None observed. | Not a 3D reference. |
| Asset loading | Nuxt build, many images, Sanity CDN/PDF links. | Useful content/product asset model. |
| Mobile behavior | Not persisted; should be checked later. | Bilingual cards need flexible layout. |
| Fallback behavior | Static by nature. | Model for Mithaq reduced-motion mode. |
| Performance risk | Image-heavy site. | Optimize image loading. |

### 7.5 Content / Trust Structure

| Trust Pattern | Observed Use | Mithaq Application |
| ------------- | ------------ | ------------------ |
| Authority copy | Clear product/category purpose. | Clear workshop/pillar labels. |
| Names / people | Founder quote appears in page text. | Mentor quote/authority lines can work. |
| Proof / numbers | Category counts and sustainability claims. | Use only real counts. |
| Institutional tone | Practical, durable, established. | Useful for mature academy tone. |
| CTA clarity | "Ver Produtos" and catalog downloads are clear. | Use workshop detail + WhatsApp CTA. |
| Content hierarchy | Categories, recent items, collections, quote. | Strong model for workshops + mentors + trust. |

### 7.6 Accessibility & Performance Notes

| Area | Observation | Mithaq Requirement |
| ---- | ----------- | ------------------ |
| Reduced motion | Not confirmed. | Required. |
| Keyboard access | Not fully tested. | Required. |
| Text readability | Strong readable editorial text. | Good model. |
| Mobile experience | Requires later verification. | Card grids must handle Arabic/English. |
| Loading / performance | 57 images observed. | Optimize posters/images. |
| Audio control | No audio observed. | Keep sound isolated and controlled. |
| Fallback | Static structure works without canvas. | Useful for Mithaq fallback. |

---

## 8. Reference 5 Analysis - Lenz & Staehelin

### 8.1 First Impression

| Item | Notes |
| ---- | ----- |
| First 5-second impression | A serious institutional law firm with a clear positioning line and strong expertise taxonomy. |
| Primary emotional effect | Authority, scale, stability, legal confidence. |
| Clarity level | High. The firm, expertise, and multilingual navigation are immediately clear. |
| Premium signals | Minimal visual noise, strong copy hierarchy, practice/sector taxonomy, multilingual structure. |
| Risk if copied blindly | Mithaq could look like a law firm rather than a legal academy. |
| Mithaq takeaway | Borrow trust architecture and legal content hierarchy, not static law-firm styling. |

### 8.2 Visual Direction

| Visual Element | Observed Pattern | Mithaq Use | Mithaq Avoid |
| -------------- | ---------------- | ---------- | ------------ |
| Color | Institutional restrained palette. | Use authority and restraint. | Avoid corporate grey flatness. |
| Lighting | Not visual-cinematic; content-led. | Use as content/trust reference only. | Do not copy lack of cinematic layer. |
| Materials | No 3D/material focus. | Not applicable. | Do not use as 3D reference. |
| Typography | Serious hierarchy and clear taxonomy. | Strong reference for bilingual legal hierarchy. | Avoid too static/traditional feel. |
| Layout | Menus, expertise, sectors, news, people/about/contact. | Use structured navigation and trust sections. | Avoid overbuilding law-firm IA. |
| Trust signals | Multilingual routes, practices, sectors, lawyers/tax experts, news/insights. | Use mentors, workshops, FAQ, proof with similar clarity. |

### 8.3 Motion & Scroll Behavior

| Motion Pattern | Description | Timing / Feeling | Mithaq Relevance |
| -------------- | ----------- | ---------------- | ---------------- |
| Scroll behavior | Traditional content scroll; no canvas observed. | Stable and clear. | Useful contrast: content clarity must survive without 3D. |
| Scene transitions | Conventional page sections. | Low-motion. | Use for legal/trust clarity. |
| Camera movement | None observed. | Not relevant. | Mithaq should keep legal content in DOM. |
| Text reveal | Content-first. | Clear. | Good for FAQ/trust/instructor copy. |
| Sound / audio | None observed. | Not relevant. | Legal authority does not need sound. |
| Motion risks | Too static if copied fully. | Low-motion. | Mithaq needs cinematic layer without losing clarity. |

### 8.4 3D / WebGL / Technical Observations

| Technical / 3D Element | Observation | Mithaq Relevance |
| ---------------------- | ----------- | ---------------- |
| Central 3D object | None observed. | Not a 3D reference. |
| Canvas / WebGL usage | 0 canvases observed. | Content authority can live outside canvas. |
| Scroll-to-3D mapping | None. | Not applicable. |
| Asset loading | TYPO3 paths observed; Matomo analytics; multilingual links EN/DE/FR/CN. | Strong reference for language routing and analytics ownership. |
| Mobile behavior | Not persisted; responsive behavior should be tested later if needed. | Use multilingual navigation as reference. |
| Fallback behavior | Static content site. | Reinforces DOM-first requirement. |
| Performance risk | Lower WebGL risk; image/content-heavy menus. | Good benchmark for content accessibility. |

### 8.5 Content / Trust Structure

| Trust Pattern | Observed Use | Mithaq Application |
| ------------- | ------------ | ------------------ |
| Authority copy | "The world's Swiss law firm" and clear expertise introduction. | Use one concise academy positioning line. |
| Names / people | Lawyers/tax experts are central to credibility. | Mentors should be prominent when assets arrive. |
| Proof / numbers | Trust from practices, sectors, insights, multilingual/global footprint. | Use verified proof only; taxonomy itself can communicate seriousness. |
| Institutional tone | Strong legal authority. | Directly useful, adapted to academy/training. |
| CTA clarity | "How can we help you?" and expertise paths. | Use "Register Interest" / WhatsApp without cheap tone. |
| Content hierarchy | Expertise, sectors, news, people, about, contact. | Strong reference for IA clarity. |

### 8.6 Accessibility & Performance Notes

| Area | Observation | Mithaq Requirement |
| ---- | ----------- | ------------------ |
| Reduced motion | Low-motion site reduces risk. | Keep legal sections readable without animation. |
| Keyboard access | Not fully tested. | Required for nav, modals, forms. |
| Text readability | Strong. | Use comparable clarity for Arabic/English. |
| Mobile experience | Needs later testing. | Bilingual nav must stay clear. |
| Loading / performance | No canvas observed. | Useful content-first benchmark. |
| Audio control | No audio observed. | Mithaq sound must be optional. |
| Fallback | DOM-first by nature. | Model for fallback content structure. |

---

## 9. Screenshot Annotations

Screenshots were attempted using the in-app browser screenshot API. The browser runtime denied file writes to both:

- `D:/Clinets/MITHAQ/mithaq-reference-analysis/screenshots/`
- `C:/tmp/mithaq-reference-screenshots/`

Because screenshots could not be persisted, this table documents the intended captures and the observed lesson from live inspection.

| Reference | Screenshot Label | What It Shows | Mithaq Lesson |
| --------- | ---------------- | ------------- | ------------- |
| Oryzo AI | Hero | Object-led product scene with bold editorial promise. | Use one symbolic object, but keep tone serious. |
| Oryzo AI | Motion moment | Object/content sections around product claims. | Tie seal/gavel motion to message. |
| Oryzo AI | Typography/content | Oversized confident copy. | Use confident headings, not parody. |
| Oryzo AI | Mobile view | Not persisted. | Must later verify 3D simplification. |
| KODE Immersive | Hero | Entry-world language, sound state, immersive atmosphere. | Strong model for chamber entry. |
| KODE Immersive | Spatial transition | Scroll-for-more / enter-world progression. | Use scroll-driven gavel-to-seal reveal without trapping user. |
| KODE Immersive | Audio control | Visible "SOUND OFF" / AudioButton clues. | Sound must be visibly controlled. |
| KODE Immersive | Mobile view | Not persisted. | Mobile opening must simplify. |
| Immersive Garden | Hero | Studio positioning and polished project rhythm. | Use authored scroll polish. |
| Immersive Garden | Scroll moment | Project reveals and case-study cadence. | Use for workshop/mentor section rhythm. |
| Immersive Garden | Content hierarchy | Project names/descriptions. | Workshop cards need similar hierarchy. |
| Immersive Garden | Mobile view | Not persisted. | Bilingual cards need testing. |
| Floema | Hero | Calm editorial/product promise. | Middle sections can be premium without heavy 3D. |
| Floema | Category section | Numbered categories and product CTAs. | Good model for training pillars/workshops. |
| Floema | Trust/content | Founder quote, sustainability, legal links. | Use mentor/trust content when real. |
| Floema | Mobile view | Not persisted. | Static fallback pattern to test later. |
| Lenz & Staehelin | Hero | Legal positioning and expertise prompt. | Trust through clarity and restraint. |
| Lenz & Staehelin | Navigation | Multilingual EN/DE/FR/CN links and expertise taxonomy. | Strong model for bilingual IA discipline. |
| Lenz & Staehelin | Trust/content | Practices, sectors, lawyers/tax experts, news/insights. | Mithaq should use academy equivalents: workshops, mentors, proof, FAQ. |
| Lenz & Staehelin | Mobile view | Not persisted. | Must later verify bilingual navigation patterns. |

---

## 10. Source-Inspection Notes

| Reference | Observed Technical Clue | Confidence | Notes |
| --------- | ----------------------- | ---------- | ----- |
| Oryzo AI | 6 canvas elements; `_astro` stylesheet; 18 images; 17 pictures; 43 SVGs | High for observed DOM, low for exact implementation | Appears canvas-heavy and asset-rich. Exact WebGL library not visible from inspected script hints. |
| Oryzo AI | Links to GitHub paper/model/code and Lusion studio/contact | High | Trust/proof structure is intentionally product/AI-satire. |
| KODE Immersive | 11 canvas elements; Nuxt assets; CSS names include `MouseTrail` and `AudioButton`; GTM present | High for DOM clues | Strong evidence of immersive canvas layer and explicit audio UI. |
| KODE Immersive | Visible text includes "SOUND OFF" and "SCROLL FOR MORE" | High | Useful for Mithaq audio and scroll-entry controls. |
| Immersive Garden | 2 canvas elements; many project links; GTM present | High | More restrained canvas count than KODE; project-driven content structure. |
| Immersive Garden | Asset paths include multiple page/block CSS bundles | Medium | Suggests componentized experience; exact framework not claimed. |
| Floema | 0 canvas elements; 57 images; Nuxt assets; Sanity CDN/PDF links | High | Premium editorial/product experience without WebGL. Useful fallback/static reference. |
| Floema | Portuguese `lang="pt"`; legal/privacy links visible | High | Demonstrates strong content/legal footer structure. |
| Lenz & Staehelin | 0 canvas elements; `lang="en-GB"`; EN/DE/FR/CN language links; TYPO3 paths; Matomo analytics | High | Strong institutional/multilingual/legal content reference. |
| Lenz & Staehelin | Expertise taxonomy and practice/sector links visible | High | Useful for Mithaq IA clarity, not visual imitation. |

---

## 11. Patterns to Borrow

| Pattern | Source Reference | Why It Works | How Mithaq Should Use It |
| ------- | ---------------- | ------------ | ------------------------ |
| Single symbolic object | Oryzo AI | Focuses attention and creates memorable brand recall. | Seal is the central symbol; gavel is only trigger. |
| Spatial entry into world | KODE Immersive | Makes the user feel they enter a designed environment. | Scroll into a legal knowledge chamber. |
| Authored scroll choreography | Immersive Garden | Motion feels deliberate and premium. | Use scroll pacing for gavel/seal/first content. |
| Calm premium restraint | Floema | Shows that premium sections can be quiet and content-led. | Use static/editorial fallback and middle sections. |
| Legal content authority | Lenz & Staehelin | Trust comes from structure, taxonomy, language, and restraint. | Use mentors, workshops, FAQ, and proof with legal clarity. |
| Sound control pattern | KODE Immersive | Makes audio explicit and user-controlled. | Use muted/default-off sound with visible control. |
| Multilingual discipline | Lenz & Staehelin | Language switching is structural, not decorative. | Plan Arabic/English routes and metadata early. |

---

## 12. Patterns to Avoid

| Pattern to Avoid | Seen In / Risk Source | Why Mithaq Should Avoid It | Safer Alternative |
| ---------------- | --------------------- | -------------------------- | ----------------- |
| Overly theatrical motion | KODE risk if copied blindly | Could feel like XR/game marketing. | Slow ceremonial legal motion. |
| Product-satire tone | Oryzo AI | Undermines legal academy seriousness. | Premium restrained authority. |
| Game-like interaction | KODE / immersive sites risk | Mithaq is not a game or XR demo. | Scroll-led story with clear CTA. |
| Decorative 3D without message | All 3D-heavy references risk | Weakens conversion and clarity. | Every 3D moment must reveal meaning. |
| Weak CTA clarity | Atmospheric sites risk | Users may admire but not inquire. | Persistent WhatsApp and clear CTA path. |
| Content hidden inside canvas | WebGL references risk | Hurts accessibility, SEO, bilingual copy. | Keep all key content in semantic DOM. |
| Fake urgency | Conversion sites generally | P0.06 excludes fake cohort/deadline logic. | Use general interest/WhatsApp inquiry. |
| Law-firm sameness | Lenz if copied literally | Mithaq is an academy, not a firm. | Borrow hierarchy, not static firm identity. |

---

## 13. Mithaq-Specific Translation

| Mithaq Area | Final Research Direction |
| ----------- | ------------------------ |
| Opening | Scroll-driven gavel trigger to seal reveal, inspired by spatial-entry and object-led references. |
| Seal | Treat as recurring identity object; it must be readable and brand-led, not generic legal decoration. |
| Gavel | Use as controlled ceremonial trigger only. Avoid violent impact, cracks, or glass effects. |
| Scroll pacing | Use pinned/controlled progression only for the vertical slice; allow escape/skip and keep CTA reachable. |
| Sound effects | Optional, muted by default or user-initiated, visible control, restrained gavel impact. |
| Typography | Combine legal authority with bilingual flexibility; avoid English-only sizing systems. |
| Bilingual layout | Plan Arabic and English in MVP from the beginning; RTL/LTR must affect layout, nav, forms, metadata. |
| Workshop previews | Use Floema/Immersive Garden-style structured cards, clearly marked as placeholder until final content arrives. |
| Mentor section | Scene 07 only; use premium placeholders for prototype, real portraits for final polish. |
| Trust section | Lenz-style authority hierarchy; forward-compatible if proof is missing; no fake metrics. |
| CTA behavior | WhatsApp is primary; keep visible, professional, and non-desperate. |
| Mobile behavior | Simplify 3D, shorten scroll strain, prioritize CTA and content. |
| Accessibility | DOM-first content, reduced motion, keyboard access, audio control, no canvas-only text. |
| Performance | One shared WebGL layer where possible, lazy assets, image budgets, mobile fallbacks. |

---

## 14. Scroll-Driven Opening Recommendation

Mithaq should make the gavel-to-seal sequence scroll-driven through a short controlled vertical slice:

1. Initial viewport: legal chamber surface and faint seal trace are visible immediately.
2. First scroll segment: gavel enters with slow, controlled movement.
3. Second scroll segment: gavel strike triggers subtle surface illumination, not cracks or explosion.
4. Third scroll segment: Mithaq Seal completes and becomes the hero object.
5. Hero content and WhatsApp CTA must appear before the user feels trapped.

Rules:

- Do not force a fixed 8-second wait.
- Do not block access to content.
- Include skip or "continue" behavior if the scroll sequence becomes too long.
- Keep reduced-motion fallback as static/fade reveal.
- On mobile, compress the sequence and prioritize hero CTA.

---

## 15. Sound Effects Recommendation

Sound can be included, but only as a controlled enhancement.

Rules:

- Default muted or activated only after user interaction.
- Visible mute/unmute control if sound exists.
- Gavel impact should be deep, restrained, and realistic.
- No dramatic trailer hits, glass sounds, horror textures, or aggressive reverbs.
- Sound must not be required to understand the sequence.
- Respect reduced-motion and accessibility settings.
- Track audio toggle only if analytics consent permits.

Best reference lesson:

KODE's visible sound-state pattern is useful. Mithaq should be quieter and more formal.

---

## 16. Bilingual / RTL Research Notes

Safe patterns for bilingual Arabic/English layouts:

- Lenz-style language structure and clear multilingual routing.
- Floema-style category hierarchy with flexible cards.
- Immersive Garden-style project/workshop summaries if text blocks are allowed to expand.
- Oryzo/KODE large type only if tested in Arabic and English separately.

Risky patterns:

- All-caps English labels as core UI language.
- Very tight typographic layouts.
- Canvas-rendered key text.
- Fixed-width CTAs that cannot handle Arabic text.
- Motion timings tied to exact line lengths.

Mithaq requirements:

- Arabic and English content must be planned together.
- Arabic remains visually prioritized, but English is part of MVP planning.
- Use `dir="rtl"` and `dir="ltr"` correctly.
- Use CSS logical properties.
- Test nav, CTA, cards, forms, and FAQ in both languages.

---

## 17. Accessibility Notes

Mithaq must not inherit the accessibility risks of experimental WebGL references.

Requirements:

- All essential content in semantic DOM.
- Keyboard-accessible navigation, modals, forms, and audio controls.
- Reduced-motion mode.
- WebGL fallback.
- Text contrast tested on dark backgrounds.
- Audio off by default or user-initiated.
- Form labels in Arabic and English.
- Modal workshop previews must trap and restore focus correctly.
- No essential legal/registration information embedded only in 3D.

---

## 18. Performance Notes

Observed risks:

- Oryzo AI and KODE use multiple canvas elements.
- KODE includes audio/mouse-trail clues.
- Immersive Garden and Floema are asset-rich.
- Floema demonstrates premium without canvas.
- Lenz demonstrates authority without animation.

Mithaq performance direction:

- Use one shared WebGL canvas where possible.
- Validate vertical slice before full build.
- Keep 3D scope focused on opening/hero/seal.
- Lazy-load workshop/mentor/trust media.
- Use compressed GLB/KTX2 assets.
- Provide mobile simplification.
- Keep DOM content visible before heavy assets complete.

---

## 19. Final Reference Strategy

Mithaq should synthesize the references this way:

- From Oryzo AI: object-led symbolic storytelling.
- From KODE Immersive: spatial entry and professional audio control.
- From Immersive Garden: authored scroll choreography and premium transition craft.
- From Floema: calm editorial structure and non-WebGL premium fallback logic.
- From Lenz & Staehelin: legal authority, content taxonomy, multilingual trust structure.

Final rule:

Mithaq should feel like a premium bilingual legal knowledge chamber, not a product gag, game-like immersive demo, law-firm template, or course platform.

---

## 20. Phase 1 Readiness Notes

P1.01 can inform Phase 1 research/planning and vertical-slice strategy.

Allowed next uses:

- Research synthesis.
- Storyflow planning.
- Motion principles.
- Bilingual IA planning.
- Accessibility/performance requirements.
- Vertical Slice First definition.

Still not authorized:

- Final UI design.
- Final 3D production.
- Final seal design.
- Frontend implementation.
- Production copy.
- Legal/compliance-sensitive claims.

Production remains conditional on unresolved assets, content, contact details, technical environment, timeline/budget/resources, and final sign-off items.

