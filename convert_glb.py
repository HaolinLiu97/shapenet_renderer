import os
import multiprocessing as mp

def convert_obj2glb(src_dir,dst_dir):
    os.system("obj2gltf -i %s -o %s"%(src_dir,dst_dir))
    return

shapenet_dataset="/data3/haolin/shapenetcore/03001627"

dst_dir="/data3/haolin/shapenetcore_glb/03001627"

model_list=os.listdir(shapenet_dataset)
model_list.sort()

pool=mp.Pool(processes=10)
for model in model_list:
    src_model_path=os.path.join(shapenet_dataset,model,"model.obj")
    dst_model_dir=os.path.join(dst_dir,model)
    if os.path.exists(dst_model_dir)==False:
        os.makedirs(dst_model_dir)
    dst_model_path=os.path.join(dst_dir,model,"model.glb")
    if os.path.isfile(dst_model_path):
        print("skipping ",dst_model_path)
        continue
    print("saving to ",dst_model_path)
    pool.apply_async(convert_obj2glb, args=(src_model_path,dst_model_path))
    #convert_obj2glb(src_model_path,dst_model_path)
pool.close()
pool.join()

