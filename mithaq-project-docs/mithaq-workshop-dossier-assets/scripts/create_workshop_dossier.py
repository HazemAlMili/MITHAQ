from pathlib import Path
import csv
import json
import math
import os
import shutil

import bpy


ROOT = Path(r"D:\Clinets\MITHAQ\MITHAQ\mithaq-project-docs\mithaq-workshop-dossier-assets")
SOURCE = ROOT / "source"
EXPORTS = ROOT / "exports"
TEXTURES = ROOT / "textures"
TEXTURES_COMPRESSED = TEXTURES / "compressed"
SANDBOX = ROOT / "sandbox"
CAPTURES = ROOT / "captures"
REPORTS = ROOT / "reports"

SOURCE_ATLAS = Path(
    r"D:\Clinets\MITHAQ\MITHAQ\mithaq-project-docs\mithaq-dark-texture-material-library\webp\leather-dark\mithaq-leather-dark-subtle-color-1024.webp"
)
ATLAS = TEXTURES / "workshop-dossier-atlas.webp"

for path in (SOURCE, EXPORTS, TEXTURES, TEXTURES_COMPRESSED, SANDBOX, CAPTURES, REPORTS):
    path.mkdir(parents=True, exist_ok=True)


def clear_scene():
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()


def make_material(name, base, roughness=0.82, metallic=0.0, noise=False):
    mat = bpy.data.materials.new(name)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        bsdf.inputs["Base Color"].default_value = base
        bsdf.inputs["Roughness"].default_value = roughness
        bsdf.inputs["Metallic"].default_value = metallic
        if noise:
            tex = mat.node_tree.nodes.new("ShaderNodeTexNoise")
            tex.inputs["Scale"].default_value = 42
            tex.inputs["Detail"].default_value = 10
            tex.inputs["Roughness"].default_value = 0.58
            bump = mat.node_tree.nodes.new("ShaderNodeBump")
            bump.inputs["Strength"].default_value = 0.022
            bump.inputs["Distance"].default_value = 0.035
            mat.node_tree.links.new(tex.outputs["Fac"], bump.inputs["Height"])
            mat.node_tree.links.new(bump.outputs["Normal"], bsdf.inputs["Normal"])
    return mat


COVER = make_material("MITHAQ_Mat_Dossier_Dark_Leather", (0.060, 0.035, 0.027, 1), 0.88, 0.0, True)
PAPER = make_material("MITHAQ_Mat_Dossier_Parchment_Stack", (0.770, 0.690, 0.560, 1), 0.84, 0.0, True)
GOLD = make_material("MITHAQ_Mat_Dossier_Muted_Brass", (0.760, 0.520, 0.210, 1), 0.42, 0.88, False)
SHADOW = make_material("MITHAQ_Mat_Dossier_Shadow_Groove", (0.018, 0.014, 0.012, 1), 0.94, 0.0, False)


def copy_atlas():
    if SOURCE_ATLAS.exists():
        shutil.copyfile(SOURCE_ATLAS, ATLAS)
        return os.path.getsize(ATLAS), "Copied from P4.06 dark leather subtle WebP; external shared atlas reference, not embedded in GLB."
    return 0, "P4.06 leather atlas source missing; procedural materials used and atlas file unavailable."


def apply_bevel_uv(obj, bevel=0.015, segments=1):
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    if bevel > 0:
        mod = obj.modifiers.new("Controlled_Dossier_Bevel", "BEVEL")
        mod.width = bevel
        mod.segments = segments
        mod.affect = "EDGES"
        normal = obj.modifiers.new("Weighted_Dossier_Normals", "WEIGHTED_NORMAL")
        bpy.ops.object.modifier_apply(modifier=mod.name)
        bpy.ops.object.modifier_apply(modifier=normal.name)
    try:
        bpy.ops.object.shade_smooth()
        bpy.ops.object.mode_set(mode="EDIT")
        bpy.ops.mesh.select_all(action="SELECT")
        bpy.ops.uv.smart_project(angle_limit=math.radians(68), island_margin=0.025)
        bpy.ops.object.mode_set(mode="OBJECT")
    except Exception:
        bpy.ops.object.mode_set(mode="OBJECT")
    obj.select_set(False)


