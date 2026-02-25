# 🧠 Deep Gradient Dynamics Analysis
### Investigating Vanishing & Exploding Gradients in Deep MLPs

[![Python](https://img.shields.io/badge/Python-3.13+-blue.svg?style=for-the-badge&logo=python)](https://www.python.org/) 
[![NumPy](https://img.shields.io/badge/Implementation-Scratch-orange.svg?style=for-the-badge&logo=numpy)](https://numpy.org/) 
[![Status](https://img.shields.io/badge/Status-Research--In--Progress-green.svg?style=for-the-badge)]()

---

## 📝 Introduction
This repository contains an engineering-grade empirical analysis of **Gradient Flow** within deep neural architectures. The project focuses on the mathematical instability of gradients when scaling network depth, specifically comparing modern and classical optimization techniques.
> **Note:** This implementation is built **from scratch** (Pure NumPy) to ensure architectural transparency and precise tracking of backpropagation chain rules.

---

## 🏗 System Architecture
We utilize a **13-layer Dense Neural Network (MLP)**. This extreme depth is strategically chosen to observe the attenuation or explosion of gradients across the layers.

## 🧪 Experimental Methodology
We analyze the gradient norm $\|\nabla W\|_2$ across the following permutations:

### ⚡ Activation Functions
- **Sigmoid:** Testing the "Saturation Zone" effect.
- **ReLU:** Analyzing the "Dead ReLU" and gradient propagation efficiency.

### 🛠 Weight Initializations
- **Xavier (Glorot):** Mathematical balancing of variance in Sigmoid layers.
- **He Initialization:** Optimizing the scale for non-linear ReLU activations.


## 🧠 Dataset & Reference
This analysis uses the **Brain Stroke CT Dataset** from Kaggle:  
[Brain Stroke CT Dataset](https://www.kaggle.com/datasets/ozguraslank/brain-stroke-ct-dataset)
![Brain CT Sample](https://cdn1.imaios.com/i/images/3/3/2/2/472233-1-eng-GB/brain-ct-axial.jpg?q=75&w=1280&s=610e28a70373ba71785af4f421f287de)

<!-- ===== ML Dashboard Highlight Section ===== -->
<div style="margin:40px 0; text-align:center;">
    
   <a href="https://mlworks1.github.io/webproject.github.io/" target="_blank"
      style="
           display:inline-block;
           padding:18px 35px;
           font-size:22px;
           font-weight:bold;
           text-decoration:none;
           border-radius:12px;
           background:linear-gradient(135deg,#0f2027,#203a43,#2c5364);
           color:#ffffff;
           box-shadow:0 10px 25px rgba(0,0,0,0.35);
           transition:all 0.3s ease;
      "
      onmouseover="this.style.transform='scale(1.05)'; this.style.boxShadow='0 15px 35px rgba(0,0,0,0.5)';"
      onmouseout="this.style.transform='scale(1)'; this.style.boxShadow='0 10px 25px rgba(0,0,0,0.35)';">
      
      🚀 View Full ML Analysis Dashboard
      
   </a>

   <p style="margin-top:12px; font-size:15px; color:#555;">
       Interactive dashboard including full analysis, insights, and visual reports
   </p>

</div>
<!-- ========================================== --> 
