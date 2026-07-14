import { AnimatedGroup, GavelProxy, ProxyLabel, ProxyStage, SealProxy } from './ProxyPrimitives';

export function Scene10FinalCTAProxy() {
  return (
    <ProxyStage>
      <ProxyLabel title="Scene 10" subtitle="Final covenant CTA proxy callback" />
      <AnimatedGroup>
        <SealProxy position={[0, 0.08, 0]} scale={1.22} />
        <GavelProxy position={[-1.55, -0.62, 0.12]} scale={0.72} />
        <mesh position={[0.95, -0.55, 0.1]}>
          <boxGeometry args={[0.96, 0.26, 0.08]} />
          <meshStandardMaterial color="#C4913A" metalness={0.45} roughness={0.48} />
        </mesh>
      </AnimatedGroup>
    </ProxyStage>
  );
}
