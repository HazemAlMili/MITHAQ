import { Html } from '@react-three/drei';
import { useMithaqStore } from '../store/mithaqStore';

export function PostProcessingGate() {
  const reducedMotion = useMithaqStore((state) => state.reducedMotion);
  const deviceTier = useMithaqStore((state) => state.deviceTier);
  const enabled = !reducedMotion && deviceTier === 'high';

  return (
    <Html position={[0, -2.35, 0]} center className="canvas-status">
      Post FX gate: {enabled ? 'available for later' : 'disabled'}
    </Html>
  );
}
