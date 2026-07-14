import { AnimatedGroup, COLORS, ProxyLabel, ProxyStage } from './ProxyPrimitives';

export function Scene05PillarsProxy() {
  return (
    <ProxyStage>
      <ProxyLabel title="Scene 05" subtitle="Five training pillar proxy cards" />
      <AnimatedGroup>
        {[-1.6, -0.8, 0, 0.8, 1.6].map((x, index) => (
          <mesh key={x} position={[x, -0.02 + index * 0.06, 0]} rotation={[0.02, 0, 0]}>
            <boxGeometry args={[0.46, 1.12, 0.06]} />
            <meshStandardMaterial color={index === 2 ? COLORS.gold : '#1E1824'} metalness={0.25} roughness={0.58} />
          </mesh>
        ))}
      </AnimatedGroup>
    </ProxyStage>
  );
}
