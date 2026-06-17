# Mithaq Language & RTL Strategy Decision Document

**Ticket:** MTHQ-P0-T06  
**Phase:** Phase 0, Project Alignment & Input Collection  
**Depends on:** MTHQ-P0-T01, MTHQ-P0-T02, MTHQ-P0-T03, MTHQ-P0-T04, MTHQ-P0-T05  
**Status:** Recommended strategy locked for client approval. Production implementation not started.

---

## 1. Recommended Language Strategy

Recommended strategy:

**Arabic-first MVP with English-ready architecture.**

This means Mithaq should be planned, written, designed, and tested first for Arabic-speaking users, while the frontend and content structure remain ready for a future English version.

Reason:

- Mithaq is likely targeting Arabic-speaking law students, graduates, junior lawyers, and legal trainees.
- Arabic is likely the strongest conversion language for the regional legal training audience.
- Arabic must not be treated as a later translation layer.
- English may still be useful later for partners, sponsors, instructors, institutional credibility, or broader reach.
- Full bilingual MVP adds content, QA, SEO, localization, and design complexity before the core assets are ready.

Recommended option:

**Option B - Arabic-First + English-Ready**

Do not choose full bilingual MVP unless the client confirms that both languages are required at launch and provides approved content in both languages.

---

## 2. MVP Language Scope

Recommended MVP scope:

- Launch language: **Arabic**
- Default content direction: **RTL**
- Primary CTA language: **Arabic**
- Primary form language: **Arabic**
- FAQ language: **Arabic**
- Workshop content language: **Arabic**
- Instructor bios: **Arabic-first**, with English versions only if provided and approved
- WhatsApp message: **Arabic by default**

English should not be included in the MVP as visible production content unless the client provides approved English copy and confirms bilingual launch scope.

---

## 3. Future Language Scope

Future scope:

- Add English as Phase 2 or as an MVP extension only if approved.
- Maintain route, content, and component architecture so English can be added without rebuilding layout foundations.
- Prepare copy/content models to support localized versions of:
  - Navigation
  - Hero copy
  - CTAs
  - Workshop cards
  - Instructor bios
  - FAQ
  - Forms
  - Metadata
  - WhatsApp messages

Recommended future route model:

```text
/        -> Arabic MVP default
/en      -> English later
```

Alternative if full bilingual launch is approved:

```text
/ar
/en
```

Final route decision is pending client confirmation.

---

## 4. RTL / LTR Direction Decision

Recommended direction:

**RTL-first with LTR-compatible components.**

Arabic pages should use:

```html
<html lang="ar" dir="rtl">
```

Future English pages should use:

```html
<html lang="en" dir="ltr">
```

Design and frontend should be built using logical layout rules from the beginning, not LTR-only spacing.

Required CSS direction approach:

- Use `margin-inline-start`
- Use `margin-inline-end`
- Use `padding-inline`
- Use `border-inline`
- Use `inset-inline-start`
- Use `inset-inline-end`
- Use `text-align: start`
- Use `text-align: end`

Avoid hardcoding `left`, `right`, `margin-left`, or `margin-right` unless a specific visual or technical case requires it.

---

## 5. Navigation Language Direction

MVP navigation should be Arabic-first.

Recommended Arabic navigation labels:

- الرئيسية
- المنهج
- المسارات
- الورش
- المحاضرون
- الأسئلة
- سجّل اهتمامك

Future English navigation labels:

- Home
- Method
- Tracks
- Workshops
- Mentors
- FAQ
- Register Interest

Navigation must be designed for RTL scanning, especially on mobile. Do not design the header in English first and mirror it later.

---

## 6. CTA Language Direction

MVP CTAs should be Arabic-first.

Recommended primary CTA:

**سجّل اهتمامك**

Recommended supporting CTA options:

- اسأل عن الورشة القادمة
- تواصل معنا عبر واتساب
- استعرض المسارات

Future English CTA options:

- Register Interest
- Ask About the Next Workshop
- Inquire via WhatsApp
- View Training Tracks

CTA rule:

Use **Register Interest / سجّل اهتمامك** until dates, prices, capacity, and registration readiness are confirmed.

Do not use direct registration wording such as "Register Now" unless the client confirms the exact registration process and program details.

---

## 7. Form Language Direction

MVP form labels should be Arabic-first.

Recommended Arabic form fields:

- الاسم الكامل
- رقم الهاتف / واتساب
- مجال الاهتمام
- رسالتك

Recommended MVP form structure:

1. Full name
2. Phone / WhatsApp number
3. Area of interest

