import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

cube = np.ones((3,3,3), dtype = "bool")

fig = plt.figure()
ax = plt.axes(projection = "3d")
ax.set_facecolor("white")
ax.voxels(cube, facecolor = "#E02050", edgecolors = "k")
ax.axis("off")
plt.show

