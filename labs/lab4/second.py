import numpy as np

A = [[-1, 0, 2], [0, 1, 0], [1, 2, -1]]
B = np.linalg.matrix_power(A, 2)
print (B)
