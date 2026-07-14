import { useFrame } from '@react-three/fiber';
import { useMemo, useRef } from 'react';
import { AdditiveBlending, DoubleSide, ShaderMaterial } from 'three';
import rippleVertexShader from '../shaders/ripple.vert?raw';
import rippleFragmentShader from '../shaders/ripple.frag?raw';
import { createRippleUniforms, MITHAQ_COLORS } from '../utils/shaderUniforms';

type Props = {
  progress: number;
  reducedMotion: boolean;
};

export function RippleShaderDemo({ progress, reducedMotion }: Props) {
  const materialRef = useRef<ShaderMaterial>(null);
  const uniforms = useMemo(() => createRippleUniforms(), []);

  useFrame(({ clock }) => {
    if (!materialRef.current) return;
    materialRef.current.uniforms.uProgress.value = reducedMotion ? 0.82 : progress;
    materialRef.current.uniforms.uOpacity.value = reducedMotion ? 0.22 : 0.74;
    materialRef.current.uniforms.uTime.value = clock.elapsedTime;
  });

  return (
    <group>
      <mesh rotation-x={-Math.PI / 2} position={[0, -0.04, 0]}>
        <planeGeometry args={[5.4, 3.4, 1, 1]} />
        <meshStandardMaterial color={MITHAQ_COLORS.wood} roughness={0.86} metalness={0} />
      </mesh>
      <mesh rotation-x={-Math.PI / 2} position={[0, -0.035, 0]}>
        <planeGeometry args={[5.4, 3.4, 1, 1]} />
        <shaderMaterial
          ref={materialRef}
          vertexShader={rippleVertexShader}
          fragmentShader={rippleFragmentShader}
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
