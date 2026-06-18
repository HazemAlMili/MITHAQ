# Mithaq Technical Environment Checklist

**Official Ticket ID:** P0.03  
**Official Ticket Name:** Technical Environment Survey  
**Phase:** Phase 0, Project Alignment & Input Collection  
**Priority:** P0  
**Status:** QA blocked pending client/technical access answers  
**Prepared date:** 2026-06-17

---

## 1. Executive Summary

This document surveys the technical environment required to build, deploy, track, and operate the Mithaq premium 3D legal academy website.

The approved technical direction remains aligned with the project plan:

- Next.js
- React
- React Three Fiber
- Three.js
- Drei
- GSAP + ScrollTrigger
- Lenis
- Framer Motion
- Zustand
- TypeScript
- Tailwind CSS + CSS variables
- Blender for 3D assets
- GLB / glTF workflow
- Meshopt / gltfpack optimization
- KTX2 / Basis texture compression
- Vercel deployment
- Lighthouse / Axe for QA
- Sentry and Vercel Analytics if approved

Current technical readiness:

**Not ready for implementation.**

Reason:

No confirmed domain, hosting account, repository, WhatsApp number, form destination, analytics ownership, deployment owner, privacy/data handling decision, or platform access matrix is available in the workspace.

Planning may continue. Implementation must not begin until the blockers listed in this checklist are resolved.

---

## 2. Domain Status

| Item | Answer |
| ---- | ------ |
| Domain name | Pending client confirmation |
| DNS provider | Pending client confirmation |
| Domain owner | Pending client confirmation |
| Access available? | Missing / not confirmed |
| Existing website? | Pending client confirmation |
| Production domain status | Pending client confirmation |
| Staging domain needed? | Recommended yes, pending hosting decision |
| Issues / blockers | Domain/DNS access is not confirmed. Production deployment cannot be planned safely without domain owner and DNS provider. |

Required client actions:

- Confirm the final domain name.
- Confirm where DNS is managed.
- Confirm who owns the domain.
- Confirm whether DNS access can be granted.
- Confirm whether an existing site must be replaced.
- Confirm whether a staging subdomain is required.

---

## 3. Hosting / Deployment Status

Recommendation:

Use **Vercel** unless the client has a strong technical or business reason to use another host.

| Item | Answer |
| ---- | ------ |
| Hosting platform | Recommended: Vercel. Final approval pending |
| Vercel account available? | Pending client/team confirmation |
| Account owner | Pending client/team confirmation |
| Preview deployments required? | Recommended yes |
| Production deployment owner | Pending client/team confirmation |
| Alternative hosting required? | Not identified |
| Issues / blockers | Hosting decision and deployment account owner are not confirmed. |

Required client/team actions:

- Approve Vercel or name the required alternative.
- Confirm whether deployment will use client account or agency/team account.
- Confirm who owns production deployment.
- Confirm whether preview deployments are required for stakeholder review.

---

## 4. Existing Codebase Status

Workspace observation:

No application repository or existing Next.js/React codebase is present in the current workspace. The workspace currently contains planning and audit documents only.

| Item | Answer |
| ---- | ------ |
| Existing repo? | Not found in current workspace; pending client/team confirmation |
| Repo URL | Missing |
| Current framework | None found locally |
| Usable for production? | Cannot assess; no codebase provided |
| Access owner | Pending client/team confirmation |
| Recommended action | If no usable repo exists, start fresh with approved stack after Phase 0 blockers are resolved |
| Issues / blockers | Repo/codebase decision is not confirmed. |

Required client/team actions:

- Confirm whether an existing repo exists.
- Provide repo URL and access if it exists.
- Confirm whether any existing code should be reused.
- If no repo exists, approve fresh project setup later.

---

## 5. Repository Setup Requirements

Recommended repository setup:

