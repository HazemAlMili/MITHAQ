# Mithaq Typography Specimen

**Official Ticket ID:** P2.03  
**Official Ticket Name:** Typography Specimen  
**Phase:** Phase 2 - Creative Concept Development  
**Priority:** P0  
**Status:** PASS WITH CONDITIONS  
**Prepared date:** 2026-06-18  
**Typeface families tested:** Cormorant Garamond, DM Sans, JetBrains Mono, Tajawal, Lemonada  

---

## 1. Executive Summary

This specimen validates Mithaq's planned bilingual typography direction before final UI design or frontend production begins.

Decision:

**Proceed with the planned typography system, with conditions.**

Recommended hierarchy:

- English display: **Cormorant Garamond**, limited to large authority moments.
- English body/UI: **DM Sans**, used for clarity, forms, FAQ, cards, and CTAs.
- Labels/system: **JetBrains Mono**, used sparingly for scene numbers and metadata only.
- Arabic body/UI: **Tajawal**, approved as the primary Arabic reading and UI family.
- Arabic display: **Tajawal Bold is the safer default. Lemonada should be limited to accent display moments only until client/Arabic copy review confirms it feels mature enough.**

Reason:

- Cormorant Garamond communicates editorial legal authority at large sizes, but can feel too classical if overused.
- DM Sans reads well and supports functional clarity, but should not dominate emotional hero moments or the site may feel SaaS-like.
- JetBrains Mono gives precision to scene labels, but becomes too technical when overused.
- Tajawal is readable and practical for Arabic UI/body needs.
- Lemonada adds Arabic personality but risks feeling decorative/playful in legal-academy contexts.

No final UI screens, final website copy, production implementation, or new roadmap ticket was created.

---

## 2. Current Mithaq Decisions

- Mithaq is a premium bilingual 3D legal academy portfolio / landing experience.
- MVP planning is bilingual.
- Arabic and English are equal product requirements.
- The visual world is dark, legal, premium, restrained, cinematic, and conversion-aware.
- P2.02 colors are candidate tokens, not final brand-approved UI.
- Filled gold CTAs require near-black text, never white text.
- `gold-dim` is decorative only.
- Red must not be used as body text on dark backgrounds.
- Typography must support WhatsApp conversion, workshop clarity, mentor credibility, FAQ readability, and final CTA trust.
- No fake luxury, playful course-platform typography, LMS, dashboard, or generic course-site feeling.

---

## 3. Typeface Overview

| Typeface | Role | Weights Tested | Notes |
| -------- | ---- | -------------- | ----- |
| Cormorant Garamond | English display | 400 Italic / 600 / 700 | Strong legal-editorial authority; use only for display and selective accents. |
| DM Sans | English body/UI | 300 / 400 / 500 / 600 | Clear and modern; keep body/UI, avoid letting it define the emotional brand alone. |
| JetBrains Mono | Labels/system | 400 / 500 | Good for scene numbers and metadata; use sparingly to avoid tech-dashboard tone. |
| Tajawal | Arabic body/UI | 400 / 500 / 700 | Best Arabic default for body, forms, CTAs, FAQ, and safe display. |
| Lemonada | Arabic display | 400 / 600 / 700 | Use with caution; may feel decorative unless restricted to short ceremonial accents. |

---

## 4. English Display Tests

Family: **Cormorant Garamond**

| Token | Size | Line Height | Weight | Test Result |
| ----- | ---: | ----------: | -----: | ----------- |
| Display XL | 88px | 0.95-1.05 | 600/700 | Strong cinematic hero scale; long line needs careful wrapping. |
| Display L | 72px | 1.0-1.1 | 600/700 | Best for primary scene headlines. |
| Display M | 56px | 1.05-1.15 | 600 | Good section headline size. |
| Heading L | 40px | 1.15-1.25 | 600 | Works for major section titles. |
| Heading M | 32px | 1.2-1.3 | 600 | Useful for mentor/card titles, but DM Sans may be clearer in dense cards. |

Test lines:

- Practical Legal Training for the Lawyers the Market Actually Needs.
- From Legal Study to Professional Readiness.
- The Mithaq Method
- Legal Research & Opinion
- Hall of Mentors

Findings:

- Sentence case feels more premium and less salesy than all caps.
- Title case works for short headings only.
- Italic 400 is useful for one ceremonial accent phrase, not for long copy.
- Parchment on dark is the primary display color.
- Gold display text should be rare; use gold for small labels, dividers, or short accent words only.
- Cormorant should not be used for body text because readability and tone become too literary.

