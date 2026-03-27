import numpy as np

# Q9 - linear algebra

# 1. two 3x3 matrices
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

print("Matrix A:\n", A)
print("Matrix B:\n", B)

# 2. matrix multiplication and element-wise
print("Matrix multiplication (A @ B):\n", A @ B)
print("Element-wise multiplication:\n", A * B)

# 3. inverse and eigenvalues
# using a non-singular matrix for inverse
C = np.array([[2, 1, 0],
              [1, 3, 1],
              [0, 1, 2]])
print("Inverse of C:\n", np.linalg.inv(C))
print("Eigenvalues of A:", np.linalg.eigvals(A))
