We Ran the optimization algorithms with these hyperparameters:

```python
lr = 0.05
momentum_beta = 0.9
rmsprop_beta = 0.9
adam_beta1 = 0.9
adam_beta2 = 0.999
epsilon = 1e-8
weight_decay = 0.01
```

With the Loss Function

$$ f(x,y)=x^2+20y^2 $$

Starting point

$$x, y = (8.0, 8.0)$$

And the Gradient

$$∇f(x, y) = [2x, 40y]$$

Now answer the questions:

### 1. Why does Gradient Descent zigzag on this function?

The function has very different curvature in the two directions:

The $y$-gradient is $20×$ more sensitive than the $x$-gradient.

With

$$ \eta=0.05$$

Gradient Descent updates each parameter as

$$ x_{t+1}=x_t-0.05(2x_t)=0.9x_t $$

and

$$ y_{t+1}=y_t-0.05(40y_t)=-y_t. $$

So starting from $y=8$:

iteration 0:  $y =  8$                            
iteration 1:  $y = -8$                               
iteration 2:  $y =  8$                           
iteration 3:  $y = -8$                      
...

The optimizer overshoots the minimum in the $y$-direction every single time.

But $x$ decreases gradually:

$x = 8$                       
$x = 7.2$                          
$x = 6.48$                         
$x = 5.832$                      
...

### 2. How does Momentum reduce this issue?

Momentum keeps a running velocity that remembers previous gradients then updates parameters using that.

Because successive gradients point in opposite directions, the momentum term prevents the optimizer from making such movements.

With momentum, oscillations are reduced, and convergence becomes much faster.

### 3. What does AdaGrad keep separately for each parameter, and why can it become too slow later in training?

AdaGrad keeps a separate accumulated squared-gradient value for each parameter and updates each parameter using its own accumulated value.

So it keeps a different learning rate adjustment for each parameter.

For the function, the $y$-gradient is much larger than the $x$-gradient. Therefore, $y$ accumulates squared gradients much faster.

AdaGrad consequently reduces the effective learning rate for $y$ more strongly than for $x$.

The problem is that the accumulated quantity only increases. Even when training gets close to the minimum and gradients become very small, it does not decrease.

Therefore, the effective learning rate becomes extremely small, so the optimizer moves slowly.

### 4. Which AdaGrad problem does RMSProp address?

We see that AdaGrad causes the effective learning rate become too small, RMSProp solve this problem by using an exponentially weighted moving average. 

Because old gradients gradually lose influence, the learning rate does not decrease forever.

### 5. How does Adam combine the ideas behind Momentum and RMSProp?

Adam combines Momentum and RMSProp by keeping two separate exponential moving averages of the gradient:

Momentum part (first moment): Adam tracks the average of the gradients that acts like Momentum because it captures the direction and accumulated movement of the gradients. so recent gradients are smoothed together, reducing noisy updates and oscillations.

RMSProp part (second moment): Adam also tracks the average of the squared gradients. This is the RMSProp idea, It gives each parameter its own adaptive scaling. The squared gradients are averaged over time. 

Adam also uses bias correction because the first and second moment start at zero.

So Adam can both smooth the zigzagging direction and adapt the step size differently for $x$ and $y$.

### 6. What is the difference between Adam and AdamW?

Adam updates parameters using the momentum and RMSProp terms, if weight decay is included in the gradient, it is typically added to the gradient. So the weight-decay term is passed through Adam's adaptive scaling.

AdamW decouples weight decay from the gradient update. First, Adam computes its normal adaptive update and weight decay is applied separately.

### 7. How is Weight Decay different from adding an L2 penalty to the loss?

If we add an L2 penalty to the loss, it gets mixed into Adam's gradient and therefore into its first and second moment calculations.

But with AdamW, weight decay is applied separately from the gradient​.

### 8. Which optimizer had the best stability/speed trade-off in your experiment? Support your answer using your plots.

With 100 iterations, we have the following table:

```
     Algorithm     |   Final x   |   Final y   |   Final Loss   
---------------------------------------------------------------
  Gradient Descent |   0.0002    |   8.0000    |    1280.00 
      Momentum     |   0.0299    |   0.0569    |       0.07 
      AdaGrad      |   7.0911    |   7.0911    |    1055.96 
      RMSprop      |   2.9277    |   2.9277    |     180.00 
       Adam        |   3.6378    |   3.6378    |     277.90 
       AdamW       |   3.4101    |   3.4101    |     244.20
```

The loss plot shows that Momentum’s loss falls much faster than the other optimizers and reaches nearly zero by about 60 iterations. Although it has strong oscillations at the beginning, those oscillations decrease over time.

In the optimizer-path plot, Gradient Descent continues to zigzag strongly, while AdaGrad, RMSProp, Adam, and AdamW move more smoothly but converge more slowly.

### 9. If a Deep Learning model's loss oscillates, what would you check before changing the optimizer?

I would first check whether the learning rate is too large, because that is one of the most common causes of oscillating loss as we saw for Gradient Descent and momentum that use a constant learning rate.

I would also check the following:

1. Loss curve: determine whether the oscillation is small and gradually decreasing, or whether the loss is diverging/increasing.

2. Gradient behavior: check for exploding or highly noisy gradients.

3. Normalization

4. Weight Initialization

5. Regularization: weight decay, dropout, gradient clipping,...

### 10. Briefly explain how Weight Initialization, Normalization, and Regularization each affect optimization.

Weight Initialization: Sets the starting values of the model's weights. It helps to prevent vanishing/exploding gradients and makes training converge faster.

Normalization: Rescales inputs or activations to more consistent ranges. This makes the optimization landscape easier to navigate, often allowing larger learning rates and faster, more stable convergence.

Regularization: Adds constraints or penalties that discourage very complex models, such as L2/weight decay or dropout. It mainly helps prevent overfitting, and can also make optimization more stable by discouraging very large weights.