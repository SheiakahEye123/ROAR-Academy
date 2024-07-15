## This is course material for Introduction to Python Scientific Programming
## Example code: matplotlib_clock.py
## Author: Allen Y. Yang
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

from datetime import datetime
import matplotlib.pyplot as plt
import os
import numpy as np

# Initialization, define some constant
path = os.path.dirname(os.path.abspath(__file__))
filename = path + '/airplane.bmp'
background = plt.imread(filename)

second_hand_length = 200
second_hand_width = 2
minute_hand_length = 150
minute_hand_width = 6
hour_hand_length = 100
hour_hand_width = 10
micro_hand_length = 200
micro_hand_width = 1
center = np.array([256, 256])

def clock_hand_vector(angle, length):
    return np.array([length * np.sin(angle), -length * np.cos(angle)])

# draw an image background
fig = plt.figure()

while True:
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_color('none')
    ax.spines['left'].set_color('none')

    ax.axis('off')

    plt.imshow(background)

    # First retrieve the time
    now_time = datetime.now()
    hour = now_time.hour % 12
    gmt = now_time.hour + 7
    minute = now_time.minute
    second = now_time.second
    millisecond = now_time.microsecond

    # Calculate end points of hour, minute, second

    hour_vector = clock_hand_vector((hour+minute/60)/12*2*np.pi, hour_hand_length)
    minute_vector = clock_hand_vector((minute + second/60)/60*2*np.pi, minute_hand_length)
    second_vector = clock_hand_vector((second + millisecond/1000000)/60*2*np.pi, second_hand_length)
    microsecond_vector = clock_hand_vector((millisecond/1000000)*2*np.pi, micro_hand_length)
    gmt_vector = clock_hand_vector((gmt+minute/60)/24*2*np.pi, hour_hand_length)



    plt.arrow(center[0], center[1], hour_vector[0], hour_vector[1], head_length = 3, linewidth = hour_hand_width, color = 'black')
    plt.arrow(center[0], center[1], minute_vector[0], minute_vector[1], linewidth = minute_hand_width, color = 'black')
    plt.arrow(center[0], center[1], second_vector[0], second_vector[1], linewidth = second_hand_width, color = 'red')
    plt.arrow(center[0], center[1], microsecond_vector[0], microsecond_vector[1], linewidth = micro_hand_width, color = 'blue')
    plt.arrow(center[0], center[1], gmt_vector[0], gmt_vector[1], linewidth = hour_hand_width, color = 'yellow')

    plt.pause(1/1000)
    plt.clf()