The message field can remain optional.

Future English form labels:

- Full Name
- Phone / WhatsApp Number
- Area of Interest
- Message

Forms must submit the user's language/locale as part of the lead data.

Recommended form payload metadata:

- `locale`
- `direction`
- `cta_source`
- `cta_label`
- `workshop_interest`, if applicable

---

## 8. FAQ Language Direction

MVP FAQ should be written natively in Arabic.

Do not write the FAQ in English first and translate it literally.

Reason:

- Legal education questions are culturally and contextually sensitive.
- Arabic phrasing affects trust and conversion.
- FAQ answers may include certificate, registration, and legal-compliance wording that must feel precise.

FAQ answers must be reviewed by:

- Client/project owner
- Admissions team
- Legal reviewer, where claims, certificates, policies, or outcomes are mentioned

English FAQ can be added later if English scope is approved.

---

## 9. 3D Seal / Text Language Direction

Recommended seal language direction:

**Arabic "ميثاق" as the primary seal identity, pending client approval and official wordmark files.**

Reason:

- The name carries the Covenant Seal concept most strongly in Arabic.
- Arabic gives the seal a native legal/cultural authority.
- It supports the Arabic-first website direction.

Allowed future options:

- Arabic-only seal
- Bilingual seal
- Abstract mark-only seal

Not approved yet:

- Final seal design
- 3D seal geometry
- WebGL seal texture
- Final logo/wordmark integration

Hard dependency:

The final seal direction cannot proceed until the client provides official Arabic/English wordmarks and approves seal adaptation, as documented in T03 and T05.

Essential content must remain in the DOM. Do not rely on 3D text or canvas-rendered text as the only source of important information.

---

## 10. Typography Requirements

This task does not choose final fonts. It defines requirements.

Arabic typography requirements:

- Arabic display type must feel premium, legal, serious, and readable.
- Arabic body type must prioritize clarity and long-form reading.
- Avoid overly decorative Arabic fonts for body copy.
- Test real Arabic copy early, including long headlines, CTA labels, FAQ answers, and workshop cards.
- Arabic type must work on mobile.
- Arabic type must support professional legal tone.

English typography requirements:

- English display type may use an editorial serif if it supports the premium legal direction.
- English body type should use a clean, readable sans-serif.
- English typography should harmonize with Arabic without forcing Arabic into a Latin-first system.

Shared typography requirements:

- Font licensing must be confirmed before production.
- Web font payload must stay within performance budgets.
- Font loading must support fallback states cleanly.
- Typography must be tested in dark premium layouts.
- Text must remain readable in reduced-motion and static fallback experiences.

---

## 11. Frontend / i18n Requirements

Frontend must be built as Arabic-first and English-ready.

Required:

- Set `lang="ar"` and `dir="rtl"` for Arabic pages.
- Support future `lang="en"` and `dir="ltr"` for English pages.
- Use CSS logical properties throughout.
- Keep text content outside the 3D canvas in semantic DOM.
- Store language-aware strings in structured content files, JSON, MDX, or CMS-ready data.
- Include locale in form submissions and analytics events.
- Localize WhatsApp messages by language.
- Localize metadata by language.
- Prepare for language-specific workshop content.

Technical decisions pending:

| Decision | Recommended Direction | Status |
| -------- | --------------------- | ------ |
| Is i18n in MVP? | Architecture yes, visible English content no | Pending client approval |
| Default locale | Arabic | Pending client approval |
| Supported MVP locales | Arabic only | Pending client approval |
| Future locale | English | Pending client approval |
| Content storage | Structured and locale-ready | Pending technical planning |
| Metadata localization | Arabic MVP, English later | Pending SEO planning |
| WhatsApp localization | Arabic default, English later | Pending CTA approval |
| Form language data | Include locale in submissions | Recommended |
| Workshop slugs | Arabic default or stable neutral slugs | Pending SEO/client decision |

Recommended route structure for MVP:

```text
/        -> Arabic default
```

Recommended future route structure:

```text
/        -> Arabic
/en      -> English
```

---

## 12. SEO Requirements

Arabic-first MVP SEO requirements:

- Arabic page title.
- Arabic meta description.
- Arabic Open Graph title.
- Arabic Open Graph description.
- Arabic structured data where relevant.
- Arabic-friendly keywords based on real search intent.
- Arabic canonical page as default.

If English is added later:

- Add localized English metadata.
- Add `hreflang`.
- Define canonical strategy.
- Use language-specific URLs.
- Decide whether slugs are translated or stable across languages.

