from pathlib import Path
import json
import math
import os

import bpy
from mathutils import Vector


ROOT = Path(r"D:\Clinets\MITHAQ\MITHAQ\mithaq-project-docs\mithaq-seal-model-production")
SOURCE = ROOT / "source"
EXPORTS = ROOT / "exports"
RENDERS = ROOT / "renders"
REPORTS = ROOT / "reports"

for path in (SOURCE, EXPORTS, RENDERS, REPORTS):
    path.mkdir(parents=True, exist_ok=True)


def clear_scene():
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()


def make_material(name, base, roughness=0.45, metallic=0.9, noise=False):
    mat = bpy.data.materials.new(name)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        bsdf.inputs["Base Color"].default_value = base
        bsdf.inputs["Metallic"].default_value = metallic
        bsdf.inputs["Roughness"].default_value = roughness
        if noise:
            noise_node = mat.node_tree.nodes.new("ShaderNodeTexNoise")
            noise_node.inputs["Scale"].default_value = 42
            noise_node.inputs["Detail"].default_value = 9
            noise_node.inputs["Roughness"].default_value = 0.58
            bump = mat.node_tree.nodes.new("ShaderNodeBump")
            bump.inputs["Strength"].default_value = 0.018
            bump.inputs["Distance"].default_value = 0.045
            mat.node_tree.links.new(noise_node.outputs["Fac"], bump.inputs["Height"])
            mat.node_tree.links.new(bump.outputs["Normal"], bsdf.inputs["Normal"])
    return mat


BRASS = make_material("MITHAQ_Mat_Brass_Gold", (0.77, 0.52, 0.19, 1), 0.45, 0.92, True)
HIGHLIGHT = make_material("MITHAQ_Mat_Gold_Highlight", (0.91, 0.75, 0.42, 1), 0.38, 0.86, True)
BRONZE = make_material("MITHAQ_Mat_Dark_Bronze", (0.28, 0.17, 0.065, 1), 0.58, 0.82, True)
GROOVE = make_material("MITHAQ_Mat_Shadow_Groove", (0.10, 0.07, 0.035, 1), 0.68, 0.55, False)


def shade_uv_bevel(obj, bevel_width=0.015, bevel_segments=2):
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    if bevel_width:
        bevel = obj.modifiers.new(name="Controlled_Seal_Bevel", type="BEVEL")
        bevel.width = bevel_width
        bevel.segments = bevel_segments
        bevel.affect = "EDGES"
        obj.modifiers.new(name="Weighted_Normals", type="WEIGHTED_NORMAL")
        bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
        bpy.ops.object.modifier_apply(modifier="Controlled_Seal_Bevel")
        bpy.ops.object.modifier_apply(modifier="Weighted_Normals")
    try:
        bpy.ops.object.shade_smooth()
        bpy.ops.object.mode_set(mode="EDIT")
        bpy.ops.mesh.select_all(action="SELECT")
        bpy.ops.uv.smart_project(angle_limit=math.radians(68), island_margin=0.02)
        bpy.ops.object.mode_set(mode="OBJECT")
    except Exception:
        bpy.ops.object.mode_set(mode="OBJECT")
    obj.select_set(False)


def add_cylinder(name, radius, depth, vertices, z, mat, bevel=0.015):
    bpy.ops.mesh.primitive_cylinder_add(
        vertices=vertices,
        radius=radius,
        depth=depth,
        end_fill_type="NGON",
        location=(0, 0, z),
    )
    obj = bpy.context.object
    obj.name = name
    obj.data.name = name + "_Mesh"
    obj.data.materials.append(mat)
    shade_uv_bevel(obj, bevel, 2)
    return obj


def add_torus(name, major, minor, z, mat, segments=80, minor_segments=6):
    bpy.ops.mesh.primitive_torus_add(
        major_segments=segments,
        minor_segments=minor_segments,
        major_radius=major,
        minor_radius=minor,
        location=(0, 0, z),
    )
    obj = bpy.context.object
    obj.name = name
    obj.data.name = name + "_Mesh"
    obj.data.materials.append(mat)
    shade_uv_bevel(obj, 0, 0)
    return obj


def load_arabic_capable_font():
    candidates = [
        Path(r"C:\Windows\Fonts\tahoma.ttf"),
        Path(r"C:\Windows\Fonts\arial.ttf"),
        Path(r"C:\Windows\Fonts\segoeui.ttf"),
        Path(r"C:\Windows\Fonts\calibri.ttf"),
    ]
    for path in candidates:
        if path.exists():
            return bpy.data.fonts.load(str(path)), str(path)
    return None, "Blender default font"


