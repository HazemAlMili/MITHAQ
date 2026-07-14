import { Color, Vector2 } from 'three';

export const MITHAQ_COLORS = {
  void: '#08070F',
  ink: '#0E0C1A',
  chamber: '#161422',
  wood: '#1C1510',
  sealGold: '#C4913A',
  goldLight: '#E8C97A',
  goldDim: '#8B6420',
  parchment: '#F2E8D0',
} as const;

export const createRippleUniforms = () => ({
  uProgress: { value: 0.55 },
  uImpactPoint: { value: new Vector2(0.5, 0.5) },
  uGoldColor: { value: new Color(MITHAQ_COLORS.sealGold) },
  uOpacity: { value: 0.74 },
  uRingWidth: { value: 0.026 },
  uEchoStrength: { value: 0.34 },
  uTime: { value: 0 },
});

export const createFractureUniforms = () => ({
  uProgress: { value: 0.64 },
  uFractureProgress: { value: 0.64 },
  uGoldColor: { value: new Color(MITHAQ_COLORS.sealGold) },
  uLineCount: { value: 8 },
  uLineWidth: { value: 0.016 },
  uGlowStrength: { value: 0.32 },
  uSeed: { value: 4.0 },
  uOpacity: { value: 0.72 },
  uTime: { value: 0 },
});

export const createSealEmergenceUniforms = () => ({
  uProgress: { value: 0.68 },
  uGoldColor: { value: new Color(MITHAQ_COLORS.sealGold) },
  uHighlightColor: { value: new Color(MITHAQ_COLORS.goldLight) },
  uEmissiveStrength: { value: 0.38 },
  uRevealSoftness: { value: 0.16 },
  uOpacity: { value: 0.94 },
  uTime: { value: 0 },
});

export const createParticleUniforms = () => ({
  uTime: { value: 0 },
  uOpacity: { value: 0.42 },
  uGoldColor: { value: new Color(MITHAQ_COLORS.sealGold) },
  uPointSize: { value: 5.5 },
  uDriftStrength: { value: 0.12 },
  uDepthFade: { value: 0.75 },
});
