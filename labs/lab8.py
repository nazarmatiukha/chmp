import numpy as np
from math import factorial
import matplotlib.pyplot as plt


x=[0.180, 0.185, 0.190, 0.195, 0.200, 0.205, 0.210, 0.215, 0.220, 0.225, 0.230]
y=[5.5154, 5.4669, 5.3263, 5.1930, 5.0664, 4.9461, 4.8317, 4.7226, 4.6185, 4.5191, 4.4242]
h = x[1] - x[0]
x1=0.189
x2=0.227
q=(x1 - x[0])/h
q1 = (x2-x[-1])/h
def n(y,j):
    arr=[]
    for i in range(len(y)):
        arr.append(y[i] - y[i-1])
    arr.pop(0)
    if j == 1:
        return arr
    else:
        j-=1
        return n(arr, j)

s_1 = y[0]+q*n(y,1)[0]+q*(q-1)*n(y,2)[0]/factorial(2)
s_2 = q*(q-1)*(q-2)*n(y,3)[0]/factorial(3)
s_3 = q*(q-1)*(q-2)*(q-3)*n(y,4)[0]/factorial(4)
s_4 = q*(q-1)*(q-2)*(q-3)*(q-4)*n(y,5)[0]/factorial(5)
n_1 = s_1 + s_2 + s_3 + s_4

print ('Значення функції у точці х1', x1, 'використовуючи Першу Інтерполяційну формулу Ньютона', round(n_1,5))


t1 = y[5] + q1*n(y,1)[4]+q1*(q1+1)*n(y,2)[3]/factorial(2)
t2 = q1*(q1+1)*(q1+2)*n(y,3)[2]/factorial(3)
t3 = q1*(q1+1)*(q1+2)*(q1+3)*n(y,4)[1]/factorial(4)
t4 = q1*(q1+1)*(q1+2)*(q1+3)*(q1+4)*n(y,4)[1]/factorial(5)
n_2 =  t1+t2+t3+t4

print ('Значення функції у точці х2', x2, 'використовуючи Другу Інтерполяційну формулу Ньютона', round(n_2,5))


x_1=np.linspace(np.min(x), np.max(x))
y_1=np.linspace(np.min(y), np.max(y))
plt.plot(x,y, 'ro', x, y)
plt.title('Графік')
plt.xlabel('x')
plt.ylabel('y')
