import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import axes3d
#main code
fig=plt.figure()
ax = fig.gca(projection='3d')
t=np.linspace(0,5*np.pi,501)
ax.plot(np.cos(t),np.sin(t),t)
plt.show()