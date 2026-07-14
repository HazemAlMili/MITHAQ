import { useMithaqStore } from '../store/mithaqStore';

export function ReducedMotionToggle() {
  const reducedMotion = useMithaqStore((state) => state.reducedMotion);
  const setReducedMotion = useMithaqStore((state) => state.setReducedMotion);

  const toggle = () => {
    const next = !reducedMotion;
    window.localStorage.setItem('mithaq-reduced-motion-override', String(next));
    setReducedMotion(next);
  };

  return (
    <button className="debug-button" type="button" onClick={toggle} data-testid="reduced-motion-toggle">
      Reduced motion: {reducedMotion ? 'ON' : 'OFF'}
    </button>
  );
}
