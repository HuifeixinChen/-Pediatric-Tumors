import os
import shutil

# 路径定义
pred_dir = r"F:\Code\Research\-Pediatric-Tumors\nnUNet_results\Dataset999_BraTSPED\nnUNetTrainer__nnUNetPlans__3d_fullres\fold_0\validation"
label_dir = r"F:\Code\Research\-Pediatric-Tumors\nnUNet_raw\Dataset999_BraTSPED\labelsTr"
out_dir = r"F:\Code\Research\-Pediatric-Tumors\labels_eval_subset"

# 创建输出文件夹
os.makedirs(out_dir, exist_ok=True)

# 匹配并复制标签文件
copied = 0
for pred_file in os.listdir(pred_dir):
    if pred_file.endswith(".nii.gz"):
        label_path = os.path.join(label_dir, pred_file)
        if os.path.exists(label_path):
            shutil.copy(label_path, os.path.join(out_dir, pred_file))
            copied += 1

print(f"共复制 {copied} 个匹配的标签文件到 labels_eval_subset")
