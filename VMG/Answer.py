import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return 2*x**2 + 8*y**2

def grad(x, y):
    return np.array([4*x, 16*y])

x = np.linspace(-5, 5, 200)
y = np.linspace(-5, 5, 200)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

plt.figure(figsize=(5,5))
plt.contour(X, Y, Z, levels=20, cmap="viridis")

for lr, color in zip([0.1, 0.01], ["red", "blue"]):

    px, py = [4.0], [4.0]
    x, y = 4.0, 4.0

    for _ in range(10):
        g = grad(x, y)
        x -= lr * g[0]
        y -= lr * g[1]

        px.append(x)
        py.append(y)

    plt.plot(px, py, "o-", color=color, label=f"lr={lr}")

plt.scatter(0, 0, color="black", s=80, label="Minimum")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Contour Plot + Gradient Descent Path")
plt.legend()
plt.axis("equal")
plt.show()