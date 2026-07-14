from pathlib import Path
import json

import bpy


ROOT = Path(r"D:\Clinets\MITHAQ\MITHAQ\mithaq-project-docs\mithaq-floating-documents-production")
EXPORTS = ROOT / "exports"
REPORTS = ROOT / "reports"
INSPECT = REPORTS / "documents-gltf-inspect.json"

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


def base_name(name):
    for doc_name in DOC_NAMES:
        if name.startswith(doc_name):
            return doc_name
    return name


def inspect_import(path):
    clear_scene()
    bpy.ops.import_scene.gltf(filepath=str(path))
    depsgraph = bpy.context.evaluated_depsgraph_get()
    tris_total = 0
    meshes = 0
    materials = set()
    triangles_per = {name: 0 for name in DOC_NAMES}
    found_docs = set()
    for obj in bpy.context.scene.objects:
        if obj.type == "MESH" and obj.name.startswith("MITHAQ_Doc_"):
            meshes += 1
            doc_name = base_name(obj.name)
            found_docs.add(doc_name)
            eval_obj = obj.evaluated_get(depsgraph)
            mesh = eval_obj.to_mesh()
            tris = 0
            for poly in mesh.polygons:
                tris += max(1, len(poly.vertices) - 2)
            eval_obj.to_mesh_clear()
            triangles_per[doc_name] += tris
            tris_total += tris
            for slot in obj.material_slots:
                if slot.material:
                    materials.add(slot.material.name)
    return {
        "status": "PASS",
        "path": str(path),
        "meshCount": meshes,
        "materialCount": len(materials),
        "totalTriangles": tris_total,
        "trianglesPerDocument": triangles_per,
        "documentCount": len(found_docs),
        "foundDocuments": sorted(found_docs),
    }


with open(INSPECT, "r", encoding="utf-8") as f:
    data = json.load(f)

raw = inspect_import(EXPORTS / "documents.raw.glb")
opt = inspect_import(EXPORTS / "documents.opt.glb")

data["rawReimportPass"] = raw["status"] == "PASS" and raw["documentCount"] == 8
data["optimizedReimportPass"] = opt["status"] == "PASS" and opt["documentCount"] == 8
data["rawImportTest"] = raw
data["optimizedImportTest"] = opt
data["validationMethod"] = f"Blender {bpy.app.version_string} background import_scene.gltf import test."

with open(INSPECT, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print("MITHAQ_DOCUMENTS_IMPORT_VALIDATION", json.dumps({"raw": raw, "optimized": opt}))