---

## 5. Arabic Display Tests

Families: **Lemonada** and **Tajawal Bold**

| Token | Size | Line Height | Lemonada Result | Tajawal Bold Result |
| ----- | ---: | ----------: | --------------- | ------------------- |
| Arabic Display L | 56px | 1.2-1.3 | Expressive but decorative risk | Stronger legal clarity |
| Arabic Display M | 48px | 1.2-1.3 | Acceptable for short ceremonial title | Recommended for hero/scene use |
| Arabic Heading L | 40px | 1.25-1.35 | Starts to feel ornamental | Recommended |
| Arabic Heading M | 32px | 1.3-1.4 | Usable only for short accent | Recommended |
| Arabic Heading S | 28px | 1.35-1.45 | Too decorative for functional UI | Recommended |

Test lines:

- ميثاق — من الدراسة إلى الاحتراف
- تدريب قانوني عملي للمحامين الذين يحتاجهم السوق
- منهج ميثاق
- البحث القانوني والرأي القانوني
- الصياغة القانونية والمذكرات

Finding:

**Lemonada should not be the default Arabic display font for Mithaq.** It can work in a short ceremonial accent, but its rounded, expressive rhythm weakens the legal authority needed for hero and scene headings. Tajawal Bold is safer, more mature, and more readable across Arabic hero, card, FAQ, and CTA contexts.

Recommendation:

- Arabic display default: **Tajawal 700**.
- Lemonada: **accent-only**, pending client/Arabic copywriter review.
- Future design decision may test a more formal Arabic display face, but this ticket does not add a new official font.

---

## 6. English Body Tests

Family: **DM Sans**

| Size / Line Height | Weight | Use | Result |
| ------------------ | -----: | --- | ------ |
| 20px / 1.7 | 400 | Hero supporting copy | Pass; comfortable and clear. |
| 18px / 1.7 | 400 | Main paragraph | Pass; primary desktop body size. |
| 16px / 1.65 | 400/500 | Cards, FAQ, forms | Pass; minimum reliable UI body. |
| 14px / 1.55 | 400/500 | Helper text, metadata support | Pass with caution; avoid long paragraphs. |

Dark background tests:

| Background | Result |
| ---------- | ------ |
| `mithaq-void` | Pass with parchment and parchment-dim. |
| `mithaq-ink` | Pass with parchment and parchment-dim. |
| `mithaq-chamber` | Pass with parchment and parchment-dim. |
| `mithaq-wood` | Pass with parchment and parchment-dim. |

Findings:

- DM Sans is best for readable content, form labels, FAQ answers, workshop body text, and button text.
- Weight 300 is elegant but too light for critical copy on dark backgrounds; reserve for large supporting copy only or remove if performance is tightened.
- Weight 600 is useful for CTA and short UI emphasis.
- Overuse can make Mithaq feel like a modern SaaS site, so emotional sections should keep Cormorant/Tajawal display leadership.

---

## 7. Arabic Body Tests

Family: **Tajawal**

| Size / Line Height | Weight | Use | Result |
| ------------------ | -----: | --- | ------ |
| 20px / 1.8 | 400/500 | Hero supporting Arabic copy | Pass; generous and comfortable. |
| 18px / 1.8 | 400 | Main Arabic paragraph | Pass; recommended body default. |
| 16px / 1.75 | 400/500 | Cards, FAQ, forms | Pass; minimum reliable Arabic UI body. |
| 14px / 1.65 | 500 | Helper/meta text | Pass with caution; use only short labels. |

Test line:

تساعد ميثاق خريجي الحقوق والمحامين في بداية الطريق على الاستعداد للممارسة العملية.

Findings:

- Tajawal is readable and practical for Arabic body/UI.
- Arabic needs more line-height than English, especially in FAQ and card body text.
- Tajawal 700 works better than Lemonada for Arabic display headings when legal seriousness matters.
- No Arabic body text should use tight line-height or decorative display treatment.

---

## 8. Labels / Scene Numbers

Family: **JetBrains Mono**

Test labels:

- 01 / 02 / 03
- WORKSHOP
- METHOD
- MENTORS
- FAQ
- REGISTER INTEREST
- 3-DAY INTENSIVE / BEGINNER / PRACTICAL

