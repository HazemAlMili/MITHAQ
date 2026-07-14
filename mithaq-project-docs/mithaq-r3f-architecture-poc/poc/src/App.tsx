import { MithaqCanvas } from './canvas/MithaqCanvas';
import { ScrollDebugPanel } from './components/ScrollDebugPanel';
import { SceneProgressMarkers } from './components/SceneProgressMarkers';
import { MITHAQ_SCENE_MAP } from './data/sceneMap';
import { useDeviceTier } from './hooks/useDeviceTier';
import { useReducedMotion } from './hooks/useReducedMotion';
import { useScrollProgress } from './hooks/useScrollProgress';
import { useWebGLSupport } from './hooks/useWebGLSupport';
import { useEffect } from 'react';
import { useMithaqStore } from './store/mithaqStore';

export default function App() {
  const setReducedMotion = useMithaqStore((state) => state.setReducedMotion);
  const setWebGLAvailable = useMithaqStore((state) => state.setWebGLAvailable);
  const setDeviceTier = useMithaqStore((state) => state.setDeviceTier);
  const setActiveScene = useMithaqStore((state) => state.setActiveScene);
  const setSceneProgress = useMithaqStore((state) => state.setSceneProgress);
  const setOpeningProgress = useMithaqStore((state) => state.setOpeningProgress);
  const setGavelStruck = useMithaqStore((state) => state.setGavelStruck);
  const setSealRevealed = useMithaqStore((state) => state.setSealRevealed);

  useWebGLSupport();
  useDeviceTier();
  useReducedMotion();
  useScrollProgress();

  useEffect(() => {
    const params = new URLSearchParams(window.location.search);
    const sceneId = Number(params.get('scene'));
    const reduced = params.get('reduced') === 'true';

    if (reduced) {
      window.localStorage.setItem('mithaq-reduced-motion-override', 'true');
      setReducedMotion(true);
    }

    if (params.get('webgl') === 'false') {
      setWebGLAvailable(false);
    }

    const forcedTier = params.get('tier');
    if (forcedTier === 'low' || forcedTier === 'mid' || forcedTier === 'high') {
      setDeviceTier(forcedTier);
    }

    const scene = MITHAQ_SCENE_MAP.find((item) => item.id === sceneId);
    if (scene) {
      window.requestAnimationFrame(() => {
        const maxScroll = Math.max(1, document.documentElement.scrollHeight - window.innerHeight);
        window.scrollTo({ top: maxScroll * scene.start + 4, behavior: 'auto' });
      });
    }
  }, [setDeviceTier, setReducedMotion, setWebGLAvailable]);

  useEffect(() => {
    window.__MITHAQ_SET_AUDIT_PROGRESS__ = (progress: number) => {
      const clamped = Math.min(1, Math.max(0, progress));
      setActiveScene(1);
      setSceneProgress(clamped);
      setOpeningProgress(clamped);
      setGavelStruck(clamped >= 0.36);
      setSealRevealed(clamped >= 0.68);
    };

    return () => {
      delete window.__MITHAQ_SET_AUDIT_PROGRESS__;
    };
  }, [setActiveScene, setGavelStruck, setOpeningProgress, setSceneProgress, setSealRevealed]);

  return (
    <main className="app-shell">
      <MithaqCanvas />
      <ScrollDebugPanel />
      <SceneProgressMarkers />
      <section className="dom-intro" aria-label="Architecture proof notice">
        <p className="eyebrow">Mithaq R3F architecture proof</p>
        <h1>Persistent canvas, scroll mapping, and scene proxy validation.</h1>
        <p>This is not final UI and contains no production website content.</p>
      </section>
      <div className="scroll-sections">
        {MITHAQ_SCENE_MAP.map((scene) => (
          <section className="scroll-section" key={scene.id} data-scene-id={scene.id}>
            <p className="eyebrow">Scene {scene.id.toString().padStart(2, '0')}</p>
            <h2>{scene.label}</h2>
            <p>Proxy section for scroll mapping only. Final content and visual design are intentionally out of scope.</p>
          </section>
        ))}
      </div>
    </main>
  );
}
