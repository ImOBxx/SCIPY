import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

np.random.seed(0)
x = np.linspace(0, 10, 100)
y = 2.5 * np.sin(1.5 * x) + np.random.normal(size=x.size)

def model_func(x, a, b):
    return a * np.sin(b * x)

params, covariance = curve_fit(model_func, x, y)

a_fit, b_fit = params

y_fit = model_func(x, a_fit, b_fit)

plt.scatter(x, y, label='Sample Data')
plt.plot(x, y_fit, label='Fitted Curve', color='red')
plt.legend()
plt.show()
