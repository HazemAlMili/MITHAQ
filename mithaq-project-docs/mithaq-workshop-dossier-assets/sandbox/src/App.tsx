import { Suspense, useMemo, useState } from 'react';
import { Canvas } from '@react-three/fiber';
import { DossierSandboxScene, SandboxMode } from './components/DossierSandboxScene';
import { MetricsPanel } from './components/MetricsPanel';

const MODES: SandboxMode[] = ['resting', 'hover', 'selected', 'multiple', 'mobile-light', 'wireframe'];

function queryMode(): SandboxMode {
  const params = new URLSearchParams(window.location.search);
  const mode = params.get('mode') as SandboxMode | null;
  return mode && MODES.includes(mode) ? mode : 'resting';
}

export default function App() {
  const [mode, setMode] = useState<SandboxMode>(queryMode);
  const isMobileLight = mode === 'mobile-light';
  const dpr = useMemo<[number, number]>(() => (isMobileLight ? [1, 1] : [1, 1.5]), [isMobileLight]);

  return (
    <main className="app-shell">
      <section className="stage">
        <Canvas
          camera={{ position: [2.7, 2.15, 4.4], fov: 42 }}
          dpr={dpr}
          gl={{ antialias: !isMobileLight, alpha: false, powerPreference: 'high-performance' }}
          shadows={!isMobileLight}
        >
          <color attach="background" args={['#08070F']} />
          <Suspense fallback={null}>
            <DossierSandboxScene mode={mode} />
          </Suspense>
        </Canvas>
      </section>

      <aside className="control-panel">
        <p className="eyebrow">P5.09 Isolated Sandbox</p>
        <h1>Mithaq Workshop Dossier</h1>
        <p className="copy">
          Atmospheric 3D dossier validation only. Workshop content remains semantic HTML in production.
        </p>
        <div className="mode-grid" aria-label="Sandbox modes">
          {MODES.map((item) => (
            <button
              key={item}
              className={item === mode ? 'active' : ''}
              onClick={() => setMode(item)}
              type="button"
            >
              {item}
            </button>
          ))}
        </div>
        <MetricsPanel mode={mode} />
      </aside>
    </main>
  );
}

