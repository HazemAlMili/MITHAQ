import { useFrame } from '@react-three/fiber';
import { useMemo, useRef } from 'react';
import { AdditiveBlending, DoubleSide, ShaderMaterial } from 'three';
import sealVertexShader from '../shaders/seal-emergence.vert?raw';
import sealFragmentShader from '../shaders/seal-emergence.frag?raw';
import { createSealEmergenceUniforms, MITHAQ_COLORS } from '../utils/shaderUniforms';

type Props = {
  progress: number;
  reducedMotion: boolean;
};

export function SealEmergenceShaderDemo({ progress, reducedMotion }: Props) {
  const materialRef = useRef<ShaderMaterial>(null);
  const uniforms = useMemo(() => createSealEmergenceUniforms(), []);

  useFrame(({ clock }) => {
    if (!materialRef.current) return;
    materialRef.current.uniforms.uProgress.value = reducedMotion ? 1.0 : progress;
    materialRef.current.uniforms.uEmissiveStrength.value = reducedMotion ? 0.12 : 0.38;
    materialRef.current.uniforms.uTime.value = clock.elapsedTime;
  });

  return (
    <group rotation-x={-0.2}>
      <mesh rotation-x={Math.PI / 2} position={[0, -0.02, 0]}>
        <cylinderGeometry args={[1.22, 1.22, 0.09, 96]} />
        <meshStandardMaterial color={MITHAQ_COLORS.goldDim} roughness={0.55} metalness={0.86} />
      </mesh>
      <mesh rotation-x={Math.PI / 2} position={[0, 0.045, 0]}>
        <torusGeometry args={[0.92, 0.055, 10, 128]} />
        <shaderMaterial
          ref={materialRef}
          vertexShader={sealVertexShader}
          fragmentShader={sealFragmentShader}
          uniforms={uniforms}
          transparent
          depthWrite={false}
          side={DoubleSide}
          blending={AdditiveBlending}
        />
      </mesh>
      <mesh rotation-x={Math.PI / 2} position={[0, 0.06, 0]}>
        <torusGeometry args={[0.52, 0.022, 8, 96]} />
        <meshStandardMaterial
          color={MITHAQ_COLORS.goldLight}
          emissive={MITHAQ_COLORS.sealGold}
          emissiveIntensity={reducedMotion ? 0.04 : progress * 0.18}
          roughness={0.42}
          metalness={0.9}
        />
      </mesh>
    </group>
  );
}