def add_box(name, location, dimensions, mat, bevel=0.015, segments=1):
    bpy.ops.mesh.primitive_cube_add(size=1, location=location)
    obj = bpy.context.object
    obj.name = name
    obj.data.name = f"{name}_Mesh"
    obj.dimensions = dimensions
    obj.data.materials.append(mat)
    apply_bevel_uv(obj, bevel, segments)
    return obj


def join_as(objects, name):
    bpy.ops.object.select_all(action="DESELECT")
    bpy.context.view_layer.objects.active = objects[0]
    for obj in objects:
        obj.select_set(True)
    bpy.ops.object.join()
    obj = bpy.context.object
    obj.name = name
    obj.data.name = f"{name}_Mesh"
    obj.select_set(False)
    return obj


def add_cylinder(name, location, radius, depth, mat, vertices=32, bevel=0.0):
    bpy.ops.mesh.primitive_cylinder_add(vertices=vertices, radius=radius, depth=depth, location=location)
    obj = bpy.context.object
    obj.name = name
    obj.data.name = f"{name}_Mesh"
    obj.data.materials.append(mat)
    apply_bevel_uv(obj, bevel, 1)
    return obj


def add_line_mark(name, x, y, z, width, mat=SHADOW):
    return add_box(name, (x, y, z), (width, 0.012, 0.006), mat, 0.002, 1)


def build_desktop_dossier():
    cover_parts = [
        add_box("MITHAQ_Dossier_Front_Cover_D", (0, 0, 0.135), (2.18, 3.02, 0.085), COVER, 0.032, 2),
        add_box("MITHAQ_Dossier_Back_Cover_D", (0, 0, 0.040), (2.22, 3.06, 0.050), COVER, 0.022, 1),
        add_box("MITHAQ_Dossier_Spine_D", (-1.13, 0, 0.105), (0.145, 3.08, 0.175), COVER, 0.030, 2),
        add_box("MITHAQ_Dossier_Corner_Detail_A_D", (0.86, 1.30, 0.187), (0.34, 0.030, 0.012), GOLD, 0.004, 1),
        add_box("MITHAQ_Dossier_Corner_Detail_B_D", (1.01, 1.15, 0.187), (0.030, 0.34, 0.012), GOLD, 0.004, 1),
    ]
    cover = join_as(cover_parts, "MITHAQ_Workshop_Dossier_Desktop_Cover")

    paper_parts = [
        add_box("MITHAQ_Dossier_Paper_Core_D", (0.10, -0.03, 0.082), (1.96, 2.76, 0.078), PAPER, 0.012, 1),
    ]
    for i in range(5):
        paper_parts.append(add_box(f"MITHAQ_Dossier_Paper_Edge_Line_{i+1}_D", (1.105, -1.05 + i * 0.48, 0.132), (0.030, 0.34, 0.006), SHADOW, 0.001, 1))
    paper = join_as(paper_parts, "MITHAQ_Workshop_Dossier_Desktop_Paper_Stack")

    plate_parts = [
        add_box("MITHAQ_Dossier_Title_Plate_D", (0.05, 0.88, 0.198), (1.18, 0.34, 0.022), GOLD, 0.018, 1),
        add_line_mark("MITHAQ_Dossier_Neutral_Line_A_D", -0.10, 0.93, 0.214, 0.70, SHADOW),
        add_line_mark("MITHAQ_Dossier_Neutral_Line_B_D", -0.10, 0.84, 0.214, 0.52, SHADOW),
        add_box("MITHAQ_Dossier_Variant_01_A_D", (-0.44, 0.67, 0.204), (0.020, 0.12, 0.010), GOLD, 0.003, 1),
        add_box("MITHAQ_Dossier_Variant_01_B_D", (-0.30, 0.67, 0.204), (0.020, 0.12, 0.010), GOLD, 0.003, 1),
        add_box("MITHAQ_Dossier_Variant_01_C_D", (-0.30, 0.61, 0.204), (0.090, 0.020, 0.010), GOLD, 0.003, 1),
        add_cylinder("MITHAQ_Dossier_Seal_Disc_D", (0.55, -0.84, 0.204), 0.155, 0.018, GOLD, 32, 0.006),
        add_cylinder("MITHAQ_Dossier_Seal_Inner_D", (0.55, -0.84, 0.218), 0.095, 0.008, SHADOW, 28, 0.003),
        add_box("MITHAQ_Dossier_Seal_Line_A_D", (0.55, -0.84, 0.225), (0.145, 0.010, 0.006), GOLD, 0.001, 1),
        add_box("MITHAQ_Dossier_Seal_Line_B_D", (0.55, -0.79, 0.225), (0.095, 0.010, 0.006), GOLD, 0.001, 1),
        add_box("MITHAQ_Dossier_Seal_Line_C_D", (0.55, -0.89, 0.225), (0.095, 0.010, 0.006), GOLD, 0.001, 1),
    ]
    plate = join_as(plate_parts, "MITHAQ_Workshop_Dossier_Desktop_Brass_Details")

    for obj in (cover, paper, plate):
        obj["mithaq_variant"] = "desktop"
        obj["content_safety"] = "No real or invented workshop data; neutral marks only."

    return [cover, paper, plate]


