import { useEffect } from 'react';
import { useMithaqStore } from '../store/mithaqStore';

export function useReducedMotion(): void {
  const setReducedMotion = useMithaqStore((state) => state.setReducedMotion);

  useEffect(() => {
    const media = window.matchMedia('(prefers-reduced-motion: reduce)');

    const applyPreference = () => {
      const manual = window.localStorage.getItem('mithaq-reduced-motion-override');
      setReducedMotion(manual === null ? media.matches : manual === 'true');
    };

    applyPreference();
    media.addEventListener('change', applyPreference);

    return () => media.removeEventListener('change', applyPreference);
  }, [setReducedMotion]);
}
