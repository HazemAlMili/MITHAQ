from pathlib import Path
import json
import math
import os

import bpy
from mathutils import Vector


ROOT = Path(r"D:\Clinets\MITHAQ\MITHAQ\mithaq-project-docs\mithaq-floating-documents-production")
SOURCE = ROOT / "source"
EXPORTS = ROOT / "exports"
RENDERS = ROOT / "renders"
REPORTS = ROOT / "reports"

for path in (SOURCE, EXPORTS, RENDERS, REPORTS):
    path.mkdir(parents=True, exist_ok=True)


DOC_NAMES = [
    "MITHAQ_Doc_01_Legal_Notes",
    "MITHAQ_Doc_02_Academic_Reference",
    "MITHAQ_Doc_03_Unfinished_Form",
    "MITHAQ_Doc_04_Case_Excerpt",
    "MITHAQ_Doc_05_Research_Sheet",
    "MITHAQ_Doc_06_Memo_Draft",
    "MITHAQ_Doc_07_Pleading_Fragment",
    "MITHAQ_Doc_08_Practice_Checklist",
]


def clear_scene():
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()


def make_material(name, base, roughness=0.82, metallic=0.0, bump=False):
    mat = bpy.data.materials.new(name)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        bsdf.inputs["Base Color"].default_value = base
        bsdf.inputs["Roughness"].default_value = roughness
        bsdf.inputs["Metallic"].default_value = metallic
        if bump:
            noise = mat.node_tree.nodes.new("ShaderNodeTexNoise")
            noise.inputs["Scale"].default_value = 38
            noise.inputs["Detail"].default_value = 8
            noise.inputs["Roughness"].default_value = 0.58
            bump_node = mat.node_tree.nodes.new("ShaderNodeBump")
            bump_node.inputs["Strength"].default_value = 0.018
            bump_node.inputs["Distance"].default_value = 0.030
            mat.node_tree.links.new(noise.outputs["Fac"], bump_node.inputs["Height"])
            mat.node_tree.links.new(bump_node.outputs["Normal"], bsdf.inputs["Normal"])
    return mat


PARCHMENT = make_material("MITHAQ_Mat_Parchment_Base", (0.950, 0.860, 0.705, 1), 0.84, 0.0, True)
PARCHMENT_DIM = make_material("MITHAQ_Mat_Parchment_Dim", (0.655, 0.570, 0.455, 1), 0.90, 0.0, True)
INK = make_material("MITHAQ_Mat_Abstract_Ink_Marks", (0.145, 0.095, 0.060, 1), 0.88, 0.0, False)
GOLD = make_material("MITHAQ_Mat_Subtle_Gold_Line", (0.690, 0.430, 0.155, 1), 0.48, 0.55, False)


def doc_curve(x, y, width, height, curl, fold):
    nx = x / width
    ny = y / height
    wave = curl * math.sin((nx + 0.5) * math.pi) * math.sin((ny + 0.5) * math.pi)
    diagonal = fold * (nx + 0.5) * (ny + 0.5)
    return wave + diagonal


def add_quad(verts, faces, mats, coords, mat_index):
    idx = len(verts)
    verts.extend(coords)
    faces.append((idx, idx + 1, idx + 2, idx + 3))
    mats.append(mat_index)


def add_mark(verts, faces, mats, width, height, x, y, w, h, z, mat_index):
    add_quad(
        verts,
        faces,
        mats,
        [
            (x, y, z),
            (x + w, y, z),
            (x + w, y + h, z),
            (x, y + h, z),
        ],
        mat_index,
    )


