import { clamp } from './clamp';

export function mapRange(value: number, inMin: number, inMax: number, outMin = 0, outMax = 1): number {
  if (inMax === inMin) {
    return outMin;
  }

  const normalized = clamp((value - inMin) / (inMax - inMin));
  return outMin + normalized * (outMax - outMin);
}
