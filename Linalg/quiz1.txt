import numpy as np

X = np.random.rand(20, 80)
y = np.random.rand(20)

print("X shape:", X.shape)
print("y shape:", y.shape)

print("Rank(X):", np.linalg.matrix_rank(X))

XtX = X.T @ X

print("XtX shape:", XtX.shape)
print("Rank(XtX):", np.linalg.matrix_rank(XtX))

print("Det(XtX):", np.linalg.det(XtX))
print("Cond(XtX):", np.linalg.cond(XtX))

is_invertible = np.linalg.matrix_rank(XtX) == XtX.shape[0]
print("Is XtX Invertible?", is_invertible)

w_pinv = np.linalg.pinv(X) @ y

y_pred = X @ w_pinv
loss = np.sum((y - y_pred) ** 2)

print("Loss (PINV):", loss)

w_lstsq = np.linalg.lstsq(X, y, rcond=None)[0]

print("PINV == LSTSQ:", np.allclose(w_pinv, w_lstsq))