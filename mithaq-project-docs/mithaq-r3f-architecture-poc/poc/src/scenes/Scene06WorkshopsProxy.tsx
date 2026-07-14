import { AnimatedGroup, COLORS, ProxyLabel, ProxyStage } from './ProxyPrimitives';

export function Scene06WorkshopsProxy() {
  return (
    <ProxyStage>
      <ProxyLabel title="Scene 06" subtitle="Workshop dossier proxy cards" />
      <AnimatedGroup>
        {[-1.05, 0, 1.05].map((x, index) => (
          <group key={x} position={[x, 0.08, 0]} rotation={[0, 0, (index - 1) * 0.08]}>
            <mesh>
              <boxGeometry args={[0.72, 1.02, 0.08]} />
              <meshStandardMaterial color="#241A14" roughness={0.76} />
            </mesh>
            <mesh position={[0, 0.38, 0.06]}>
              <boxGeometry args={[0.42, 0.045, 0.025]} />
              <meshStandardMaterial color={COLORS.gold} metalness={0.45} roughness={0.5} />
            </mesh>
            <mesh position={[0, -0.12, 0.06]}>
              <boxGeometry args={[0.54, 0.025, 0.025]} />
              <meshStandardMaterial color={COLORS.parchment} roughness={0.76} />
            </mesh>
          </group>
        ))}
      </AnimatedGroup>
    </ProxyStage>
  );
}
