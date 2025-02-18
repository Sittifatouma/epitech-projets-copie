import gym
import numpy as np
import pickle
import matplotlib.pyplot as plt

# Create the environment
env = gym.make('FrozenLake-v1', is_slippery=False)

# Set hyperparameters
num_episodes = 30000
alpha = 0.9  # Learning rate
gamma = 0.9  # Discount factor
epsilon = 0.9  # Amount of randomness in the action selection


# See global result
tot_reward = 0

# List of outcomes to plot
outcomes = []

# Initialize the Q-table with zeros
Q = np.zeros((env.observation_space.n, env.action_space.n))

# Define the epsilon-greedy policy
def policy(state, epsilon):
    if np.random.uniform() < epsilon:
        action = env.action_space.sample()
    else:
        action = np.argmax(Q[state])
    return action

# Loop over episodes
for i in range(num_episodes):
    # By default, we consider our outcome to be a failure
    outcomes.append("Failure")

    # Reset the environment and get the initial state
    state = env.reset()
    state = 0
    # Choose the initial action using the policy
    action = policy(state, epsilon)
    # Initialize the episode reward
    episode_reward = 0
    # number of step to acheive 
    step = 0
    # Loop over time steps
    while True:
        #Increament step
        step += 1
        # Take the chosen action and observe the resulting state and reward
        next_state, reward, done, trunc, info = env.step(action)
        # Choose the next action using the policy
        next_action = policy(next_state, epsilon)
        # Update the Q-table using the SARSA update rule
        Q[state][action] = Q[state][action] + alpha*(reward + gamma*Q[next_state][next_action] - Q[state][action])
        # Update the episode reward

        episode_reward += reward
        # Update the state and action
        state = next_state
        action = next_action

        # If we have a reward, it means that our outcome is a success
        if reward:
          outcomes[-1] = "Success"
          print('Episode: {} Reward: {} Steps Taken: {}'.format(i,reward, step))
         # Check if the episode is done

        if done:
            if episode_reward == 1:
                tot_reward += 1
            break
    # Print the episode reward
    #print("Episode:", i, "Reward:", episode_reward)


print("Final result: ", tot_reward,"/",num_episodes)

# Store Q-table in a file 
with open("sarsa_qTable.pkl", 'wb') as f:
    pickle.dump(Q, f)

# Plot outcomes
plt.figure(figsize=(12, 5))
plt.xlabel("Run number")
plt.ylabel("Outcome")
ax = plt.gca()
ax.set_facecolor('#efeeea')
plt.bar(range(len(outcomes)), outcomes, color="#0A047A", width=1.0)
plt.show()
