import { useFrame } from '@react-three/fiber';
import { useMemo, useRef } from 'react';
import { AdditiveBlending, BufferAttribute, BufferGeometry, ShaderMaterial } from 'three';
import particleVertexShader from '../shaders/atmospheric-particles.vert?raw';
import particleFragmentShader from '../shaders/atmospheric-particles.frag?raw';
import { createParticleUniforms } from '../utils/shaderUniforms';
import { DeviceQuality, getParticleCount } from '../utils/deviceQuality';

type Props = {
  reducedMotion: boolean;
  quality: DeviceQuality;
};

function seededRandom(seed: number) {
  return Math.sin(seed * 12.9898) * 43758.5453 % 1;
}

export function AtmosphericParticlesDemo({ reducedMotion, quality }: Props) {
  const materialRef = useRef<ShaderMaterial>(null);
  const uniforms = useMemo(() => createParticleUniforms(), []);
  const count = getParticleCount(quality, reducedMotion);

  const geometry = useMemo(() => {
    const positions = new Float32Array(count * 3);
    const seeds = new Float32Array(count);
    for (let i = 0; i < count; i += 1) {
      const a = seededRandom(i + 1.1);
      const b = seededRandom(i + 9.7);
      const c = seededRandom(i + 17.3);
      positions[i * 3] = (a - 0.5) * 5.8;
      positions[i * 3 + 1] = (b - 0.5) * 2.2 + 0.45;
      positions[i * 3 + 2] = (c - 0.5) * 3.2;
      seeds[i] = Math.abs(seededRandom(i + 31.2));
    }
    const bufferGeometry = new BufferGeometry();
    bufferGeometry.setAttribute('position', new BufferAttribute(positions, 3));
    bufferGeometry.setAttribute('aSeed', new BufferAttribute(seeds, 1));
    return bufferGeometry;
  }, [count]);

  useFrame(({ clock }) => {
    if (!materialRef.current) return;
    materialRef.current.uniforms.uTime.value = reducedMotion ? 0 : clock.elapsedTime;
    materialRef.current.uniforms.uOpacity.value = reducedMotion ? 0.10 : 0.42;
    materialRef.current.uniforms.uDriftStrength.value = reducedMotion ? 0.0 : quality === 'low' ? 0.07 : 0.12;
    materialRef.current.uniforms.uPointSize.value = quality === 'low' ? 4.5 : 5.5;
  });

  return (
    <points geometry={geometry}>
      <shaderMaterial
        ref={materialRef}
        vertexShader={particleVertexShader}
        fragmentShader={particleFragmentShader}
        uniforms={uniforms}
        transparent
        depthWrite={false}
        blending={AdditiveBlending}
      />
    </points>
  );
}
