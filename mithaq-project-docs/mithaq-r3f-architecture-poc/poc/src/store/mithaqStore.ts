import { create } from 'zustand';
import { clamp } from '../utils/clamp';

export type DeviceTier = 'high' | 'mid' | 'low';
export type Language = 'en' | 'ar';

export interface MithaqStore {
  activeScene: number;
  sceneProgress: number;
  scrollProgress: number;

  openingComplete: boolean;
  openingProgress: number;
  gavelStruck: boolean;
  sealRevealed: boolean;

  criticalAssetsLoaded: boolean;
  loadingProgress: number;

  reducedMotion: boolean;
  webGLAvailable: boolean;
  deviceTier: DeviceTier;

  navOpen: boolean;
  activeModal: string | null;
  language: Language;

  ctaSource: string | null;

  setActiveScene: (n: number) => void;
  setSceneProgress: (n: number) => void;
  setScrollProgress: (n: number) => void;

  completeOpening: () => void;
  resetOpening: () => void;
  setOpeningProgress: (n: number) => void;
  setGavelStruck: (v: boolean) => void;
  setSealRevealed: (v: boolean) => void;

  setCriticalAssetsLoaded: (v: boolean) => void;
  setLoadingProgress: (n: number) => void;

  setReducedMotion: (v: boolean) => void;
  setWebGLAvailable: (v: boolean) => void;
  setDeviceTier: (t: DeviceTier) => void;

  setNavOpen: (v: boolean) => void;
  openModal: (id: string) => void;
  closeModal: () => void;
  setLanguage: (l: Language) => void;

  setCtaSource: (source: string | null) => void;
  skipOpening: () => void;
}

export const useMithaqStore = create<MithaqStore>((set) => ({
  activeScene: 1,
  sceneProgress: 0,
  scrollProgress: 0,

  openingComplete: false,
  openingProgress: 0,
  gavelStruck: false,
  sealRevealed: false,

  criticalAssetsLoaded: false,
  loadingProgress: 0,

  reducedMotion: false,
  webGLAvailable: true,
  deviceTier: 'mid',

  navOpen: false,
  activeModal: null,
  language: 'en',

  ctaSource: null,

  setActiveScene: (n) => set({ activeScene: Math.min(10, Math.max(1, Math.round(n))) }),
  setSceneProgress: (n) => set({ sceneProgress: clamp(n) }),
  setScrollProgress: (n) => set({ scrollProgress: clamp(n) }),

  completeOpening: () => set({ openingComplete: true, openingProgress: 1, gavelStruck: true, sealRevealed: true }),
  resetOpening: () => set({ openingComplete: false, openingProgress: 0, gavelStruck: false, sealRevealed: false }),
  setOpeningProgress: (n) => set({ openingProgress: clamp(n) }),
  setGavelStruck: (v) => set({ gavelStruck: v }),
  setSealRevealed: (v) => set({ sealRevealed: v }),

  setCriticalAssetsLoaded: (v) => set({ criticalAssetsLoaded: v }),
  setLoadingProgress: (n) => set({ loadingProgress: clamp(n) }),

  setReducedMotion: (v) => set({ reducedMotion: v }),
  setWebGLAvailable: (v) => set({ webGLAvailable: v }),
  setDeviceTier: (t) => set({ deviceTier: t }),

  setNavOpen: (v) => set({ navOpen: v }),
  openModal: (id) => set({ activeModal: id }),
  closeModal: () => set({ activeModal: null }),
  setLanguage: (l) => set({ language: l }),

  setCtaSource: (source) => set({ ctaSource: source }),
  skipOpening: () => set({ openingComplete: true, openingProgress: 1, gavelStruck: true, sealRevealed: true, activeScene: 2 })
}));
