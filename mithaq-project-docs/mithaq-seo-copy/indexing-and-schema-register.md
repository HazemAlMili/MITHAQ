# Indexing and Schema Register

| Route | Indexing Decision | Schema Type | Readiness | Blocking Dependency |
| --- | --- | --- | --- | --- |
| `/` | Index | `EducationalOrganization`, `Organization`, `WebSite` | Ready for client review | Final domain, logo/OG image, canonical locale strategy, client approval |
| `/register` | Index or Noindex Pending Final Strategy | `BreadcrumbList`; optional `WebPage` | Conditional | Final form destination, privacy/data language, indexing strategy |
| `/workshops/[slug]` | Noindex Until Approved | `BreadcrumbList`; `Course` only after workshop approval | Template only | Confirmed workshop inventory and full bilingual page content |
| `/about` | Do Not Create Yet | None | Not approved | Route approval and brand/about copy |
| `/instructors` | Do Not Create Yet | `Person` only after verified profiles | Not approved | Verified instructor profiles, portraits, consent, route approval |
| `/workshops` | Do Not Create Yet | None until approved | Conditional/deferred | Workshop index route approval and confirmed inventory |
| `/privacy` | Do Not Create Yet until legal copy exists | None or `WebPage` | Legal dependency | Approved privacy policy |
| Prototype / sandbox routes | Noindex Until Approved | None | Internal only | Production route approval |

## Structured-Data Recommendations

### EducationalOrganization

Recommended route: `/`

Required verified fields:

- Official organization name.
- Logo.
- URL/domain.
- Contact method.
- SameAs/social links if approved.
- Address only if approved.

Current readiness: Conditional.

Blocking dependencies: final domain, logo, contact details, social/profile links if any.

### Organization

Recommended route: `/`

Required verified fields:

- Official name.
- URL.
- Logo.
- Contact point if approved.

Current readiness: Conditional.

Blocking dependencies: same as `EducationalOrganization`.

### WebSite

Recommended route: `/`

Required verified fields:

- Site name.
- URL.
- Locale/canonical strategy.

Current readiness: Conditional.

Blocking dependencies: final domain and locale strategy.

### FAQPage

Recommended route: `/` Scene 09, after FAQ copy approval.

Required verified fields:

- Approved public FAQ questions and answers.
- No internal dependency markers in public content.

Current readiness: Partial.

Blocking dependencies: P6.04 client approval and operational decisions for conditional FAQ answers.

### Course

Recommended route: `/workshops/[slug]` only after each workshop is verified.

Required verified fields:

- Workshop title.
- Description.
- Provider.
- Course/workshop instance details only if verified.
- No fake price, date, duration, rating, review, offer, or certificate claim.

Current readiness: Not ready.

Blocking dependencies: confirmed workshop inventory.

### Person

Recommended route: future instructor pages only after approval.

Required verified fields:

- Name.
- Role.
- Bio.
- Image/portrait with consent.
- SameAs/profiles if approved.

Current readiness: Not ready.

Blocking dependencies: verified instructor inventory, portraits, consent, and route approval.

### BreadcrumbList

Recommended route: `/register` and `/workshops/[slug]` after route implementation.

Required verified fields:

- Final route paths.
- Final localized labels.
- Canonical URL.

Current readiness: Conditional.

Blocking dependencies: final route and locale implementation decisions.

## Schema Types Not Recommended Yet

- `Review` - no verified reviews.
- `AggregateRating` - no verified ratings.
- `Event` - no confirmed dates/events.
- `Offer` - no confirmed pricing/payment/offers.
- `CourseInstance` - no confirmed schedule, mode, or duration.
- `Person` - blocked until verified instructors exist.
