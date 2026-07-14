import { AnimatedGroup, COLORS, ProxyLabel, ProxyStage } from './ProxyPrimitives';

export function Scene08TrustProxy() {
  return (
    <ProxyStage>
      <ProxyLabel title="Scene 08" subtitle="Trust and credibility proof block proxies" />
      <AnimatedGroup>
        {[-0.95, 0, 0.95].map((x, index) => (
          <mesh key={x} position={[x, 0.05, 0]} scale={[1, 0.65 + index * 0.18, 1]}>
            <boxGeometry args={[0.58, 0.72, 0.08]} />
            <meshStandardMaterial color={index === 1 ? COLORS.goldDim : '#17131F'} roughness={0.62} />
          </mesh>
        ))}
      </AnimatedGroup>
    </ProxyStage>
  );
}
