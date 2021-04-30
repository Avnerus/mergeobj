import sys
import bpy


if __name__ == "__main__":
    args = sys.argv[sys.argv.index('--'):]

    print("Loading Mesh A")
    bpy.ops.import_scene.obj(filepath=args[1])
    A = bpy.context.object

    print("Loading Mesh B")
    bpy.ops.import_scene.obj(filepath=args[2])
    B = bpy.context.object
    
    A.select_set(True)
    B.select_set(True)

    print("Combining")
    bpy.ops.object.join()

    C = bpy.context.object
    C.select_set(True)
    bpy.context.view_layer.objects.active = C

    bpy.ops.export_scene.obj(
        filepath=args[3],
        use_selection=True
    )