def build_mobile_dossier():
    parts = [
        add_box("MITHAQ_Dossier_Mobile_Cover", (0, 0, 0.095), (2.05, 2.82, 0.075), COVER, 0.018, 1),
        add_box("MITHAQ_Dossier_Mobile_Back", (0, 0, 0.035), (2.08, 2.85, 0.044), COVER, 0.014, 1),
        add_box("MITHAQ_Dossier_Mobile_Spine", (-1.04, 0, 0.075), (0.110, 2.86, 0.120), COVER, 0.014, 1),
    ]
    cover = join_as(parts, "MITHAQ_Workshop_Dossier_Mobile_Cover")

    paper = add_box("MITHAQ_Workshop_Dossier_Mobile_Paper_Stack", (0.08, -0.02, 0.056), (1.82, 2.52, 0.050), PAPER, 0.006, 1)
    detail = join_as(
        [
            add_box("MITHAQ_Dossier_Mobile_Title_Plate", (0.04, 0.82, 0.143), (0.94, 0.24, 0.014), GOLD, 0.006, 1),
            add_cylinder("MITHAQ_Dossier_Mobile_Seal_Disc", (0.51, -0.78, 0.145), 0.110, 0.012, GOLD, 20, 0.003),
            add_box("MITHAQ_Dossier_Mobile_Neutral_Line", (0.02, 0.82, 0.153), (0.48, 0.009, 0.004), SHADOW, 0.001, 1),
        ],
        "MITHAQ_Workshop_Dossier_Mobile_Brass_Details",
    )

    for obj in (cover, paper, detail):
        obj.location.x += 3.2
        obj["mithaq_variant"] = "mobile"
        obj["content_safety"] = "No real or invented workshop data; neutral marks only."

    return [cover, paper, detail]


def count_stats(objects):
    depsgraph = bpy.context.evaluated_depsgraph_get()
    triangles = 0
    vertices = 0
    materials = set()
    mesh_count = 0
    for obj in objects:
        mesh_count += 1
        eval_obj = obj.evaluated_get(depsgraph)
        mesh = eval_obj.to_mesh()
        vertices += len(mesh.vertices)
        for poly in mesh.polygons:
            triangles += max(1, len(poly.vertices) - 2)
        eval_obj.to_mesh_clear()
        for slot in obj.material_slots:
            if slot.material:
                materials.add(slot.material.name)
    return {
        "triangles": triangles,
        "vertices": vertices,
        "meshes": mesh_count,
        "materials": len(materials),
        "materialNames": sorted(materials),
        "textures": 0,
    }


