from pathlib import Path
import json
import math
import os

import bpy
from mathutils import Vector


ROOT = Path(r"D:\Clinets\MITHAQ\MITHAQ\mithaq-project-docs\mithaq-gavel-model-production")
SOURCE = ROOT / "source"
EXPORTS = ROOT / "exports"
PREVIEW = ROOT / "preview"
VALIDATION = ROOT / "validation"

for path in (SOURCE, EXPORTS, PREVIEW, VALIDATION):
    path.mkdir(parents=True, exist_ok=True)


def clear_scene():
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()


def make_material(name, base, roughness=0.75, metallic=0.0, noise=False):
    mat = bpy.data.materials.new(name)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        bsdf.inputs["Base Color"].default_value = base
        bsdf.inputs["Roughness"].default_value = roughness
        bsdf.inputs["Metallic"].default_value = metallic
        if noise:
            noise_node = mat.node_tree.nodes.new("ShaderNodeTexNoise")
            noise_node.inputs["Scale"].default_value = 22
            noise_node.inputs["Detail"].default_value = 11
            noise_node.inputs["Roughness"].default_value = 0.58
            bump = mat.node_tree.nodes.new("ShaderNodeBump")
            bump.inputs["Strength"].default_value = 0.045
            bump.inputs["Distance"].default_value = 0.055
            mat.node_tree.links.new(noise_node.outputs["Fac"], bump.inputs["Height"])
            mat.node_tree.links.new(bump.outputs["Normal"], bsdf.inputs["Normal"])
    return mat


WOOD = make_material("Mithaq_Dark_Wood", (0.105, 0.061, 0.034, 1), 0.78, 0.0, True)
DARK_WOOD = make_material("Mithaq_Dark_Wood_Darker_Endgrain", (0.055, 0.034, 0.024, 1), 0.86, 0.0, True)
BRASS = make_material("Mithaq_Muted_Brass", (0.62, 0.43, 0.17, 1), 0.35, 0.92, True)
EDGE = make_material("Mithaq_Edge_Wear_Optional", (0.78, 0.60, 0.31, 1), 0.48, 0.8, False)


def shade_and_uv(obj):
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    bpy.ops.object.shade_smooth()
    try:
        bpy.ops.object.mode_set(mode="EDIT")
        bpy.ops.mesh.select_all(action="SELECT")
        bpy.ops.uv.smart_project(angle_limit=math.radians(66), island_margin=0.025)
        bpy.ops.object.mode_set(mode="OBJECT")
    except Exception:
        bpy.ops.object.mode_set(mode="OBJECT")
    obj.select_set(False)


def add_cylinder(name, radius, depth, vertices, location, rotation, mat):
    bpy.ops.mesh.primitive_cylinder_add(
        vertices=vertices,
        radius=radius,
        depth=depth,
        end_fill_type="NGON",
        location=location,
        rotation=rotation,
    )
    obj = bpy.context.object
    obj.name = name
    obj.data.name = name + "_Mesh"
    obj.data.materials.append(mat)
    bevel = obj.modifiers.new(name="Controlled_Bevels", type="BEVEL")
    bevel.width = 0.035
    bevel.segments = 3
    bevel.affect = "EDGES"
    obj.modifiers.new(name="Weighted_Normals", type="WEIGHTED_NORMAL")
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    bpy.ops.object.modifier_apply(modifier="Controlled_Bevels")
    bpy.ops.object.modifier_apply(modifier="Weighted_Normals")
    obj.select_set(False)
    shade_and_uv(obj)
    return obj


def add_cone(name, r1, r2, depth, vertices, location, rotation, mat):
    bpy.ops.mesh.primitive_cone_add(
        vertices=vertices,
        radius1=r1,
        radius2=r2,
        depth=depth,
        end_fill_type="NGON",
        location=location,
        rotation=rotation,
    )
    obj = bpy.context.object
    obj.name = name
    obj.data.name = name + "_Mesh"
    obj.data.materials.append(mat)
    bevel = obj.modifiers.new(name="Small_Edge_Bevels", type="BEVEL")
    bevel.width = 0.018
    bevel.segments = 3
    obj.modifiers.new(name="Weighted_Normals", type="WEIGHTED_NORMAL")
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    bpy.ops.object.modifier_apply(modifier="Small_Edge_Bevels")
    bpy.ops.object.modifier_apply(modifier="Weighted_Normals")
    obj.select_set(False)
    shade_and_uv(obj)
    return obj


