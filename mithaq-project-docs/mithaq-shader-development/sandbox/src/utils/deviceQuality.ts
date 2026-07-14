export type DeviceQuality = 'desktop' | 'low';

export function getParticleCount(quality: DeviceQuality, reducedMotion: boolean) {
  if (reducedMotion) return 36;
  return quality === 'low' ? 80 : 220;
}

export function getDeviceQualityFromQuery(): DeviceQuality {
  const params = new URLSearchParams(window.location.search);
  return params.get('quality') === 'low' ? 'low' : 'desktop';
}
