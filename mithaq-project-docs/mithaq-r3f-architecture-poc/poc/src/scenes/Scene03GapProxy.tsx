import { AnimatedGroup, PaperPlane, ProxyLabel, ProxyStage } from './ProxyPrimitives';

export function Scene03GapProxy() {
  const papers: Array<[[number, number, number], [number, number, number], number]> = [
    [[-1.35, 0.18, 0.2], [0.2, 0.1, -0.32], 0.92],
    [[-0.55, 0.72, -0.1], [-0.22, 0.1, 0.18], 0.82],
    [[0.42, 0.38, 0.25], [0.16, -0.2, 0.28], 0.88],
    [[1.22, -0.1, -0.08], [-0.12, 0.32, -0.22], 0.78],
    [[-0.05, -0.42, 0.15], [0.22, -0.08, 0.08], 0.72]
  ];

  return (
    <ProxyStage>
      <ProxyLabel title="Scene 03" subtitle="The Gap: drifting document proxies" />
      <AnimatedGroup speed={0.18}>
        {papers.map(([position, rotation, scale], index) => (
          <PaperPlane key={index} position={position} rotation={rotation} scale={scale} />
        ))}
      </AnimatedGroup>
    </ProxyStage>
  );
}
