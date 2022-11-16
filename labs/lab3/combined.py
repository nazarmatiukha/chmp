from scipy.misc import derivative

def f(x):
   return 3 * x ** 4 - 4 * x ** 3 + 2 * x ** 2 - 4 * x - 1

a = 1
b = 2
eps = 0.0001

def combined(a, b, eps):
   if derivative(f, a, n=1) * derivative(f, a, n=2) < 0:
       a0 = b
       b0 = a
   else:
       a0 = a
       b0 = b
   xp1 = a0
   xp2 = b0
   while (xp2 - xp1) > eps:
       xn1 = xp1 - f(xp1) * (xp2 - xp1) / (f(xp2) - f(xp1))
       xn2 = xp2 - f(xp2) / derivative(f, xp2, n=1)
       xp1 = xn1
       xp2 = xn2
   x = (xp1 + xp2) / 2
   print(x)

combined(a, b, eps)

