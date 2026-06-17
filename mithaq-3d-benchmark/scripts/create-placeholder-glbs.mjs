import { mkdir, writeFile } from 'node:fs/promises';
import { dirname, resolve } from 'node:path';

const outDir = resolve('public/models');

function pad4(value) {
  return (4 - (value % 4)) % 4;
}

function box(width, height, depth, center, name) {
  const [cx, cy, cz] = center;
  const x = width / 2;
  const y = height / 2;
  const z = depth / 2;
  const faces = [
    { n: [1, 0, 0], v: [[x, -y, -z], [x, y, -z], [x, y, z], [x, -y, z]] },
    { n: [-1, 0, 0], v: [[-x, -y, z], [-x, y, z], [-x, y, -z], [-x, -y, -z]] },
    { n: [0, 1, 0], v: [[-x, y, -z], [-x, y, z], [x, y, z], [x, y, -z]] },
    { n: [0, -1, 0], v: [[-x, -y, z], [-x, -y, -z], [x, -y, -z], [x, -y, z]] },
    { n: [0, 0, 1], v: [[-x, -y, z], [x, -y, z], [x, y, z], [-x, y, z]] },
    { n: [0, 0, -1], v: [[x, -y, -z], [-x, -y, -z], [-x, y, -z], [x, y, -z]] }
  ];
  const positions = [];
  const normals = [];
  const indices = [];
  for (const face of faces) {
    const start = positions.length / 3;
    for (const point of face.v) {
      positions.push(point[0] + cx, point[1] + cy, point[2] + cz);
      normals.push(...face.n);
    }
    indices.push(start, start + 1, start + 2, start, start + 2, start + 3);
  }
  return { name, positions, normals, indices };
}

function seal(radius, depth, segments, rings, center, name) {
  const [cx, cy, cz] = center;
  const positions = [];
  const normals = [];
  const indices = [];
  const half = depth / 2;

  for (const side of [-1, 1]) {
    const base = positions.length / 3;
    for (let r = 0; r <= rings; r++) {
      const rr = radius * (r / rings);
      for (let s = 0; s <= segments; s++) {
        const angle = (s / segments) * Math.PI * 2;
        const ripple = Math.sin(r * 0.8) * 0.004 * (rings > 10 ? 1 : 0);
        positions.push(cx + Math.cos(angle) * rr, cy + Math.sin(angle) * rr, cz + side * (half + ripple));
        normals.push(0, 0, side);
      }
    }
    for (let r = 0; r < rings; r++) {
      for (let s = 0; s < segments; s++) {
        const a = base + r * (segments + 1) + s;
        const b = a + 1;
        const c = a + segments + 1;
        const d = c + 1;
        if (side > 0) indices.push(a, c, b, b, c, d);
        else indices.push(a, b, c, b, d, c);
      }
    }
  }

  const sideBase = positions.length / 3;
  for (let zSide = 0; zSide <= 1; zSide++) {
    const z = zSide === 0 ? -half : half;
    for (let s = 0; s <= segments; s++) {
      const angle = (s / segments) * Math.PI * 2;
      const nx = Math.cos(angle);
      const ny = Math.sin(angle);
      positions.push(cx + nx * radius, cy + ny * radius, cz + z);
      normals.push(nx, ny, 0);
    }
  }
  for (let s = 0; s < segments; s++) {
    const a = sideBase + s;
    const b = a + 1;
    const c = sideBase + (segments + 1) + s;
    const d = c + 1;
    indices.push(a, c, b, b, c, d);
  }

  return { name, positions, normals, indices };
}

function combine(meshes) {
  const positions = [];
  const normals = [];
  const indices = [];
  const ranges = [];
  for (const mesh of meshes) {
    const vertexOffset = positions.length / 3;
    const indexOffset = indices.length;
    positions.push(...mesh.positions);
    normals.push(...mesh.normals);
    for (const index of mesh.indices) {
      indices.push(index + vertexOffset);
    }
    ranges.push({
      name: mesh.name,
      indexOffset,
      indexCount: mesh.indices.length
    });
  }
  return { positions, normals, indices, ranges };
}

function minMax(values) {
  const min = [Infinity, Infinity, Infinity];
  const max = [-Infinity, -Infinity, -Infinity];
  for (let i = 0; i < values.length; i += 3) {
    for (let axis = 0; axis < 3; axis++) {
      min[axis] = Math.min(min[axis], values[i + axis]);
      max[axis] = Math.max(max[axis], values[i + axis]);
    }
  }
  return { min, max };
}

