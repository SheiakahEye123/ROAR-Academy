import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,4)
plt.plot(x, np.append(((x[:2]*2)),(x[2:]*-1)+4))
plt.show()