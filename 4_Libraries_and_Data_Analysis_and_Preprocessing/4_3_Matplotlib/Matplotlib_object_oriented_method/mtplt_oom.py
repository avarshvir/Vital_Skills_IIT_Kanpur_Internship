import matplotlib.pyplot as plt
import numpy as np
X = np.array([1,2,3,4,5,6])
y = np.array([1.2,0.2,1,5,2,7])
fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.3,0.3,0.3,0.3])
axes.plot(X,y)
axes2.plot((X,y))
plt.show()
