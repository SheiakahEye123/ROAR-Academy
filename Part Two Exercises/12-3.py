import numpy as np

v = np.array([np.arange(6)+(i*10) for i in range(6)])
blue = v[:,1]
pink = v[1,2:4]
green = v[2:4,4:6]
orange = v[np.arange(1,3)*2][:,np.arange(0,3)*2]
print(blue)
print(pink)
print(green)
print(orange)