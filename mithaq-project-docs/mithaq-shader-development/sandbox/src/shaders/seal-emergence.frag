precision highp float;

uniform float uProgress;
uniform vec3 uGoldColor;
uniform vec3 uHighlightColor;
uniform float uEmissiveStrength;
uniform float uRevealSoftness;
uniform float uOpacity;
uniform float uTime;

varying vec2 vUv;
varying vec3 vNormal;
varying vec3 vWorldPosition;

void main() {
  vec2 centered = vUv - 0.5;
  float angle = atan(centered.y, centered.x);
  float normalizedAngle = (angle + 3.14159265) / 6.2831853;
  float radius = length(centered);
  float sweep = smoothstep(uProgress - uRevealSoftness, uProgress + uRevealSoftness, normalizedAngle);
  float radialWake = smoothstep(0.05, 0.40, radius) * (1.0 - smoothstep(0.56, 0.72, radius));
  float reveal = (1.0 - sweep) * radialWake;
  float rim = pow(1.0 - abs(dot(normalize(vNormal), vec3(0.0, 0.0, 1.0))), 2.0);
  float warmPulse = 0.92 + 0.08 * sin(uTime * 1.2);

  vec3 base = mix(uGoldColor * 0.52, uGoldColor, reveal);
  vec3 highlight = uHighlightColor * rim * uEmissiveStrength * reveal * warmPulse;
  float alpha = clamp((0.10 + reveal * 0.90) * uOpacity, 0.0, 1.0);

  gl_FragColor = vec4(base + highlight, alpha);
}
