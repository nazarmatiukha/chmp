import matplotlib.pyplot as plt
import numpy as np

from scipy.interpolate import CubicSpline
import numpy as np
import matplotlib.pyplot as plt
x = [1.3, 1.9, 2.6, 2.8, 3.1]
y = [1.63, 2.18, 1.46, 1.17, 2.95]
if np.any(np.diff(x) < 0):
    indexes = np.argsort(x).astype(int)
    x = np.array(x)[indexes]
    y = np.array(y)[indexes]

f = CubicSpline(x, y, bc_type='natural')
x_new = np.linspace(min(x), max(x), 100)
y_new = f(x_new)

plt.plot(x_new, y_new)
plt.scatter(x, y)
plt.title('Cubic Spline Interpolation')
plt.show()
