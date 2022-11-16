import matplotlib.pyplot as plt
import numpy as np

from scipy.interpolate import CubicSpline
import numpy as np
import matplotlib.pyplot as plt
x = [0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.8, 2, 2.3, 2.4, 2.6, 2.8, 3, 3.3, 3.4, 3.6, 3.8, 4, 4.2, 4.4, 4.5]
y = [1.915806276, 1.420647119, 1.151082442, 1.066095067, 1.124667817, 1.285783512, 1.508424974, 1.751575026, 0.812718429, 2.092313737, 2.236923379, 4.752951542, 1.540109783, 1.46, 1.17, 2.693978043, 4.388608062, 4.73, 3.901135507, 0.048974275, -8.035802391, -21.56251319, -41.74047681, -54.70159053]
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
