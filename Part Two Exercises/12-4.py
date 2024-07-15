import numpy as np

def swap_rows(M,a,b):
    size = len(M)
    if type(a) != int or type(b) != int:
        raise ValueError
    if (0 > a >= size) or (0 > b >= size):
        raise Exception
    
    vb = np.copy(M[b,:])

    M[b,:] = M[a,:] 
    M[a,:] = vb

def swap_cols(M,a,b):
    size = len(M)
    if type(a) != int or type(b) != int:
        raise ValueError
    if (0 > a >= size) or (0 > b >= size):
        raise Exception
    
    vb = np.copy(M[:,b])

    M[:,b] = np.copy(M[:,a]) 
    M[:,a] = vb


v = np.array([np.arange(6)+(i*10) for i in range(6)])

print(v)

swap_cols(v, 0, 5)

print(v)

swap_rows(v,0,5)

print(v)

    

