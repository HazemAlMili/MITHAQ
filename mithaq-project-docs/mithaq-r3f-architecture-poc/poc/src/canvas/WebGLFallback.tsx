import { MITHAQ_SCENE_MAP } from '../data/sceneMap';
import { useMithaqStore } from '../store/mithaqStore';

export function WebGLFallback() {
  const activeScene = useMithaqStore((state) => state.activeScene);
  const label = MITHAQ_SCENE_MAP.find((scene) => scene.id === activeScene)?.label ?? 'Unknown scene';

  return (
    <div className="webgl-fallback" role="status" aria-live="polite">
      <p className="eyebrow">Mithaq WebGL fallback active</p>
      <h1>{label}</h1>
      <p>CTA placeholder</p>
    </div>
  );
}
