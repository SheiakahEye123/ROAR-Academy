import numpy as np

v1 = np.matrix([[6, 9, 1],
                [4, 24, 8]])
v2 = np.matrix([[6, 9, 1],
                [4, 24, 8]])
v3 = np.matrix([[-2,3],
                [3,-4]])

x1 = 2
x2 = np.eye(2,2)
x3 = v3.I

print(2*v1)
print(x2@v2)
print(x3@v3)