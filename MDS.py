import numpy as np
from scipy.spatial.distance import pdist, squareform
from sklearn.manifold import MDS
import matplotlib.pyplot as plt

np.random.seed(0)
data_3d = np.random.rand(10, 3)

dist_matrix = squareform(pdist(data_3d, 'euclidean'))

mds = MDS(n_components=2, dissimilarity='precomputed', random_state=0)
data_2d = mds.fit_transform(dist_matrix)

print("Original Matrix")
print(data_3d)

print("\nTransformed 2D dataset using mds: ")
print(data_2d)

fig = plt.figure()

ax = fig.add_subplot(121, projection='3d')
ax.scatter(data_3d[:, 0], data_3d[:, 1], data_3d[:, 2], c='r', marker='o')
ax.set_title('Original 3D Dataset')

plt.subplot(122)
plt.scatter(data_2d[:, 0], data_2d[:, 1], c='b', marker='o')
plt.title('Transformed 2D Dataset using MDS')
plt.xlabel('Dimension 1')
plt.ylabel('Dimension 2')

plt.tight_layout()
plt.show()
