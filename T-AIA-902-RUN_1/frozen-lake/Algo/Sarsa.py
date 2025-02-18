import random

import gym
import numpy as np
import matplotlib.pyplot as plt

env = gym.make('FrozenLake-v1', is_slippery = False)

env.env.P[0]

state_size = 16
action_space = env.action_space.n
alpha = 0.1
gamma = 1
state_action_vals = np.random.randn(state_size, action_space)
policy = np.zeros(state_size, dtype=int)
#episodes = 20000
episodes = 2000
eps = 0.2
#test_episodes = 50
test_episodes = 50
#test_every = 1000
test_every = 100
test_episode = []
rewards = []


def select_action(state, eps):
    sample = np.random.uniform()
    if sample < eps:
        return env.action_space.sample()
    else:
        return state_action_vals[state].argmax()

for ep in range(episodes):
    print("BEGIN")
    print(ep)
    state = env.reset()
    state = 0
    action = select_action(state, eps)
    done = False
    while not done:
        print("boucle")
        next_state, reward, done, _ , bar= env.step(action)
        next_action = select_action(state, eps)
        action_value = state_action_vals[state, action]
        next_action_value = state_action_vals[next_state, next_action]
        delta = reward + gamma * next_action_value - action_value
        state_action_vals[state, action] += alpha * delta
        state, action = next_state, next_action

    if ep % test_every == 0:
        if ep != 0:
            total_rewards = 0
            for _ in range(test_episodes):
                done = False
                state = env.reset()
                state = 0
        
                while not done:
                    print(ep)
                    action = state_action_vals[state].argmax()
                    state, reward, done, _, bar = env.step(action)
                    print(state)
                    print(action)
                    total_rewards += reward
            rewards.append(total_rewards / test_episodes)
            test_episode.append(ep)

#fig, ax = plt.subplots()
#ax.plot(test_episode, rewards)
#ax.set_title('Episodes vs average rewards')
#ax.set_xlabel('Episode')
#_ = ax.set_ylabel('Average reward')
print("Final:")
print(test_episode)
print(rewards)