def create_document_mesh(name, width, height, curl, fold, mark_seed, location, rotation):
    nx = 3
    ny = 4
    thickness = 0.018
    verts = []
    faces = []
    mat_indices = []

    top_index = {}
    bottom_index = {}
    for iy in range(ny + 1):
        y = -height / 2 + height * iy / ny
        for ix in range(nx + 1):
            x = -width / 2 + width * ix / nx
            z = doc_curve(x, y, width, height, curl, fold)
            top_index[(ix, iy)] = len(verts)
            verts.append((x, y, z))
            bottom_index[(ix, iy)] = len(verts)
            verts.append((x, y, z - thickness))

    for iy in range(ny):
        for ix in range(nx):
            faces.append(
                (
                    top_index[(ix, iy)],
                    top_index[(ix + 1, iy)],
                    top_index[(ix + 1, iy + 1)],
                    top_index[(ix, iy + 1)],
                )
            )
            mat_indices.append(0)
            faces.append(
                (
                    bottom_index[(ix, iy + 1)],
                    bottom_index[(ix + 1, iy + 1)],
                    bottom_index[(ix + 1, iy)],
                    bottom_index[(ix, iy)],
                )
            )
            mat_indices.append(1)

    for ix in range(nx):
        faces.append((top_index[(ix, 0)], bottom_index[(ix, 0)], bottom_index[(ix + 1, 0)], top_index[(ix + 1, 0)]))
        mat_indices.append(1)
        faces.append((top_index[(ix + 1, ny)], bottom_index[(ix + 1, ny)], bottom_index[(ix, ny)], top_index[(ix, ny)]))
        mat_indices.append(1)
    for iy in range(ny):
        faces.append((top_index[(0, iy + 1)], bottom_index[(0, iy + 1)], bottom_index[(0, iy)], top_index[(0, iy)]))
        mat_indices.append(1)
        faces.append((top_index[(nx, iy)], bottom_index[(nx, iy)], bottom_index[(nx, iy + 1)], top_index[(nx, iy + 1)]))
        mat_indices.append(1)

    top_z = 0.035
    left = -width * 0.36
    top = height * 0.31
    line_h = height * 0.012
    gap = height * 0.055
    lengths = [0.62, 0.48, 0.68, 0.40, 0.55, 0.32, 0.60, 0.46]
    for i in range(7 + (mark_seed % 3)):
        line_w = width * lengths[(i + mark_seed) % len(lengths)]
        y = top - i * gap
        x = left + (0.035 * ((i + mark_seed) % 3))
        add_mark(verts, faces, mat_indices, width, height, x, y, line_w, line_h, top_z, 2)

    if mark_seed in (2, 4, 7):
        for i in range(3):
            x = width * (0.15 + 0.13 * i)
            y = -height * (0.12 + 0.06 * i)
            add_mark(verts, faces, mat_indices, width, height, x, y, width * 0.10, height * 0.035, top_z + 0.002, 2)

    if mark_seed in (3, 8):
        add_mark(verts, faces, mat_indices, width, height, -width * 0.34, height * 0.39, width * 0.42, line_h, top_z + 0.003, 3)

    mesh = bpy.data.meshes.new(name + "_Mesh")
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    bpy.context.collection.objects.link(obj)
    obj.data.materials.append(PARCHMENT)
    obj.data.materials.append(PARCHMENT_DIM)
    obj.data.materials.append(INK)
    obj.data.materials.append(GOLD)
    for face, mat_index in zip(obj.data.polygons, mat_indices):
        face.material_index = mat_index

    obj.location = location
    obj.rotation_euler = rotation
    obj["document_role"] = name.replace("MITHAQ_Doc_", "").replace("_", " ")
    obj["content_safety"] = "Abstract marks only; no readable legal text, personal data, court symbols, case numbers, stamps, or claims."

    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    bpy.ops.object.shade_smooth()
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    try:
        bpy.ops.object.mode_set(mode="EDIT")
        bpy.ops.mesh.select_all(action="SELECT")
        bpy.ops.uv.smart_project(angle_limit=math.radians(68), island_margin=0.025)
        bpy.ops.object.mode_set(mode="OBJECT")
    except Exception:
        bpy.ops.object.mode_set(mode="OBJECT")
    obj.select_set(False)
    return obj


def create_anchor(name, location):
    obj = bpy.data.objects.new(name, None)
    obj.empty_display_type = "PLAIN_AXES"
    obj.empty_display_size = 0.32
    obj.location = location
    bpy.context.collection.objects.link(obj)
    return obj


def build_documents():
    configs = [
        (0.78, 1.08, 0.020, 0.010, (-1.60, 0.30, 0.52), (math.radians(14), math.radians(-18), math.radians(-18))),
        (0.72, 1.02, -0.018, -0.008, (-0.80, 0.78, 0.18), (math.radians(-10), math.radians(20), math.radians(12))),
        (0.82, 1.16, 0.024, -0.006, (0.05, 0.52, 0.42), (math.radians(9), math.radians(-10), math.radians(4))),
        (0.70, 0.96, -0.016, 0.014, (0.90, 0.70, -0.05), (math.radians(-14), math.radians(16), math.radians(20))),
        (0.78, 1.10, 0.019, -0.012, (1.52, -0.05, 0.28), (math.radians(12), math.radians(-22), math.radians(32))),
        (0.74, 1.04, -0.014, 0.006, (0.64, -0.78, 0.62), (math.radians(-8), math.radians(12), math.radians(-8))),
        (0.68, 0.95, 0.017, 0.012, (-0.30, -0.92, 0.03), (math.radians(18), math.radians(8), math.radians(-34))),
        (0.80, 1.08, -0.020, -0.010, (-1.15, -0.56, 0.30), (math.radians(-12), math.radians(-18), math.radians(24))),
    ]
    objects = []
    for i, name in enumerate(DOC_NAMES):
        width, height, curl, fold, loc, rot = configs[i]
        objects.append(create_document_mesh(name, width, height, curl, fold, i + 1, loc, rot))
    create_anchor("MITHAQ_Documents_Orbit_Center", (0, 0, 0.26))
    create_anchor("MITHAQ_Documents_Converge_Target", (0.15, -0.18, 0.14))
    create_anchor("MITHAQ_Documents_Camera_Preview", (2.2, -3.2, 1.75))
    bpy.context.scene["Mithaq_P5_05_Notes"] = (
        "Eight separate low-poly floating document meshes for Scene 03. "
        "Abstract marks only; no fake legal identities, court/government marks, or readable claims."
    )
    return objects