function makeGlb({ scenario, segments, rings }) {
  const meshes = [
    box(2.5, 0.18, 0.18, [-0.55, -0.06, 0], 'placeholder_gavel_handle'),
    box(0.78, 0.52, 0.62, [0.76, 0.18, 0], 'placeholder_gavel_head'),
    seal(0.78, 0.12, segments, rings, [0, 0.32, -0.78], 'placeholder_seal')
  ];
  const data = combine(meshes);
  const positionBuffer = Buffer.from(new Float32Array(data.positions).buffer);
  const normalBuffer = Buffer.from(new Float32Array(data.normals).buffer);
  const indexArray = data.positions.length / 3 > 65535 ? new Uint32Array(data.indices) : new Uint16Array(data.indices);
  const indexBuffer = Buffer.from(indexArray.buffer);

  const positionOffset = 0;
  const normalOffset = positionOffset + positionBuffer.length + pad4(positionBuffer.length);
  const indexOffset = normalOffset + normalBuffer.length + pad4(normalBuffer.length);
  const binLength = indexOffset + indexBuffer.length + pad4(indexBuffer.length);
  const bin = Buffer.alloc(binLength);
  positionBuffer.copy(bin, positionOffset);
  normalBuffer.copy(bin, normalOffset);
  indexBuffer.copy(bin, indexOffset);

  const bounds = minMax(data.positions);
  const componentType = indexArray instanceof Uint32Array ? 5125 : 5123;
  const indexByteSize = componentType === 5125 ? 4 : 2;
  const gltf = {
    asset: { version: '2.0', generator: 'Mithaq placeholder benchmark generator' },
    scene: 0,
    scenes: [{ nodes: [0] }],
    nodes: [{ name: `mithaq_placeholder_${scenario}`, mesh: 0 }],
    meshes: [
      {
        name: `mithaq_placeholder_${scenario}`,
        primitives: data.ranges.map((range, i) => ({
          attributes: { POSITION: 0, NORMAL: 1 },
          indices: 2 + i,
          material: i === 2 ? 1 : 0
        }))
      }
    ],
    materials: [
      {
        name: 'dark_bronze_placeholder',
        pbrMetallicRoughness: {
          baseColorFactor: [0.38, 0.25, 0.13, 1],
          metallicFactor: 0.55,
          roughnessFactor: 0.58
        }
      },
      {
        name: 'restrained_gold_placeholder',
        pbrMetallicRoughness: {
          baseColorFactor: [0.86, 0.67, 0.34, 1],
          metallicFactor: 0.75,
          roughnessFactor: 0.42
        }
      }
    ],
    buffers: [{ byteLength: bin.length }],
    bufferViews: [
      { buffer: 0, byteOffset: positionOffset, byteLength: positionBuffer.length, target: 34962 },
      { buffer: 0, byteOffset: normalOffset, byteLength: normalBuffer.length, target: 34962 },
      ...data.ranges.map((range) => ({
        buffer: 0,
        byteOffset: indexOffset + range.indexOffset * indexByteSize,
        byteLength: range.indexCount * indexByteSize,
        target: 34963
      }))
    ],
    accessors: [
      {
        bufferView: 0,
        componentType: 5126,
        count: data.positions.length / 3,
        type: 'VEC3',
        min: bounds.min,
        max: bounds.max
      },
      {
        bufferView: 1,
        componentType: 5126,
        count: data.normals.length / 3,
        type: 'VEC3'
      },
      ...data.ranges.map((range, i) => ({
        bufferView: 2 + i,
        componentType,
        count: range.indexCount,
        type: 'SCALAR'
      }))
    ]
  };

  const json = Buffer.from(JSON.stringify(gltf));
  const jsonPadded = Buffer.concat([json, Buffer.alloc(pad4(json.length), 0x20)]);
  const totalLength = 12 + 8 + jsonPadded.length + 8 + bin.length;
  const header = Buffer.alloc(12);
  header.writeUInt32LE(0x46546c67, 0);
  header.writeUInt32LE(2, 4);
  header.writeUInt32LE(totalLength, 8);
  const jsonHeader = Buffer.alloc(8);
  jsonHeader.writeUInt32LE(jsonPadded.length, 0);
  jsonHeader.writeUInt32LE(0x4e4f534a, 4);
  const binHeader = Buffer.alloc(8);
  binHeader.writeUInt32LE(bin.length, 0);
  binHeader.writeUInt32LE(0x004e4942, 4);
  return Buffer.concat([header, jsonHeader, jsonPadded, binHeader, bin]);
}

await mkdir(outDir, { recursive: true });
const light = makeGlb({ scenario: 'light', segments: 32, rings: 3 });
const upper = makeGlb({ scenario: 'upper', segments: 192, rings: 90 });
await writeFile(resolve(outDir, 'mithaq-placeholder-light.glb'), light);
await writeFile(resolve(outDir, 'mithaq-placeholder-upper.glb'), upper);

console.log(`Generated ${light.length} bytes -> ${resolve(outDir, 'mithaq-placeholder-light.glb')}`);
console.log(`Generated ${upper.length} bytes -> ${resolve(outDir, 'mithaq-placeholder-upper.glb')}`);
