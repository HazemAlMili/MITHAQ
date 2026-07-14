# Gavel R3F Handoff Notes

**Ticket:** P5.02 - Gavel Model Production  
**Status:** PASS WITH CONDITIONS  
**Date:** 2026-06-21  

---

## Import Path

Recommended future production path:

```txt
/public/assets/models/mithaq/gavel.opt.glb
```

Do not move the asset into production paths during P5.02.

---

## Scale

Suggested initial R3F scale:

```txt
scale: 1.0
```

Final scale must be validated against the final Seal and desk. The asset is modeled in a neutral Blender scale and should be treated as a gavel-sized object relative to a legal desk scene.

---

## Orientation

The gavel head runs along the local X axis. The handle extends along the negative local Y axis.

Use a parent group in R3F for Scene 01 composition and rotate/position that group for:

- suspended descent
- strike contact
- resting callback

---

## Pivot / Strike Animation

Blender includes:

```txt
Gavel_Pivot_Helper
```

Location:

```txt
(0, -0.18, 0)
```

This helper marks the intended animation pivot near the handle/head joint.

Recommended animation:

- Scroll-driven descent
- Very short controlled contact
- No bounce
- No violent smash
- Gavel recedes after Seal reveal

---

## Contact Point

Blender includes:

```txt
Gavel_Contact_Point_Negative_X
```

Location:

```txt
(-0.78, 0, 0)
```

Use this as the conceptual desk impact/contact reference. The gavel's negative-X head face is the intended striking face.

---

## Materials

| Material | R3F Tuning Notes |
| --- | --- |
| `Mithaq_Dark_Wood` | Keep high roughness; avoid orange or glossy plastic response. |
| `Mithaq_Dark_Wood_Darker_Endgrain` | End/contact faces should stay dark and serious. |
| `Mithaq_Muted_Brass` | High metalness but controlled roughness; avoid mirror chrome. |
| `Mithaq_Edge_Wear_Optional` | Subtle highlight only; no glitter/gold flood. |

No external textures are used. Materials are procedural in Blender and exported as material values/noise-bump source behavior where supported.

---

## Shadows

Recommended:

- `castShadow = true`
- `receiveShadow = false` on gavel meshes
- desk receives shadow
- use soft warm key light from upper-left

Avoid:

- harsh horror shadows
- neon rim lighting
- overbright brass highlight

---

## Mobile

The optimized GLB is small enough for testing on mobile, but mobile use is not automatically approved.

Mobile options:

1. Use same GLB if Scene 01 vertical-slice testing passes.
2. Use static poster if FPS or memory drops.
3. Create future mobile LOD only if testing requires it.

---

## Fallback

Fallback equivalent:

- Static seal/desk hero poster
- Final CTA static seal/gavel callback poster

The gavel is not required for understanding content or reaching CTA.

---

## Limitations

- Optimized GLB uses Blender Draco compression because `gltfpack` is unavailable in this shell.
- Final R3F import validation is pending.
- Final Scene 01 lighting validation is pending.
- Relative scale to final Seal/desk is pending.
- Real-device performance validation is pending.

