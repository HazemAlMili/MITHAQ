import { useEffect } from 'react';
import { MITHAQ_SCENE_MAP, getSceneByProgress } from '../data/sceneMap';
import { useMithaqStore } from '../store/mithaqStore';
import { clamp } from '../utils/clamp';
import { mapRange } from '../utils/mapRange';

export function useScrollProgress(): void {
  const setScrollProgress = useMithaqStore((state) => state.setScrollProgress);
  const setActiveScene = useMithaqStore((state) => state.setActiveScene);
  const setSceneProgress = useMithaqStore((state) => state.setSceneProgress);
  const setOpeningProgress = useMithaqStore((state) => state.setOpeningProgress);
  const setGavelStruck = useMithaqStore((state) => state.setGavelStruck);
  const setSealRevealed = useMithaqStore((state) => state.setSealRevealed);
  const completeOpening = useMithaqStore((state) => state.completeOpening);

  useEffect(() => {
    let raf = 0;

    const update = () => {
      const maxScroll = Math.max(1, document.documentElement.scrollHeight - window.innerHeight);
      const progress = clamp(window.scrollY / maxScroll);
      const activeScene = getSceneByProgress(progress);
      const sceneProgress = mapRange(progress, activeScene.start, activeScene.end);

      setScrollProgress(progress);
      setActiveScene(activeScene.id);
      setSceneProgress(sceneProgress);

      if (activeScene.id === 1) {
        setOpeningProgress(sceneProgress);
        setGavelStruck(sceneProgress >= 0.36);
        setSealRevealed(sceneProgress >= 0.68);
      } else if (activeScene.id > 1) {
        completeOpening();
      }
    };

    const onScroll = () => {
      window.cancelAnimationFrame(raf);
      raf = window.requestAnimationFrame(update);
    };

    update();
    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', onScroll);

    return () => {
      window.cancelAnimationFrame(raf);
      window.removeEventListener('scroll', onScroll);
      window.removeEventListener('resize', onScroll);
    };
  }, [
    completeOpening,
    setActiveScene,
    setGavelStruck,
    setOpeningProgress,
    setSceneProgress,
    setScrollProgress,
    setSealRevealed
  ]);
}

export function scrollToScene(sceneId: number): void {
  const scene = MITHAQ_SCENE_MAP.find((item) => item.id === sceneId);
  if (!scene) {
    return;
  }

  const maxScroll = Math.max(1, document.documentElement.scrollHeight - window.innerHeight);
  window.scrollTo({ top: maxScroll * scene.start + 2, behavior: 'auto' });
}
