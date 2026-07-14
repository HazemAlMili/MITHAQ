import { Canvas } from '@react-three/fiber';
import { Suspense } from 'react';
import { SceneManager } from './SceneManager';
import { SharedEnvironment } from './SharedEnvironment';
import { PostProcessingGate } from './PostProcessingGate';
import { WebGLFallback } from './WebGLFallback';
import { useMithaqStore } from '../store/mithaqStore';
import { MobilePerformanceProbe } from '../audit/MobilePerformanceProbe';

function dprForTier(tier: 'high' | 'mid' | 'low'): [number, number] {
  if (tier === 'high') {
    return [1, 1.5];
  }

  if (tier === 'mid') {
    return [1, 1];
  }

  return [1, 1];
}

export function MithaqCanvas() {
  const webGLAvailable = useMithaqStore((state) => state.webGLAvailable);
  const deviceTier = useMithaqStore((state) => state.deviceTier);

  if (!webGLAvailable) {
    return <WebGLFallback />;
  }

  return (
    <div className="canvas-layer" aria-hidden="true">
      <Canvas
        camera={{ position: [0, 1.35, 4.9], fov: 42, near: 0.1, far: 50 }}
        dpr={dprForTier(deviceTier)}
        gl={{ antialias: deviceTier === 'high', powerPreference: deviceTier === 'high' ? 'high-performance' : 'default' }}
      >
        <Suspense fallback={null}>
          <SharedEnvironment />
          <SceneManager />
          <PostProcessingGate />
          <MobilePerformanceProbe />
        </Suspense>
      </Canvas>
    </div>
  );
}
