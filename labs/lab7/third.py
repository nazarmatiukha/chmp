import numpy as np
import math
arr_x = [1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
arr_y = [10.517, 10.193, 9.807, 9.387, 8.977, 8.637]
h = arr_x[1] - arr_x[0]
print (h)
arr_1 = []
arr_2 = []
arr_3 = []
arr_4 = []
for i in range(len(arr_y)):
   arr_1.append(arr_y[i] - arr_y[i-1])
arr_1.pop (0)
print('arr_1 = ', arr_1)

for j in range(len(arr_1)):
   arr_2.append(arr_1[j] - arr_1[j-1])
arr_2.pop (0)
print('arr_2 = ',arr_2 )

for k in range(len(arr_2)):
   arr_3.append(arr_2[k] - arr_2[k-1])
arr_3.pop (0)
print('arr_3=',arr_3)

for l in range(len(arr_3)):
   arr_4.append(arr_3[l] - arr_3[l-1])
arr_4.pop (0)
print('arr_4=',arr_4)

y1 = 1/ h * (arr_1[1] - (arr_2[1]/ 2) + (arr_3[1] /3) - (arr_4[1]/4))
y2 = 1/ (h**2) * (arr_2[1] - arr_3[1] + 11/12*arr_4[1])

print ('Перша похідна =', y1)
print ('Друга похідна =', y2)