def add_torus(name, major, minor, location, rotation, mat):
    bpy.ops.mesh.primitive_torus_add(
        major_segments=72,
        minor_segments=8,
        major_radius=major,
        minor_radius=minor,
        location=location,
        rotation=rotation,
    )
    obj = bpy.context.object
    obj.name = name
    obj.data.name = name + "_Mesh"
    obj.data.materials.append(mat)
    obj.modifiers.new(name="Weighted_Normals", type="WEIGHTED_NORMAL")
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    bpy.ops.object.modifier_apply(modifier="Weighted_Normals")
    obj.select_set(False)
    shade_and_uv(obj)
    return obj


def add_knurled_grooves(parent_collection=None):
    grooves = []
    for x in (-0.54, 0.54):
        for offset in (-0.035, 0.035):
            obj = add_torus(
                f"Gavel_Subtle_Brass_Groove_{x:+.2f}_{offset:+.2f}",
                0.337,
                0.008,
                (x + offset, 0, 0),
                (0, math.radians(90), 0),
                EDGE,
            )
            grooves.append(obj)
    return grooves


def build_gavel():
    objects = []

    # Head along X axis, formal judicial proportions.
    head = add_cylinder("Gavel_Head", 0.34, 1.32, 80, (0, 0, 0), (0, math.radians(90), 0), WOOD)
    objects.append(head)

    left_face = add_cylinder("Gavel_Contact_Face_Left", 0.345, 0.105, 80, (-0.712, 0, 0), (0, math.radians(90), 0), DARK_WOOD)
    right_face = add_cylinder("Gavel_Contact_Face_Right", 0.345, 0.105, 80, (0.712, 0, 0), (0, math.radians(90), 0), DARK_WOOD)
    objects += [left_face, right_face]

    band_l = add_torus("Gavel_Brass_Band_Left", 0.348, 0.038, (-0.52, 0, 0), (0, math.radians(90), 0), BRASS)
    band_r = add_torus("Gavel_Brass_Band_Right", 0.348, 0.038, (0.52, 0, 0), (0, math.radians(90), 0), BRASS)
    objects += [band_l, band_r]
    objects += add_knurled_grooves()

    # Handle extends along negative Y with slight ceremonial taper.
    handle = add_cone("Gavel_Handle", 0.105, 0.165, 2.28, 64, (0, -1.21, -0.02), (math.radians(90), 0, 0), WOOD)
    objects.append(handle)

    collar = add_torus("Gavel_Brass_Collar", 0.19, 0.035, (0, -0.19, -0.02), (math.radians(90), 0, 0), BRASS)
    objects.append(collar)

    grip = add_cylinder("Gavel_Handle_End_Knob", 0.148, 0.18, 64, (0, -2.38, -0.02), (math.radians(90), 0, 0), DARK_WOOD)
    objects.append(grip)

    grip_band = add_torus("Gavel_Handle_Subtle_Brass_End_Band", 0.151, 0.014, (0, -2.27, -0.02), (math.radians(90), 0, 0), BRASS)
    objects.append(grip_band)

    # Contact marker is a small non-rendered empty at the striking face center.
    pivot = bpy.data.objects.new("Gavel_Pivot_Helper", None)
    pivot.empty_display_type = "PLAIN_AXES"
    pivot.empty_display_size = 0.22
    pivot.location = (0, -0.18, 0)
    bpy.context.collection.objects.link(pivot)

    contact = bpy.data.objects.new("Gavel_Contact_Point_Negative_X", None)
    contact.empty_display_type = "SPHERE"
    contact.empty_display_size = 0.08
    contact.location = (-0.78, 0, 0)
    bpy.context.collection.objects.link(contact)

    for obj in objects:
        obj.parent = pivot

    bpy.context.scene["Mithaq_P5_02_Notes"] = (
        "Premium judicial gavel. Pivot helper at handle/head joint for strike/descent. "
        "Contact point empty marks negative-X striking face. Seal remains hero."
    )
    return objects, pivot, contact


