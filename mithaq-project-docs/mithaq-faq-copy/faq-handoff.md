# FAQ Handoff

## Recommended FAQ Order

1. FAQ-01 - Who is Mithaq for?
2. FAQ-02 - How is Mithaq different from university legal study?
3. FAQ-03 - What skills does Mithaq training focus on?
4. FAQ-10 - How can I know which workshop suits my level?
5. FAQ-04 - Are workshops online, in person, or hybrid?
6. FAQ-05 - Can I join a single workshop?
7. FAQ-06 - How long are workshops or training tracks?
8. FAQ-07 - Is a certificate provided?
9. FAQ-08 - Are sessions recorded?
10. FAQ-09 - How does registration or inquiry work?

Reason: Start with fit and positioning, move into skills and workshop suitability, then handle operational questions, and end with the conversion path.

## Suggested Default-Open Item

Default-open item: FAQ-01 - Who is Mithaq for?

Reason: It clarifies audience fit immediately without exposing unresolved operational policies first.

## Long-Answer Risks

- FAQ-03 may expand once workshop inventory exists; keep it concise.
- FAQ-04 to FAQ-08 should remain short until real policies are approved.
- FAQ-09 should not become a full form/privacy explanation without approved legal copy.

## Mobile Wrapping Risks

- English: "How can I know which workshop suits my level?" may need two lines.
- Arabic: `هل تُقدَّم الورش أونلاين أم حضوريًا أم بنظام هجين؟` may wrap to three lines; acceptable if line-height is generous.
- Arabic CTA `اسأل ميثاق عبر واتساب` should remain one line when possible.
- Avoid narrow accordion headers that force awkward Arabic word breaks.

## Arabic Punctuation and RTL Notes

- Use Arabic question mark `؟` for Arabic questions.
- Use Arabic comma `،` in Arabic answers.
- Use `dir="rtl"` for Arabic FAQ containers.
- Use `text-align: start`, not hard-coded right alignment.
- Use logical spacing such as `margin-inline`, `padding-inline`, and `inset-inline`.
- Keep English dependency markers out of public UI; they are documentation-only.
- Do not animate Arabic text letter-by-letter.

## Links or CTAs Required

- WhatsApp fallback CTA: `Ask Mithaq on WhatsApp` / `اسأل ميثاق عبر واتساب`
- Inquiry fallback CTA: `Register Your Interest` / `سجّل اهتمامك`
- Final WhatsApp URL depends on `WHATSAPP_NUMBER_PENDING`.
- Inquiry form route/destination remains conditional pending form implementation details.

## Answers That Must Not Publish Before Client Confirmation

These can be reviewed, but should not publish as final policy without client confirmation:

- FAQ-04 - workshop delivery format.
- FAQ-05 - single-workshop participation.
- FAQ-06 - workshop or track duration.
- FAQ-07 - certificate policy.
- FAQ-08 - recording/replay policy.
- FAQ-09 - final WhatsApp number and form destination.
- FAQ-10 - workshop inventory and level labels.

## Public vs Internal Copy

- Public answers should not show `[CLIENT INPUT REQUIRED: ...]`.
- Dependency markers should remain in documentation and handoff only.
- If a conditional answer is published before policy approval, keep the safe public wording and remove internal markers from UI.

## Scope Confirmation

No accordion, UI, React, R3F, CSS, Figma, CMS, i18n, RTL implementation, forms, routes, workshop cards, instructor bios, proof points, payment terms, privacy text, or later roadmap work was started.
