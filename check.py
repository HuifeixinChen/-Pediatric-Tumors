import os

imagesTr_dir = r"F:\Code\Research\-Pediatric-Tumors\nnUNet_raw\Dataset999_BraTSPED\imagesTr"
labelsTr_dir = r"F:\Code\Research\-Pediatric-Tumors\nnUNet_raw\Dataset999_BraTSPED\labelsTr"

case_ids = [f.replace("_0000.nii.gz", "") for f in os.listdir(imagesTr_dir) if f.endswith("_0000.nii.gz")]
missing_cases = []

for cid in case_ids:
    complete = True
    for i in range(4):
        img_path = os.path.join(imagesTr_dir, f"{cid}_000{i}.nii.gz")
        if not os.path.exists(img_path):
            print(f"{cid} 缺少模态 _000{i}")
            complete = False
    label_path = os.path.join(labelsTr_dir, f"{cid}.nii.gz")
    if not os.path.exists(label_path):
        print(f"{cid} 缺少标签")
        complete = False
    if not complete:
        missing_cases.append(cid)

print(f"\n共发现不完整样本数量: {len(missing_cases)}")
print("不完整样本列表：")
for cid in missing_cases:
    print(cid)

print(f"\nnumTraining 应为: {len(case_ids) - len(missing_cases)}")
