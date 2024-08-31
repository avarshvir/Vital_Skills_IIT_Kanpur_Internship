import numpy as np
import matplotlib.pyplot as plt
X = np.array([1,2,3,4,5])
y = np.array([2,4,6,8,10])
plt.plot(X,y,'r',label='y = 2X')
plt.legend()
plt.show()