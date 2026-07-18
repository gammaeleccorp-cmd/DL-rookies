import numpy as np

# تابع
def f(x, y):
    return x**2 + 5*y**2

# گرادیان
def grad(x, y):
    return np.array([2*x, 10*y])

# حالت اولیه
x, y = 4.0, 4.0

# learning rate (می‌تونی تغییر بدی: 0.1 یا 0.01)
lr = 0.01

print("Start -> x, y, f(x,y)")
print(x, y, f(x, y))
print("-"*40)

for i in range(10):
    g = grad(x, y)

    x = x - lr * g[0]
    y = y - lr * g[1]

    print(f"step {i} -> x={x:.3f}, y={y:.3f}, f={f(x,y):.3f}")