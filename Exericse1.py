import scipy
from scipy import constants
from scipy.optimize import root
from math import cos
from scipy.optimize import minimize
import scipy.version

print(constants.liter)

print(scipy.__version__)

print(dir(constants))

def eqn(x):
    return x + cos(x)

myroot = root(eqn, 0)

print(myroot)

