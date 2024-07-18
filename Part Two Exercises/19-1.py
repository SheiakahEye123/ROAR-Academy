## This is course material for Introduction to Modern Artificial Intelligence
## Example code: cartpole_dqn.py
## Author: Allen Y. Yang
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

# Please make sure to install openAI gym module
# https://github.com/openai/gym
import random
import gym
import os
import numpy as np
from collections import deque
import matplotlib.pyplot as plt

import tensorflow
from keras.models import Sequential
from keras.layers import Dense


EPISODES = 10

x = np.array([])
y = np.array([])
z = np.array([])

class PIDControl:
    def __init__(self,Kp,Ki,Kd):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
    
        self.ersum = 0
        self.e = 0


        self.model = Sequential()
        self.model.add(Dense(4,input_shape=(1,),activation="sigmoid"))
        self.model.add(Dense(1,activation="linear"))
        self.model.compile(loss='mean_squared_error')

    def update(self, t, goal):
        prevError = self.e
        self.e = t - goal
        self.ersum += self.e

        p = self.e * self.Kp
        i = self.ersum * self.Ki
        d = (self.e - prevError) * self.Kd

        return [p, i, d]
    
pid = PIDControl(0.005,0,0.03)

if __name__ == "__main__":
    env = gym.make('CartPole-v1')
    state_size = env.observation_space.shape[0]
    action_size = env.action_space.n
    done = False


    for e in range(EPISODES):
        state = env.reset()
        state = np.reshape(state, [1, state_size])
        # x = np.array([])
        # y =np.array([])
        # z = np.array([])
        for time in range(100):
            env.render()
            # print(pid.update(state[0,2]))
            pidA = pid.update(state[0][2],0)

            action = 0 if np.sum(np.array(pidA)) < 0 else 1
            next_state, r, d, _ = env.step(action)
            next_state = np.reshape(next_state, [1, state_size])
            state = next_state
            if done:
                print("ep: {}/{}, score: {}, e: {:,2}".format(e, EPISODES, time, pidA))

        # print(y.shape,z.shape)
    