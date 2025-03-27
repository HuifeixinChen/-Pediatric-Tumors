以下是你项目的 `README.md` 最终整理版本，已做到：

- 去除所有复制提示与表情符号  
- 结构清晰，内容完整  
- 包含项目动机、模型说明、数据说明、环境配置、训练推理流程、可视化、引用与联系方式  

你可以直接复制粘贴此内容作为 `README.md` 文件内容：

---

```markdown
# nnUNet v2 for Pediatric Brain Tumor Segmentation

This repository implements a complete pipeline for pediatric brain tumor segmentation using nnU-Net v2 on the BraTS-PEDs 2024 dataset.

---

## Project Motivation

Pediatric brain tumor segmentation is a critical task in neuro-oncology. Due to the limited data availability and high anatomical variability in pediatric populations, it requires robust and adaptive models. This project leverages nnU-Net v2, a self-configuring deep learning framework, to tackle this challenge efficiently and reproducibly.

This repository includes a copy of the nnU-Net v2 codebase (original: https://github.com/MIC-DKFZ/nnUNet), which will be extended with custom modules and improvements tailored for pediatric tumor segmentation.

---

## Models Used

This project is built upon the official implementation of nnU-Net v2 (v2.2) developed by MIC-DKFZ. It automatically configures preprocessing, architecture, and training settings based on dataset properties.

### Key Model Features

- Architecture: 3D U-Net (full resolution)
- Trainer: nnUNetTrainer (default)
- Loss Function: Dice + Cross Entropy
- Data Augmentation: On-the-fly random spatial and intensity transformations
- Folds: 5-fold cross-validation

---

## Dataset

Due to licensing and size constraints, the BraTS-PEDs 2024 dataset is not included in this repository.

You can download the dataset from the official challenge website:  
https://www.synapse.org/#!Synapse:syn36637543/wiki/627069

After downloading, place the dataset in the following structure:

```
data/BraTS-PEDs2024_Training_small_set/
```

The dataset configuration (`dataset.json`) is defined accordingly.

---

## Environment Setup

We recommend using Conda for a clean Python environment:

```bash
conda create -n nnunetv2 python=3.10 -y
conda activate nnunetv2
pip install -e "git+https://github.com/MIC-DKFZ/nnUNet.git@v2.2#egg=nnunetv2"
pip install -r requirements.txt
```

---

## Project Structure

```
.
├── data/                             # Ignored raw and preprocessed data
├── dataset.json                      # Dataset configuration file
├── preprocess.py                     # Preprocessing script
├── generate_dataset_json.py          # For nnUNet format JSON generation
├── train_fold0.bat                   # Train Fold 0 (Windows script)
├── train_all_folds.bat               # Train all 5 folds
├── test.py                           # Inference on test set
├── visualise_prediction.py          # Overlay predictions on slices
├── Visualize each.py                # Slice-wise visualization
├── Visualize network.py             # Architecture structure viewer
├── Visualize mean.py                # Aggregated results plotting
├── .gitignore                        # Ignores large/raw data and cache files
└── README.md                         # This file
```

---

## Training

Run preprocessing first:

```bash
python preprocess.py
```

Train on a specific fold:

```bash
nnUNetv2_train 999 0
```

Train on all folds:

```bash
nnUNetv2_train 999 ALL
```

---

## Inference

Run prediction using a trained model:

```bash
nnUNetv2_predict -i <input_dir> -o <output_dir> -d 999 -f 0 -tr nnUNetTrainer
```

---

## Visualization

This project provides several custom visualization tools:

- `visualise_prediction.py` – Overlay prediction vs ground truth
- `Visualize each.py` – Slice-by-slice results
- `Visualize mean.py` – Aggregated score visualization
- `Visualize network.py` – Network architecture viewer

---

## Citation

If you use this project or nnUNet, please cite the following:

```bibtex
@article{Isensee2021nnUNet,
  title={nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation},
  author={Isensee, Fabian and Jaeger, Paul F and Kohl, Simon A A and Petersen, Jens and Maier-Hein, Klaus H},
  journal={Nature Methods},
  volume={18},
  pages={203--211},
  year={2021}
}
```

---

## Contact

Maintained by Huifeixin Chen.  
For questions or collaboration, please open an issue or pull request on GitHub.
