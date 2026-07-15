# Proof Handoff

## Recommended Scene 08 Order

### Current Pre-Launch State

1. Eyebrow: Trust and Credibility / الثقة والمصداقية
2. Headline: Trust Starts With Clear Information / تبدأ الثقة من وضوح المعلومات
3. Short body copy explaining that verified public proof is not available yet.
4. Three process-based trust cards:
   - Clear Training Information
   - Direct Suitability Questions
   - No Unsupported Promises
5. CTA to ask a question through the approved inquiry path.

Do not show empty proof slots, zero counters, placeholder testimonials, or “coming soon” proof cards.

### Future Verified-Proof State

If evidence becomes available, use this order:

1. Verified quantitative proof, only with source records and approved display format.
2. Approved testimonials with consent and attribution.
3. Instructor authority proof, only after P6.06 verification.
4. Institutional proof, only with permission and approved relationship wording.
5. Programme evidence, only with records and participant/content consent.

## Number-Display Rules

- Never round upward without approval.
- Animated counters must stop at the verified value.
- Record numerator, date range, inclusion/exclusion rules, calculation method, and last verified date.
- Use exact numbers unless the client/legal reviewer approves a rounded display.
- Do not show “+” or “over” unless the source record supports it and approval is documented.

Example:

```text
Raw verified count: 87
Allowed display: 87 participants
Not allowed without approval: 90+ participants
```

## Testimonial Formatting

- Use original wording or an approved edited version only.
- Keep a record of grammar edits.
- Do not combine multiple testimonials into one quote.
- Do not attribute a quote to an organization unless authorized.
- Anonymous publication requires explicit approval.
- Arabic testimonial translation/localization must preserve meaning and claim strength.

## Attribution Requirements

For every public testimonial or proof card, store:

- source document or original message
- source date
- person or organization attribution preference
- consent status
- approved public wording
- reviewer/approver when known

## Logo Constraints

Do not display partner, sponsor, accreditation, university, firm, press, or institutional logos until all are verified:

- relationship type
- current status
- logo permission
- correct brand file
- brand guideline restrictions
- required legal wording
- expiry or review date

Participation by an individual from an organization does not prove a partnership with that organization.

## Mobile and RTL Risks

- Avoid dense proof grids on mobile; use one-column cards.
- Keep Arabic proof labels short and avoid stacked legal nouns.
- Use `text-align: start`, `margin-inline`, and `padding-inline` in future implementation.
- Do not rely on logo recognition; include accessible text.
- Ensure numbers remain readable in RTL layouts and do not reorder surrounding punctuation incorrectly.
- Keep mixed Arabic/English organization names isolated if approved later.

## Accessibility Equivalent

Every visual proof module must have a plain-language equivalent:

- counter value plus what it measures
- testimonial text plus attribution
- logo relationship described in text
- certificate/accreditation claim with exact approved wording

Proof must be understandable without animation, hover, counters, logos, or 3D.

## SEO and Schema Implications

Do not implement or recommend proof-backed schema until evidence exists:

- No `Review`
- No `AggregateRating`
- No `Event`
- No `Offer`
- No `CourseInstance`
- No `Person` schema for instructors
- No course/workshop schema for placeholder workshop pages

`FAQPage` remains conditional on approved FAQ copy and removal of internal dependency markers.

## Items That Must Remain Hidden

- participant counts
- workshop counts
- training hours
- satisfaction rates
- testimonials
- ratings
- partner/sponsor logos
- institutional affiliations
- certificate issuance
- accreditation claims
- instructor credentials
- press mentions
- “trusted by” copy
- “leading,” “proven,” or “best” credibility claims

## Implementation Boundary

This handoff is content guidance only.

No Scene 08 implementation, React, R3F, CSS, counters, schema, CMS, routes, analytics, or metadata changes were started.
