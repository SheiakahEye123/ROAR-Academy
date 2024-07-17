import tensorflow as tf
from keras.datasets import mnist
from keras.models import Sequential
import numpy as np
import random
import matplotlib.pyplot as plt
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D

batch_size = 128
num_classes = 10
epochs = 500

(X, Y), (testX, testY) = mnist.load_data()

X = np.array(X) / 255
Y = np.array(Y)

plt.imshow(X[random.randint(0,255)])
plt.show()

model = Sequential()
model.add(Conv2D(64,kernel_size=(8,8),padding="valid",strides=(1,1), input_shape=(600,28,28),activation='sigmoid'))
model.add(MaxPooling2D(pool_size=(4,4)))
model.add(Conv2D(32,kernel_size=(5,5),padding="valid",strides=(1,1),activation='sigmoid'))
model.add(MaxPooling2D(pool_size=(4,4)))

model.add(Flatten())

model.add(Dense(12,activation='sigmoid'))
model.add(Dropout(0.5))
model.add(Dense(12,activation='sigmoid'))
model.add(Dense(num_classes,activation='softmax'))

model.compile(loss='mean_squared_error',
              optimizer='adagrad',
              metrics=['accuracy'])

model.fit(X,Y,verbose=1,validation_split=0.2,batch_size=600)