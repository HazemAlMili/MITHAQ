# Mithaq Workshop Dossier 3D Cards

Ticket: P5.09 — Workshop Dossier 3D Cards  
Status: PASS WITH CONDITIONS  
Date: 2026-07-14

## Purpose

This package creates a lightweight reusable 3D dossier system for Scene 06 — Workshops & Course Preview. The dossiers are atmospheric legal objects only. Real workshop names, details, CTAs, prices, dates, availability, and instructor data must remain semantic HTML in production.

## Outputs

- `source/workshop-dossier-master.blend`
- `exports/workshop-dossier.desktop.glb`
- `exports/workshop-dossier.desktop.opt.glb`
- `exports/workshop-dossier.mobile.glb`
- `exports/workshop-dossier.mobile.opt.glb`
- `textures/workshop-dossier-atlas.webp`
- `sandbox/`
- `captures/dossier-desktop-resting.png`
- `captures/dossier-desktop-hover.png`
- `captures/dossier-multiple-layout.png`
- `captures/dossier-mobile-light.png`
- `reports/dossier-production-report.md`
- `reports/asset-metrics.csv`
- `reports/isolated-performance-report.md`
- `reports/dossier-handoff-notes.md`

## Quick Validation Summary

- Desktop dossier: `1,480` triangles, `3` meshes, optimized GLB `17,544` bytes.
- Mobile dossier: `420` triangles, `3` meshes, optimized GLB `8,304` bytes.
- Sandbox production build: passed.
- Sandbox final capture pass: `6` captures, `0` console errors.
- Scene 06 production integration: not started.

## Conditions

- `gltfpack` is unavailable in the current shell; optimized GLBs use Blender Draco export.
- Tiny geometric seal treatment is a restrained stand-in pending final approved Mithaq seal artwork.
- Real-device mobile approval remains pending, especially because P5.08 failed the full mobile runtime performance floor.

