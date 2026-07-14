import { Canvas } from '@react-three/fiber';
import { ChangeEvent, useMemo, useState } from 'react';
import { RippleShaderDemo } from './RippleShaderDemo';
import { FractureLinesShaderDemo } from './FractureLinesShaderDemo';
import { SealEmergenceShaderDemo } from './SealEmergenceShaderDemo';
import { AtmosphericParticlesDemo } from './AtmosphericParticlesDemo';
import { DeviceQuality, getDeviceQualityFromQuery } from '../utils/deviceQuality';
import { MITHAQ_COLORS } from '../utils/shaderUniforms';

type Mode = 'ripple' | 'fracture' | 'seal' | 'particles' | 'combined';

const modes: Array<{ id: Mode; label: string }> = [
  { id: 'ripple', label: 'Ripple' },
  { id: 'fracture', label: 'Fracture Lines' },
  { id: 'seal', label: 'Seal Emergence' },
  { id: 'particles', label: 'Atmospheric Particles' },
  { id: 'combined', label: 'Combined Opening FX' },
];

function getInitialMode(): Mode {
  const value = new URLSearchParams(window.location.search).get('mode');
  if (value === 'fracture' || value === 'seal' || value === 'particles' || value === 'combined') return value;
  return 'ripple';
}

function getInitialProgress() {
  const raw = Number(new URLSearchParams(window.location.search).get('progress'));
  return Number.isFinite(raw) ? Math.min(1, Math.max(0, raw)) : 0.64;
}

function SceneContent({ mode, progress, reducedMotion, quality }: {
  mode: Mode;
  progress: number;
  reducedMotion: boolean;
  quality: DeviceQuality;
}) {
  const showRipple = mode === 'ripple' || mode === 'combined';
  const showFracture = mode === 'fracture' || mode === 'combined';
  const showSeal = mode === 'seal' || mode === 'combined';
  const showParticles = mode === 'particles' || mode === 'combined';

  return (
    <>
      <color attach="background" args={[MITHAQ_COLORS.void]} />
      <fog attach="fog" args={[MITHAQ_COLORS.void, 4.2, 8.5]} />
      <ambientLight intensity={0.18} />
      <directionalLight position={[-3.2, 4.0, 3.1]} intensity={1.8} color="#f0c67a" />
      <pointLight position={[2.8, 1.8, 2.4]} intensity={0.55} color={MITHAQ_COLORS.sealGold} />

      <group position={[0, -0.25, 0]}>
        {showRipple && <RippleShaderDemo progress={progress} reducedMotion={reducedMotion} />}
        {showFracture && <FractureLinesShaderDemo progress={progress} reducedMotion={reducedMotion} />}
      </group>

      {showSeal && (
        <group position={[mode === 'combined' ? 0.15 : 0, mode === 'combined' ? 0.58 : 0.05, 0]} scale={mode === 'combined' ? 0.82 : 1.1}>
          <SealEmergenceShaderDemo progress={progress} reducedMotion={reducedMotion} />
        </group>
      )}

      {showParticles && <AtmosphericParticlesDemo quality={quality} reducedMotion={reducedMotion} />}
    </>
  );
}

export function ShaderSandboxScene() {
  const [mode, setMode] = useState<Mode>(getInitialMode);
  const [progress, setProgress] = useState(getInitialProgress);
  const [quality, setQuality] = useState<DeviceQuality>(getDeviceQualityFromQuery);
  const [reducedMotion, setReducedMotion] = useState(new URLSearchParams(window.location.search).get('reduced') === '1');

  const activeLabel = useMemo(() => modes.find((item) => item.id === mode)?.label ?? 'Ripple', [mode]);

  function updateProgress(event: ChangeEvent<HTMLInputElement>) {
    setProgress(Number(event.target.value));
  }

  function updateQuality(event: ChangeEvent<HTMLSelectElement>) {
    setQuality(event.target.value === 'low' ? 'low' : 'desktop');
  }

  return (
    <main className="sandbox">
      <div className="canvas" data-testid="shader-canvas-wrap">
        <Canvas camera={{ position: [2.4, 2.0, 4.2], fov: 45 }} gl={{ antialias: true, alpha: false }}>
          <SceneContent mode={mode} progress={progress} reducedMotion={reducedMotion} quality={quality} />
        </Canvas>
      </div>

      <section className="panel" aria-label="Shader sandbox controls">
        <p className="eyebrow">P5.06 Shader Sandbox</p>
        <h1 className="title">{activeLabel}</h1>

        <div className="tabs" role="tablist" aria-label="Shader modes">
          {modes.map((item) => (
            <button
              className="tab"
              data-active={item.id === mode}
              key={item.id}
              onClick={() => setMode(item.id)}
              role="tab"
              aria-selected={item.id === mode}
              type="button"
            >
              {item.label}
            </button>
          ))}
        </div>

        <div className="controls">
          <label className="control-row">
            <span>Progress</span>
            <input min="0" max="1" step="0.01" value={progress} onChange={updateProgress} type="range" />
            <span>{progress.toFixed(2)}</span>
          </label>

          <label className="control-row">
            <span>Quality</span>
            <select value={quality} onChange={updateQuality}>
              <option value="desktop">Desktop, 220 particles</option>
              <option value="low">Low/mobile, 80 particles</option>
            </select>
            <span />
          </label>

          <label className="checkbox-row">
            <input
              checked={reducedMotion}
              onChange={(event) => setReducedMotion(event.target.checked)}
              type="checkbox"
            />
            Reduced motion preview
          </label>
        </div>

        <p className="note">
          Isolated shader work only. No ScrollTrigger, Lenis, routing, production timeline, or full opening integration.
          Effects are intentionally muted gold, slow, and non-explosive.
        </p>
      </section>

      <div className="status">Mode: {mode} / Reduced: {reducedMotion ? 'on' : 'off'}</div>
    </main>
  );
}
