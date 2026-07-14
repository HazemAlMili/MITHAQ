import { Clone, Html, OrbitControls, useGLTF } from '@react-three/drei';
import { ThreeEvent, useFrame, useThree } from '@react-three/fiber';
import { useEffect, useMemo, useRef, useState } from 'react';
import * as THREE from 'three';

export type SandboxMode = 'resting' | 'hover' | 'selected' | 'multiple' | 'mobile-light' | 'wireframe';

declare global {
  interface Window {
    __MITHAQ_DOSSIER_METRICS__?: {
      mode: SandboxMode;
      averageFps: number;
      samples: number;
      rendererInfo: {
        calls: number;
        triangles: number;
        geometries: number;
        textures: number;
        programs: number | string;
      };
      consoleErrors: number;
    };
  }
}

const DESKTOP = '/models/workshop-dossier.desktop.opt.glb';
const MOBILE = '/models/workshop-dossier.mobile.opt.glb';
const DRACO = '/draco/gltf/';

function DeskReference({ mobile }: { mobile: boolean }) {
  return (
    <mesh receiveShadow position={[0, -0.09, 0]} rotation={[-Math.PI / 2, 0, 0]}>
      <boxGeometry args={[6.4, 4.2, 0.06]} />
      <meshStandardMaterial color="#1C1510" roughness={0.88} metalness={0} />
      {!mobile && (
        <Html position={[0, 0.08, -1.95]} center className="scene-label">
          Scene 06 dossier validation only
        </Html>
      )}
    </mesh>
  );
}

function DossierInstance({
  scene,
  position,
  rotation,
  scale = 1,
  hover,
  selected,
  wireframe,
  interactive,
}: {
  scene: THREE.Object3D;
  position: [number, number, number];
  rotation: [number, number, number];
  scale?: number;
  hover?: boolean;
  selected?: boolean;
  wireframe?: boolean;
  interactive?: boolean;
}) {
  const group = useRef<THREE.Group>(null);
  const [pointerHover, setPointerHover] = useState(false);
  const activeHover = hover || pointerHover;
  const targetLift = activeHover ? 0.05 : 0;
  const targetTilt = activeHover ? -0.045 : 0;

  useFrame((_, delta) => {
    if (!group.current) return;
    group.current.position.y = THREE.MathUtils.damp(group.current.position.y, position[1] + targetLift, 12, delta);
    group.current.rotation.x = THREE.MathUtils.damp(group.current.rotation.x, rotation[0] + targetTilt, 12, delta);
  });

  useEffect(() => {
    scene.traverse((child) => {
      const mesh = child as THREE.Mesh;
      if (!mesh.isMesh) return;
      mesh.castShadow = true;
      mesh.receiveShadow = true;
      if (wireframe && mesh.material) {
        const base = Array.isArray(mesh.material) ? mesh.material[0] : mesh.material;
        mesh.material = new THREE.MeshBasicMaterial({
          color: '#E8C97A',
          wireframe: true,
          transparent: true,
          opacity: 0.78,
          name: `wire_${base.name}`,
        });
      }
      if (selected && mesh.material && !wireframe) {
        const materials = Array.isArray(mesh.material) ? mesh.material : [mesh.material];
        materials.forEach((material) => {
          if ('emissive' in material && material.name.includes('Brass')) {
            (material as THREE.MeshStandardMaterial).emissive = new THREE.Color('#8B6420');
            (material as THREE.MeshStandardMaterial).emissiveIntensity = 0.15;
          }
        });
      }
    });
  }, [scene, selected, wireframe]);

  const onOver = (event: ThreeEvent<PointerEvent>) => {
    if (!interactive) return;
    event.stopPropagation();
    setPointerHover(true);
  };

  const onOut = (event: ThreeEvent<PointerEvent>) => {
    if (!interactive) return;
    event.stopPropagation();
    setPointerHover(false);
  };

  return (
    <group
      ref={group}
      position={position}
      rotation={rotation}
      scale={scale}
      onPointerOver={onOver}
      onPointerOut={onOut}
    >
      <Clone object={scene} />
    </group>
  );
}

function MetricsRecorder({ mode }: { mode: SandboxMode }) {
  const gl = useThree((state) => state.gl);
  const frames = useRef<number[]>([]);
  const last = useRef<number | null>(null);

  useFrame(({ clock }) => {
    const now = clock.elapsedTime;
    if (last.current !== null) {
      const delta = now - last.current;
      if (delta > 0) {
        frames.current.push(1 / delta);
        if (frames.current.length > 180) frames.current.shift();
      }
    }
    last.current = now;
    const averageFps =
      frames.current.length === 0 ? 0 : frames.current.reduce((sum, value) => sum + value, 0) / frames.current.length;
    const info = gl.info;
    window.__MITHAQ_DOSSIER_METRICS__ = {
      mode,
      averageFps,
      samples: frames.current.length,
      rendererInfo: {
        calls: info.render.calls,
        triangles: info.render.triangles,
        geometries: info.memory.geometries,
        textures: info.memory.textures,
        programs: info.programs?.length ?? 'unknown',
      },
      consoleErrors: 0,
    };
  });

  return null;
}

export function DossierSandboxScene({ mode }: { mode: SandboxMode }) {
  const desktop = useGLTF(DESKTOP, DRACO);
  const mobile = useGLTF(MOBILE, DRACO);
  const mobileMode = mode === 'mobile-light';
  const selected = mode === 'selected';
  const hover = mode === 'hover';
  const wireframe = mode === 'wireframe';

  const positions = useMemo<[number, number, number][]>(() => {
    if (mode !== 'multiple') return [[0, 0.03, 0]];
    return [
      [-1.45, 0.03, -0.12],
      [0, 0.045, 0],
      [1.42, 0.03, 0.14],
    ];
  }, [mode]);

  return (
    <>
      <ambientLight intensity={0.25} />
      <directionalLight position={[-3.2, 4.2, 3.8]} intensity={2.3} color="#E8C97A" castShadow={!mobileMode} />
      <pointLight position={[3.2, 1.2, 2.1]} intensity={0.45} color="#C4913A" />
      <DeskReference mobile={mobileMode} />
      {positions.map((position, index) => (
        <DossierInstance
          key={`${mode}-${index}`}
          scene={mobileMode ? mobile.scene : desktop.scene}
          position={position}
          rotation={[-Math.PI / 2, 0, index === 0 ? -0.14 : index === 2 ? 0.12 : 0]}
          scale={mobileMode ? 0.92 : 1}
          hover={hover && index === 0}
          selected={selected}
          wireframe={wireframe}
          interactive={!mobileMode && mode === 'resting'}
        />
      ))}
      {selected && (
        <mesh position={[0, 0.085, 0]} rotation={[-Math.PI / 2, 0, 0]}>
          <ringGeometry args={[0.86, 0.9, 96]} />
          <meshBasicMaterial color="#C4913A" transparent opacity={0.42} />
        </mesh>
      )}
      <OrbitControls enablePan={false} enableZoom={!mobileMode} maxPolarAngle={Math.PI / 2.35} minDistance={3.2} maxDistance={6} />
      <MetricsRecorder mode={mode} />
    </>
  );
}
