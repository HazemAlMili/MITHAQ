# Dynamic Metadata Templates

These patterns are reusable specifications only. They are not publishable metadata until their required fields are verified.

## Workshop Page Template

Route Pattern: `/workshops/[slug]`

Template Status: Template Only - Not Publishable Until Workshop Approval

Indexing Rule: `noindex` until all required dynamic fields are approved.

### Required Dynamic Fields

- `[WORKSHOP TITLE]`
- `[WORKSHOP TITLE ARABIC]`
- `[CONFIRMED AUDIENCE]`
- `[CONFIRMED AUDIENCE ARABIC]`
- `[CONFIRMED PRIMARY SKILL]`
- `[CONFIRMED PRIMARY SKILL ARABIC]`
- `[CONFIRMED LEVEL]`
- `[CONFIRMED FORMAT]`
- `[CONFIRMED DURATION]`
- `[CONFIRMED LANGUAGE]`
- `[CONFIRMED CERTIFICATE POLICY]`
- `[CONFIRMED PRICE OR INQUIRY-ONLY STATUS]`
- `[WORKSHOP SLUG]`

### English Pattern

Title:

```text
[WORKSHOP TITLE] | Mithaq Legal Academy
```

Description:

```text
Learn about [WORKSHOP TITLE], including audience fit, [CONFIRMED PRIMARY SKILL], format, and how to ask Mithaq for details.
```

OG Title:

```text
[WORKSHOP TITLE] | Mithaq
```

OG Description:

```text
Explore confirmed details for [WORKSHOP TITLE] and ask Mithaq whether it suits your current legal training needs.
```

Canonical Pattern:

```text
https://[CLIENT INPUT REQUIRED: DOMAIN]/workshops/[WORKSHOP SLUG]
```

### Arabic Pattern

Title:

```text
[WORKSHOP TITLE ARABIC] | ميثاق
```

Description:

```text
تعرّف على [WORKSHOP TITLE ARABIC]، والجمهور المناسب، و[CONFIRMED PRIMARY SKILL ARABIC]، وطريقة الاستفسار من ميثاق.
```

OG Title:

```text
[WORKSHOP TITLE ARABIC] | ميثاق
```

OG Description:

```text
اطّلع على التفاصيل المعتمدة لـ [WORKSHOP TITLE ARABIC] واسأل ميثاق إن كانت مناسبة لاحتياجك التدريبي الحالي.
```

Canonical Pattern:

```text
https://[CLIENT INPUT REQUIRED: DOMAIN]/ar/workshops/[WORKSHOP SLUG]
```

### Conditions for Indexability

A workshop page may be indexed only when:

- Workshop title is approved in English and Arabic.
- Audience, level, skills, format, duration, and language are approved.
- Certificate, recording, pricing/inquiry, and availability policy are either confirmed or omitted.
- Instructor references are verified or omitted.
- Page body content is complete in both languages.
- Canonical and hreflang rules are finalized.

## Instructor Page Template

Route Pattern: `/instructors/[slug]` or `/instructors`

Template Status: Future / Not Approved

Indexing Rule: Do Not Create Yet

Reason: Instructor routes are deferred and P6.06 found no verified instructor inventory or portraits.

### Required Dynamic Fields Before Any Future Metadata

- `[INSTRUCTOR NAME]`
- `[INSTRUCTOR NAME ARABIC]`
- `[VERIFIED CURRENT ROLE]`
- `[VERIFIED ORGANIZATION OR PROFESSIONAL CONTEXT]`
- `[VERIFIED EXPERTISE AREAS]`
- `[APPROVED BIO]`
- `[APPROVED PORTRAIT]`
- `[PUBLICATION CONSENT]`

### Future English Pattern Only After Approval

```text
[INSTRUCTOR NAME] | Mithaq Mentor
```

### Future Arabic Pattern Only After Approval

```text
[INSTRUCTOR NAME ARABIC] | مرشدو ميثاق
```

No instructor metadata should be published until profiles are verified and routes are approved.

## Privacy Page Template

Route Pattern: `/privacy`

Template Status: Planned / Legal Dependency

Indexing Rule: Noindex or Do Not Create Yet until approved legal/privacy copy exists.

Reason: A privacy page is recommended before collecting real form data, but no approved policy copy exists in the current content package.
