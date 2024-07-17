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
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
import matplotlib.pyplot as plt

EPISODES = 100

class PIDControl:
    def __init__(self,Kp,Ki,Kd,goal):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.goal = goal
    def update(self, t):
        e = self.goal - t



if __name__ == "__main__":
    env = gym.make('CartPole-v1',render_mode='rgb_array')
    state_size = env.observation_space.shape[0]
    action_size = env.action_space.n
    done = False


    for e in range(EPISODES):
        state = env.reset()
        # state = np.reshape(state, [1, state_size])
        # env.render_mode = "rgb_array"
        for time in range(500):
            # env.render()
            # action = agent.act(state)
            # next_state, reward, done, _ = env.step(action)
            r = env.render()

            print(time)
            if time % 10 == 0:
                plt.imshow(r)
                plt.show()
