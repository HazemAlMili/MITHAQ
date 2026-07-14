from pathlib import Path
import json

import bpy


ROOT = Path(r"D:\Clinets\MITHAQ\MITHAQ\mithaq-project-docs\mithaq-desk-environment-production")
EXPORTS = ROOT / "exports"
REPORTS = ROOT / "reports"
INSPECT = REPORTS / "desk-gltf-inspect.json"


def clear_scene():
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()


def inspect_import(path):
    clear_scene()
    bpy.ops.import_scene.gltf(filepath=str(path))
    depsgraph = bpy.context.evaluated_depsgraph_get()
    tris = 0
    meshes = 0
    materials = set()
    for obj in bpy.context.scene.objects:
        if obj.type == "MESH":
            meshes += 1
            eval_obj = obj.evaluated_get(depsgraph)
            mesh = eval_obj.to_mesh()
            for poly in mesh.polygons:
                tris += max(1, len(poly.vertices) - 2)
            eval_obj.to_mesh_clear()
            for slot in obj.material_slots:
                if slot.material:
                    materials.add(slot.material.name)
    return {
        "status": "PASS",
        "path": str(path),
        "meshCount": meshes,
        "materialCount": len(materials),
        "triangleCount": tris,
    }


with open(INSPECT, "r", encoding="utf-8") as f:
    data = json.load(f)

raw = inspect_import(EXPORTS / "desk.raw.glb")
opt = inspect_import(EXPORTS / "desk.opt.glb")

data["rawReimportPass"] = raw["status"] == "PASS"
data["optimizedReimportPass"] = opt["status"] == "PASS"
data["rawImportTest"] = raw
data["optimizedImportTest"] = opt
data["validationMethod"] = f"Blender {bpy.app.version_string} background import_scene.gltf import test."

with open(INSPECT, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print("MITHAQ_DESK_IMPORT_VALIDATION", json.dumps({"raw": raw, "optimized": opt}))
