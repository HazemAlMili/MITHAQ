precision highp float;

uniform float uTime;
uniform float uPointSize;
uniform float uDriftStrength;
uniform float uDepthFade;

attribute float aSeed;

varying float vAlpha;

void main() {
  vec3 pos = position;
  pos.x += sin(uTime * 0.18 + aSeed * 7.13) * uDriftStrength;
  pos.y += cos(uTime * 0.14 + aSeed * 5.71) * uDriftStrength * 0.42;
  pos.z += sin(uTime * 0.11 + aSeed * 3.37) * uDriftStrength * 0.58;

  vec4 mvPosition = modelViewMatrix * vec4(pos, 1.0);
  float depth = clamp(1.0 - abs(mvPosition.z) * 0.055, 0.0, 1.0);
  vAlpha = mix(0.22, 1.0, depth * uDepthFade);
  gl_PointSize = uPointSize * (260.0 / max(90.0, -mvPosition.z));
  gl_Position = projectionMatrix * mvPosition;
}
