import gym
import numpy as np
import time
import pickle, os

env = gym.make('FrozenLake-v1', is_slippery = False, render_mode="rgb_array")

print('BEGIN SARSA ALGO LOADED')

with open("sarsa_qTable.pkl", 'rb') as f:
	Q =   pickle.load(f)
	
terminated = np.bool_(True)

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

		#os.system('clear')

print('END SARSA ALGO LOADED')