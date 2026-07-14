import { useMithaqStore } from '../store/mithaqStore';

export function DeviceTierBadge() {
  const tier = useMithaqStore((state) => state.deviceTier);
  return <span className={`device-badge device-badge--${tier}`}>Device tier: {tier}</span>;
}
