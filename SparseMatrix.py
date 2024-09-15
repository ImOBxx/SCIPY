import numpy as np
from scipy.sparse import csr_matirx, coo_matrix
from scipy.sparse import random

rows = 1000
cols = 1000
density = 0.01

sparse_matrix = random(rows, cols, density = density, format = 'csr', dtype = np.float64)

csr_sparse = sparse_matrix.tocsr()
csr_sparse = sparse_matrix.tocsc()
csr_sparse = sparse_matrix.tocso()

vector