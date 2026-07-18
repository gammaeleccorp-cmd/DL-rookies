import numpy as np

# -------------------------
# 1. ساخت داده‌ها
# -------------------------
X = np.random.rand(10, 50)
y = np.random.rand(10)

print("X shape:", X.shape)
print("y shape:", y.shape)

# -------------------------
# 2. Rank بررسی
# -------------------------
print("\nRank(X):", np.linalg.matrix_rank(X))

XtX = X.T @ X

print("XtX shape:", XtX.shape)
print("Rank(XtX):", np.linalg.matrix_rank(XtX))

# -------------------------
# 3. بررسی معکوس پذیری
# -------------------------
print("\nDet(XtX):", np.linalg.det(XtX))
print("Cond(XtX):", np.linalg.cond(XtX))

# شرط معکوس پذیری
is_invertible = np.linalg.matrix_rank(XtX) == XtX.shape[0]
print("\nIs XtX invertible?", is_invertible)

# -------------------------
# 4. حل معادله (3 روش)
# -------------------------

# روش 1: inverse (فقط وقتی invertible باشد)
if is_invertible:
    w_inv = np.linalg.inv(XtX) @ X.T @ y
else:
    w_inv = None

# روش 2: pseudo inverse (SVD)
w_pinv = np.linalg.pinv(X) @ y

# روش 3: least squares
w_lstsq = np.linalg.lstsq(X, y, rcond=None)[0]

# -------------------------
# 5. مقایسه جواب‌ها
# -------------------------
if w_inv is not None:
    print("\nCompare inv vs pinv:", np.allclose(w_inv, w_pinv))
    print("Compare inv vs lstsq:", np.allclose(w_inv, w_lstsq))

print("Compare pinv vs lstsq:", np.allclose(w_pinv, w_lstsq))

# -------------------------
# 6. پیش‌بینی و Loss
# -------------------------
w = w_pinv  # یا lstsq

y_pred = X @ w
loss = np.sum((y - y_pred) ** 2)

print("\nLoss:", loss)