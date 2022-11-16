import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange 

x=[-4, 0,3,4]
y=[-15,-11,-8,25]
def lagranzh(x,y,t):
    lg=0
    for j in range(len(y)):
        p1=1
        p2=1
        for i in range(len(x)):
            if i==j:
                p1=p1*1 
                p2=p2*1
            else:
                p1=p1*(t-x[i])
                p2=p2*(x[j]-x[i])
        lg=lg+y[j]*p1/p2
    return lg

xnew=np.linspace(np.min(x),np.max(x),100)
ynew=[lagranzh(x,y,i) for i in xnew]
plt.plot(x,y,'o',xnew,ynew)
plt.title('Lagrange Polynomial_1')
plt.grid(True)
plt.show()

f = lagrange(x, y)
fig = plt.figure(figsize = (10,8))
plt.plot(xnew, f(xnew), 'b', x, y, 'ro')
plt.title('Lagrange Polynomial_2')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.show()