def count_model_stats():
    depsgraph = bpy.context.evaluated_depsgraph_get()
    triangles_per = {}
    total = 0
    mesh_count = 0
    materials = set()
    for obj in bpy.context.scene.objects:
        if obj.type == "MESH" and obj.name in DOC_NAMES:
            mesh_count += 1
            eval_obj = obj.evaluated_get(depsgraph)
            mesh = eval_obj.to_mesh()
            tris = 0
            for poly in mesh.polygons:
                tris += max(1, len(poly.vertices) - 2)
            eval_obj.to_mesh_clear()
            triangles_per[obj.name] = tris
            total += tris
            for slot in obj.material_slots:
                if slot.material:
                    materials.add(slot.material.name)
    return {
        "totalTriangles": total,
        "trianglesPerDocument": {name: triangles_per.get(name, 0) for name in DOC_NAMES},
        "meshes": mesh_count,
        "materials": len(materials),
        "materialNames": sorted(materials),
        "textures": 0,
        "textureDimensions": [],
    }


def setup_lighting():
    bpy.context.scene.world = bpy.data.worlds.new("Mithaq_Documents_Dark_World") if not bpy.context.scene.world else bpy.context.scene.world
    bpy.context.scene.world.color = (0.006, 0.005, 0.008)
    bpy.ops.object.light_add(type="AREA", location=(-3.0, -3.4, 3.6))
    key = bpy.context.object
    key.name = "Mithaq_Documents_Warm_Key_Light"
    key.data.energy = 470
    key.data.size = 4.4
    key.data.color = (1.0, 0.82, 0.60)
    bpy.ops.object.light_add(type="POINT", location=(2.7, 2.4, 2.0))
    rim = bpy.context.object
    rim.name = "Mithaq_Documents_Subtle_Rim_Light"
    rim.data.energy = 54
    rim.data.color = (1.0, 0.72, 0.38)


def look_at(obj, target):
    direction = Vector(target) - obj.location
    obj.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()


def setup_camera(name, location, target, focal=70, ortho=False, ortho_scale=4.4):
    cam_data = bpy.data.cameras.new(name + "_Camera")
    cam = bpy.data.objects.new(name + "_Camera", cam_data)
    bpy.context.collection.objects.link(cam)
    cam.location = location
    look_at(cam, target)
    cam.data.lens = focal
    if ortho:
        cam.data.type = "ORTHO"
        cam.data.ortho_scale = ortho_scale
    return cam


def render_preview(path, cam, wireframe=False):
    bpy.context.scene.camera = cam
    bpy.context.scene.render.filepath = str(path)
    bpy.context.scene.render.resolution_x = 1400
    bpy.context.scene.render.resolution_y = 900
    bpy.context.scene.eevee.taa_render_samples = 64

    wire_objs = []
    if wireframe:
        wire_mat = make_material("MITHAQ_Mat_Wireframe_Gold", (0.86, 0.64, 0.25, 1), 0.45, 0.0)
        for obj in list(bpy.context.scene.objects):
            if obj.type == "MESH" and obj.name in DOC_NAMES:
                dup = obj.copy()
                dup.data = obj.data.copy()
                dup.name = obj.name + "_WireframePreview"
                dup.data.materials.clear()
                dup.data.materials.append(wire_mat)
                bpy.context.collection.objects.link(dup)
                mod = dup.modifiers.new("Wireframe_Render_Modifier", "WIREFRAME")
                mod.thickness = 0.004
                mod.use_replace = False
                wire_objs.append(dup)
                obj.hide_render = True

    bpy.ops.render.render(write_still=True)

    for obj in wire_objs:
        bpy.data.objects.remove(obj, do_unlink=True)
    for obj in bpy.context.scene.objects:
        if obj.name in DOC_NAMES:
            obj.hide_render = False


