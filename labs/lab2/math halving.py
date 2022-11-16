import numpy as np
import matplotlib.pyplot as plt

def f(x):
   return 3*x**4-4*x**3+2*x**2-4*x-1

a = 1
b = 2
eps = 0.0001

def rec(a, b, eps):
   if abs(f(b) - f(a)) <= eps:
       print('Обчислюємо корінь')
       return
   mid = (a + b) / 2
   if f(mid) == 0 or abs(f(mid)) <= eps:
       print(f'Корінь знаходиться в точці x={mid}')
   elif f(a) * f(mid) < 0:
       rec(a, mid, eps)
   else:
       rec(mid, b, eps)
rec(a,b,eps)

x = np.arange(a, b, eps)

plt.plot(x, f(x))
plt.xlabel('x')
plt.ylabel('y')
plt.title('Ділення навпіл')
plt.grid()
plt.show()
