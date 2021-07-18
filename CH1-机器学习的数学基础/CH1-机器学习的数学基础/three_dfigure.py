import numpy as np
import matplotlib.pyplot as plt
import random
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.gca(projection='3d')
# prepare data
x = np.arange(-100, 100, 0.5)
y = np.arange(-100, 100, 0.5)
x, y = np.meshgrid(x, y)
a=-10
b=10
z = np.square(a-x) + b*np.square(y - x**2)
surf = ax.plot_surface(x, y, z, cmap='rainbow')

fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()