| Size | Letter Spacing | Weight | Result |
| ---: | -------------: | -----: | ------ |
| 11px | 0.08em | 400 | Readable; least tech-heavy. |
| 11px | 0.12em | 500 | Best scene-number balance. |
| 12px | 0.12em | 500 | Best metadata label size. |
| 12px | 0.15em | 500 | Premium but wide; use short labels only. |
| 13px | 0.08em | 400/500 | Useful for badges, but can feel too technical. |

Recommendation:

- Scene numbers: **11px / 1.35 / 500 / 0.12em**.
- Metadata labels: **12px / 1.35 / 500 / 0.08-0.12em**.
- Avoid long labels in mono.
- Do not use mono for paragraph copy, CTA text, or Arabic.

---

## 9. Bilingual Pairing Tests

### Option A - Separate Arabic And English Blocks

Arabic and English appear as separate blocks, with independent font choices and line-height.

Result: **Pass with caution.** Works for bilingual overview sections, but can become dense in the hero.

### Option B - Arabic Primary / English Secondary

Arabic headline leads; English appears as smaller support.

Result: **Recommended for Arabic-first localized pages or bilingual brand moments.** Preserves Arabic maturity and avoids English dominance.

### Option C - English Primary / Arabic Secondary

English headline leads; Arabic appears as smaller support.

Result: **Use only on English-localized pages.** Not recommended as the default bilingual MVP pattern because Arabic may feel secondary.

### Option D - Language-Specific Layouts

Arabic and English do not appear together in the same hero; each language gets its own localized layout.

Result: **Best recommendation for Mithaq MVP.** It protects composition, performance, copy hierarchy, accessibility, and mobile wrapping.

Final bilingual recommendation:

Use **Option D** for primary pages. Use **Option B** only for brand/signature moments where both languages intentionally appear together.

Rule:

Do not mix Cormorant and Tajawal/Lemonada in the same line. Use separate elements.

---

## 10. CTA Typography Tests

CTA types tested:

- Primary outline gold CTA
- Filled gold CTA with near-black text
- Text link CTA
- WhatsApp CTA
- Workshop card CTA
- Form submit button

English CTA text:

- Register Interest
- View Workshop Details
- Ask About This Workshop

Arabic CTA text:

- سجّل اهتمامك
- اعرف تفاصيل الورشة
- اسأل عن هذه الورشة

| CTA Type | English Font | Arabic Font | Recommended Weight | Result |
| -------- | ------------ | ----------- | ------------------ | ------ |
| Primary outline gold | DM Sans | Tajawal | 600 / 700 | Pass |
| Filled gold | DM Sans | Tajawal | 600 / 700 | Pass only with near-black text |
| Text link | DM Sans | Tajawal | 500 / 500 | Pass |
| WhatsApp CTA | DM Sans | Tajawal | 600 / 700 | Pass |
| Workshop card CTA | DM Sans | Tajawal | 500 / 500 | Pass |
| Form submit | DM Sans | Tajawal | 600 / 700 | Pass |

Findings:

- English CTA should use sentence case or title case, not full uppercase.
- Arabic CTA should use Tajawal 700 for primary actions and Tajawal 500 for secondary actions.
- White text on gold is not allowed.
- Filled gold CTAs must use `mithaq-void` or equivalent near-black text.
- Focus state should use `gold-light` ring plus outline, not color shift alone.

---

## 11. Forms / FAQ / Workshop Typography Tests

Specimen blocks tested, not final UI:

| Context | Recommended Typography | Result |
| ------- | ---------------------- | ------ |
| FAQ question | DM Sans 18/600 or Tajawal 18/700 | Pass |
| FAQ answer | DM Sans 16-18/400 or Tajawal 16-18/400 | Pass |
| Workshop title | Cormorant 32/600 for English; Tajawal 28-32/700 for Arabic | Pass |
| Workshop body | DM Sans 16/400; Tajawal 16/400 | Pass |
| Metadata | JetBrains Mono 11-12/500; Arabic metadata should use Tajawal 14/500 | Pass |
| Form label | DM Sans 14/500; Tajawal 15/500 | Pass |
| Input text | DM Sans 16/400; Tajawal 16/400 | Pass |
| Helper text | DM Sans 14/400; Tajawal 14/400 | Pass |
| Error text | Parchment on red-authority surface or parchment + error border | Pass with P2.02 guardrails |
| Mentor name | Cormorant 32/600; Tajawal 28-32/700 | Pass |
| Mentor title/bio | DM Sans 14-16; Tajawal 15-16 | Pass |
| Trust stat | Cormorant/Tajawal display number plus DM/Tajawal label | Pass only with verified content |

---

## 12. Mobile Wrapping Tests

