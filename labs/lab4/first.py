import numpy as np
#номер 2
A = [[2, 3, 1], [-1, 1, 0], [1, 2, -1]]
B = [[1, 2, 1], [0, 1, 2], [3, 1, 1]]
AB = np.dot(A,B)
BA = np.dot(B,A)
print (AB-BA)
