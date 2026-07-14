from pathlib import Path
import json
import bpy

ROOT = Path(r"D:\Clinets\MITHAQ\MITHAQ\mithaq-project-docs\mithaq-gavel-model-production")
VALIDATION = ROOT / "validation"
RAW = ROOT / "exports" / "gavel.raw.glb"
OPT = ROOT / "exports" / "gavel.opt.glb"
INSPECT = VALIDATION / "gavel-gltf-inspect.json"


def clear():
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()


def import_status(path):
    clear()
    try:
        bpy.ops.import_scene.gltf(filepath=str(path))
        meshes = [obj for obj in bpy.context.scene.objects if obj.type == "MESH"]
        materials = set()
        tris = 0
        depsgraph = bpy.context.evaluated_depsgraph_get()
        for obj in meshes:
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
            "mesh_count": len(meshes),
            "material_count": len(materials),
            "triangle_count": tris,
        }
    except Exception as exc:
        return {"status": "FAIL", "error": str(exc)}


with open(INSPECT, "r", encoding="utf-8") as f:
    data = json.load(f)

data["raw_import_test"] = import_status(RAW)
data["optimized_import_test"] = import_status(OPT)
data["validation_method"] = "Blender 5.1.2 background import_scene.gltf import test."

with open(INSPECT, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print("MITHAQ_GAVEL_IMPORT_VALIDATION", json.dumps({
    "raw": data["raw_import_test"],
    "optimized": data["optimized_import_test"],
}))
