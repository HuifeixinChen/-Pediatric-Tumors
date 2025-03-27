import nibabel as nib
import matplotlib.pyplot as plt

img_path = 'F:\Code\Research\-Pediatric-Tumors\Data\BraTS-PEDs2024_Training_small_set\BraTS-PED-00002-000\BraTS-PED-00002-000-t2w.nii.gz'
img = nib.load(img_path)
data = img.get_fdata()

slice_index = data.shape[2] // 2  # 取中间切片
plt.imshow(data[:, :, slice_index], cmap='gray')
plt.title('Middle slice of T1 MRI')
plt.show()
