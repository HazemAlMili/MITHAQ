import { AnimatedGroup, GavelProxy, ProxyLabel, ProxyStage, SealProxy } from './ProxyPrimitives';
import { useMithaqStore } from '../store/mithaqStore';

export function Scene01GavelSealProxy() {
  const sceneProgress = useMithaqStore((state) => state.sceneProgress);
  const strikeY = Math.max(-0.22, 0.9 - sceneProgress * 3.2);
  const sealScale = Math.max(0.08, Math.min(1, (sceneProgress - 0.52) * 2.4));

  return (
    <ProxyStage>
      <ProxyLabel title="Scene 01" subtitle="Gavel trigger -> Seal reveal proxy" />
      <AnimatedGroup>
        <GavelProxy position={[-1.05, strikeY, 0.15]} scale={1.05} />
        <SealProxy position={[0.52, -0.34, 0.02]} scale={sealScale} />
      </AnimatedGroup>
    </ProxyStage>
  );
}
