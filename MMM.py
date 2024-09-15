import numpy as np
from scipy import stats

data = np.random.rand(100)

mean = stats.tmean(data)

median = np.median(data)

variance = stats.tvar(data)

print()
print("Mean: ", mean)
print("Median: ", median)
print("Variance: ", variance)
print()