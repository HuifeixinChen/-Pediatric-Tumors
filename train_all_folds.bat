@echo off
echo 正在依次训练五折（Fold 0 到 Fold 4）...

call conda activate nnunet_env

set nnUNet_raw=F:/Code/Research/-Pediatric-Tumors/nnUNet_raw
set nnUNet_preprocessed=F:/Code/Research/-Pediatric-Tumors/nnUNet_preprocessed
set nnUNet_results=F:/Code/Research/-Pediatric-Tumors/nnUNet_results

nnUNetv2_train Dataset999_BraTSPED 3d_fullres 0
nnUNetv2_train Dataset999_BraTSPED 3d_fullres 1
nnUNetv2_train Dataset999_BraTSPED 3d_fullres 2
nnUNetv2_train Dataset999_BraTSPED 3d_fullres 3
nnUNetv2_train Dataset999_BraTSPED 3d_fullres 4

pause
