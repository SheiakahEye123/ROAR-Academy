import numpy as np
from matplotlib import pyplot as plt, image
import os

path = os.path.dirname(os.path.abspath(__file__))

lenna = path + '/../samples/' + 'lenna.bmp'
flag = path + '/' + 'united-states-of-america-flag-png-large.png'

lenna_data = image.imread(lenna)
flag_data = image.imread(flag)

data = lenna_data.copy()
w, h = flag_data.shape

print(w,h)