# From a Single Neuron to a CNN: Neural Network Fundamentals with FashionMNIST

This project is a practical study of neural network fundamentals, starting from a single artificial neuron and progressing to a Convolutional Neural Network (CNN) using PyTorch and the FashionMNIST dataset.

## Part 1 - Neural Network Fundamentals

Topics covered:
- Artificial Neuron
- Perceptron
- AND gate
- XOR problem
- Activation Functions
- Loss Functions
- Gradient Descent
- Learning Rate
- Backpropagation
- Optimizers

## Part 2 - FashionMNIST with PyTorch

The implementation is completed in 12 steps:

1. **Download FashionMNIST and visualize images**
2. **Tensor, Dataset and DataLoader**
3. **Simple MLP with nn.Linear**
4. **Activation and Loss**
5. **Backpropagation with loss.backward()**
6. **Optimizers: SGD and Adam**
7. **Learning Rate experiments and Loss visualization**
8. **Validation Accuracy**
9. **Overfitting experiment**
10. **Reducing Overfitting with Dropout and weight_decay**
11. **Convert MLP to CNN with Conv2d and MaxPool**
12. **Compare final MLP and CNN accuracy**

## Technologies

- Python
- PyTorch
- TorchVision
- NumPy
- Matplotlib
- Jupyter Notebook

## Main File

MLP_Fadaei.ipynb

## Requirements

Required packages are listed in requirements.txt.

Install them with:

pip install -r requirements.txt

Then open MLP_Fadaei.ipynb in Jupyter Notebook and run the cells from top to bottom.

## Visualization

Plots are saved as PNG files next to the notebook, and the corresponding Markdown cells display the saved plots directly below the relevant code.

## Learning Goal

The main goal of this project is to understand neural network fundamentals and how weights, bias, loss, gradients, learning rate, backpropagation, optimization, overfitting, regularization and convolutional layers affect the learning process.
