import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,4)

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Sample Graph!")

plt.xticks(np.arange(1, 3.5, 0.5), ["1.0","1.5","2.0","2.5","3.0"])
plt.ylim(1,4)
plt.xlim(1,3.0)

plt.plot(x, np.append(((x[:2]*2)),(x[2:]*-1)+4),color = "blue", linewidth = 1)
plt.show()