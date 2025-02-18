import gym
import numpy as np
import time
import pickle, os

print('BEGIN Q-TABLE ALGO LOADED')


env = gym.make('FrozenLake-v1', is_slippery = False, render_mode="rgb_array")

with open("frozenLake_qTable.pkl", 'rb') as f:
	Q =   pickle.load(f)

	
#Q = np.array([[0.531441, 0.59049, 0.59049, 0.531441],
#              [0.531441, 0., 0.6561, 0.59049],
#              [0.59049, 0.729, 0.59049, 0.6561],
#              [0.6561, 0., 0.58560639, 0.40155481],
#              [0.59049, 0.6561, 0., 0.531441],
#              [0., 0., 0., 0.],
#              [0., 0.81, 0., 0.6561],
#              [0., 0., 0., 0.],
#              [0.6561, 0., 0.729, 0.59049],
#              [0.6561, 0.81, 0.81, 0.],
#              [0.729, 0.9, 0., 0.729],
#              [0., 0., 0., 0.],
#              [0., 0., 0., 0.],
#              [0., 0.81, 0.9, 0.729],
#              [0.81, 0.9, 1., 0.81],
#              [0., 0., 0., 0.]])

# Hyperparameters
episodes = 50        # Total number of episodes

def choose_action(state):
	action = np.argmax(Q[state, :])
	return action

# start
for episode in range(episodes):

	state = env.reset()
	t = 0
	state = 0
	while t < 100:
	#	env.render()
		action = choose_action(state)
		state2, reward, done, trunc, info = env.step(action)  
		state = state2
		t += 1

		if done:
			print('Episode: {} Reward: {} Steps Taken: {}'.format(episode,reward, t))
			break


print('END Q-TABLE ALGO LOADED')