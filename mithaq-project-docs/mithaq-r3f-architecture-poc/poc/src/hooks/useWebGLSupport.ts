import { useEffect } from 'react';
import { useMithaqStore } from '../store/mithaqStore';

export function detectWebGLSupport(): boolean {
  try {
    const canvas = document.createElement('canvas');
    return Boolean(canvas.getContext('webgl2') || canvas.getContext('webgl'));
  } catch {
    return false;
  }
}

export function useWebGLSupport(): void {
  const setWebGLAvailable = useMithaqStore((state) => state.setWebGLAvailable);

  useEffect(() => {
    setWebGLAvailable(detectWebGLSupport());
  }, [setWebGLAvailable]);
}
