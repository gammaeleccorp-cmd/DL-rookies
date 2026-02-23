<section style="padding:40px; background:#111; color:#fff; text-align:center;">
  <h1 style="font-size:36px; margin-bottom:20px;">
    🚀 Project Progress Update
  </h1>
  <p style="font-size:22px; font-weight:bold;">
    I've built the usurped candle model up to this point.
  </p>
  <p style="font-size:18px; margin-top:15px; opacity:0.8;">
    In the next update, we’ll move on to a more in-depth analysis and evaluation.
  </p>
</section>

<div align="center">

# 🧠 Deep Gradient Dynamics Analysis
### Investigating Vanishing & Exploding Gradients in Deep MLPs

[![Python](https://img.shields.io/badge/Python-3.13+-blue.svg?style=for-the-badge&logo=python)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/Implementation-Scratch-orange.svg?style=for-the-badge&logo=numpy)](https://numpy.org/)
[![Status](https://img.shields.io/badge/Status-Research--In--Progress-green.svg?style=for-the-badge)]()

</div>

---

## 📝 Introduction
This repository contains an engineering-grade empirical analysis of **Gradient Flow** within deep neural architectures. The project focuses on the mathematical instability of gradients when scaling network depth, specifically comparing modern and classical optimization techniques.

> **Note:** This implementation is built **from scratch** (Pure NumPy) to ensure architectural transparency and precise tracking of backpropagation chain rules.

---

## 🏗 System Architecture
We utilize a **13-layer Dense Neural Network (MLP)**. This extreme depth is strategically chosen to observe the attenuation or explosion of gradients across the layers.

### 📊 Layer Specifications
<table align="center">
  <thead>
    <tr>
      <th>Layer Index</th>
      <th>Type</th>
      <th>Input</th>
      <th>Output</th>
      <th>Total Parameters</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><b>L1</b></td><td>Dense (Input)</td><td>150,528</td><td>512</td><td>77,070,848</td></tr>
    <tr><td><b>L2-L3</b></td><td>Dense (Hidden)</td><td>512</td><td>256</td><td>393,984</td></tr>
    <tr><td><b>L4-L6</b></td><td>Dense (Hidden)</td><td>256</td><td>128</td><td>115,200</td></tr>
    <tr><td><b>L7-L9</b></td><td>Dense (Hidden)</td><td>128</td><td>32</td><td>26,896</td></tr>
    <tr><td><b>L10-L12</b></td><td>Dense (Hidden)</td><td>32</td><td>16</td><td>1,856</td></tr>
    <tr><td><b>L13</b></td><td>Dense (Output)</td><td>16</td><td>3</td><td>51</td></tr>
  </tbody>
</table>

---

## 🧪 Experimental Methodology
We analyze the gradient norm $\|\nabla W\|_2$ across the following permutations:

### ⚡ Activation Functions
* **Sigmoid:** Testing the "Saturation Zone" effect.
* **ReLU:** Analyzing the "Dead ReLU" and gradient propagation efficiency.

### 🛠 Weight Initializations
* **Xavier (Glorot):** Mathematical balancing of variance in Sigmoid layers.
* **He Initialization:** Optimizing the scale for non-linear ReLU activations.



---

## 🚀 Key Insights & Metrics
In this project, we track:
1.  **Gradient Norm per Layer:** How the magnitude of $\frac{\partial L}{\partial W^{(l)}}$ changes as it travels from $L_{13}$ to $L_1$.
2.  **Weight Distribution:** Monitoring the standard deviation of weights during training.
3.  **Future Roadmap:**
    * [x] MLP Implementation
    * [ ] CNN Architecture Suppor
