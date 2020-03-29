# shapenet_renderer
Rendering script for shapenet object dataset using blender2.8

## Some preparation
Firstly, use obj2gltf to convert all your models in your shapenet dataset into .glb format. You can refer to the github page for [obj2gltf](https://github.com/CesiumGS/obj2gltf)
You can convert your model using the "convert_glb.py", in which you need to modify the variable 'shapenet_dataset', which contains a lot of obj models, and 'dst_dir', where you save your converted glb file.

## Render the model
You should install blender 2.8a. This script is tested on MacOS and Linux, and it should work on Windows.
Run the script by:
```python
blender --background get_pcd.blend -P render_rgb_depth.py
```
This script will render both RGB and Depth of the model.<br/>
Also remember to change 'shapenet_dir' and 'dst_dir' to where you save your glb model and where you want to save your results.<br/>
The results will be saved in OPEN_EXR format, you can also save it to png or jpg by modifying line 62 and line 63.
