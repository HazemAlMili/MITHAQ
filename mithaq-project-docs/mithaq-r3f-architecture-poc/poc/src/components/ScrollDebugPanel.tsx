import { MITHAQ_SCENE_MAP } from '../data/sceneMap';
import { scrollToScene } from '../hooks/useScrollProgress';
import { useMithaqStore } from '../store/mithaqStore';
import { DeviceTierBadge } from './DeviceTierBadge';
import { ReducedMotionToggle } from './ReducedMotionToggle';

export function ScrollDebugPanel() {
  const activeScene = useMithaqStore((state) => state.activeScene);
  const sceneProgress = useMithaqStore((state) => state.sceneProgress);
  const scrollProgress = useMithaqStore((state) => state.scrollProgress);
  const reducedMotion = useMithaqStore((state) => state.reducedMotion);
  const webGLAvailable = useMithaqStore((state) => state.webGLAvailable);
  const setCtaSource = useMithaqStore((state) => state.setCtaSource);
  const activeLabel = MITHAQ_SCENE_MAP.find((scene) => scene.id === activeScene)?.label ?? 'Unknown';

  return (
    <aside className="debug-panel" data-testid="debug-panel">
      <p className="eyebrow">P5.07 Architecture PoC</p>
      <h2>{activeScene.toString().padStart(2, '0')} / {activeLabel}</h2>
      <dl>
        <div><dt>Global scroll</dt><dd>{scrollProgress.toFixed(3)}</dd></div>
        <div><dt>Scene progress</dt><dd>{sceneProgress.toFixed(3)}</dd></div>
        <div><dt>Reduced motion</dt><dd>{reducedMotion ? 'true' : 'false'}</dd></div>
        <div><dt>WebGL</dt><dd>{webGLAvailable ? 'available' : 'fallback'}</dd></div>
      </dl>
      <DeviceTierBadge />
      <ReducedMotionToggle />
      <button className="debug-button" type="button" onClick={() => setCtaSource(`scene-${activeScene}`)}>
        Set CTA source placeholder
      </button>
      <div className="scene-jump-list" aria-label="Jump to scene">
        {MITHAQ_SCENE_MAP.map((scene) => (
          <button key={scene.id} type="button" onClick={() => scrollToScene(scene.id)}>
            {scene.id}
          </button>
        ))}
      </div>
    </aside>
  );
}
