precision highp float;

uniform float uOpacity;
uniform vec3 uGoldColor;

varying float vAlpha;

void main() {
  vec2 p = gl_PointCoord - 0.5;
  float d = length(p);
  float disc = 1.0 - smoothstep(0.10, 0.50, d);
  float core = 1.0 - smoothstep(0.0, 0.18, d);
  vec3 color = mix(uGoldColor * 0.45, uGoldColor, core);
  gl_FragColor = vec4(color, disc * vAlpha * uOpacity);
}
