import { useMithaqStore } from '../store/mithaqStore';

export function SharedEnvironment() {
  const reducedMotion = useMithaqStore((state) => state.reducedMotion);

  return (
    <>
      <color attach="background" args={['#08070F']} />
      <ambientLight intensity={0.22} />
      <directionalLight position={[-4, 6, 4]} intensity={1.45} color="#E8C97A" />
      <pointLight position={[3.5, 2.5, 3]} intensity={reducedMotion ? 0.25 : 0.45} color="#C4913A" />
    </>
  );
}
