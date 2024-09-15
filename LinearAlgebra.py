import numpy as np
from scipy import linalg

matrix = np.array([[4, 2], [3, 1]])

deter = linalg.det(matrix)

inverse = linalg.inv(matrix)

eigenvalues, eigenvectors = linalg.eig(matrix)

print()
print("Matrix: ")
print(matrix)
print()
print("Determinant: ")
print(deter)
print()
print("Inverse: ")
print(inverse)
print()
print("Eigenvalues: ")
print(eigenvalues)
print()
print("Eigenvectors: ")
print(eigenvectors)
print()