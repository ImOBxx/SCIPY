import numpy as np
from scipy import stats

np.random.seed(0)
s1 = np.random.normal(loc = 5, scale = 2, size = 100)
s2 = np.random.normal(loc = 5.5, scale = 2, size = 100)

t_stat, p_value = stats.ttest_ind(s1, s2)

print("T_Statistics: ", t_stat)
print("P-value: ", p_value)