precision highp float;

uniform float uProgress;
uniform float uFractureProgress;
uniform vec3 uGoldColor;
uniform float uLineCount;
uniform float uLineWidth;
uniform float uGlowStrength;
uniform float uSeed;
uniform float uOpacity;
uniform float uTime;

varying vec2 vUv;

float lineSegment(vec2 p, vec2 a, vec2 b, float width) {
  vec2 pa = p - a;
  vec2 ba = b - a;
  float h = clamp(dot(pa, ba) / dot(ba, ba), 0.0, 1.0);
  float d = length(pa - ba * h);
  float cap = smoothstep(0.0, 0.04, h) * (1.0 - smoothstep(0.94, 1.0, h));
  return (1.0 - smoothstep(width, width * 2.5, d)) * cap;
}

void main() {
  vec2 p = vUv - 0.5;
  p.x *= 1.35;
  float total = 0.0;
  float glow = 0.0;
  float progress = clamp(min(uProgress, uFractureProgress), 0.0, 1.0);

  for (int i = 0; i < 8; i++) {
    float enabled = step(float(i) + 0.5, uLineCount);
    float fi = float(i);
    float angle = -2.65 + fi * 0.72 + 0.08 * sin(uSeed + fi * 2.1);
    float len = mix(0.18, 0.70 + 0.08 * sin(fi + uSeed), progress);
    vec2 dir = vec2(cos(angle), sin(angle));
    vec2 start = dir * 0.055;
    vec2 end = dir * len;
    float line = lineSegment(p, start, end, uLineWidth);
    float soft = lineSegment(p, start, end, uLineWidth * 3.7);
    total += line * enabled;
    glow += soft * enabled;
  }

  float fadeIn = smoothstep(0.04, 0.18, progress);
  float fadeOut = 1.0 - smoothstep(0.86, 1.0, uProgress);
  float alpha = (total + glow * uGlowStrength) * fadeIn * fadeOut * uOpacity;
  vec3 color = mix(uGoldColor * 0.74, uGoldColor, total);

  gl_FragColor = vec4(color, alpha);
}
