import numpy as np
a = [[1, 2, 4], [1, 3, 4], [2, -1, -1]]
print('A =',a)
b = [[5], [6], [1]]
print('B =',b)

def cramer (a, b):
    a_det = np.linalg.det(a)
    print('Детермінант матриці =', a_det)

    if (a_det != 0):
        A1 = np.matrix(a)
        A1[:, 0] = b
        print('A1 =', A1)

        A2 = np.matrix(a)
        A2[:, 1] = b
        print('A2: \n',A2)

        A3 = np.matrix(a)
        A3[:, 2] = b
        print('A3 =',A3)

        x = np.linalg.det(A1) / a_det
        y = np.linalg.det(A2) / a_det
        z = np.linalg.det(A3) / a_det

        print('X = ', round(x,5))
        print('Y =', round(y,5))
        print('Z =', round(z,5))

    else:
        print("Розв'язків немає")

cramer(a,b)
