import numpy as np

def f(x, y):
    return 2*x**2 + 8*y**2

def grad(x, y):
    return np.array([4*x, 16*y])

H = np.array([[4, 0],
              [0, 16]])

print(H)

eigvals, eigvecs = np.linalg.eig(H)

print(eigvals)

for lr in [0.1, 0.01]:
    print(f"\nLearning Rate = {lr}")

    x, y = 4.0, 4.0

    for i in range(10):
        g = grad(x, y)

        x -= lr * g[0]
        y -= lr * g[1]

        print(f"step {i}: x={x:.3f}, y={y:.3f}, f={f(x,y):.3f}")