import { useFrame, useThree } from '@react-three/fiber';
import { useEffect } from 'react';
import { useMithaqStore } from '../store/mithaqStore';

declare global {
  interface Window {
    __MITHAQ_AUDIT__?: {
      rendererInfo: {
        calls: number;
        triangles: number;
        geometries: number;
        textures: number;
        programs: number | null;
      };
      state: {
        activeScene: number;
        sceneProgress: number;
        deviceTier: string;
        reducedMotion: boolean;
        postProcessing: boolean;
      };
      updatedAt: number;
    };
  }
}

declare global {
  interface Window {
    __MITHAQ_SET_AUDIT_PROGRESS__?: (progress: number) => void;
  }
}

export function MobilePerformanceProbe() {
  const gl = useThree((state) => state.gl);
  const activeScene = useMithaqStore((state) => state.activeScene);
  const sceneProgress = useMithaqStore((state) => state.sceneProgress);
  const deviceTier = useMithaqStore((state) => state.deviceTier);
  const reducedMotion = useMithaqStore((state) => state.reducedMotion);

  useEffect(() => {
    window.__MITHAQ_AUDIT__ = {
      rendererInfo: {
        calls: 0,
        triangles: 0,
        geometries: 0,
        textures: 0,
        programs: null
      },
      state: {
        activeScene,
        sceneProgress,
        deviceTier,
        reducedMotion,
        postProcessing: false
      },
      updatedAt: performance.now()
    };
  }, [activeScene, deviceTier, reducedMotion, sceneProgress]);

  useFrame(() => {
    window.__MITHAQ_AUDIT__ = {
      rendererInfo: {
        calls: gl.info.render.calls,
        triangles: gl.info.render.triangles,
        geometries: gl.info.memory.geometries,
        textures: gl.info.memory.textures,
        programs: gl.info.programs?.length ?? null
      },
      state: {
        activeScene,
        sceneProgress,
        deviceTier,
        reducedMotion,
        postProcessing: deviceTier === 'high' && !reducedMotion
      },
      updatedAt: performance.now()
    };
  });

  return null;
}
