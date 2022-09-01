import numpy as np
from numpy import linalg

a = np.array([[4, 2, 1], [1, 3, 0], [0, 5, 4]])
b = np.array([4, 12, -3])
x = linalg.solve(a, b)
print('x = ', x[0])
print('y = ', x[1])
print('z = ', x[2])