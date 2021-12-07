import gym
# This will register the custom environment
from custom_env import RobotEnv

import logging
import numpy as np
import time

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Flatten
from tensorflow.keras.optimizers import Adam

from rl.agents.dqn import DQNAgent
from rl.policy import BoltzmannQPolicy, EpsGreedyQPolicy
from rl.memory import SequentialMemory


#ENV_NAME = "RobotEnv"

# Create the environment
#env = gym.make(ENV_NAME)

env = RobotEnv()


nb_actions = env.action_space.n        
print(nb_actions)
# Build a neural network model
model = Sequential()
model.add(Flatten(input_shape=(1,) + env.observation_space.shape))
model.add(Dense(12))
model.add(Activation('relu'))
model.add(Dense(12))
model.add(Activation('relu'))
model.add(Dense(12))
model.add(Activation('relu'))
model.add(Dense(nb_actions))
model.add(Activation('linear'))



print(model.summary())
print(model.output_shape)

nb_episode_steps = 15
nb_episodes = 100

# Finally, we configure and compile our agent. You can use every built-in Keras optimizer and
# even the metrics!
memory = SequentialMemory(limit=10, window_length=1)
policy = BoltzmannQPolicy()
#policy = EpsGreedyQPolicy()
dqn = DQNAgent(model=model, nb_actions=nb_actions, memory=memory, nb_steps_warmup=10,
               target_model_update=1e-3, policy=policy)
dqn.compile(Adam(lr=1e-3), metrics=['mae'])

# Okay, now it's time to learn something! We visualize the training here for show, but this
# slows down training quite a lot. You can always safely abort the training prematurely using
# Ctrl + C.
dqn.fit(env, nb_steps=10, visualize=False, verbose=2)

# After training is done, we save the final weights.
dqn.save_weights('dqn_{}_weights.h5f'.format("weights"), overwrite=True)

# Finally, evaluate our algorithm for 5 episodes.
dqn.test(env, nb_episodes=5, visualize=True)
