import { MITHAQ_SCENE_MAP } from '../data/sceneMap';
import { useMithaqStore } from '../store/mithaqStore';

export function SceneProgressMarkers() {
  const activeScene = useMithaqStore((state) => state.activeScene);
  const sceneProgress = useMithaqStore((state) => state.sceneProgress);

  return (
    <div className="scene-markers" aria-label="Scene progress markers">
      {MITHAQ_SCENE_MAP.map((scene) => (
        <div key={scene.id} className={`scene-marker ${activeScene === scene.id ? 'is-active' : ''}`}>
          <span>{scene.id.toString().padStart(2, '0')}</span>
          <b style={{ transform: `scaleX(${activeScene === scene.id ? sceneProgress : activeScene > scene.id ? 1 : 0})` }} />
        </div>
      ))}
    </div>
  );
}
