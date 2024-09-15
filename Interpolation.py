import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

x = np.linspace(0, 10, num = 11, endpoint = True)
y = np.sin(x)

f = interpolate.interp1d(x, y, kind = 'cubic')

x_new = np.linspace(0, 10, num = 100, endpoint = True)
y_new = f(x_new)

plt.plot(x, y, 'o', label = 'Original Data Points')
plt.plot(x_new, y_new, '_', label = 'Interpolated Data')
plt.legend()
plt.show()