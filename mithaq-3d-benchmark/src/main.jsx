import React, { Suspense, useEffect, useMemo, useRef, useState } from 'react';
import { createRoot } from 'react-dom/client';
import { Canvas, useFrame, useLoader, useThree } from '@react-three/fiber';
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js';
import './styles.css';

const params = new URLSearchParams(window.location.search);
const scenario = params.get('scenario') === 'B' ? 'B' : 'A';
const forceFallback = params.get('fallback') === '1';
const forceReduced = params.get('reduced') === '1';
const forceBadModel = params.get('badmodel') === '1';
const reducedMotion =
  forceReduced || window.matchMedia?.('(prefers-reduced-motion: reduce)')?.matches;

const modelPath =
  forceBadModel
    ? '/models/missing-placeholder.glb'
    : scenario === 'B'
    ? '/models/mithaq-placeholder-upper.glb'
    : '/models/mithaq-placeholder-light.glb';

window.__mithaqBenchmark = {
  scenario,
  modelPath,
  startedAt: performance.now(),
  domVisibleAt: performance.now(),
  canvasMountedAt: null,
  modelLoadedAt: null,
  firstInteractiveFeelAt: null,
  fpsSamples: [],
  lowFps: null,
  avgFps: null,
  scrollProgress: 0,
  webglAvailable: null,
  reducedMotion,
  fallback: false
};

function hasWebGL() {
  try {
    const canvas = document.createElement('canvas');
    return Boolean(
      window.WebGL2RenderingContext && canvas.getContext('webgl2')
    ) || Boolean(canvas.getContext('webgl') || canvas.getContext('experimental-webgl'));
  } catch {
    return false;
  }
}

function useScrollProgress() {
  const [progress, setProgress] = useState(0);

  useEffect(() => {
    const update = () => {
      const max = document.documentElement.scrollHeight - window.innerHeight;
      const value = max > 0 ? Math.min(1, Math.max(0, window.scrollY / max)) : 0;
      window.__mithaqBenchmark.scrollProgress = value;
      setProgress(value);
    };
    update();
    window.addEventListener('scroll', update, { passive: true });
    window.addEventListener('resize', update);
    return () => {
      window.removeEventListener('scroll', update);
      window.removeEventListener('resize', update);
    };
  }, []);

  return progress;
}

function FpsProbe() {
  const last = useRef(performance.now());
  const samples = useRef([]);

  useFrame(() => {
    const now = performance.now();
    const delta = now - last.current;
    last.current = now;
    if (delta > 0) {
      const fps = 1000 / delta;
      samples.current.push(fps);
      if (samples.current.length > 240) samples.current.shift();
      const avg = samples.current.reduce((sum, value) => sum + value, 0) / samples.current.length;
      const low = Math.min(...samples.current);
      window.__mithaqBenchmark.fpsSamples = samples.current.slice();
      window.__mithaqBenchmark.avgFps = Number(avg.toFixed(1));
      window.__mithaqBenchmark.lowFps = Number(low.toFixed(1));
    }
  });

  return null;
}

function CameraRig({ progress }) {
  const { camera } = useThree();

  useFrame(() => {
    camera.position.set(0, 1.45 + progress * 0.35, 5.2 - progress * 1.8);
    camera.lookAt(0, 0.2 + progress * 0.2, 0);
  });

  return null;
}

function PlaceholderHero({ progress }) {
  const gltf = useLoader(GLTFLoader, modelPath);
  const group = useRef();

  useEffect(() => {
    window.__mithaqBenchmark.modelLoadedAt = performance.now();
    window.__mithaqBenchmark.firstInteractiveFeelAt = performance.now();
  }, []);

  useFrame(() => {
    if (!group.current) return;
    group.current.rotation.y = -0.32 + progress * 0.72;
    group.current.position.y = -0.15 + progress * 0.12;
    const seal = group.current.getObjectByName('placeholder_seal');
    if (seal) {
      seal.rotation.z = progress * Math.PI * 0.9;
      seal.position.z = -0.65 + progress * 0.95;
    }
  });

  return (
    <group ref={group} scale={scenario === 'B' ? 0.85 : 1}>
      <primitive object={gltf.scene} />
    </group>
  );
}

function Scene({ progress }) {
  useEffect(() => {
    window.__mithaqBenchmark.canvasMountedAt = performance.now();
  }, []);

  return (
    <>
      <color attach="background" args={['#100f0d']} />
      <ambientLight intensity={0.55} />
      <directionalLight position={[2.5, 4, 2]} intensity={2.1} color="#ffd99a" />
      <directionalLight position={[-3, 2, -2]} intensity={0.8} color="#7f97b8" />
      <mesh position={[0, -0.88, -0.15]} rotation={[-Math.PI / 2, 0, 0]} receiveShadow>
        <planeGeometry args={[9, 7]} />
        <meshStandardMaterial color="#221812" roughness={0.86} metalness={0.08} />
      </mesh>
      <Suspense fallback={null}>
        <PlaceholderHero progress={progress} />
      </Suspense>
      <CameraRig progress={progress} />
      <FpsProbe />
    </>
  );
}