def add_text_mesh():
    font, font_source = load_arabic_capable_font()
    bpy.ops.object.text_add(location=(0, -0.16, 0.255), rotation=(0, 0, 0))
    txt = bpy.context.object
    txt.name = "MITHAQ_Seal_Arabic_Text_Curve"
    txt.data.name = "MITHAQ_Seal_Arabic_Text_CurveData"
    # Blender text objects do not consistently shape Arabic in background export.
    # This uses presentation-form glyphs in visual order so the converted mesh reads as "ميثاق".
    txt.data.body = "\uFED5\uFE8E\uFE9C\uFEF4\uFEE3"
    txt.data.align_x = "CENTER"
    txt.data.align_y = "CENTER"
    txt.data.size = 0.62
    txt.data.extrude = 0.035
    txt.data.resolution_u = 3
    if font:
        txt.data.font = font
    txt.data.materials.append(HIGHLIGHT)
    bpy.context.view_layer.objects.active = txt
    txt.select_set(True)
    bpy.ops.object.convert(target="MESH")
    obj = bpy.context.object
    obj.name = "MITHAQ_Seal_Arabic_Text"
    obj.data.name = "MITHAQ_Seal_Arabic_Text_Mesh"
    shade_uv_bevel(obj, 0.002, 1)
    obj["font_source"] = font_source
    obj["legibility_note"] = "Arabic brand text target is ميثاق; stakeholder calligraphy review remains required."
    return obj, font_source


def add_abstract_scales():
    parts = []

    stem = add_cylinder("MITHAQ_Seal_Legal_Motif_Stem", 0.018, 0.58, 24, 0.255, HIGHLIGHT, 0.004)
    stem.rotation_euler[0] = math.radians(90)
    stem.location.y = 0.47
    stem.scale.x = 1.0
    parts.append(stem)

    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0.74, 0.282))
    beam = bpy.context.object
    beam.name = "MITHAQ_Seal_Legal_Motif_Balance_Beam"
    beam.data.name = "MITHAQ_Seal_Legal_Motif_Balance_Beam_Mesh"
    beam.dimensions = (0.92, 0.035, 0.026)
    beam.data.materials.append(HIGHLIGHT)
    shade_uv_bevel(beam, 0.01, 1)
    parts.append(beam)

    for side, x in (("Left", -0.34), ("Right", 0.34)):
        bpy.ops.mesh.primitive_cube_add(size=1, location=(x, 0.61, 0.281))
        hanger = bpy.context.object
        hanger.name = f"MITHAQ_Seal_Legal_Motif_{side}_Hanger"
        hanger.data.name = hanger.name + "_Mesh"
        hanger.dimensions = (0.018, 0.27, 0.018)
        hanger.data.materials.append(HIGHLIGHT)
        shade_uv_bevel(hanger, 0.004, 1)
        parts.append(hanger)

        bpy.ops.mesh.primitive_uv_sphere_add(segments=24, ring_count=6, radius=0.13, location=(x, 0.48, 0.272))
        pan = bpy.context.object
        pan.name = f"MITHAQ_Seal_Legal_Motif_{side}_Abstract_Pan"
        pan.data.name = pan.name + "_Mesh"
        pan.scale.z = 0.10
        pan.scale.y = 0.46
        pan.data.materials.append(BRASS)
        shade_uv_bevel(pan, 0.002, 1)
        parts.append(pan)

    for obj in parts:
        obj["motif_note"] = "Minimal abstract scales reference only; no state, court, government, eagle, flag, crown, sword, or crest symbolism."

    bpy.ops.object.select_all(action="DESELECT")
    bpy.context.view_layer.objects.active = stem
    for obj in parts:
        obj.select_set(True)
    bpy.ops.object.join()
    motif = bpy.context.object
    motif.name = "MITHAQ_Seal_Legal_Motif"
    motif.data.name = "MITHAQ_Seal_Legal_Motif_Mesh"
    motif["motif_note"] = "Minimal abstract scales reference only; no state, court, government, eagle, flag, crown, sword, or crest symbolism."
    return [motif]