Widths tested conceptually in the rendered specimen:

- 320px
- 375px
- 390px
- 430px

Critical phrase behavior:

| Phrase | Mobile Result | Recommendation |
| ------ | ------------- | -------------- |
| Practical Legal Training for the Lawyers the Market Actually Needs. | Wraps to 3-5 lines depending on width | Use 42-46px max hero display; avoid 48px for long English line at 320px. |
| ميثاق — من الدراسة إلى الاحتراف | Wraps cleanly | Use Tajawal 700 at 38-44px with 1.18-1.25 line-height. |
| تدريب قانوني عملي للمحامين الذين يحتاجهم السوق | Long Arabic headline needs generous line-height | Use 32-38px or split into localized lines. |
| Register Interest | Fits | DM Sans 16/600. |
| سجّل اهتمامك | Fits | Tajawal 16-17/700. |
| View Workshop Details | Fits but may need compact button padding | Avoid uppercase. |
| اعرف تفاصيل الورشة | Fits | Tajawal 16/500 or 700. |
| Who is Mithaq for? | Fits | FAQ question can use 18px. |
| لمن صُممت ميثاق؟ | Fits | Use Tajawal 18/700. |

Mobile scale recommendation:

| Token | English | Arabic |
| ----- | ------- | ------ |
| Mobile Display | 42-46px / 1.08-1.15 | 38-44px / 1.18-1.25 |
| Mobile H1 | 36-40px / 1.12-1.2 | 34-38px / 1.22-1.3 |
| Mobile H2 | 28-32px / 1.18-1.25 | 28-32px / 1.25-1.35 |
| Mobile H3 | 22-24px / 1.25-1.3 | 22-24px / 1.3-1.4 |
| Mobile Body | 16-18px / 1.65-1.75 | 16-18px / 1.75-1.85 |
| Mobile Small | 14-15px / 1.55-1.65 | 14-15px / 1.65-1.75 |
| Mobile Label | 11-12px / 1.2-1.4 | Use Tajawal 14px if Arabic label text is needed |

---

## 13. Font Loading / Performance Notes

Measured source:

- Google Fonts CSS requested with a modern Chrome user agent.
- WOFF2 files were downloaded from `fonts.gstatic.com` into `mithaq-typography-specimen/fonts`.
- Google Fonts pages and Google Fonts GitHub directories were checked for family availability and source files.

Production-relevant measured WOFF2 sizes:

| Font | Weights Needed | Can Remove | Estimated WOFF2 Size | Loading Recommendation |
| ---- | -------------- | ---------- | -------------------: | ---------------------- |
| Cormorant Garamond | Normal 600-700 Latin + Italic 400 Latin | Do not load body weights; consider dropping italic if unused | 59.9 KB | Self-host Latin subset; preload normal display only on hero pages; lazy/non-preload italic. |
| DM Sans | Latin 400/500/600; 300 optional | Remove 300 if performance tight | 36.1 KB | Self-host variable Latin subset; preload if used above fold. |
| JetBrains Mono | Latin 400/500 | Remove if labels can use DM Sans; otherwise keep one variable file | 30.7 KB | Self-host; do not preload unless scene labels render above fold. |
| Tajawal | Arabic 400/500/700 | Keep all three if Arabic UI is MVP; remove 500 only if QA allows | 26.2 KB | Self-host Arabic subset; preload 400 and 700 on Arabic pages. |
| Lemonada | Arabic 400/600/700 variable | Remove entirely if accent use is rejected | 26.0 KB | Load only on pages/sections where approved accent display appears; do not preload by default. |

Estimated minimal launch payload:

- English route, no Lemonada: Cormorant normal + DM Sans + optional JetBrains = about **103.6 KB** without Cormorant italic, or **126.7 KB** with italic.
- Arabic route, no Lemonada: Tajawal = about **26.2 KB**.
- Full bilingual with all tested subsets: about **178.9 KB**.

Performance recommendation:

1. Self-host WOFF2 files.
2. Use `font-display: swap`.
3. Preload only above-the-fold critical fonts per locale.
4. Avoid loading Lemonada unless approved for a visible accent.
5. Do not load every available font weight.
6. Do not load Latin subsets for Arabic-only pages unless English appears on that page.
7. Re-measure final production font files after final font decisions and subsetting.

---

## 14. Accessibility Checks