def setup_scene():
    bpy.context.scene.render.engine = "BLENDER_EEVEE"
    bpy.context.scene.eevee.taa_samples = 64
    bpy.context.scene.eevee.taa_render_samples = 64
    bpy.context.scene.view_settings.view_transform = "Filmic"
    bpy.context.scene.view_settings.look = "Medium High Contrast"
    bpy.context.scene.view_settings.exposure = -0.18
    bpy.context.scene.world = bpy.data.worlds.new("Mithaq_Dossier_Dark_World") if not bpy.context.scene.world else bpy.context.scene.world
    bpy.context.scene.world.color = (0.006, 0.005, 0.008)
    bpy.ops.object.light_add(type="AREA", location=(-2.8, -3.8, 4.0))
    key = bpy.context.object
    key.name = "MITHAQ_Dossier_Warm_Key_Light"
    key.data.energy = 470
    key.data.size = 4.5
    key.data.color = (1.0, 0.82, 0.58)
    bpy.ops.object.light_add(type="POINT", location=(2.4, 2.8, 1.8))
    rim = bpy.context.object
    rim.name = "MITHAQ_Dossier_Subtle_Gold_Rim_Light"
    rim.data.energy = 55
    rim.data.color = (1.0, 0.70, 0.38)


def add_camera(name, location, rotation, lens=70, ortho=False, ortho_scale=4.2):
    cam_data = bpy.data.cameras.new(f"{name}_Camera")
    cam = bpy.data.objects.new(f"{name}_Camera", cam_data)
    bpy.context.collection.objects.link(cam)
    cam.location = location
    cam.rotation_euler = rotation
    cam.data.lens = lens
    if ortho:
        cam.data.type = "ORTHO"
        cam.data.ortho_scale = ortho_scale
    return cam


def render(path, cam, objects=None, wireframe=False):
    bpy.context.scene.camera = cam
    bpy.context.scene.render.filepath = str(path)
    bpy.context.scene.render.resolution_x = 1400
    bpy.context.scene.render.resolution_y = 900
    hidden = []
    wire_objs = []
    if objects is not None:
        allowed = set(objects)
        for obj in bpy.context.scene.objects:
            if obj.type == "MESH" and obj not in allowed:
                obj.hide_render = True
                hidden.append(obj)
    if wireframe and objects:
        wire_mat = make_material("MITHAQ_Mat_Dossier_Wire_Gold", (0.86, 0.64, 0.25, 1), 0.5, 0.0)
        for obj in objects:
            dup = obj.copy()
            dup.data = obj.data.copy()
            dup.name = obj.name + "_WireframePreview"
            dup.data.materials.clear()
            dup.data.materials.append(wire_mat)
            bpy.context.collection.objects.link(dup)
            mod = dup.modifiers.new("Wireframe_Render_Modifier", "WIREFRAME")
            mod.thickness = 0.006
            mod.use_replace = False
            wire_objs.append(dup)
            obj.hide_render = True
            hidden.append(obj)
    bpy.ops.render.render(write_still=True)
    for obj in wire_objs:
        bpy.data.objects.remove(obj, do_unlink=True)
    for obj in hidden:
        obj.hide_render = False


def export_variant(path, objects, draco=False):
    bpy.ops.object.select_all(action="DESELECT")
    for obj in objects:
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


def validate_import(path):
    before = set(bpy.data.objects)
    bpy.ops.import_scene.gltf(filepath=str(path))
    imported = [obj for obj in bpy.data.objects if obj not in before]
    mesh_count = sum(1 for obj in imported if obj.type == "MESH")
    for obj in imported:
        bpy.data.objects.remove(obj, do_unlink=True)
    return mesh_count > 0


