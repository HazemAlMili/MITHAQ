precision highp float;

uniform float uProgress;
uniform vec2 uImpactPoint;
uniform vec3 uGoldColor;
uniform float uOpacity;
uniform float uRingWidth;
uniform float uEchoStrength;
uniform float uTime;

varying vec2 vUv;

float ring(float dist, float radius, float width) {
  return 1.0 - smoothstep(0.0, width, abs(dist - radius));
}

void main() {
  vec2 aspectUv = vec2(vUv.x, vUv.y * 0.72);
  vec2 aspectImpact = vec2(uImpactPoint.x, uImpactPoint.y * 0.72);
  float dist = distance(aspectUv, aspectImpact);

  float eased = 1.0 - pow(1.0 - clamp(uProgress, 0.0, 1.0), 3.0);
  float radius = mix(0.035, 0.72, eased);
  float primary = ring(dist, radius, uRingWidth);
  float echo = ring(dist, max(0.0, radius - 0.13), uRingWidth * 1.25) * uEchoStrength;
  float lateFade = 1.0 - smoothstep(0.78, 1.0, uProgress);
  float earlyFade = smoothstep(0.02, 0.12, uProgress);
  float pulse = 0.92 + 0.08 * sin(uTime * 1.7);

  float alpha = (primary + echo) * lateFade * earlyFade * uOpacity;
  vec3 color = uGoldColor * pulse;

  gl_FragColor = vec4(color, alpha);
}
