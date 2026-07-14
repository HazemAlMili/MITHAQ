import { useEffect, useState } from 'react';
import { SandboxMode } from './DossierSandboxScene';

type Metrics = NonNullable<Window['__MITHAQ_DOSSIER_METRICS__']>;

export function MetricsPanel({ mode }: { mode: SandboxMode }) {
  const [metrics, setMetrics] = useState<Metrics | null>(null);

  useEffect(() => {
    const id = window.setInterval(() => {
      setMetrics(window.__MITHAQ_DOSSIER_METRICS__ ?? null);
    }, 300);
    return () => window.clearInterval(id);
  }, []);

  return (
    <dl className="metrics" data-mode={mode}>
      <div>
        <dt>Mode</dt>
        <dd>{metrics?.mode ?? mode}</dd>
      </div>
      <div>
        <dt>Average FPS</dt>
        <dd>{metrics ? metrics.averageFps.toFixed(1) : 'warming'}</dd>
      </div>
      <div>
        <dt>Draw Calls</dt>
        <dd>{metrics?.rendererInfo.calls ?? '...'}</dd>
      </div>
      <div>
        <dt>Triangles</dt>
        <dd>{metrics?.rendererInfo.triangles ?? '...'}</dd>
      </div>
      <div>
        <dt>Textures</dt>
        <dd>{metrics?.rendererInfo.textures ?? '...'}</dd>
      </div>
    </dl>
  );
}