- Repo name: `mithaq-website`
- Branches: `main`, `staging`, `feature/*`
- PR review required before merging to `main`
- CI checks required before production deployment
- Environment variables stored in Vercel, not committed to repo

| Item | Answer |
| ---- | ------ |
| Repo owner | Pending client/team confirmation |
| Repo name | Recommended: `mithaq-website` |
| Branch strategy | Recommended: `main`, `staging`, `feature/*` |
| PR review required? | Recommended yes |
| CI required? | Recommended yes |
| Issues / blockers | Repo owner and access model are not confirmed. |

Required client/team actions:

- Confirm GitHub/GitLab/Bitbucket owner.
- Confirm repository name.
- Confirm PR approval owner.
- Confirm CI expectations.
- Confirm who can manage environment variables.

---

## 6. Contact / Inquiry Infrastructure

Conversion direction from Phase 0:

- Primary: Register Interest via WhatsApp.
- Secondary: simple 3-field inquiry form.

| Item | Answer |
| ---- | ------ |
| Official WhatsApp number | Missing |
| WhatsApp owner | Pending client/admissions confirmation |
| WhatsApp Business? | Pending client/admissions confirmation |
| Prefilled message approved? | Recommended, pending approval |
| Source-aware WhatsApp text needed? | Recommended for tracking, pending approval |
| Official email | Missing |
| Form destination | Missing |
| Response owner | Pending client/admissions confirmation |
| Issues / blockers | WhatsApp number and response owner are missing. Final CTA implementation remains blocked. |

Required client actions:

- Provide official WhatsApp number.
- Confirm who responds to WhatsApp.
- Confirm whether WhatsApp Business is used.
- Approve prefilled WhatsApp message.
- Confirm whether source-aware text should be included.
- Provide official email.
- Confirm response process and owner.

---

## 7. Form Infrastructure

Recommended MVP fields:

1. Full Name
2. Phone / WhatsApp Number
3. Area of Interest / Workshop Interest

| Item | Answer |
| ---- | ------ |
| Form fields | Recommended 3-field MVP; pending client approval |
| Submit destination | Missing |
| Spam protection required? | Recommended yes; tool pending decision |
| Success message | Missing |
| Error message | Missing |
| Data owner | Pending client/admissions confirmation |
| Issues / blockers | Form destination, data owner, consent/privacy requirements, and spam protection decision are missing. |

Possible form destination options:

- Email
- Google Sheet
- CRM
- Database
- API route

Required client/team actions:

- Confirm form destination.
- Confirm who receives submissions.
- Confirm data owner.
- Confirm spam protection approach, such as Turnstile or reCAPTCHA.
- Approve success/error messages later during UX/content work.

---

## 8. Analytics Requirements

Recommended analytics events:

- `hero_cta_click`
- `whatsapp_click`
- `workshop_card_cta_click`
- `final_cta_click`
- `registration_form_start`
- `registration_form_submit`
- `form_error`
- `faq_open`
- `opening_skipped`
- `gavel_sequence_complete`

| Item | Answer |
| ---- | ------ |
| Analytics platform | Recommended: Vercel Analytics plus GA4 if marketing requires it. Final decision pending |
| Account owner | Pending client/team confirmation |
| Events required | Recommended events listed above; pending approval |
| Pixel required? | Pending marketing decision |
| Consent requirements | Pending privacy/legal decision |
| Issues / blockers | Analytics platform, account owner, and consent requirements are not confirmed. |

Required client/team actions:

- Confirm analytics tool.
- Confirm analytics account owner.
- Confirm if GA4, Meta Pixel, LinkedIn Insight Tag, or other pixels are required.
- Confirm tracking consent requirements.
- Approve conversion events.

---

## 9. Error Monitoring Requirements

Recommendation:

Use **Sentry** if custom WebGL/shader work is included.

