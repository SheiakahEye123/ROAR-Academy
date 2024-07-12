import numpy as np
from matplotlib import pyplot as plt, image
import os
import PIL

path = os.path.dirname(os.path.abspath(__file__))

lenna = path + '/../samples/' + 'lenna.bmp'
flag = path + '/' + 'united-states-of-america-flag-medium.jpg'

lenna_data = image.imread(lenna)
flag_data = image.imread(flag)

w, h, c = flag_data.shape
w = 100
h = 100
print(w, h)

data = lenna_data.copy()
flagd = flag_data.copy()


data[:h,:w] = flagd[:h,:w]
plt.imshow(data)
plt.show()