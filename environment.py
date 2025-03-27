import os

pred_dir = r"F:/Code/Research/-Pediatric-Tumors/nnUNet_results/Dataset999_BraTSPED/nnUNetTrainer__nnUNetPlans__3d_fullres/fold_0/validation"
label_dir = r"F:/Code/Research/-Pediatric-Tumors/labels_eval_subset"

pred_files = set(f for f in os.listdir(pred_dir) if f.endswith(".nii.gz"))
label_files = set(f for f in os.listdir(label_dir) if f.endswith(".nii.gz"))

missing_labels = pred_files - label_files
missing_predictions = label_files - pred_files

print("预测中这些文件在标签中没有对应：")
for f in missing_labels:
    print(f)

print("\n 标签中这些文件在预测中没有对应：")
for f in missing_predictions:
    print(f)

print(f"\n完全匹配文件数：{len(pred_files & label_files)}")