| Item | Answer |
| ---- | ------ |
| Sentry required? | Recommended yes, pending approval |
| Account owner | Pending client/team confirmation |
| Error types to track | WebGL/canvas errors, shader/runtime errors, form submission errors, route/runtime errors |
| Issues / blockers | Sentry approval and account owner are not confirmed. |

Required client/team actions:

- Confirm whether Sentry is approved.
- Confirm account owner.
- Confirm whether WebGL/canvas and form submission errors should be tracked.

---

## 10. Asset Hosting Requirements

Recommended public paths:

```text
/public/models/
/public/textures/
/public/images/
/public/posters/
```

Recommended cache strategy:

- Use immutable cache headers for versioned 3D models and textures.
- Keep optimized assets under agreed size budgets.
- Do not host unoptimized GLB/textures in production.

| Item | Answer |
| ---- | ------ |
| Asset hosting location | Recommended: Vercel/public assets or CDN-backed public folder; pending implementation planning |
| Cache strategy | Recommended immutable cache for versioned `/models` and `/textures` assets |
| 3D asset folder | Recommended: `/public/models/` |
| Texture folder | Recommended: `/public/textures/` |
| Image folder | Recommended: `/public/images/` and `/public/posters/` |
| Issues / blockers | Final brand/content/3D assets are missing, so production asset hosting cannot be finalized. |

Required team actions:

- Confirm production asset size budgets during implementation planning.
- Confirm cache header configuration when hosting is approved.
- Keep placeholder assets separate from final production assets.

---

## 11. Environment Variables

Potential environment variables:

| Item | Answer |
| ---- | ------ |
| Required env vars | See list below |
| Owner of values | Pending client/team confirmation |
| Missing values | All values missing |
| Security notes | Do not expose private keys through `NEXT_PUBLIC_*`; store private values only as server-side env vars |

Candidate variables:

```text
NEXT_PUBLIC_SITE_URL=
NEXT_PUBLIC_WHATSAPP_NUMBER=
CONTACT_EMAIL=
FORM_DESTINATION=
GA_MEASUREMENT_ID=
SENTRY_DSN=
```

Security notes:

- `NEXT_PUBLIC_*` variables are visible to the browser.
- Do not place private API keys, private tokens, SMTP credentials, CRM secrets, or webhook secrets in public variables.
- Server-side form secrets must be stored as private environment variables in the deployment platform.

Required client/team actions:

- Provide final site URL after domain decision.
- Provide official WhatsApp number.
- Provide contact email.
- Confirm form destination.
- Provide analytics IDs if required.
- Provide Sentry DSN if approved.

---

## 12. Privacy / Legal Technical Requirements

The planned inquiry form will collect personal data.

| Item | Answer |
| ---- | ------ |
| Personal data collected | Yes, if form is used: name, phone/WhatsApp number, area of interest, optional message |
| Privacy policy required? | Recommended yes; pending legal/client confirmation |
| Cookie consent required? | Pending analytics/pixel decision |
| Terms required? | Pending legal/client confirmation |
| Disclaimer required? | Recommended yes for education/training vs legal advice/services; pending legal approval |
| Issues / blockers | Privacy/data handling decision is missing. Form implementation remains blocked until consent/privacy requirements are confirmed. |

Required client/legal actions:

- Confirm privacy policy requirements.
- Confirm whether cookie consent is needed.
- Confirm terms requirements.
- Confirm education/training disclaimer.
- Confirm how inquiry data may be used and stored.

---

## 13. Access Matrix

