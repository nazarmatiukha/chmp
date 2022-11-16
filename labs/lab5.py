import numpy as np
from scipy import optimize
from scipy.misc import derivative
import math

x0 = 0.66
y0 = 0.58
delta = 0.1

def f1(y):
    return -math.cos(y)+1.5

def f2(x):
    return (1+math.sin(x-0.5))/2

df1_x0 = abs(derivative(f1, x0 + delta, n=1))
df2_x0 = abs(derivative(f2, x0 + delta, n=1))
df1_y0 = abs(derivative(f1, y0 + delta, n=1))
df2_y0 = abs(derivative(f2, y0 + delta, n=1))
if df1_x0 + df2_x0 < 1 and df1_y0 + df2_y0 < 1:
    print('The convergence conditions of the iteration method are fulfilled')
    def iter(x, y, e):
        xn = x
        yn = y
        xn1 = f2(x)
        yn1 = f1(y)
        n = 1
        while ((abs(xn1 - xn) >= e) & (abs(yn1 - yn) >= e)):
            xn = xn1
            yn = yn1
            xn1 = f2(yn)
            yn1 = f1(xn)
            n += 1
        print('Simple iteration:')
        print('x=', xn, '\ny=', yn, '\nThe amount of iteration = ', n)
    iter(x0, y0, 0.0001)
else:
    print('The convergence conditions of the iteration method are not fulfilled')

def f3(x):
    return math.cos(x[1])+x[0] - 1.5, 2*x[1]-math.sin(x[0]-0.5) - 1

s = optimize.root(f3, [0., 0.], method='hybr')
print('Check', s.x)
