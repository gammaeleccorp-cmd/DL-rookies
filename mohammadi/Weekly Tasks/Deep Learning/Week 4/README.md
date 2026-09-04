# Optimization Algorithms

To use the algorithms, ensure that **optimizer_benchmark.py** and the Python file used to run them are in the same project folder. I have already created **run.ipynb**.

Open run.ipynb and simply import the algorithms and plots:

```python
from optimizer_benchmark import Update_Parameter as up
from optimizer_benchmark import Plot
```

`Update_Parameter` provides the following methods:

```python
- gradient_descent(loss, gradient, x, y, lr=0.05, iterations=100)
- momentum(loss, gradient, x, y, lr=0.05, m_beta=0.9, iterations=100)
- adagrad(loss, gradient, x, y, lr=0.05, eps=1e-8, iterations=100)
- rmsprop(loss, gradient, x, y, lr=0.05, r_beta=0.9, eps=1e-8, iterations=100)
- adam(loss, gradient, x, y, lr=0.05, beta1=0.9, beta2=0.999, eps=1e-8, iterations=100)
- adamw(loss, gradient, x, y, lr=0.05, beta1=0.9, beta2=0.999, weight_decay=0.01, eps=1e-8, iterations=100)
- result(gradient_descent, momentum, adagrad, rmsprop, adam, adamw)
```

Here, `loss` and `gradient` are defined functions by user.                                
`result` shows the final x, y and loss for every optimizer.

Each algorithm returns lists of

```
- x and y
- loss
- gradient
- Effective learning rate (if the optimizer adapts it)
```

`Plot` has the following methods:

```python
- loss_vs_iter(losses, title='Loss vs Iteration')
- contour_plot(loss, X_list, Y_list, title="Optimizer Paths")
- gd_vs_adam(gradient_descent, adam, title="Gradient Descent vs Adam")
```

The required inputs are defined as follows:

`losses` = `[l_gd, l_m, l_ag, l_r, l_a, l_aw]`                                                  
`X_list` = `[x_gd, x_m, x_ag, x_r, x_a, x_aw]`                                      
`Y_list` = `[y_gd, y_m, y_ag, y_r, y_a, y_aw]`                                      

---
### Final optimizer conclusion:

Based on the loss plot and optimizer-path plot, Momentum was the best optimizer in this experiment.

It achieved the fastest convergence, reducing the loss from about 1340 to nearly 0 within roughly 60 iterations. Although its path shows large oscillations initially, these oscillations are gradually damped and the optimizer eventually reaches the minimum near (0,0).

The other optimizers were more stable initially, but they converged much more slowly. Gradient Descent also suffered from severe zigzagging and failed to make significant progress, while AdaGrad, RMSProp, Adam, and AdamW still had relatively high losses after 100 iterations.

Therefore, for these specific hyperparameters and this function:

Momentum gives the best speed/stability trade-off.

It is the best choice for this particular experiment, not necessarily for every deep-learning problem.
