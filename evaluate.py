from nnunetv2.evaluation.evaluate_predictions import compute_metrics_on_folder2
from multiprocessing import freeze_support

if __name__ == "__main__":
    freeze_support()  # Windows 多进程评估必须加这句
    compute_metrics_on_folder2(
        "F:/Code/Research/-Pediatric-Tumors/labels_eval_subset",  # ground truth
        "F:/Code/Research/-Pediatric-Tumors/nnUNet_results/Dataset999_BraTSPED/nnUNetTrainer__nnUNetPlans__3d_fullres/fold_0/validation",  # prediction
        "F:/Code/Research/-Pediatric-Tumors/nnUNet_preprocessed/Dataset999_BraTSPED/dataset.json",  # dataset.json
        "F:/Code/Research/-Pediatric-Tumors/nnUNet_preprocessed/Dataset999_BraTSPED/nnUNetPlans.json",  # plan file
        "F:/Code/Research/-Pediatric-Tumors/fold0_metrics_output.json",  # output metrics
        8  # num processes
    )
