from pathlib import Path
import json
import math
import os

import bpy


ROOT = Path(r"D:\Clinets\MITHAQ\MITHAQ\mithaq-project-docs\mithaq-desk-environment-production")
SOURCE = ROOT / "source"
EXPORTS = ROOT / "exports"
RENDERS = ROOT / "renders"
REPORTS = ROOT / "reports"

GAVEL_GLB = Path(r"D:\Clinets\MITHAQ\MITHAQ\mithaq-project-docs\mithaq-gavel-model-production\exports\gavel.opt.glb")
SEAL_GLB = Path(r"D:\Clinets\MITHAQ\MITHAQ\mithaq-project-docs\mithaq-seal-model-production\exports\seal.opt.glb")

for path in (SOURCE, EXPORTS, RENDERS, REPORTS):
    path.mkdir(parents=True, exist_ok=True)


def clear_scene():
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()


def make_material(name, base, roughness=0.8, metallic=0.0, bump=False, wave=False):
    mat = bpy.data.materials.new(name)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        bsdf.inputs["Base Color"].default_value = base
        bsdf.inputs["Roughness"].default_value = roughness
        bsdf.inputs["Metallic"].default_value = metallic
        if bump or wave:
            noise = mat.node_tree.nodes.new("ShaderNodeTexNoise")
            noise.inputs["Scale"].default_value = 34 if bump else 18
            noise.inputs["Detail"].default_value = 12
            noise.inputs["Roughness"].default_value = 0.62
            bump_node = mat.node_tree.nodes.new("ShaderNodeBump")
            bump_node.inputs["Strength"].default_value = 0.030 if bump else 0.018
            bump_node.inputs["Distance"].default_value = 0.055 if bump else 0.04
            mat.node_tree.links.new(noise.outputs["Fac"], bump_node.inputs["Height"])
            mat.node_tree.links.new(bump_node.outputs["Normal"], bsdf.inputs["Normal"])
    return mat


WOOD = make_material("MITHAQ_Mat_Dark_Wenge_Wood", (0.110, 0.080, 0.055, 1), 0.82, 0.0, True)
EDGE_WOOD = make_material("MITHAQ_Mat_Desk_Edge_Dark_Wood", (0.070, 0.050, 0.038, 1), 0.86, 0.0, True)
LEATHER = make_material("MITHAQ_Mat_Aged_Dark_Leather", (0.095, 0.055, 0.037, 1), 0.88, 0.0, True)
GROOVE = make_material("MITHAQ_Mat_Subtle_Groove_Shadow", (0.020, 0.016, 0.013, 1), 0.92, 0.0, False)


def shade_uv_bevel(obj, bevel_width=0.02, bevel_segments=2):
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    if bevel_width:
        bevel = obj.modifiers.new(name="Controlled_Premium_Bevel", type="BEVEL")
        bevel.width = bevel_width
        bevel.segments = bevel_segments
        bevel.affect = "EDGES"
        obj.modifiers.new(name="Weighted_Normals", type="WEIGHTED_NORMAL")
        bpy.ops.object.modifier_apply(modifier="Controlled_Premium_Bevel")
        bpy.ops.object.modifier_apply(modifier="Weighted_Normals")
    try:
        bpy.ops.object.shade_smooth()
        bpy.ops.object.mode_set(mode="EDIT")
        bpy.ops.mesh.select_all(action="SELECT")
        bpy.ops.uv.smart_project(angle_limit=math.radians(68), island_margin=0.025)
        bpy.ops.object.mode_set(mode="OBJECT")
    except Exception:
        bpy.ops.object.mode_set(mode="OBJECT")
    obj.select_set(False)


def add_box(name, location, dimensions, mat, bevel=0.02, segments=2):
    bpy.ops.mesh.primitive_cube_add(size=1, location=location)
    obj = bpy.context.object
    obj.name = name
    obj.data.name = name + "_Mesh"
    obj.dimensions = dimensions
    obj.data.materials.append(mat)
    shade_uv_bevel(obj, bevel, segments)
    return obj


