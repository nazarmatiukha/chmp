from scipy.misc import derivative

def f(x):
   return 3*x**4-4*x**3+2*x**2-4*x-1
a = 1
b = 2

eps = 0.0001

def nuton(a,b,eps):
   df = derivative(f, b, n = 1)
   df2 = derivative(f, b, n = 2)
   if (df*df2>0):
       xi = b
   else:
       xi = a
   df = derivative(f,xi, n= 1)
   xi_1 = xi - f(xi)/df
   while (abs(xi_1 - xi)>eps):
       xi = xi_1
       xi_1 = xi - f(xi)/df
   return print ('За методом Ньютона корінь знаходиться в точці x = ', xi_1)
nuton (a,b,eps)