SEO note:

This task does not write final SEO content. It only locks the language and localization direction.

---

## 13. Accessibility Requirements

Language and RTL implementation must support accessibility from the beginning.

Required:

- Correct `lang` attribute.
- Correct `dir` attribute.
- Proper focus order in RTL layouts.
- Screen reader reading order must match visual/content order.
- Form labels must be in the correct language.
- FAQ must use semantic structure.
- Buttons and links must have clear accessible names.
- No key content should exist only in canvas or 3D textures.
- Reduced-motion fallback must include the same essential Arabic content.
- Mobile tap targets must remain accessible in RTL.

Accessibility rule:

The WebGL layer may support atmosphere and brand story, but the actual content must remain readable, selectable, and accessible in DOM.

---

## 14. Client Answers

The following answers are required from the client/project owner.

| Question | Recommended Answer | Status |
| -------- | ------------------ | ------ |
| What is the primary audience language? | Arabic | Pending |
| Should MVP launch Arabic only, English only, or both? | Arabic MVP | Pending |
| Is Arabic the primary conversion language? | Yes | Pending |
| Should WhatsApp messages be Arabic, English, or dynamic? | Arabic default, dynamic later | Pending |
| Are workshop names Arabic, English, or bilingual? | Arabic-first | Pending |
| Are instructor bios Arabic, English, or both? | Arabic-first | Pending |
| Are testimonials Arabic, English, or both? | Use original language, Arabic-first if available | Pending |
| How should the brand appear? | Pending official brand decision | Pending |
| Should navigation be Arabic-first? | Yes | Pending |
| Is English needed for institutional credibility at launch? | Phase 2 unless required | Pending |
| Are disclaimers needed in Arabic, English, or both? | Arabic MVP, English later if bilingual | Pending legal review |
| Will professional translation be provided if bilingual? | Required if bilingual | Pending |
| Should SEO target Arabic, English, or both? | Arabic MVP, English later | Pending |
| Should future workshop pages support bilingual URLs? | Yes, architecture-ready | Pending |
| Is timeline/budget enough for bilingual MVP? | Assume no until confirmed | Pending |

---

## 15. Risks and Mitigation

| Risk | Why It Matters | Mitigation |
| ---- | -------------- | ---------- |
| Arabic becomes an afterthought | Weak Arabic experience reduces premium feel and local credibility | Design RTL-first and write Arabic natively |
| Bilingual MVP expands scope too much | Full bilingual launch increases content, QA, SEO, and design workload | Use Arabic-first MVP with English-ready architecture unless bilingual is required |
| English-first weakens conversion | Arabic-speaking users may feel the site is distant or corporate | Confirm primary audience language before choosing English-first |
| Arabic typography feels cheap | Typography is a major authority signal | Use high-quality Arabic typography and test real Arabic copy early |
| Frontend becomes LTR-only | RTL added later causes expensive refactoring | Use CSS logical properties and locale-aware layout from day one |
| 3D text becomes unreadable | Arabic in 3D seal or texture can lose clarity | Keep seal simple and keep essential text in DOM |
| SEO is planned only in English | Arabic users may not find the site | Create Arabic-first metadata and search strategy |
| Legal disclaimers are translated poorly | Legal meaning may shift between languages | Require legal review in each published language |

---

## 16. Final Decision Status

Recommended decision:

- **MVP language strategy:** Arabic-first
- **Visible MVP languages:** Arabic only, unless client approves bilingual scope
- **Future language support:** English-ready architecture
- **Default direction:** RTL
- **Future direction support:** LTR-compatible components
- **CTA language:** Arabic-first
- **Form language:** Arabic-first
- **FAQ language:** Native Arabic
- **Seal language direction:** Arabic "ميثاق" preferred, pending official wordmark and seal approval
- **Frontend architecture:** Locale-aware, RTL-first, CSS logical properties required
- **SEO direction:** Arabic-first metadata, English-ready later
- **Accessibility direction:** Correct `lang`/`dir`, semantic DOM content, no canvas-only critical text

Final approval required from:

- Client / Founder
- Product Lead
- UX Strategist
- Arabic Copywriter
- Frontend Lead
- Legal Reviewer where disclaimers or claims are involved

Production reminder:

This decision does not unblock final UI, final Mithaq Seal, final 3D seal, frontend logo integration, production copywriting, or legal/compliance-sensitive claims. Those remain blocked until the client provides the required brand assets, content assets, contact details, and legal approvals documented in T03, T04, and T05.