def build_seal():
    objects = []
    objects.append(add_cylinder("MITHAQ_Seal_Back_Plate", 1.82, 0.16, 96, 0.0, BRONZE, 0.025))
    objects.append(add_cylinder("MITHAQ_Seal_Base", 1.72, 0.075, 96, 0.10, BRASS, 0.018))
    objects.append(add_torus("MITHAQ_Seal_Outer_Rim", 1.57, 0.105, 0.18, HIGHLIGHT, 96, 8))
    objects.append(add_torus("MITHAQ_Seal_Inner_Rim", 1.03, 0.038, 0.205, HIGHLIGHT, 80, 6))
    objects.append(add_torus("MITHAQ_Seal_Shadow_Groove_Outer", 1.30, 0.018, 0.202, GROOVE, 72, 5))
    objects.append(add_torus("MITHAQ_Seal_Shadow_Groove_Inner", 0.72, 0.014, 0.207, GROOVE, 72, 5))
    text, font_source = add_text_mesh()
    objects.append(text)
    objects.extend(add_abstract_scales())

    origin = bpy.data.objects.new("MITHAQ_Seal_Origin_Center", None)
    origin.empty_display_type = "PLAIN_AXES"
    origin.empty_display_size = 0.25
    origin.location = (0, 0, 0)
    bpy.context.collection.objects.link(origin)
    for obj in objects:
        obj.parent = origin

    bpy.context.scene["Mithaq_P5_03_Notes"] = (
        "Seal-led covenant object. Circular official seal with raised concentric rims, "
        "embossed Arabic brand text, and minimal abstract legal motif. Gavel remains trigger."
    )
    bpy.context.scene["Arabic_Font_Source"] = font_source
    bpy.context.scene["Arabic_Legibility_Status"] = (
        "Arabic text is geometry converted from system font. Final wordmark/calligraphy approval remains pending."
    )
    return objects, origin, font_source


def count_model_stats():
    depsgraph = bpy.context.evaluated_depsgraph_get()
    tris = 0
    mesh_count = 0
    materials = set()
    for obj in bpy.context.scene.objects:
        if obj.type == "MESH" and obj.name.startswith("MITHAQ_Seal_"):
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
    bpy.context.scene.world = bpy.data.worlds.new("Mithaq_Seal_Dark_World") if not bpy.context.scene.world else bpy.context.scene.world
    bpy.context.scene.world.color = (0.006, 0.005, 0.008)
    bpy.ops.object.light_add(type="AREA", location=(-3.4, -4.4, 4.5))
    key = bpy.context.object
    key.name = "Mithaq_Seal_Warm_Key_Light"
    key.data.energy = 560
    key.data.size = 4.4
    key.data.color = (1.0, 0.82, 0.56)
    bpy.ops.object.light_add(type="POINT", location=(3.2, 2.8, 2.2))
    rim = bpy.context.object
    rim.name = "Mithaq_Seal_Subtle_Rim_Light"
    rim.data.energy = 80
    rim.data.color = (1.0, 0.74, 0.38)


def setup_camera(name, location, rotation, focal=82, ortho=False, ortho_scale=4.6):
    cam_data = bpy.data.cameras.new(name + "_Camera")
    cam = bpy.data.objects.new(name + "_Camera", cam_data)
    bpy.context.collection.objects.link(cam)
    cam.location = location
    cam.rotation_euler = rotation
    cam.data.lens = focal
    if ortho:
        cam.data.type = "ORTHO"
        cam.data.ortho_scale = ortho_scale
    cam.data.dof.use_dof = False
    return cam


def render_preview(path, cam, wireframe=False):
    bpy.context.scene.camera = cam
    bpy.context.scene.render.filepath = str(path)
    bpy.context.scene.render.resolution_x = 1400
    bpy.context.scene.render.resolution_y = 1000
    bpy.context.scene.eevee.taa_render_samples = 64

    wire_objs = []
    if wireframe:
        wire_mat = make_material("MITHAQ_Mat_Wireframe_Gold", (0.88, 0.70, 0.30, 1), 0.4, 0.0, False)
        for obj in list(bpy.context.scene.objects):
            if obj.type == "MESH" and obj.name.startswith("MITHAQ_Seal_"):
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
        if obj.name.startswith("MITHAQ_Seal_") and obj.type == "MESH":
            obj.hide_render = False


