import { MITHAQ_SCENE_MAP, getSceneByProgress } from '../data/sceneMap';
import { useMithaqStore } from '../store/mithaqStore';
import { mapRange } from '../utils/mapRange';

export function useSceneProgress() {
  const scrollProgress = useMithaqStore((state) => state.scrollProgress);
  const activeScene = getSceneByProgress(scrollProgress);
  const sceneProgress = mapRange(scrollProgress, activeScene.start, activeScene.end);

  return {
    sceneMap: MITHAQ_SCENE_MAP,
    activeScene,
    sceneProgress
  };
}
