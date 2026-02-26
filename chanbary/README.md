<div align="center">

## 🚀 **View Full ML Analysis Dashboard**

👉 **[Click Here for Interactive Dashboard](https://mlworks1.github.io/webproject.github.io/)**

*Interactive insights, gradient histograms, and loss curves in real-time*

</div>

<div align="center">
  
# 🧠 **DEEP GRADIENT DYNAMICS**
### VANISHING & EXPLODING GRADIENT ANALYZER

[![Python](https://img.shields.io/badge/Python-3.13+-blue?style=for-the-badge&logo=python)](https://python.org)
[![NumPy](https://img.shields.io/badge/Implementation-Scratch-orange?style=for-the-badge&logo=numpy)](https://numpy.org)
[![Research](https://img.shields.io/badge/Status-Research--In--Progress-green?style=for-the-badge)]()

---

## 📝 Introduction

This repository contains an **engineering-grade empirical analysis** of Gradient Flow within deep neural architectures. The project focuses on the mathematical instability of gradients when scaling network depth.

> **Note:** This implementation is built **from scratch (Pure NumPy)** to ensure architectural transparency and precise tracking of backpropagation chain rules.

</div>

## 🏗 System Architecture
We utilize a **13-layer Dense Neural Network (MLP)** to observe:
- Gradient Attenuation
- Weight Magnitude Explosion  
- Layer-wise Activation Mean

## 🧪 Experimental Methodology
Analyzing the gradient norm ‖∇W‖₂ across:

| **Parameter** | **Comparison** |
|--------------|----------------|
| ⚡ Activation | Sigmoid (Saturation) vs ReLU (Efficiency) |
| 🛠 Initialization | Xavier (Glorot) vs He |

## 🧠 Dataset
This analysis uses the **Brain Stroke CT Dataset** from Kaggle to test real-world convergence.