def join_objects(objects, name):
    bpy.ops.object.select_all(action="DESELECT")
    bpy.context.view_layer.objects.active = objects[0]
    for obj in objects:
        obj.select_set(True)
    bpy.ops.object.join()
    obj = bpy.context.object
    obj.name = name
    obj.data.name = name + "_Mesh"
    return obj


def create_anchor(name, location):
    obj = bpy.data.objects.new(name, None)
    obj.empty_display_type = "PLAIN_AXES"
    obj.empty_display_size = 0.35
    obj.location = location
    bpy.context.collection.objects.link(obj)
    return obj


def build_desk():
    objects = []
    objects.append(add_box("MITHAQ_Desk_Surface", (0, 0, 0), (8.4, 5.2, 0.18), WOOD, 0.045, 2))
    objects.append(add_box("MITHAQ_Desk_Front_Edge", (0, -2.66, -0.02), (8.55, 0.24, 0.28), EDGE_WOOD, 0.04, 2))
    objects.append(add_box("MITHAQ_Desk_Side_Edge_Left", (-4.27, 0, -0.015), (0.23, 5.15, 0.24), EDGE_WOOD, 0.035, 2))
    objects.append(add_box("MITHAQ_Desk_Side_Edge_Right", (4.27, 0, -0.015), (0.23, 5.15, 0.24), EDGE_WOOD, 0.035, 2))

    leather = add_box("MITHAQ_Leather_Writing_Pad", (-0.55, -0.25, 0.125), (4.15, 2.58, 0.052), LEATHER, 0.055, 4)
    objects.append(leather)

    seam_parts = [
        add_box("MITHAQ_Leather_Pad_Groove_Top", (-0.55, 0.92, 0.158), (3.72, 0.032, 0.014), GROOVE, 0.006, 1),
        add_box("MITHAQ_Leather_Pad_Groove_Bottom", (-0.55, -1.42, 0.158), (3.72, 0.032, 0.014), GROOVE, 0.006, 1),
        add_box("MITHAQ_Leather_Pad_Groove_Left", (-2.43, -0.25, 0.158), (0.032, 2.18, 0.014), GROOVE, 0.006, 1),
        add_box("MITHAQ_Leather_Pad_Groove_Right", (1.33, -0.25, 0.158), (0.032, 2.18, 0.014), GROOVE, 0.006, 1),
    ]
    objects.append(join_objects(seam_parts, "MITHAQ_Leather_Pad_Subtle_Groove"))

    placement_parts = [
        add_box("MITHAQ_Placement_Dossier_Zone_A", (2.35, 0.88, 0.106), (1.28, 0.026, 0.010), GROOVE, 0.004, 1),
        add_box("MITHAQ_Placement_Dossier_Zone_B", (2.35, 0.54, 0.106), (1.28, 0.026, 0.010), GROOVE, 0.004, 1),
        add_box("MITHAQ_Placement_Dossier_Zone_C", (2.35, 0.20, 0.106), (1.28, 0.026, 0.010), GROOVE, 0.004, 1),
    ]
    placement = join_objects(placement_parts, "MITHAQ_Desk_Subtle_Placement_Zones")
    placement["note"] = "Low-relief placement cues only; no P5.05 document production."
    objects.append(placement)

    anchors = [
        create_anchor("MITHAQ_Anchor_Gavel_Strike", (-1.15, -0.30, 0.23)),
        create_anchor("MITHAQ_Anchor_Seal_Center", (0.28, -0.24, 0.25)),
        create_anchor("MITHAQ_Anchor_Camera_Hero", (2.4, -4.2, 2.25)),
    ]

    bpy.context.scene["Mithaq_P5_04_Notes"] = (
        "Dark premium legal desk environment. Desk remains the stage, not the hero. "
        "Gavel and Seal are separate assets; preview-only imports are not exported."
    )
    bpy.context.scene["Mithaq_Desk_Anchor_Notes"] = (
        "Gavel strike anchor: (-1.15, -0.30, 0.23). Seal center anchor: (0.28, -0.24, 0.25)."
    )
    return objects, anchors


