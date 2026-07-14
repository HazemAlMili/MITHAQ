from pathlib import Path
import math

import bpy
from mathutils import Vector


ROOT = Path(r"D:\Clinets\MITHAQ\MITHAQ\mithaq-project-docs\mithaq-desk-environment-production")
SOURCE = ROOT / "source" / "desk.blend"
RENDERS = ROOT / "renders"


def look_at(obj, target):
    direction = Vector(target) - obj.location
    obj.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()


bpy.ops.wm.open_mainfile(filepath=str(SOURCE))

cam_data = bpy.data.cameras.new("Desk_Leather_Detail_Rerender_Camera")
cam = bpy.data.objects.new("Desk_Leather_Detail_Rerender_Camera", cam_data)
bpy.context.collection.objects.link(cam)
cam.location = (2.15, -2.30, 0.86)
look_at(cam, (0.95, -1.22, 0.16))
cam.data.lens = 82

bpy.context.scene.camera = cam
bpy.context.scene.render.filepath = str(RENDERS / "desk-preview-leather-pad-detail.png")
bpy.context.scene.render.resolution_x = 1400
bpy.context.scene.render.resolution_y = 900
bpy.context.scene.render.engine = "BLENDER_EEVEE"
bpy.context.scene.eevee.taa_render_samples = 64
bpy.context.scene.view_settings.view_transform = "Filmic"
bpy.context.scene.view_settings.look = "Medium High Contrast"
bpy.context.scene.view_settings.exposure = -0.10
bpy.context.scene.view_settings.gamma = 1.0

bpy.ops.render.render(write_still=True)
print("RERENDERED_DESK_LEATHER_DETAIL", RENDERS / "desk-preview-leather-pad-detail.png")
