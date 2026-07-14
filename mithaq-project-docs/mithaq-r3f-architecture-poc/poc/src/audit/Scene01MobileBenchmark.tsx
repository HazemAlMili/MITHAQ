import { Html, useGLTF } from '@react-three/drei';
import { useFrame } from '@react-three/fiber';
import { useMemo, useRef } from 'react';
import { AdditiveBlending, BufferAttribute, BufferGeometry, Group, Points, ShaderMaterial } from 'three';
import { useMithaqStore } from '../store/mithaqStore';

const gold = '#C4913A';

declare global {
  interface Window {
    __MITHAQ_AUDIT_PROGRESS_VALUE__?: number;
  }
}

function getBenchmarkProgress(elapsedTime: number, reducedMotion: boolean): number {
  if (reducedMotion) {
    return 1;
  }

  if (typeof window.__MITHAQ_AUDIT_PROGRESS_VALUE__ === 'number') {
    return Math.min(1, Math.max(0, window.__MITHAQ_AUDIT_PROGRESS_VALUE__));
  }

  return (elapsedTime % 4.3) / 4.3;
}

function RipplePlane() {
  const material = useMemo(
    () =>
      new ShaderMaterial({
        transparent: true,
        depthWrite: false,
        blending: AdditiveBlending,
        uniforms: {
          uProgress: { value: 0 },
          uGold: { value: [0.77, 0.57, 0.23] },
          uOpacity: { value: 0.48 }
        },
        vertexShader: `
          varying vec2 vUv;
          void main() {
            vUv = uv;
            gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
          }
        `,
        fragmentShader: `
          varying vec2 vUv;
          uniform float uProgress;
          uniform vec3 uGold;
          uniform float uOpacity;
          void main() {
            vec2 p = vUv - vec2(0.5);
            float d = length(p);
            float ring = smoothstep(0.024, 0.0, abs(d - uProgress * 0.62));
            float echo = smoothstep(0.018, 0.0, abs(d - max(0.0, uProgress - 0.22) * 0.5)) * 0.32;
            float fade = 1.0 - smoothstep(0.78, 1.0, uProgress);
            gl_FragColor = vec4(uGold, (ring + echo) * fade * uOpacity);
          }
        `
      }),
    []
  );

  const reducedMotion = useMithaqStore((state) => state.reducedMotion);

  useFrame(({ clock }) => {
    const progress = getBenchmarkProgress(clock.elapsedTime, reducedMotion);
    material.uniforms.uProgress.value = reducedMotion ? 0.82 : Math.max(0, Math.min(1, (progress - 0.32) * 2.1));
  });

  return (
    <mesh rotation={[-Math.PI / 2, 0, 0]} position={[0, -0.97, 0]}>
      <planeGeometry args={[4.2, 4.2, 1, 1]} />
      <primitive attach="material" object={material} />
    </mesh>
  );
}

function AuditParticles() {
  const deviceTier = useMithaqStore((state) => state.deviceTier);
  const reducedMotion = useMithaqStore((state) => state.reducedMotion);
  const points = useRef<Points>(null);
  const count = deviceTier === 'low' ? 32 : 80;
  const geometry = useMemo(() => {
    const positions = new Float32Array(count * 3);
    for (let index = 0; index < count; index += 1) {
      positions[index * 3] = (Math.random() - 0.5) * 5.2;
      positions[index * 3 + 1] = Math.random() * 2.8 - 0.3;
      positions[index * 3 + 2] = (Math.random() - 0.5) * 3.6;
    }
    const buffer = new BufferGeometry();
    buffer.setAttribute('position', new BufferAttribute(positions, 3));
    return buffer;
  }, [count]);

  useFrame(({ clock }) => {
    if (!points.current || reducedMotion) {
      return;
    }
    points.current.rotation.y = Math.sin(clock.elapsedTime * 0.08) * 0.08;
  });

  return (
    <points ref={points} geometry={geometry}>
      <pointsMaterial color={gold} size={deviceTier === 'low' ? 0.018 : 0.024} transparent opacity={0.25} depthWrite={false} />
    </points>
  );
}

export function Scene01MobileBenchmark() {
  const gavel = useGLTF('/audit-assets/gavel.opt.glb', '/draco/gltf/');
  const seal = useGLTF('/audit-assets/seal.opt.glb', '/draco/gltf/');
  const desk = useGLTF('/audit-assets/desk.opt.glb', '/draco/gltf/');
  const group = useRef<Group>(null);
  const gavelGroup = useRef<Group>(null);
  const sealGroup = useRef<Group>(null);
  const reducedMotion = useMithaqStore((state) => state.reducedMotion);
  const deviceTier = useMithaqStore((state) => state.deviceTier);

  useFrame(({ clock }) => {
    if (!group.current) {
      return;
    }

    const progress = getBenchmarkProgress(clock.elapsedTime, reducedMotion);
    const strikeProgress = Math.min(1, progress * 2.8);
    const sealProgress = Math.max(0, Math.min(1, (progress - 0.44) * 2.4));

    group.current.position.z = reducedMotion ? -0.18 : -progress * 0.24;
    group.current.rotation.x = reducedMotion ? -0.08 : -0.1 + progress * 0.05;

    if (gavelGroup.current) {
      gavelGroup.current.position.y = -0.56 + (1 - strikeProgress) * 1.15;
    }

    if (sealGroup.current) {
      const scale = 0.28 + sealProgress * 0.78;
      sealGroup.current.scale.setScalar(scale);
    }
  });

  return (
    <group ref={group} scale={deviceTier === 'low' ? 0.86 : 0.94}>
      <Html position={[0, 1.88, 0]} center className="scene-html-label">
        <strong>P5.08 Scene 01 Audit</strong>
        <span>Real gavel + seal + desk workload</span>
      </Html>
      <primitive object={desk.scene} position={[0, -1.06, 0]} scale={1.08} />
      <group ref={gavelGroup} position={[-0.72, 0.59, 0.08]} rotation={[0.12, 0.18, -0.62]} scale={0.62}>
        <primitive object={gavel.scene} />
      </group>
      <group ref={sealGroup} position={[0.54, -0.58, 0.02]} rotation={[Math.PI / 2, 0, 0]} scale={0.28}>
        <primitive object={seal.scene} />
      </group>
      <RipplePlane />
      <AuditParticles />
    </group>
  );
}