def count_model_stats():
    depsgraph = bpy.context.evaluated_depsgraph_get()
    tris = 0
    mesh_count = 0
    materials = set()
    for obj in bpy.context.scene.objects:
        if obj.type == "MESH" and (obj.name.startswith("MITHAQ_Desk_") or obj.name.startswith("MITHAQ_Leather_")):
            mesh_count += 1
            eval_obj = obj.evaluated_get(depsgraph)
            mesh = eval_obj.to_mesh()
            for poly in mesh.polygons:
                tris += max(1, len(poly.vertices) - 2)
            eval_obj.to_mesh_clear()
            for slot in obj.material_slots:
                if slot.material:
                    materials.add(slot.material.name)
    return {
        "triangles": tris,
        "meshes": mesh_count,
        "materials": len(materials),
        "materialNames": sorted(materials),
        "textures": 0,
        "textureDimensions": [],
    }


def setup_lighting():
    bpy.context.scene.world = bpy.data.worlds.new("Mithaq_Desk_Dark_World") if not bpy.context.scene.world else bpy.context.scene.world
    bpy.context.scene.world.color = (0.006, 0.005, 0.008)
    bpy.ops.object.light_add(type="AREA", location=(-3.6, -4.4, 4.5))
    key = bpy.context.object
    key.name = "Mithaq_Desk_Warm_Key_Light"
    key.data.energy = 620
    key.data.size = 5.0
    key.data.color = (1.0, 0.82, 0.58)
    bpy.ops.object.light_add(type="POINT", location=(3.2, 2.6, 2.1))
    rim = bpy.context.object
    rim.name = "Mithaq_Desk_Subtle_Rim_Light"
    rim.data.energy = 65
    rim.data.color = (1.0, 0.72, 0.38)


def setup_camera(name, location, rotation, focal=70, ortho=False, ortho_scale=7.2):
    cam_data = bpy.data.cameras.new(name + "_Camera")
    cam = bpy.data.objects.new(name + "_Camera", cam_data)
    bpy.context.collection.objects.link(cam)
    cam.location = location
    cam.rotation_euler = rotation
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
            if obj.type == "MESH" and (obj.name.startswith("MITHAQ_Desk_") or obj.name.startswith("MITHAQ_Leather_")):
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

    bpy.ops.render.render(write_still=True)

    for obj in wire_objs:
        bpy.data.objects.remove(obj, do_unlink=True)
    for obj in bpy.context.scene.objects:
        if obj.name.startswith("MITHAQ_Desk_") or obj.name.startswith("MITHAQ_Leather_"):
            obj.hide_render = False


def import_preview_asset(path, prefix, location, scale, rotation=(0, 0, 0)):
    before = set(bpy.data.objects)
    bpy.ops.import_scene.gltf(filepath=str(path))
    imported = [obj for obj in bpy.data.objects if obj not in before]
    root = bpy.data.objects.new(prefix + "_Preview_Root", None)
    root.empty_display_type = "PLAIN_AXES"
    root.empty_display_size = 0.25
    root.location = location
    root.scale = (scale, scale, scale)
    root.rotation_euler = rotation
    bpy.context.collection.objects.link(root)
    for obj in imported:
        obj.name = prefix + "_Preview_" + obj.name
        obj.parent = root
        if obj.type == "MESH":
            obj["preview_only"] = "Imported for desk-preview-hero-gavel-seal-layout.png only; excluded from desk export."
    return [root] + imported


def remove_objects(objects):
    for obj in objects:
        if obj.name in bpy.data.objects:
            bpy.data.objects.remove(obj, do_unlink=True)


