import numpy as np

# Q3 - 2D arrays and matrices

# 1. 3x3 matrix with values 1 to 9
mat = np.arange(1, 10).reshape(3, 3)
print("Matrix:\n", mat)

# 2. transpose
print("Transpose:\n", mat.T)

# 3. row-wise and column-wise sums
print("Row-wise sum:", np.sum(mat, axis=1))
print("Column-wise sum:", np.sum(mat, axis=0))

# 4. determinant
det = np.linalg.det(mat)
print("Determinant:", det)
# note: this will be 0 since it's a singular matrix
