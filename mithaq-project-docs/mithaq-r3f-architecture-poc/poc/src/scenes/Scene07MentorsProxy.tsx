import { AnimatedGroup, COLORS, ProxyLabel, ProxyStage } from './ProxyPrimitives';

export function Scene07MentorsProxy() {
  return (
    <ProxyStage>
      <ProxyLabel title="Scene 07" subtitle="Hall of mentors proxy slabs" />
      <AnimatedGroup>
        {[-1.25, 0, 1.25].map((x) => (
          <group key={x} position={[x, 0.12, 0]}>
            <mesh>
              <boxGeometry args={[0.7, 1.1, 0.08]} />
              <meshStandardMaterial color="#15111D" roughness={0.64} />
            </mesh>
            <mesh position={[0, 0.22, 0.07]}>
              <cylinderGeometry args={[0.18, 0.18, 0.04, 32]} />
              <meshStandardMaterial color={COLORS.goldDim} metalness={0.38} roughness={0.54} />
            </mesh>
            <mesh position={[0, -0.34, 0.07]}>
              <boxGeometry args={[0.46, 0.04, 0.03]} />
              <meshStandardMaterial color={COLORS.parchment} roughness={0.76} />
            </mesh>
          </group>
        ))}
      </AnimatedGroup>
    </ProxyStage>
  );
}
