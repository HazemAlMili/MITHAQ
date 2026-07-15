# Scene Copy Handoff

## Suggested Line Breaks

Use line breaks as design guidance only. Do not hard-code meaning into line breaks.

### Scene 01

Mithaq

A legal academy built around discipline, readiness, and the serious work of entering practice.

### Scene 02

Practical Legal Training
for Professional Readiness

Mithaq helps law graduates and early-career legal professionals build the research, writing, and workplace skills that real legal practice expects.

### Scene 03

Legal Knowledge Needs
Practice Behind It

### Scene 04

A Method for Turning Knowledge
Into Capability

### Scene 05

Five Capabilities
for Early Legal Practice

### Scene 06

Focused Training Engagements,
Not Course Clutter

### Scene 07

Guidance Must Come
From Credible People

### Scene 08

Trust Built
on Verified Evidence

### Scene 09

Before You Ask,
Get the Essentials

### Scene 10

Begin With the Right
Legal Training Conversation

## Maximum Content Widths

- Eyebrows: 18-28 characters where possible.
- Display headlines: 10-14 words maximum on desktop, 9 words maximum on mobile.
- Body copy: target 56-68 characters per line on desktop.
- Mobile body copy: target 24-32 characters per line, with no essential phrase split across more than two lines.
- CTA labels: keep as single-line buttons whenever possible.

## Emphasis Words

The following words may receive visual emphasis if the design system supports it:

- Scene 02: Practical Legal Training; Professional Readiness
- Scene 03: Knowledge; Practice
- Scene 04: Method; Capability
- Scene 05: Capabilities
- Scene 08: Verified Evidence
- Scene 10: Training Conversation

Do not over-emphasize `gold` or use gold text for body copy.

## Copy That Must Not Be Split

- Mithaq Legal Academy
- Practical Legal Training
- Professional Readiness
- Ask About Mithaq Workshops
- Discover the Mithaq Method
- Legal Research and Opinion
- Legal Writing and Memo Drafting
- Register Your Interest

## Mobile Truncation Risks

- Scene 02 headline should use the P6.01 mobile variant.
- Scene 06 headline may wrap awkwardly; use the mobile variant when card/dossier visuals reduce space.
- Scene 07 headline should avoid looking like a claim about currently approved mentors until profiles exist.
- Scene 10 headline should use the mobile variant if the final CTA section is compact.

## RTL / Localization Considerations for P6.03

- Arabic localization should not be literal if it weakens clarity or legal tone.
- Keep English and Arabic text as separate localizable elements.
- Do not animate Arabic letter-by-letter.
- Avoid mixing English and Arabic fonts on one animated line.
- Arabic headings may need more line-height than English.
- The P6.03 translator/localization reviewer should re-evaluate the tone of "covenant", "readiness", "practice gap", and "mentor" language.

## Dynamic Content Boundaries

The following must remain dynamic or pending until approved:

- Workshop cards, titles, formats, dates, durations, prices, availability, CTAs, and details.
- Mentor names, roles, bios, photos, expertise labels, and credentials.
- Proof points, participant numbers, testimonials, logos, institutional relationships, certificates, and affiliations.
- FAQ questions and answers.
- WhatsApp destination and inquiry form destination.
- Privacy/compliance language.

## Implementation Notes

- All main meaning must remain DOM text, not baked into 3D, images, or canvas.
- 3D and motion may support tone but must not be required to understand the copy.
- CTA content must be reachable without WebGL.
- Reduced-motion and static fallback should preserve Scene 02 and Scene 10 conversion clarity.
- P5.08 mobile performance limits should keep mobile copy text-first.

## Scope Confirmation

No React, R3F, GSAP, CSS, Figma, CMS, Arabic localization, workshop content, FAQ content, proof content, or production implementation was started in P6.02.