def export_glb(path, draco=False):
    bpy.ops.object.select_all(action="DESELECT")
    for obj in bpy.context.scene.objects:
        if obj.type == "MESH" and (obj.name.startswith("MITHAQ_Desk_") or obj.name.startswith("MITHAQ_Leather_")):
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
    build_desk()
    setup_lighting()

    bpy.context.scene.render.engine = "BLENDER_EEVEE"
    bpy.context.scene.eevee.taa_samples = 64
    bpy.context.scene.view_settings.view_transform = "Filmic"
    bpy.context.scene.view_settings.look = "Medium High Contrast"
    bpy.context.scene.view_settings.exposure = -0.18
    bpy.context.scene.view_settings.gamma = 1.0

    cameras = {
        "top": setup_camera("Desk_Top", (0, 0, 7.2), (0, 0, 0), 70, True, 7.2),
        "perspective": setup_camera("Desk_Perspective", (4.0, -5.0, 2.8), (math.radians(62), 0, math.radians(39)), 64),
        "hero": setup_camera("Desk_Hero_Gavel_Seal", (3.1, -4.9, 2.55), (math.radians(61), 0, math.radians(34)), 72),
        "leather": setup_camera("Desk_Leather_Detail", (1.3, -2.65, 1.05), (math.radians(67), 0, math.radians(22)), 95),
        "wireframe": setup_camera("Desk_Wireframe", (4.0, -5.0, 2.8), (math.radians(62), 0, math.radians(39)), 64),
    }

    render_preview(RENDERS / "desk-preview-top.png", cameras["top"])
    render_preview(RENDERS / "desk-preview-perspective.png", cameras["perspective"])
    render_preview(RENDERS / "desk-preview-leather-pad-detail.png", cameras["leather"])
    render_preview(RENDERS / "desk-preview-wireframe.png", cameras["wireframe"], wireframe=True)

    preview_objects = []
    if GAVEL_GLB.exists():
        preview_objects.extend(import_preview_asset(GAVEL_GLB, "Gavel", (-1.18, -0.40, 0.34), 0.74, (0, 0, math.radians(-16))))
    if SEAL_GLB.exists():
        preview_objects.extend(import_preview_asset(SEAL_GLB, "Seal", (0.58, -0.12, 0.39), 0.46, (0, 0, math.radians(0))))
    render_preview(RENDERS / "desk-preview-hero-gavel-seal-layout.png", cameras["hero"])
    remove_objects(preview_objects)

    stats = count_model_stats()
    stats.update(
        {
            "asset": "Mithaq Legal Desk Environment",
            "ticket": "P5.04",
            "blenderVersion": bpy.app.version_string,
            "optimizationMethod": "Blender GLTF exporter Draco compression fallback; gltfpack unavailable in execution shell.",
            "anchors": {
                "MITHAQ_Anchor_Gavel_Strike": [-1.15, -0.30, 0.23],
                "MITHAQ_Anchor_Seal_Center": [0.28, -0.24, 0.25],
                "MITHAQ_Anchor_Camera_Hero": [2.4, -4.2, 2.25],
            },
            "conditions": [
                "gltfpack unavailable in execution shell; Blender Draco compression used for desk.opt.glb.",
                "Final material/art approval, KTX2 conversion, mobile LOD, R3F import validation, ripple shader validation, and real-device performance validation remain pending.",
                "Gavel and Seal were imported for one preview render only and are not baked into desk.raw.glb or desk.opt.glb.",
            ],
        }
    )

    bpy.ops.wm.save_as_mainfile(filepath=str(SOURCE / "desk.blend"))
    export_glb(EXPORTS / "desk.raw.glb", draco=False)
    export_glb(EXPORTS / "desk.opt.glb", draco=True)

    stats["rawGlbBytes"] = os.path.getsize(EXPORTS / "desk.raw.glb")
    stats["optimizedGlbBytes"] = os.path.getsize(EXPORTS / "desk.opt.glb")
    stats["sourceBlendBytes"] = os.path.getsize(SOURCE / "desk.blend")
    stats["rawReimportPass"] = False
    stats["optimizedReimportPass"] = False

    with open(REPORTS / "desk-gltf-inspect.json", "w", encoding="utf-8") as f:
        json.dump(stats, f, indent=2)

    with open(REPORTS / "desk-file-size-log.md", "w", encoding="utf-8") as f:
        f.write(f"desk.raw.glb: {stats['rawGlbBytes']} bytes / {stats['rawGlbBytes'] / 1024 / 1024:.4f} MB\n")
        f.write(f"desk.opt.glb: {stats['optimizedGlbBytes']} bytes / {stats['optimizedGlbBytes'] / 1024 / 1024:.4f} MB\n")
        f.write("target: <= 1.2 MB\n")
        f.write(f"result: {'PASS' if stats['optimizedGlbBytes'] <= 1.2 * 1024 * 1024 else 'FAIL'}\n")

    print("MITHAQ_DESK_STATS", json.dumps(stats))


if __name__ == "__main__":
    main()
