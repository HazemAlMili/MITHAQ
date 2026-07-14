import { useFrame } from '@react-three/fiber';
import { useMemo, useRef } from 'react';
import { AdditiveBlending, DoubleSide, ShaderMaterial } from 'three';
import fractureVertexShader from '../shaders/fracture-lines.vert?raw';
import fractureFragmentShader from '../shaders/fracture-lines.frag?raw';
import { createFractureUniforms } from '../utils/shaderUniforms';

type Props = {
  progress: number;
  reducedMotion: boolean;
};

export function FractureLinesShaderDemo({ progress, reducedMotion }: Props) {
  const materialRef = useRef<ShaderMaterial>(null);
  const uniforms = useMemo(() => createFractureUniforms(), []);

  useFrame(({ clock }) => {
    if (!materialRef.current) return;
    materialRef.current.uniforms.uProgress.value = reducedMotion ? 0.72 : progress;
    materialRef.current.uniforms.uFractureProgress.value = reducedMotion ? 0.72 : progress;
    materialRef.current.uniforms.uOpacity.value = reducedMotion ? 0.20 : 0.72;
    materialRef.current.uniforms.uTime.value = clock.elapsedTime;
  });

  return (
    <group>
      <mesh rotation-x={-Math.PI / 2} position={[0, -0.04, 0]}>
        <planeGeometry args={[5.4, 3.4, 1, 1]} />
        <meshStandardMaterial color="#1c1510" roughness={0.88} metalness={0} />
      </mesh>
      <mesh rotation-x={-Math.PI / 2} position={[0, -0.03, 0]}>
        <planeGeometry args={[4.8, 3.2, 1, 1]} />
        <shaderMaterial
          ref={materialRef}
          vertexShader={fractureVertexShader}
          fragmentShader={fractureFragmentShader}
          uniforms={uniforms}
          transparent
          depthWrite={false}
          side={DoubleSide}
          blending={AdditiveBlending}
        />
      </mesh>
    </group>
  );
}
