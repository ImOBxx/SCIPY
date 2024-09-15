import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

np.random.seed(0)
time = np.linspace(0, 1, 500, endpoint = False)
data = np.sin(2 * np.pi * 7 * time) + np.random.randn(500) * 0.5

b, a = signal.butter(4, 0.1)

filtered_data = signal.filtfilt(b, a, data)

plt.plot(time, data, label = 'Original Data')

plt.plot(time, filtered_data, label = 'Filtered Data', linewidth = 2)

plt.legend()

plt.show()