def count_model_stats():
    depsgraph = bpy.context.evaluated_depsgraph_get()
    tris = 0
    mesh_count = 0
    materials = set()
    textures = set()
    for obj in bpy.context.scene.objects:
        if obj.type == "MESH" and obj.name.startswith("Gavel_"):
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
        "triangle_count": tris,
        "mesh_count": mesh_count,
        "material_count": len(materials),
        "materials": sorted(materials),
        "texture_count": len(textures),
        "texture_dimensions": [],
        "uv_status": "Smart UV Project applied to visible mesh objects; procedural materials used.",
        "pivot_origin_note": "Gavel_Pivot_Helper at (0, -0.18, 0); Gavel_Contact_Point_Negative_X at (-0.78, 0, 0).",
    }


def setup_lighting():
    bpy.context.scene.world = bpy.data.worlds.new("Mithaq_Dark_World") if not bpy.context.scene.world else bpy.context.scene.world
    bpy.context.scene.world.color = (0.006, 0.005, 0.009)
    bpy.ops.object.light_add(type="AREA", location=(-3.8, -4.3, 4.6))
    key = bpy.context.object
    key.name = "Mithaq_Warm_Key_Light"
    key.data.energy = 520
    key.data.size = 4.0
    bpy.ops.object.light_add(type="POINT", location=(3.2, 2.8, 2.0))
    rim = bpy.context.object
    rim.name = "Mithaq_Subtle_Rim_Light"
    rim.data.energy = 55
    rim.data.color = (1.0, 0.78, 0.42)


def setup_camera(name, location, rotation, focal=70):
    cam_data = bpy.data.cameras.new(name + "_Camera")
    cam = bpy.data.objects.new(name + "_Camera", cam_data)
    bpy.context.collection.objects.link(cam)
    cam.location = location
    cam.rotation_euler = rotation
    cam.data.lens = focal
    cam.data.dof.use_dof = True
    cam.data.dof.focus_distance = 4.0
    cam.data.dof.aperture_fstop = 5.6
    return cam


def render_preview(path, cam, wireframe=False):
    bpy.context.scene.camera = cam
    bpy.context.scene.render.filepath = str(path)
    bpy.context.scene.render.resolution_x = 1400
    bpy.context.scene.render.resolution_y = 900
    bpy.context.scene.eevee.taa_render_samples = 64

    wire_objs = []
    if wireframe:
        wire_mat = make_material("Mithaq_Wireframe_Gold", (0.88, 0.67, 0.26, 1), 0.4, 0.0, False)
        for obj in list(bpy.context.scene.objects):
            if obj.type == "MESH" and obj.name.startswith("Gavel_"):
                dup = obj.copy()
                dup.data = obj.data.copy()
                dup.name = obj.name + "_WireframePreview"
                dup.data.materials.clear()
                dup.data.materials.append(wire_mat)
                bpy.context.collection.objects.link(dup)
                mod = dup.modifiers.new("Wireframe_Render_Modifier", "WIREFRAME")
                mod.thickness = 0.008
                mod.use_replace = False
                wire_objs.append(dup)
                obj.hide_render = True
    bpy.ops.render.render(write_still=True)

    for obj in wire_objs:
        bpy.data.objects.remove(obj, do_unlink=True)
    for obj in bpy.context.scene.objects:
        if obj.name.startswith("Gavel_") and obj.type == "MESH":
            obj.hide_render = False


