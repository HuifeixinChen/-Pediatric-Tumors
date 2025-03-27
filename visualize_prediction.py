import nibabel as nib
import matplotlib.pyplot as plt
import numpy as np

pred_file = "F:/Code/Research/-Pediatric-Tumors/nnUNet_results/Dataset999_BraTSPED/nnUNetTrainer__nnUNetPlans__3d_fullres/fold_0/validation/BraTS-PED-00028-000.nii.gz"
label_file = "F:/Code/Research/-Pediatric-Tumors/nnUNet_raw/Dataset999_BraTSPED/labelsTr/BraTS-PED-00028-000.nii.gz"

pred = nib.load(pred_file).get_fdata()
label = nib.load(label_file).get_fdata()

slice_id = pred.shape[2] // 2

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(label[:, :, slice_id], cmap='jet')
plt.title("Ground Truth")
plt.subplot(1, 2, 2)
plt.imshow(pred[:, :, slice_id], cmap='jet')
plt.title("Prediction")
plt.tight_layout()
plt.show()
