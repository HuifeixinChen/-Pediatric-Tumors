# 🧠 nnUNet v2 for Pediatric Brain Tumor Segmentation

This repository implements a complete pipeline for pediatric brain tumor segmentation using **nnU-Net v2** on the **BraTS-PEDs 2024** dataset.

---

## 🔍 Project Motivation

Pediatric brain tumor segmentation is a critical task in neuro-oncology. Due to the limited data availability and high anatomical variability in pediatric populations, it requires robust and adaptive models. This project leverages **nnU-Net v2**, a self-configuring deep learning framework, to tackle this challenge efficiently and reproducibly.

---

## 🧠 Models Used

This project is built upon the official implementation of **nnU-Net v2 (v2.2)** developed by [MIC-DKFZ](https://github.com/MIC-DKFZ/nnUNet). It automatically configures preprocessing, architecture, and training settings based on dataset properties.

### ✅ Key Model Features:

- **Architecture**: 3D U-Net (full resolution)
- **Trainer**: `nnUNetTrainer` (default)
- **Loss Function**: Dice + Cross Entropy
- **Data Augmentation**: On-the-fly random spatial & intensity transformations
- **Folds**: 5-fold cross-validation

---

## 📂 Dataset

Due to licensing and size constraints, the **BraTS-PEDs 2024** dataset is **NOT included** in this repository.

You can download the dataset from the official challenge website:  
👉 [https://www.synapse.org/#!Synapse:syn36637543/wiki/627069](https://www.synapse.org/#!Synapse:syn36637543/wiki/627069)

After downloading, place the dataset in the following structure:

