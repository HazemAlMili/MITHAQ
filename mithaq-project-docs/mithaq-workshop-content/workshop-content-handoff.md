# Workshop Content Handoff

## Recommended Workshop Order

No public order is recommended yet because no confirmed workshop inventory exists.

When inventory is confirmed, order workshops by visitor decision value:

1. Most foundational / broad-fit workshop.
2. Research-focused workshop.
3. Writing or memo-focused workshop.
4. Professional readiness or workplace workshop.
5. Career infrastructure or specialized workshop.

Do not use this as a substitute for real inventory approval.

## Compact-Card Field Limits

- Title: 2-8 words.
- Audience/level label: 2-5 words.
- Value line: 12-22 English words; Arabic should fit in 1-3 short lines.
- Skill points: 3-8 English words each; Arabic should remain compact.
- CTA: 2-5 English words; Arabic CTA should remain one line where possible.
- Hide format, duration, certificate, price, and availability unless confirmed.

## Expanded-Detail Boundaries

Expanded detail may include:

- Short introduction.
- Intended audience.
- Learning outcomes.
- Confirmed delivery details.
- Inquiry CTA.

Expanded detail must not include:

- Full curricula.
- Lesson plans.
- Instructor biographies.
- Prices, dates, capacity, or certificates unless verified.
- Payment, booking, checkout, or account language.
- Testimonials or proof points.

## Mobile Title / Wrapping Risks

- Arabic titles can run longer than English; test 2-line and 3-line card states.
- Avoid narrow dossier overlays for semantic text.
- Keep `اسأل عن هذه الورشة` and `اعرف تفاصيل الورشة` as tested CTA labels.
- If title wraps awkwardly, use a shorter approved Arabic title rather than shrinking text excessively.

## Arabic / RTL Notes

- Use P6.03 glossary terms: `الورش`, `تدريب قانوني عملي`, `الجاهزية المهنية`, `البحث القانوني`, `الصياغة القانونية`, `منهج ميثاق`.
- Use `dir="rtl"` for Arabic card content.
- Use `text-align: start` and logical spacing such as `margin-inline` and `padding-inline`.
- Do not mix Arabic and English title fragments in one line unless the workshop name is officially bilingual.
- Keep `[CLIENT INPUT REQUIRED: ...]` markers out of public UI.

## Dossier-to-HTML Mapping

The P5.09 dossier asset is atmospheric only. Map semantic workshop content to DOM/HTML:

| Dossier / 3D Role | HTML Content Role |
| --- | --- |
| Closed legal dossier silhouette | Workshop card container |
| Small neutral mark / plate | Optional visual index, not content |
| Hover / selected light response | Interaction state only |
| Dossier stack / multi-layout | Multiple workshop cards |
| Mobile-light fallback | Static or DOM-first workshop list |

Never bake real or placeholder workshop titles, dates, prices, instructor names, or CTAs into the GLB.

## CTA Destination Assumptions

- Primary card CTA: WhatsApp inquiry.
- Secondary card/detail CTA: View Details, only when `/workshops/[slug]` content exists.
- Form path: Register Interest / inquiry form.
- WhatsApp number remains `WHATSAPP_NUMBER_PENDING` until supplied.
- Workshop-specific WhatsApp messages must include only confirmed workshop titles.

## Fields Hidden Until Confirmed

- Format.
- Duration.
- Schedule/date.
- Location/platform.
- Language.
- Capacity.
- Certificate status.
- Recording availability.
- Price/payment/inquiry-only status.
- Instructor reference.
- Availability/status label.
- Practical output or exercise.

## Claims Review Guidance

Every future public workshop statement must be tagged before publication:

- `Verified`
- `Client Confirmation Required`
- `Internal Only`

Do not publish `Client Confirmation Required` or `Internal Only` statements as facts.

## Scene 06 Implementation Scope

No Scene 06 implementation was started. This package creates content schema and handoff guidance only.
