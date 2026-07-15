# SEO Copy Handoff

## Title and Description Limits

- English title target: 45-60 characters.
- English title hard maximum: about 65 characters.
- English description target: 120-155 characters.
- English description hard maximum: about 160 characters.
- Arabic should be judged visually and semantically, not forced to match English character counts.
- Include brand name once per title.
- Avoid keyword stuffing.

## Canonical Assumptions

- Final domain is not confirmed.
- Homepage canonical should point to the final primary locale URL.
- `/register` canonical depends on whether Arabic default or explicit locale prefixes are used.
- `/workshops/[slug]` canonical must not be finalized until the slug and workshop content are approved.
- Placeholder and prototype routes should not receive public canonical metadata.

## Locale and Hreflang Notes

Two IA options remain possible:

- Arabic default with English prefixed routes.
- Equal locale prefixes for Arabic and English.

Hreflang should be planned only after the final locale strategy is selected.

Recommended future hreflang set:

- Arabic page variant.
- English page variant.
- `x-default` pointing to the default market/language decision.

Do not create duplicate locale pages without finalized canonical and hreflang rules.

## OG Image Requirements

Recommended OG image concept:

- Dark premium Mithaq seal/desk composition.
- Clear Mithaq identity.
- No text-heavy layout.
- No fake workshop, instructor, proof, certificate, date, or price claims.
- Arabic/English variants may be needed if text is included.

Dependencies:

- Final seal/wordmark approval.
- Final static fallback or brand poster asset.
- Client approval of social-sharing visual.

## Dynamic-Field Rules

Dynamic metadata must use only verified fields:

- Workshop title.
- Workshop slug.
- Audience.
- Primary skill.
- Level.
- Delivery format.
- Duration.
- Language.
- Certificate policy.
- Price/inquiry status.
- Instructor relationship.

If any required field is missing, keep the page `noindex` or omit that field from public metadata.

## Pages That Must Remain Noindex / Not Created

- Placeholder workshop detail pages.
- Empty or placeholder instructor pages.
- Draft register page if privacy/form destination is unresolved.
- Internal prototypes and sandboxes.
- Any duplicate locale route without canonical/hreflang strategy.
- `/about`, `/instructors`, `/workshops`, and `/privacy` until each route/content package is approved.

## Metadata Requiring Client Approval

- Homepage title and description.
- Register page title and description.
- Workshop dynamic title/description patterns.
- Arabic metadata wording.
- OG image concept.
- Final brand naming and domain.
- Any structured data using organization details.

## Public Metadata Guardrails

Keep:

- Practical legal training.
- Professional readiness.
- Law graduates and early-career legal professionals.
- Legal research and legal writing.
- Inquiry/register-interest path.

Avoid:

- Best / number one / leading claims.
- Guaranteed career outcomes.
- Certificates or accreditation unless approved.
- Workshop dates, prices, duration, format, or availability unless confirmed.
- Instructor names or credentials until verified.
- Reviews, ratings, events, offers, or pricing schema without evidence.

## Implementation Scope Confirmation

No metadata, structured data, routes, sitemap, robots.txt, analytics, CMS, React, Next.js, or technical SEO implementation was started in P6.07.