def export_glb(path, draco=False):
    bpy.ops.object.select_all(action="DESELECT")
    for obj in bpy.context.scene.objects:
        if obj.type == "MESH" and obj.name in DOC_NAMES:
            obj.select_set(True)
    kwargs = {
        "filepath": str(path),
        "export_format": "GLB",
        "use_selection": True,
        "export_apply": True,
        "export_yup": True,
        "export_lights": False,
        "export_cameras": False,
    }
    if draco:
        kwargs.update(
            {
                "export_draco_mesh_compression_enable": True,
                "export_draco_mesh_compression_level": 6,
                "export_draco_position_quantization": 14,
                "export_draco_normal_quantization": 10,
                "export_draco_texcoord_quantization": 12,
            }
        )
    bpy.ops.export_scene.gltf(**kwargs)


def main():
    clear_scene()
    build_documents()
    setup_lighting()

    bpy.context.scene.render.engine = "BLENDER_EEVEE"
    bpy.context.scene.eevee.taa_samples = 64
    bpy.context.scene.view_settings.view_transform = "Filmic"
    bpy.context.scene.view_settings.look = "Medium High Contrast"
    bpy.context.scene.view_settings.exposure = -0.08
    bpy.context.scene.view_settings.gamma = 1.0

    cameras = {
        "cluster": setup_camera("Documents_Cluster", (2.6, -3.9, 2.1), (0, 0, 0.26), 70),
        "orbit": setup_camera("Documents_Orbit", (0, 0, 5.2), (0, 0, 0.0), 70, True, 4.4),
        "single": setup_camera("Documents_Single_Detail", (-0.95, -2.35, 1.15), (-0.55, -0.55, 0.23), 92),
        "dark": setup_camera("Documents_Dark_Scene", (2.2, -3.4, 1.65), (0.10, 0.02, 0.25), 78),
        "wireframe": setup_camera("Documents_Wireframe", (2.6, -3.9, 2.1), (0, 0, 0.26), 70),
    }

    render_preview(RENDERS / "documents-preview-cluster.png", cameras["cluster"])
    render_preview(RENDERS / "documents-preview-orbit-layout.png", cameras["orbit"])
    render_preview(RENDERS / "documents-preview-single-detail.png", cameras["single"])
    render_preview(RENDERS / "documents-preview-dark-scene.png", cameras["dark"])
    render_preview(RENDERS / "documents-preview-wireframe.png", cameras["wireframe"], wireframe=True)

    stats = count_model_stats()
    stats.update(
        {
            "asset": "Mithaq Floating Documents",
            "ticket": "P5.05",
            "blenderVersion": bpy.app.version_string,
            "optimizationMethod": "Blender GLTF exporter Draco compression fallback; gltfpack unavailable in execution shell.",
            "documentCount": len(DOC_NAMES),
            "conditions": [
                "gltfpack unavailable in execution shell; Blender Draco compression used for documents.opt.glb.",
                "Final material/art approval, mobile LOD, R3F import validation, and Scene 03 orbit/convergence validation remain pending.",
                "No readable fake legal text, court/government marks, personal data, official stamps, or fake legal claims are included.",
            ],
        }
    )

    bpy.ops.wm.save_as_mainfile(filepath=str(SOURCE / "documents.blend"))
    export_glb(EXPORTS / "documents.raw.glb", draco=False)
    export_glb(EXPORTS / "documents.opt.glb", draco=True)

    stats["rawGlbBytes"] = os.path.getsize(EXPORTS / "documents.raw.glb")
    stats["optimizedGlbBytes"] = os.path.getsize(EXPORTS / "documents.opt.glb")
    stats["sourceBlendBytes"] = os.path.getsize(SOURCE / "documents.blend")
    stats["rawReimportPass"] = False
    stats["optimizedReimportPass"] = False

    with open(REPORTS / "documents-gltf-inspect.json", "w", encoding="utf-8") as f:
        json.dump(stats, f, indent=2)

    with open(REPORTS / "documents-file-size-log.md", "w", encoding="utf-8") as f:
        f.write(f"documents.raw.glb: {stats['rawGlbBytes']} bytes / {stats['rawGlbBytes'] / 1024 / 1024:.4f} MB\n")
        f.write(f"documents.opt.glb: {stats['optimizedGlbBytes']} bytes / {stats['optimizedGlbBytes'] / 1024 / 1024:.4f} MB\n")
        f.write("target: <= 500 KB preferred, <= 1.2 MB hard maximum\n")
        result = "PASS" if stats["optimizedGlbBytes"] <= 500 * 1024 else "FAIL"
        f.write(f"result: {result}\n")

    print("MITHAQ_DOCUMENTS_STATS", json.dumps(stats))


if __name__ == "__main__":
    main()
