import numpy as np
import gym # pip intall gym
from IPython.display import clear_output
import matplotlib.pyplot as plt
import time 
import random
import pickle

environment = gym.make('FrozenLake-v1', is_slippery = False)


qtable = np.zeros((environment.observation_space.n, environment.action_space.n))

# Hyperparameters
episodes = 3000        # Total number of episodes
alpha = 0.7            # Learning rate
gamma = 0.7            # Discount factor
epsilon = 0.9          # Amount of randomness in the action selection
epsilon_decay = 0.001  # Fixed amount to decrease

# List of outcomes to plot
outcomes = []

tot_reward = 0

print('Q-table before training:')
print(qtable)

# Training
for _ in range(episodes):
    state = environment.reset()
    done = False
    state = 0
    step = 0

    # By default, we consider our outcome to be a failure
    outcomes.append("Failure")
    
    # Until the agent gets stuck in a hole or reaches the goal, keep training it
    while not done:
        
        step += 1
        # Generate a random number between 0 and 1
        rnd = np.random.random()

        # If random number < epsilon, take a random action
        if rnd < epsilon:   
          action = environment.action_space.sample()
        # Else, take the action with the highest value in the current state  // maximise les chances de gagner
        else:
          action = np.argmax(qtable[state])
             
        # Implement this action and move the agent in the desired direction
        new_state, reward, done,  trunc, info= environment.step(action)


        # Update Q(s,a)
        qtable[state, action] = qtable[state, action] + \
                                alpha * (reward + gamma * np.max(qtable[new_state]) - qtable[state, action])
        
        # Update our current state
        state = new_state

        # If we have a reward, it means that our outcome is a success
        if reward:
          tot_reward += 1
          outcomes[-1] = "Success"
          print('Episode: {} Reward: {} Steps Taken: {}'.format(_,reward, step))


    # Update epsilon
    epsilon = max(epsilon - epsilon_decay, 0)

print()
print('===========================================')
print('Q-table after training:')
print(qtable)
print("Final result: ", tot_reward,"/",episodes)


with open("frozenLake_qTable.pkl", 'wb') as f:
    pickle.dump(qtable, f)

# Plot outcomes
plt.figure(figsize=(12, 5))
plt.xlabel("Run number")
plt.ylabel("Outcome")
ax = plt.gca()
ax.set_facecolor('#efeeea')
plt.bar(range(len(outcomes)), outcomes, color="#0A047A", width=1.0)
plt.show()