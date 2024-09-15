import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def model(y, t):
    dydt = -2 * y + np.sin(t)
    return dydt

y0 = np.array([1.0])

t = np.linspace(0, 10, 100)

solution = odeint(model, y0, t)

plt.plot(t, solution)
plt.xlabel('Time')
plt.ylabel('y(t)')
plt.title('Solution Of ODE')
plt.show()