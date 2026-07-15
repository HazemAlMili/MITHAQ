# Hero Copy Handoff

## Recommended Line Breaks

Line breaks are visual recommendations only. Meaning must not depend on forced breaks.

### English Desktop

```text
Practical Legal Training
for Professional Readiness
```

### Arabic Desktop

```text
تدريب قانوني عملي
لجاهزية مهنية أوضح
```

### English Mobile

```text
Practical Legal Training
for Readiness
```

### Arabic Mobile

```text
تدريب قانوني عملي
لجاهزية مهنية
```

## Maximum Text Widths

| Breakpoint | Recommendation |
| --- | --- |
| Desktop English | 620–720px hero copy column. |
| Desktop Arabic | 660–760px hero copy column; allow more line-height. |
| Mobile English | Full width minus safe page padding; avoid more than 3 headline lines. |
| Mobile Arabic | Full width minus safe page padding; allow comfortable line-height and no clipped ascenders/descenders. |

## Words to Visually Emphasize

Use typographic hierarchy, not animated gimmicks.

| English | Arabic | Reason |
| --- | --- | --- |
| Practical Legal Training | تدريب قانوني عملي | States category clearly. |
| Professional Readiness | جاهزية مهنية | States transformation. |
| research, writing, workplace skills | البحث، الصياغة، بيئة العمل | Makes value practical. |

Do not overuse gold text. Use parchment/ivory body text on dark. Filled gold CTAs must use near-black text.

## Arabic / English Localization Notes

- Arabic and English should be localized as separate hero layouts, not displayed as one mixed line.
- Arabic should not be animated letter-by-letter.
- Arabic heading line-height should be more generous than English.
- Do not force literal translation where Arabic rhythm weakens.
- Use Tajawal 700 as the safe Arabic display default from prior typography decisions.
- Keep Lemonada accent-only pending review.

## Mobile Truncation Risks

| Risk | Mitigation |
| --- | --- |
| Arabic headline wrapping into too many lines | Use the short mobile headline. |
| Primary CTA too long | Mobile label may shorten to `اسأل عن الورش` / `Ask About Workshops`. |
| Subheadline crowding CTA | Use the mobile supporting line and keep CTA immediately visible. |
| Seal/3D competing with text | Text-first mobile layout; static/fallback poster allowed. |

## CTA Destination Assumptions

| CTA | Destination | Status |
| --- | --- | --- |
| Ask About Mithaq Workshops | WhatsApp link | `[CLIENT INPUT REQUIRED]` final WhatsApp number. |
| Discover the Mithaq Method | Scene 04 anchor or method section | Requires final anchor/routing convention later. |
| Register Interest | `/register` | Requires final form destination. |

## Missing Client Inputs

- `[CLIENT INPUT REQUIRED]` Official WhatsApp number.
- `[CLIENT INPUT REQUIRED]` Form destination.
- `[CLIENT INPUT REQUIRED]` Final legal/compliance review.
- `[CLIENT INPUT REQUIRED]` Final Arabic copy approval.
- `[CLIENT INPUT REQUIRED]` Final English copy approval.
- `[CLIENT INPUT REQUIRED]` Final workshop availability/details if the CTA should mention “upcoming”.
- `[CLIENT INPUT REQUIRED]` Final brand/wordmark/seal approval.

## Implementation Safety

- Do not bake hero text into WebGL, 3D textures, posters, or images.
- Hero H1, subheadline, and CTAs must be semantic DOM content.
- The same copy must be available in WebGL fallback and reduced-motion states.
- WhatsApp link must remain accessible without canvas.
- No production implementation was started in P6.01.
- No Scene 01 or Scene 03–10 copy was written beyond necessary adjacent-reference guardrails.
- P6.02 was not created or executed.

