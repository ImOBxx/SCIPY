import numpy as np
from scipy.fftpack import fft2

data = np.random.rand(4, 4)

dft_result = fft2(data)

print()
print("Original 2D Array: ")
print(data)

print("\nDFT Of the 2D Array: ")
print(dft_result)
print()