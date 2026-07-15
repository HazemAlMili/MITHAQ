# Arabic Localization Handoff

## RTL Layout Notes

- Use `dir="rtl"` for Arabic scene containers.
- Use `text-align: start`, not hard-coded `right`.
- Use logical spacing: `margin-inline`, `padding-inline`, and `inset-inline`.
- Keep DOM order semantic; do not reverse DOM order just to match visual composition.
- CTA groups should mirror visually in RTL while preserving logical tab order.
- Do not mix Arabic and English copy in one animated text line.

## Recommended Line Breaks

Line breaks are design guidance only.

### Scene 01

ميثاق

أكاديمية قانونية تقوم على الانضباط
والجاهزية والعمل الجاد للدخول إلى الممارسة المهنية.

### Scene 02

تدريب قانوني عملي
لجاهزية مهنية أوضح

### Scene 03

المعرفة القانونية
تحتاج إلى تدريب يختبرها

### Scene 04

منهج يحوّل المعرفة
إلى قدرة مهنية

### Scene 05

خمس قدرات
لبداية الممارسة القانونية

### Scene 06

تجارب تدريب مركّزة
لا بطاقات دورات مزدحمة

### Scene 07

الإرشاد الموثوق
جزء من التدريب الجاد

### Scene 08

الثقة تُبنى
على أدلة موثقة

### Scene 09

قبل أن تسأل
اعرف الأساسيات

### Scene 10

ابدأ بحوار واضح
حول التدريب المناسب لك

## Maximum Preferred Heading Lines

- Desktop display: 2 lines preferred, 3 lines allowed for Scene 06 if needed.
- Mobile display: 2-3 lines maximum.
- CTA labels should remain one line when possible.
- Avoid squeezing Arabic by reducing line-height too far; Arabic needs more vertical room than Latin text.

## Words That Should Remain Together

- أكاديمية ميثاق القانونية
- تدريب قانوني عملي
- الجاهزية المهنية
- البحث القانوني
- الرأي القانوني
- الصياغة القانونية
- منهج ميثاق
- ورش ميثاق
- سجّل اهتمامك
- اسأل عبر واتساب

## CTA Width Risks

- `اسأل عن ورش ميثاق` is acceptable for desktop; mobile variant `اسأل عن الورش` is safer.
- `اكتشف منهج ميثاق` is acceptable; mobile variant `اكتشف المنهج` is safer.
- `اطّلع على محاور التدريب` may require a medium-width button.
- `اطلب معلومات إضافية` is wider than English and should not be forced into a narrow chip.

## Mixed-Direction Text Issues

- Keep `WhatsApp` either as `واتساب` in public copy or as a configured brand spelling across the site.
- Keep `[CLIENT INPUT REQUIRED: ...]` placeholders in LTR-safe documentation only; they should not appear in public UI.
- If `WebGL`, `R3F`, `CTA`, or `RTL` appear in handoff notes, wrap them with direction-safe markup in implementation.
- Avoid inline URLs inside Arabic body copy where possible; use CTA elements.

## Punctuation Concerns

- Use Arabic comma `،` in Arabic sentences.
- Use Arabic question mark `؟` in public Arabic questions when future FAQ content is written.
- Avoid excessive punctuation and exclamation marks.
- Keep colon-heavy internal labels out of public UI.

## Font and Shaping Considerations

- Tajawal remains the safe Arabic body/UI default.
- Tajawal 700 remains the safe Arabic display default.
- Lemonada should remain accent-only pending review and should not carry long legal copy.
- Do not animate Arabic letter-by-letter.
- Use full-word, full-line, fade, slide, or block reveals for Arabic.
- Verify Arabic shaping in real browser rendering, especially diacritics in `سجّل` and `تخطَّ`.

## Mobile Risks

- Scene 03 body is conceptually dense; use the mobile variant on narrow screens.
- Scene 06 headline can become long; use mobile headline when card/dossier visuals reduce width.
- Scene 07 must not imply approved mentor identities before profiles are confirmed.
- Scene 08 proof placeholders must not leak to public UI.
- Scene 10 CTA buttons should stack if button text wraps.

## Visual Emphasis in RTL

- If emphasis exists, it should follow Arabic reading flow from right to left.
- Do not rely on English-style left-positioned emphasis marks.
- Gold emphasis should be restrained and never used for long Arabic body copy.

## Dependencies Awaiting Client Approval

- Final wordmark and seal approval.
- Final opening fallback review.
- Final WhatsApp number.
- Form destination and privacy language.
- Client approval of P6.01 recommended hero copy.
- Approved form success message.
- Approved instructor profiles.
- Confirmed workshop inventory.
- Verified proof points.
- Approved FAQ answers and policy details.
- Final legal/compliance review of CTA language.

## Implementation Scope Confirmation

This task did not implement RTL, i18n routing, React, R3F, GSAP, CSS, Figma, CMS, or production content integration. It created Arabic copy and handoff guidance only.