def export_glb(path, draco=False):
    bpy.ops.object.select_all(action="DESELECT")
    for obj in bpy.context.scene.objects:
        if obj.name.startswith("Gavel_"):
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
    objects, pivot, contact = build_gavel()
    setup_lighting()

    # Add a dark matte floor for preview renders only; excluded from export by name.
    floor_mat = make_material("Mithaq_Preview_Dark_Background", (0.012, 0.010, 0.016, 1), 0.9, 0.0, False)
    bpy.ops.mesh.primitive_plane_add(size=7, location=(0, -0.55, -0.42))
    floor = bpy.context.object
    floor.name = "Preview_Dark_Matte_Ground"
    floor.data.materials.append(floor_mat)

    bpy.context.scene.render.engine = "BLENDER_EEVEE"
    bpy.context.scene.eevee.taa_samples = 64
    bpy.context.scene.view_settings.view_transform = "Filmic"
    bpy.context.scene.view_settings.look = "Medium High Contrast"
    bpy.context.scene.view_settings.exposure = -0.15
    bpy.context.scene.view_settings.gamma = 1.0

    stats = count_model_stats()
    stats["blender_version"] = bpy.app.version_string
    stats["source_file"] = str(SOURCE / "gavel.blend")
    stats["raw_glb"] = str(EXPORTS / "gavel.raw.glb")
    stats["optimized_glb"] = str(EXPORTS / "gavel.opt.glb")

    # Preview cameras.
    cameras = {
        "front": setup_camera("Front", (0, -4.3, 1.25), (math.radians(76), 0, 0), 82),
        "side": setup_camera("Side", (4.2, -0.9, 1.05), (math.radians(76), 0, math.radians(82)), 82),
        "perspective": setup_camera("Perspective", (3.1, -4.3, 2.25), (math.radians(64), 0, math.radians(37)), 70),
        "opening_angle": setup_camera("Opening_Angle", (-2.4, -3.2, 2.15), (math.radians(61), 0, math.radians(-32)), 78),
        "wireframe": setup_camera("Wireframe", (2.9, -3.9, 2.1), (math.radians(63), 0, math.radians(34)), 70),
    }

    render_preview(PREVIEW / "gavel-preview-front.png", cameras["front"])
    render_preview(PREVIEW / "gavel-preview-side.png", cameras["side"])
    render_preview(PREVIEW / "gavel-preview-perspective.png", cameras["perspective"])
    render_preview(PREVIEW / "gavel-preview-opening-angle.png", cameras["opening_angle"])
    render_preview(PREVIEW / "gavel-preview-wireframe.png", cameras["wireframe"], wireframe=True)

    # Hide preview-only floor before saving/exporting final source.
    floor.hide_viewport = True
    floor.hide_render = True

    bpy.ops.wm.save_as_mainfile(filepath=str(SOURCE / "gavel.blend"))
    export_glb(EXPORTS / "gavel.raw.glb", draco=False)

    # Real fallback optimization if gltfpack is unavailable: Blender Draco-compressed GLB.
    export_glb(EXPORTS / "gavel.opt.glb", draco=True)

    stats["raw_file_size_bytes"] = os.path.getsize(EXPORTS / "gavel.raw.glb")
    stats["optimized_file_size_bytes"] = os.path.getsize(EXPORTS / "gavel.opt.glb")
    stats["optimization_method"] = "Blender GLTF exporter Draco compression fallback; gltfpack unavailable in shell."
    stats["previews"] = [
        "gavel-preview-front.png",
        "gavel-preview-side.png",
        "gavel-preview-perspective.png",
        "gavel-preview-opening-angle.png",
        "gavel-preview-wireframe.png",
    ]

    with open(VALIDATION / "gavel-gltf-inspect.json", "w", encoding="utf-8") as f:
        json.dump(stats, f, indent=2)

    with open(VALIDATION / "gavel-file-size.txt", "w", encoding="utf-8") as f:
        f.write(f"raw_glb_bytes={stats['raw_file_size_bytes']}\n")
        f.write(f"optimized_glb_bytes={stats['optimized_file_size_bytes']}\n")
        f.write(f"optimized_glb_mb={stats['optimized_file_size_bytes'] / 1024 / 1024:.4f}\n")

    print("MITHAQ_GAVEL_STATS", json.dumps(stats))


if __name__ == "__main__":
    main()
