import sympy as sp
from sympy import *
a=1
b=2
eps=0.0001
def f(x, switch):
  f = 3*x**4-4*x**3+2*x**2-4*x-1
  fd1 = sp.diff(f)
  fd2 = sp.diff(fd1)
  if switch == 0:
      return f
  elif switch == 1:
      return fd1
  elif switch == 2:
      return fd2


if f(a, 0)*f(a, 2) > 0:
  x0 = a
  xi = b
else:
  x0 = b
  xi = a

xi_1 = xi-((xi-x0)/(f(xi, 0)-f(x0, 0))*f(xi, 0))

while abs(xi_1-xi)>eps:
  xi = xi_1
  xi_1 = xi-((xi-x0)/(f(xi, 0)-f(x0, 0))*f(xi, 0))
else:
  print (f'Корінь знаходиться в точці x = {xi_1}')
