import gymnasium as gym
import numpy as np


def Sarsa_epsilon_greedy(environment, epsilon = 0.9, alpha = 0.1, gamma = 0.99, epoch_number = 8000):
   environment_space_length: int = environment.observation_space.n # type: ignore
   action_space_length: int = environment.action_space.n # type: ignore
   Q_sa = np.zeros((environment_space_length, action_space_length))


   # Define the epsilon-greedy policy
   def policy(state, epsilon):
        if np.random.uniform() < epsilon:
            action = environment.action_space.sample()
        else:
            action = np.argmax(Q_sa[state])
        return action


   # Training
   for _ in range(epoch_number):
        state = environment.reset()
        stop = False
        state = 0
        step = 0

        action = policy(state, epsilon)
        
        # Until the agent gets stuck in a hole or reaches the goal, keep training it
        while not stop:
            step += 1

            # Take the chosen action and observe the resulting state and reward
            next_state, reward, done, trunc, info = environment.step(action)

            # Choose the next action using the policy
            next_action = policy(next_state, epsilon)
                
            # Update the Q-table using the SARSA update rule
            #Q_sa[state][action] = Q_sa[state][action] + alpha*(reward + gamma*Q_sa[next_state][next_action] - Q_sa[state][action])

            Q_sa[state, action] = Q_sa[state, action] + alpha * (reward + gamma * Q_sa[next_state, next_action] - Q_sa[state, action])
   

            # Update the state and action
            state = next_state
            action = next_action
            # If we have a reward, it means that our outcome is a success
            #if reward:
            #   if (reward == 20):
            #       print(str(_))
            stop = done or trunc


        # Update epsilon
        #epsilon = max(epsilon - epsilon_decay, 0)

   return Q_sa


