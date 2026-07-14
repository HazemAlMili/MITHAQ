import { AnimatedGroup, COLORS, ProxyLabel, ProxyStage } from './ProxyPrimitives';

export function Scene09FAQProxy() {
  return (
    <ProxyStage>
      <ProxyLabel title="Scene 09" subtitle="FAQ line stack proxy" />
      <AnimatedGroup>
        {[-0.72, -0.32, 0.08, 0.48].map((y, index) => (
          <group key={y} position={[0, y, 0]}>
            <mesh>
              <boxGeometry args={[2.1, 0.045, 0.045]} />
              <meshStandardMaterial color={COLORS.parchment} roughness={0.72} />
            </mesh>
            <mesh position={[-0.92, -0.14, 0]}>
              <boxGeometry args={[0.55 + index * 0.1, 0.025, 0.035]} />
              <meshStandardMaterial color={COLORS.goldDim} roughness={0.6} />
            </mesh>
          </group>
        ))}
      </AnimatedGroup>
    </ProxyStage>
  );
}
