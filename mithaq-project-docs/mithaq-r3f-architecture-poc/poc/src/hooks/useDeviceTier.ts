import { useEffect } from 'react';
import { DeviceTier, useMithaqStore } from '../store/mithaqStore';

declare global {
  interface Navigator {
    deviceMemory?: number;
  }
}

function detectDeviceTier(webGLAvailable: boolean): DeviceTier {
  if (!webGLAvailable) {
    return 'low';
  }

  const cores = navigator.hardwareConcurrency ?? 4;
  const memory = navigator.deviceMemory ?? 4;
  const mobile = /Android|iPhone|iPad|iPod|Mobile/i.test(navigator.userAgent);

  if (mobile || cores <= 4 || memory <= 4) {
    return 'low';
  }

  if (cores >= 8 && memory >= 8) {
    return 'high';
  }

  return 'mid';
}

export function useDeviceTier(): void {
  const webGLAvailable = useMithaqStore((state) => state.webGLAvailable);
  const setDeviceTier = useMithaqStore((state) => state.setDeviceTier);

  useEffect(() => {
    const forcedTier = new URLSearchParams(window.location.search).get('tier');
    if (forcedTier === 'high' || forcedTier === 'mid' || forcedTier === 'low') {
      setDeviceTier(forcedTier);
      return;
    }

    setDeviceTier(detectDeviceTier(webGLAvailable));
  }, [setDeviceTier, webGLAvailable]);
}
