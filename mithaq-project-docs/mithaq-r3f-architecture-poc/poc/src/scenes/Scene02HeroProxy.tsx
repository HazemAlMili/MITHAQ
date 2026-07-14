import { AnimatedGroup, ProxyLabel, ProxyStage, SealProxy } from './ProxyPrimitives';

export function Scene02HeroProxy() {
  return (
    <ProxyStage>
      <ProxyLabel title="Scene 02" subtitle="Hero seal anchor proxy" />
      <AnimatedGroup>
        <SealProxy position={[0, 0.02, 0]} scale={1.45} />
        <mesh position={[0, -0.18, 0.08]}>
          <boxGeometry args={[1.8, 0.08, 0.08]} />
          <meshStandardMaterial color="#F2E8D0" roughness={0.7} />
        </mesh>
      </AnimatedGroup>
    </ProxyStage>
  );
}
