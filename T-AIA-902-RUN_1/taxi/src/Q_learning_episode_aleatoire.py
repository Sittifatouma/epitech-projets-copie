import gymnasium as gym
import numpy as np


def Q_learning_episode_aleatoire(environment, alpha = 0.1, gamma = 0.99, epoch_number = 8000):
   environment_space_length: int = environment.observation_space.n # type: ignore
   action_space_length: int = environment.action_space.n # type: ignore
   Q_sa = np.zeros((environment_space_length, action_space_length))

   # Training
   for _ in range(epoch_number):
        state = environment.reset()
        stop = False
        state = 0
        step = 0
        
        # Until the agent gets stuck in a hole or reaches the goal, keep training it
        while not stop:
            step += 1
            # Generate a random number between 0 and 1
            rnd = np.random.random()
            
            action = environment.action_space.sample()
            
                
            # Implement this action and move the agent in the desired direction
            new_state, reward, done,  trunc, info = environment.step(action)

            # Update Q(s,a)
            Q_sa[state, action] = Q_sa[state, action] + \
                                    alpha * (reward + gamma * np.max(Q_sa[new_state]) - Q_sa[state, action])
            
            # Update our current state
            state = new_state
            # If we have a reward, it means that our outcome is a success
           # if reward:
           #    if (reward == 20):
           #        print('Episode: {} Reward: {} Steps Taken: {}'.format( _ , reward, step))
            stop = done or trunc


        # Update epsilon
        #epsilon = max(epsilon - epsilon_decay, 0)

   return Q_sa