| Area | Pass / Concern | Notes |
| ---- | -------------- | ----- |
| English display readability | Pass | Cormorant passes at large sizes on dark backgrounds; avoid body use. |
| Arabic display readability | Concern | Lemonada is readable in short lines but too decorative for default legal display; Tajawal Bold passes. |
| English body readability | Pass | DM Sans 16px minimum, 18px preferred. |
| Arabic body readability | Pass | Tajawal 16px minimum, 18px preferred; needs higher line-height. |
| CTA readability | Pass | DM Sans/Tajawal work; filled gold must use near-black text. |
| Labels readability | Pass with caution | JetBrains Mono good at 11-12px; overuse feels technical. |
| Mobile wrapping | Pass with caution | Long English/Arabic hero lines need localized wrapping and size caps. |
| Contrast safety | Pass | P2.02 parchment/dim/gold rules preserved. |
| Font payload | Concern | All tested fonts total about 178.9 KB; Lemonada and mono should be conditional. |

Accessibility guardrails:

- Minimum body size: 16px.
- Prefer 18px for main reading text.
- Arabic line-height should be 1.75-1.85 for body.
- No decorative-only Arabic.
- No critical text in images or 3D.
- No mixed Arabic/English fonts in the same line.
- Focus rings must remain visible and not rely on color alone.

---

## 15. Typography Guardrail Table

| Keep | Avoid |
| ---- | ----- |
| Cormorant for large English authority moments | Using Cormorant for all text |
| DM Sans for clarity and body reading | Making the site feel like SaaS |
| JetBrains Mono for precise labels only | Overusing mono as a tech aesthetic |
| Tajawal for Arabic body/UI readability | Treating Arabic as secondary |
| Lemonada only if it feels mature and legal | Decorative Arabic that feels playful |
| Parchment text on dark | White text on gold CTAs |
| Separate Arabic/English elements | Mixing English and Arabic fonts on one line |
| Generous Arabic line-height | Cramped Arabic text |
| Minimal font weights | Loading every available weight |

---

## 16. Typography Decision Output

| Decision Area | Recommended Decision | Notes |
| ------------- | -------------------- | ----- |
| English display font | Keep Cormorant Garamond | Use 600/700 for display; 400 italic only as rare accent. |
| English body font | Keep DM Sans | Use 400/500/600; 300 optional and removable. |
| Label/system font | Keep JetBrains Mono with limits | Scene numbers and metadata only. |
| Arabic display font | Use Tajawal 700 by default; Lemonada accent-only | Lemonada requires client/Arabic copywriter review before broad use. |
| Arabic body font | Keep Tajawal | Best current Arabic UI/body option. |
| CTA font strategy | DM Sans for English, Tajawal for Arabic | Filled gold requires near-black text. |
| Scene number style | JetBrains Mono 11px/500/0.12em | Gold accent, sparse use. |
| Mobile typography adjustment | Reduce display scale; increase Arabic line-height | Arabic should not inherit tight English display metrics. |
| Font loading strategy | Self-host WOFF2, locale-aware preloads | Keep minimal subsets and re-measure final assets. |
| Fonts to avoid/remove | Remove Lemonada if not approved; remove DM Sans 300 if unused | Avoid loading every possible weight. |

---

## 17. Final Recommendation

**PASS WITH CONDITIONS - P2.03 complete. Typography specimen, accessibility checks, font loading notes, and final recommendation are clear.**

Conditions:

1. Lemonada should not be approved as the default Arabic display type without client/Arabic copywriter review.
2. Use Tajawal 700 as the safe Arabic display default for now.
3. Confirm final font licensing and self-hosting terms before production.
4. Re-measure final production subsets after any font or weight reduction.
5. Validate rendered Arabic typography with native Arabic review before final UI design.

The typography direction is strong enough to proceed into later creative planning, but final UI production remains blocked until official brand assets, content, Arabic/English approvals, and technical decisions are complete.

---

## 18. Quality Gate

| Gate | Status |
| ---- | ------ |
| All official typefaces tested | PASS |
| English display sizes tested | PASS |
| Arabic display sizes tested | PASS |
| Cormorant tested at major display sizes | PASS |
| DM Sans tested at body and UI sizes | PASS |
| JetBrains Mono tested for labels and scene numbers | PASS |
| Tajawal and Lemonada compared | PASS |
| Bilingual pairing layouts tested | PASS |
| CTA typography states tested | PASS |
| Mobile wrapping tests included | PASS |
| Font loading/WOFF2 size notes included | PASS |
| Accessibility concerns documented | PASS |
| Recommendations clear | PASS |
| Avoided final UI design | PASS |
| Avoided production implementation | PASS |

