@echo off
echo 正在激活环境并开始训练 Fold 0...

:: 激活 Conda 环境（路径请确认与你本机一致）
call conda activate nnunet_env

:: 设置 nnUNet 环境变量
set nnUNet_raw=F:/Code/Research/-Pediatric-Tumors/nnUNet_raw
set nnUNet_preprocessed=F:/Code/Research/-Pediatric-Tumors/nnUNet_preprocessed
set nnUNet_results=F:/Code/Research/-Pediatric-Tumors/nnUNet_results

:: 启动训练 Fold 0
nnUNetv2_train Dataset999_BraTSPED 3d_fullres 0

pause
