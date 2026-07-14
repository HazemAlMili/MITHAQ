import { AnimatedGroup, COLORS, ProxyLabel, ProxyStage } from './ProxyPrimitives';

export function Scene04MethodProxy() {
  return (
    <ProxyStage>
      <ProxyLabel title="Scene 04" subtitle="Method order: aligned legal desk blocks" />
      <AnimatedGroup>
        {[-1.05, 0, 1.05].map((x, index) => (
          <mesh key={x} position={[x, 0.02, index * 0.08]}>
            <boxGeometry args={[0.72, 0.08, 0.92]} />
            <meshStandardMaterial color={index === 1 ? COLORS.goldDim : COLORS.parchment} roughness={0.72} />
          </mesh>
        ))}
      </AnimatedGroup>
    </ProxyStage>
  );
}
