from nnunetv2.dataset_conversion.generate_dataset_json import generate_dataset_json

output_folder = "F:/Code/Research/-Pediatric-Tumors/nnUNet_raw/Dataset999_BraTSPED"

generate_dataset_json(
    output_folder=output_folder,
    channel_names={
        0: "T1CE",
        1: "T1N",
        2: "T2F",
        3: "T2W"
    },
    labels={
        "background": 0,
        "ET": 1,
        "NET": 2,
        "CC": 3,
        "ED": 4
    },
    num_training_cases=155,  # 替换为实际完整数量（运行脚本①得到）
    file_ending=".nii.gz",
    dataset_name="BraTSPED",
    description="Pediatric brain tumor segmentation with 4 MRI modalities.",
    license="CC-BY-SA 4.0",
    converted_by="Your Name"
)
