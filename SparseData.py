from scipy.sparse import csr_matrix
import numpy as np

arr = np.array([0, 0, 0, 0, 0, 1, 1, 0, 2])

csr = csr_matrix(arr).data                   #.data
print(csr)

print(csr_matrix(arr).count_nonzero())

arr1 = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])

mat = csr_matrix(arr1)
mat.sum_duplicates()

print(mat)
