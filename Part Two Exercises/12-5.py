import numpy as np

def set_array(L, rows, cols):
    if type(L) not in [list,tuple,dict]:
        raise ValueError
    if rows * cols != len(L):
        raise Exception
    return np.array([np.array([L[c * cols + i] for i in range(cols)]) for c in range(rows)])

li = [0,0,1,3,2,3,2,3,2,3,1,2,4,1,2,4,2,3,2,4,2,3,1,2,4,2,4]
print(len(li), 3*9)
nparry = set_array(li,3,9)
print(nparry)
nparry = set_array(li,9,3)
print(nparry)