| Tool / Platform | Access Owner | Access Available? | Missing Access | Required Action |
| --------------- | ------------ | ----------------- | -------------- | --------------- |
| Domain / DNS | Pending client confirmation | Not confirmed | Domain registrar / DNS access | Confirm owner and grant access when needed |
| Vercel | Pending client/team confirmation | Not confirmed | Vercel project/account access | Approve hosting owner |
| GitHub | Pending client/team confirmation | Not confirmed | Repo/org access | Confirm repo owner and access model |
| Analytics | Pending client/marketing confirmation | Not confirmed | GA4/Vercel Analytics/Pixel access | Confirm platform and owner |
| Sentry | Pending client/team confirmation | Not confirmed | Sentry org/project access | Confirm if required |
| Email | Pending client/admissions confirmation | Not confirmed | Official inbox/form receiver | Provide email and owner |
| WhatsApp | Pending client/admissions confirmation | Not confirmed | Official number and responder access | Provide number and owner |
| Google Sheet / CRM | Pending client/admissions confirmation | Not confirmed | Destination access | Confirm form destination |
| Figma | Pending design/team confirmation | Not confirmed | Figma workspace access | Confirm design workspace |
| Asset folders | Pending client/project manager confirmation | Partially available locally for audits only | Shared client upload folder | Provide shared folder for official assets |

---

## 14. Technical Readiness Checklist

| Item | Status | Owner | Blocker? | Required Action |
| ---- | ------ | ----- | -------- | --------------- |
| Domain / DNS | Missing | Client / Domain owner | Yes | Confirm domain, DNS provider, and access |
| Hosting / Vercel | Pending client confirmation | Technical Lead / Client | Yes | Approve Vercel or alternative and identify deployment owner |
| Repo / Codebase | Missing | Technical Lead | Yes | Confirm existing repo or approve fresh setup later |
| WhatsApp Number | Missing | Client / Admissions | Yes | Provide official number and owner |
| Form Destination | Missing | Client / Admissions / Integration Lead | Yes | Confirm email, sheet, CRM, database, or API route |
| Analytics | Pending client confirmation | Marketing / Technical Lead | No, unless tracking required for launch | Confirm platform, owner, and events |
| Sentry | Pending client confirmation | Technical Lead | No, but recommended for WebGL | Confirm whether Sentry is approved |
| Asset Hosting | Pending implementation planning | Frontend Lead | No, blocked indirectly by missing assets | Confirm folders/cache strategy during implementation |
| Environment Variables | Missing | Technical Lead / Client | Yes | Provide values after domain/contact/analytics decisions |
| Privacy / Legal Technical Requirements | Missing | Legal Reviewer / Client | Yes if forms or analytics are used | Confirm privacy, consent, cookies, and disclaimer needs |
| Access Matrix | Missing | Project Manager | Yes | Identify access owners and grant access as needed |

---

## 15. Blockers

The following blockers are unresolved:

1. Domain/DNS access is not confirmed.
2. Hosting platform and deployment owner are not confirmed.
3. Repository/codebase decision is not confirmed.
4. Official WhatsApp number is missing.
5. WhatsApp response owner is missing.
6. Form destination is missing.
7. Data owner for submissions is missing.
8. Privacy/data handling requirements are not confirmed.
9. Analytics ownership is missing if tracking is required for launch.
10. Environment variable values are missing.
11. Access owners for DNS, Vercel, GitHub, analytics, Sentry, email, WhatsApp, CRM/sheet, Figma, and asset folders are not confirmed.

Implementation must not begin until the critical blockers are resolved or formally marked as not required for MVP.

---

## 16. Final Technical Readiness Status

**QA BLOCKED.**

P0.03 cannot be marked technically ready because required environment answers and access details are missing.

Exact missing answers required:

- Domain name, DNS provider, owner, and access status.
- Hosting approval, Vercel account owner, and deployment owner.
- Existing repo status or approval to start fresh later.
- Repository owner, name, branch strategy, and PR/CI expectations.
- Official WhatsApp number and response owner.
- Official email and form destination.
- Form spam protection decision.
- Analytics platform, account owner, events, and consent requirements.
- Sentry approval and account owner.
- Environment variable values and owners.
- Privacy policy, cookie consent, terms, disclaimer, and personal data handling decisions.
- Access owner matrix for all required tools/platforms.

Required next action:

Client/project owner and technical lead must complete the missing answers above before implementation begins.

