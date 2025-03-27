import os, shutil

source_root = r"F:\Code\Research\-Pediatric-Tumors\Data\BraTS-PEDs2024_Training_small_set"
task_dir = r"F:\Code\Research\-Pediatric-Tumors\nnUNet_raw\Dataset999_BraTSPED"
imagesTr = os.path.join(task_dir, "imagesTr")
labelsTr = os.path.join(task_dir, "labelsTr")

os.makedirs(imagesTr, exist_ok=True)
os.makedirs(labelsTr, exist_ok=True)

modal_map = {
    "-t1c.nii.gz": "_0000.nii.gz",
    "-t1n.nii.gz": "_0001.nii.gz",
    "-t2f.nii.gz": "_0002.nii.gz",
    "-t2w.nii.gz": "_0003.nii.gz",
}

for case_folder in os.listdir(source_root):
    case_path = os.path.join(source_root, case_folder)
    if not os.path.isdir(case_path): continue
    for file in os.listdir(case_path):
        fpath = os.path.join(case_path, file)
        if file.endswith("-seg.nii.gz"):
            target = os.path.join(labelsTr, case_folder + ".nii.gz")
            shutil.copyfile(fpath, target)
        else:
            for suffix, nnUNet_suffix in modal_map.items():
                if file.endswith(suffix):
                    target = os.path.join(imagesTr, case_folder + nnUNet_suffix)
                    shutil.copyfile(fpath, target)
