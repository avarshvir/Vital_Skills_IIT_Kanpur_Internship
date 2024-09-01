import matplotlib.pyplot as plt
import numpy as np
X = np.array([1,2,3,4,5,6])
y = np.array([1.2,0.2,1,5,2,7])

plt.subplot(1,2,1)
plt.plot(X,y)
plt.subplot(1,2,2)
plt.plot(X,y,'r--')
plt.show()