def write_metrics(rows):
    with open(REPORTS / "asset-metrics.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["Variant", "Triangles", "Vertices", "Meshes", "Materials", "GLB Size", "Texture Payload", "Draw Calls"],
        )
        writer.writeheader()
        writer.writerows(rows)


def main():
    clear_scene()
    atlas_bytes, atlas_note = copy_atlas()
    desktop_objects = build_desktop_dossier()
    mobile_objects = build_mobile_dossier()
    setup_scene()

    bpy.context.scene["Mithaq_P5_09_Notes"] = (
        "Workshop dossier asset set for Scene 06 only. Atmospheric 3D object; real workshop content must remain DOM/HTML."
    )
    bpy.context.scene["Content_Safety"] = "No real or invented workshop title, date, price, instructor, accreditation, or urgency is baked into the GLB."

    resting_cam = add_camera("Dossier_Resting", (2.55, -4.0, 2.25), (math.radians(61), 0, math.radians(33)), 72)
    hover_cam = add_camera("Dossier_Hover", (2.55, -4.0, 2.25), (math.radians(61), 0, math.radians(33)), 72)
    multi_cam = add_camera("Dossier_Multi", (3.8, -4.8, 3.2), (math.radians(60), 0, math.radians(39)), 60)
    mobile_cam = add_camera("Dossier_Mobile", (5.25, -3.5, 2.2), (math.radians(62), 0, math.radians(48)), 72)

    render(CAPTURES / "dossier-desktop-resting.png", resting_cam, desktop_objects)

    for obj in desktop_objects:
        obj.location.z += 0.045
        obj.rotation_euler.x = math.radians(1.6)
    render(CAPTURES / "dossier-desktop-hover.png", hover_cam, desktop_objects)
    for obj in desktop_objects:
        obj.location.z -= 0.045
        obj.rotation_euler.x = 0

    duplicates = []
    for idx, (x, y, rz) in enumerate([(-1.8, 0.35, -12), (0.0, 0.0, 0), (1.75, -0.32, 10)]):
        for obj in desktop_objects:
            dup = obj.copy()
            dup.data = obj.data
            dup.animation_data_clear()
            dup.name = f"{obj.name}_Instance_{idx+1}"
            dup.location.x += x
            dup.location.y += y
            dup.rotation_euler.z = math.radians(rz)
            dup["instancing_note"] = "Shared mesh data duplicate for validation; production should use instancing where practical."
            bpy.context.collection.objects.link(dup)
            duplicates.append(dup)
    render(CAPTURES / "dossier-multiple-layout.png", multi_cam, duplicates)
    for obj in duplicates:
        bpy.data.objects.remove(obj, do_unlink=True)

    render(CAPTURES / "dossier-mobile-light.png", mobile_cam, mobile_objects)
    render(CAPTURES / "dossier-wireframe-debug.png", resting_cam, desktop_objects, wireframe=True)

    desktop_stats = count_stats(desktop_objects)
    mobile_stats = count_stats(mobile_objects)

    bpy.ops.wm.save_as_mainfile(filepath=str(SOURCE / "workshop-dossier-master.blend"))

    export_variant(EXPORTS / "workshop-dossier.desktop.glb", desktop_objects, draco=False)
    export_variant(EXPORTS / "workshop-dossier.desktop.opt.glb", desktop_objects, draco=True)
    export_variant(EXPORTS / "workshop-dossier.mobile.glb", mobile_objects, draco=False)
    export_variant(EXPORTS / "workshop-dossier.mobile.opt.glb", mobile_objects, draco=True)

    desktop_raw = os.path.getsize(EXPORTS / "workshop-dossier.desktop.glb")
    desktop_opt = os.path.getsize(EXPORTS / "workshop-dossier.desktop.opt.glb")
    mobile_raw = os.path.getsize(EXPORTS / "workshop-dossier.mobile.glb")
    mobile_opt = os.path.getsize(EXPORTS / "workshop-dossier.mobile.opt.glb")

    desktop_reimport = validate_import(EXPORTS / "workshop-dossier.desktop.opt.glb")
    mobile_reimport = validate_import(EXPORTS / "workshop-dossier.mobile.opt.glb")

    inspect = {
        "asset": "Mithaq Workshop Dossier 3D Cards",
        "ticket": "P5.09",
        "blenderVersion": bpy.app.version_string,
        "optimizationMethod": "Blender GLTF exporter Draco compression fallback; gltfpack unavailable in execution shell.",
        "atlasBytes": atlas_bytes,
        "atlasNote": atlas_note,
        "desktop": {
            **desktop_stats,
            "rawGlbBytes": desktop_raw,
            "optimizedGlbBytes": desktop_opt,
            "optimizedReimportPass": desktop_reimport,
            "drawCallsExpected": desktop_stats["meshes"],
        },
        "mobile": {
            **mobile_stats,
            "rawGlbBytes": mobile_raw,
            "optimizedGlbBytes": mobile_opt,
            "optimizedReimportPass": mobile_reimport,
            "drawCallsExpected": mobile_stats["meshes"],
        },
        "contentSafety": "No real or invented workshop content included.",
        "conditions": [
            "gltfpack unavailable in execution shell; Blender Draco export used for optimized GLBs.",
            "Tiny geometric seal treatment is a restrained substitute pending final approved seal artwork/wordmark.",
            "Real-device validation remains pending because P5.08 mobile runtime failed hard floor.",
        ],
    }

    with open(REPORTS / "dossier-gltf-inspect.json", "w", encoding="utf-8") as f:
        json.dump(inspect, f, indent=2)

    write_metrics(
        [
            {
                "Variant": "Source Blend",
                "Triangles": desktop_stats["triangles"],
                "Vertices": desktop_stats["vertices"],
                "Meshes": desktop_stats["meshes"],
                "Materials": desktop_stats["materials"],
                "GLB Size": os.path.getsize(SOURCE / "workshop-dossier-master.blend"),
                "Texture Payload": atlas_bytes,
                "Draw Calls": desktop_stats["meshes"],
            },
            {
                "Variant": "Desktop Raw",
                "Triangles": desktop_stats["triangles"],
                "Vertices": desktop_stats["vertices"],
                "Meshes": desktop_stats["meshes"],
                "Materials": desktop_stats["materials"],
                "GLB Size": desktop_raw,
                "Texture Payload": atlas_bytes,
                "Draw Calls": desktop_stats["meshes"],
            },
            {
                "Variant": "Desktop Optimized",
                "Triangles": desktop_stats["triangles"],
                "Vertices": desktop_stats["vertices"],
                "Meshes": desktop_stats["meshes"],
                "Materials": desktop_stats["materials"],
                "GLB Size": desktop_opt,
                "Texture Payload": atlas_bytes,
                "Draw Calls": desktop_stats["meshes"],
            },
            {
                "Variant": "Mobile Raw",
                "Triangles": mobile_stats["triangles"],
                "Vertices": mobile_stats["vertices"],
                "Meshes": mobile_stats["meshes"],
                "Materials": mobile_stats["materials"],
                "GLB Size": mobile_raw,
                "Texture Payload": atlas_bytes,
                "Draw Calls": mobile_stats["meshes"],
            },
            {
                "Variant": "Mobile Optimized",
                "Triangles": mobile_stats["triangles"],
                "Vertices": mobile_stats["vertices"],
                "Meshes": mobile_stats["meshes"],
                "Materials": mobile_stats["materials"],
                "GLB Size": mobile_opt,
                "Texture Payload": atlas_bytes,
                "Draw Calls": mobile_stats["meshes"],
            },
        ]
    )

    print("MITHAQ_DOSSIER_INSPECT", json.dumps(inspect))


if __name__ == "__main__":
    main()

