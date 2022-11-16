import numpy as np
A = [[1, 2, 4], [1, 3, 4], [2, -1, -1]]
print('A =',A)
B = [[5], [6], [1]]
print('B =',B)

A_inv = np.linalg.inv(A)
print (A_inv)

X = A_inv.dot(B)
print ('X =', X)