function StaticFallback({ reason }) {
  window.__mithaqBenchmark.fallback = true;
  return (
    <div className="fallback-visual" role="img" aria-label="Static premium benchmark fallback">
      <div className="fallback-seal">M</div>
      <p>{reason}</p>
    </div>
  );
}

class BenchmarkErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { failed: false };
  }

  static getDerivedStateFromError() {
    return { failed: true };
  }

  componentDidCatch(error) {
    window.__mithaqBenchmark.fallback = true;
    window.__mithaqBenchmark.error = error?.message || 'Benchmark render error';
  }

  render() {
    if (this.state.failed) {
      return <StaticFallback reason="Static fallback active" />;
    }
    return this.props.children;
  }
}

function MetricsPanel() {
  const [metrics, setMetrics] = useState({});

  useEffect(() => {
    const interval = window.setInterval(() => {
      const b = window.__mithaqBenchmark;
      const perf = window.performance;
      const resources = perf?.getEntriesByType?.('resource') || [];
      const nav = perf?.getEntriesByType?.('navigation')?.[0];
      const model = resources.find((resource) => resource.name.includes('.glb'));
      const jsBytes = resources
        .filter((resource) => resource.name.includes('/assets/') && resource.name.endsWith('.js'))
        .reduce((sum, resource) => sum + (resource.transferSize || resource.encodedBodySize || 0), 0);
      const cssBytes = resources
        .filter((resource) => resource.name.includes('/assets/') && resource.name.endsWith('.css'))
        .reduce((sum, resource) => sum + (resource.transferSize || resource.encodedBodySize || 0), 0);
      setMetrics({
        scenario: b.scenario,
        fallback: b.fallback,
        reducedMotion: b.reducedMotion,
        webglAvailable: b.webglAvailable,
        avgFps: b.avgFps,
        lowFps: b.lowFps,
        scrollProgress: Number((b.scrollProgress || 0).toFixed(3)),
        canvasMountedMs: b.canvasMountedAt ? Math.round(b.canvasMountedAt - b.startedAt) : null,
        modelLoadedMs: b.modelLoadedAt ? Math.round(b.modelLoadedAt - b.startedAt) : null,
        firstInteractiveFeelMs: b.firstInteractiveFeelAt
          ? Math.round(b.firstInteractiveFeelAt - b.startedAt)
          : null,
        domVisibleMs: b.domVisibleAt ? Math.round(b.domVisibleAt - b.startedAt) : null,
        navigationDurationMs: nav ? Math.round(nav.duration) : null,
        domContentLoadedMs: nav ? Math.round(nav.domContentLoadedEventEnd) : null,
        loadEndMs: nav ? Math.round(nav.loadEventEnd) : null,
        modelDurationMs: model ? Math.round(model.duration) : null,
        modelBytes: model ? model.transferSize || model.encodedBodySize || 0 : null,
        jsBytes,
        cssBytes
      });
    }, 250);
    return () => window.clearInterval(interval);
  }, []);

  return (
    <output id="benchmark-metrics" aria-hidden="true">
      {JSON.stringify(metrics)}
    </output>
  );
}

function App() {
  const webglAvailable = useMemo(() => hasWebGL(), []);
  const progress = useScrollProgress();

  useEffect(() => {
    window.__mithaqBenchmark.webglAvailable = webglAvailable;
  }, [webglAvailable]);

  const shouldFallback = forceFallback || reducedMotion || !webglAvailable;

  return (
    <main>
      <section className="hero-benchmark" aria-label="Mithaq 3D feasibility benchmark">
        <div className="dom-overlay">
          <p className="eyebrow">Mithaq benchmark only</p>
          <h1>Scroll-driven gavel to seal feasibility test</h1>
          <p className="summary">
            Placeholder R3F scene validating DOM-first content, canvas loading,
            scroll motion, fallback behavior, and CTA visibility.
          </p>
          <div className="actions">
            <a className="primary-cta" href="https://wa.me/" aria-label="Placeholder WhatsApp CTA">
              Register Interest
            </a>
            <span className="scenario-pill">Scenario {scenario}</span>
          </div>
        </div>

        <div className="canvas-layer" aria-hidden="true">
          {shouldFallback ? (
            <StaticFallback
              reason={reducedMotion ? 'Reduced motion fallback active' : 'Static fallback active'}
            />
          ) : (
            <BenchmarkErrorBoundary>
              <Canvas
                dpr={scenario === 'B' ? [1, 1.5] : [1, 2]}
                camera={{ position: [0, 1.45, 5.2], fov: 42 }}
                gl={{ antialias: scenario === 'A', powerPreference: 'high-performance' }}
              >
                <Scene progress={progress} />
              </Canvas>
            </BenchmarkErrorBoundary>
          )}
        </div>
      </section>

      <section className="scroll-pad">
        <div>
          <h2>Scroll range</h2>
          <p>
            This area creates a minimal scroll range so the camera and placeholder
            seal can be mapped to user-controlled progression. It is not a final
            Mithaq scene.
          </p>
        </div>
      </section>
      <MetricsPanel />
    </main>
  );
}

createRoot(document.getElementById('root')).render(<App />);
