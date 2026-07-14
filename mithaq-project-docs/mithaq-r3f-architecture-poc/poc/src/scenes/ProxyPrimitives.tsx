import { Html } from '@react-three/drei';
import { useFrame } from '@react-three/fiber';
import { ReactNode, useRef } from 'react';
import { Group } from 'three';
import { useMithaqStore } from '../store/mithaqStore';

export const COLORS = {
  void: '#08070F',
  ink: '#0E0C1A',
  chamber: '#161422',
  wood: '#1C1510',
  gold: '#C4913A',
  goldLight: '#E8C97A',
  goldDim: '#8B6420',
  parchment: '#F2E8D0'
};

export function ProxyStage({ children }: { children: ReactNode }) {
  return (
    <group>
      <mesh position={[0, -1.18, 0]} rotation={[-Math.PI / 2, 0, 0]}>
        <planeGeometry args={[7, 4]} />
        <meshStandardMaterial color={COLORS.wood} roughness={0.9} metalness={0} />
      </mesh>
      {children}
    </group>
  );
}

export function ProxyLabel({ title, subtitle }: { title: string; subtitle: string }) {
  return (
    <Html position={[0, 1.9, 0]} center className="scene-html-label">
      <strong>{title}</strong>
      <span>{subtitle}</span>
    </Html>
  );
}

export function AnimatedGroup({ children, speed = 0.08 }: { children: ReactNode; speed?: number }) {
  const ref = useRef<Group>(null);
  const reducedMotion = useMithaqStore((state) => state.reducedMotion);
  const sceneProgress = useMithaqStore((state) => state.sceneProgress);

  useFrame(({ clock }) => {
    if (!ref.current || reducedMotion) {
      return;
    }

    ref.current.rotation.y = Math.sin(clock.elapsedTime * speed) * 0.12 + sceneProgress * 0.08;
  });

  return <group ref={ref}>{children}</group>;
}

export function SealProxy({ position = [0, 0, 0], scale = 1 }: { position?: [number, number, number]; scale?: number }) {
  return (
    <group position={position} scale={scale}>
      <mesh rotation={[Math.PI / 2, 0, 0]}>
        <torusGeometry args={[0.74, 0.045, 16, 96]} />
        <meshStandardMaterial color={COLORS.gold} metalness={0.85} roughness={0.42} />
      </mesh>
      <mesh rotation={[Math.PI / 2, 0, 0]}>
        <torusGeometry args={[0.5, 0.022, 12, 72]} />
        <meshStandardMaterial color={COLORS.goldLight} metalness={0.75} roughness={0.48} />
      </mesh>
      <mesh position={[0, 0.01, 0]} rotation={[Math.PI / 2, 0, 0]}>
        <cylinderGeometry args={[0.44, 0.44, 0.035, 96]} />
        <meshStandardMaterial color="#6B4B18" metalness={0.7} roughness={0.56} />
      </mesh>
    </group>
  );
}

export function GavelProxy({ position = [-1.1, -0.35, 0.18], scale = 1 }: { position?: [number, number, number]; scale?: number }) {
  return (
    <group position={position} rotation={[0.25, 0, -0.55]} scale={scale}>
      <mesh rotation={[0, 0, Math.PI / 2]}>
        <cylinderGeometry args={[0.16, 0.16, 1.05, 32]} />
        <meshStandardMaterial color="#21140D" roughness={0.75} />
      </mesh>
      <mesh position={[0, -0.62, 0]} rotation={[0, 0, Math.PI / 2]}>
        <cylinderGeometry args={[0.055, 0.08, 1.25, 24]} />
        <meshStandardMaterial color="#1B100A" roughness={0.82} />
      </mesh>
      <mesh position={[-0.33, 0, 0]} rotation={[0, 0, Math.PI / 2]}>
        <torusGeometry args={[0.165, 0.018, 12, 32]} />
        <meshStandardMaterial color={COLORS.goldDim} metalness={0.85} roughness={0.42} />
      </mesh>
      <mesh position={[0.33, 0, 0]} rotation={[0, 0, Math.PI / 2]}>
        <torusGeometry args={[0.165, 0.018, 12, 32]} />
        <meshStandardMaterial color={COLORS.goldDim} metalness={0.85} roughness={0.42} />
      </mesh>
    </group>
  );
}

export function PaperPlane({
  position,
  rotation = [0, 0, 0],
  scale = 1
}: {
  position: [number, number, number];
  rotation?: [number, number, number];
  scale?: number;
}) {
  return (
    <group position={position} rotation={rotation} scale={scale}>
      <mesh>
        <boxGeometry args={[0.52, 0.72, 0.012]} />
        <meshStandardMaterial color={COLORS.parchment} roughness={0.84} />
      </mesh>
      <mesh position={[0, 0.15, 0.01]}>
        <boxGeometry args={[0.36, 0.018, 0.006]} />
        <meshStandardMaterial color="#3A2A1C" roughness={0.9} />
      </mesh>
      <mesh position={[0, -0.02, 0.01]}>
        <boxGeometry args={[0.42, 0.014, 0.006]} />
        <meshStandardMaterial color="#584635" roughness={0.9} />
      </mesh>
      <mesh position={[-0.09, -0.17, 0.01]}>
        <boxGeometry args={[0.24, 0.014, 0.006]} />
        <meshStandardMaterial color="#584635" roughness={0.9} />
      </mesh>
    </group>
  );
}