def export_glb(path, draco=False):
    bpy.ops.object.select_all(action="DESELECT")
    for obj in bpy.context.scene.objects:
        if obj.name.startswith("MITHAQ_Seal_"):
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
    objects, origin, font_source = build_seal()
    setup_lighting()

    floor_mat = make_material("MITHAQ_Mat_Preview_Dark_Background", (0.010, 0.008, 0.014, 1), 0.92, 0.0, False)
    bpy.ops.mesh.primitive_plane_add(size=7, location=(0, 0, -0.10))
    floor = bpy.context.object
    floor.name = "Preview_Dark_Matte_Background"
    floor.data.materials.append(floor_mat)
    floor.hide_render = True
    floor.hide_viewport = True

    bpy.context.scene.render.engine = "BLENDER_EEVEE"
    bpy.context.scene.eevee.taa_samples = 64
    bpy.context.scene.view_settings.view_transform = "Filmic"
    bpy.context.scene.view_settings.look = "Medium High Contrast"
    bpy.context.scene.view_settings.exposure = -0.12
    bpy.context.scene.view_settings.gamma = 1.0

    cameras = {
        "front": setup_camera("Seal_Front", (0, -0.01, 6.2), (0, 0, 0), 80, True, 4.2),
        "perspective": setup_camera("Seal_Perspective", (3.0, -4.2, 3.2), (math.radians(57), 0, math.radians(36)), 82),
        "hero_dark": setup_camera("Seal_Hero_Dark", (2.1, -3.6, 2.45), (math.radians(58), 0, math.radians(28)), 92),
        "side_depth": setup_camera("Seal_Side_Depth", (4.5, -0.7, 0.72), (math.radians(82), 0, math.radians(81)), 105),
        "wireframe": setup_camera("Seal_Wireframe", (2.9, -4.1, 3.0), (math.radians(58), 0, math.radians(34)), 82),
    }

    render_preview(RENDERS / "seal-preview-front.png", cameras["front"])
    render_preview(RENDERS / "seal-preview-perspective.png", cameras["perspective"])
    render_preview(RENDERS / "seal-preview-hero-dark.png", cameras["hero_dark"])
    render_preview(RENDERS / "seal-preview-side-depth.png", cameras["side_depth"])
    render_preview(RENDERS / "seal-preview-wireframe.png", cameras["wireframe"], wireframe=True)

    stats = count_model_stats()
    stats.update(
        {
            "asset": "Mithaq Seal",
            "ticket": "P5.03",
            "blenderVersion": bpy.app.version_string,
            "arabicText": "ميثاق",
            "arabicFontSource": font_source,
            "arabicLegibility": "Present as converted mesh using Arabic presentation-form glyph workaround; needs stakeholder/logo/calligraphy review.",
            "optimizationMethod": "Blender GLTF exporter Draco compression fallback; gltfpack unavailable in execution shell.",
            "conditions": [
                "gltfpack unavailable in execution shell; Blender Draco compression used for seal.opt.glb.",
                "Arabic text uses presentation-form glyphs for Blender mesh legibility; final wordmark/calligraphy approval remains pending.",
                "Final stakeholder art approval, mobile LOD, R3F import validation, and real-device performance validation remain pending.",
            ],
        }
    )

    bpy.ops.wm.save_as_mainfile(filepath=str(SOURCE / "seal.blend"))
    export_glb(EXPORTS / "seal.raw.glb", draco=False)
    export_glb(EXPORTS / "seal.opt.glb", draco=True)

    stats["rawGlbBytes"] = os.path.getsize(EXPORTS / "seal.raw.glb")
    stats["optimizedGlbBytes"] = os.path.getsize(EXPORTS / "seal.opt.glb")
    stats["sourceBlendBytes"] = os.path.getsize(SOURCE / "seal.blend")
    stats["rawReimportPass"] = False
    stats["optimizedReimportPass"] = False

    with open(REPORTS / "seal-gltf-inspect.json", "w", encoding="utf-8") as f:
        json.dump(stats, f, indent=2, ensure_ascii=False)

    with open(REPORTS / "seal-file-size-log.md", "w", encoding="utf-8") as f:
        f.write(f"seal.raw.glb: {stats['rawGlbBytes']} bytes / {stats['rawGlbBytes'] / 1024 / 1024:.4f} MB\n")
        f.write(f"seal.opt.glb: {stats['optimizedGlbBytes']} bytes / {stats['optimizedGlbBytes'] / 1024 / 1024:.4f} MB\n")
        f.write("target: <= 1.2 MB\n")
        f.write(f"result: {'PASS' if stats['optimizedGlbBytes'] <= 1.2 * 1024 * 1024 else 'FAIL'}\n")

    print("MITHAQ_SEAL_STATS", json.dumps(stats, ensure_ascii=False))


if __name__ == "__main__":
    main()
