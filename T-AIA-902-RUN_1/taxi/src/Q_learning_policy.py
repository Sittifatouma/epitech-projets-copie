import gymnasium as gym
import numpy as np
import random




def Q_learning_policy(environment, epsilon = 0.1, alpha = 0.1, gamma = 0.99, epoch_number = 8000, policy_type='epsilon_greedy',tau=0.1,controlMode=False):
   environment_space_length: int = environment.observation_space.n # type: ignore
   action_space_length: int = environment.action_space.n # type: ignore
   Q_sa = np.zeros((environment_space_length, action_space_length))


   def epsilon_greedy(state, epsilon):
    if random.uniform(0, 1) < epsilon:
        action = environment.action_space.sample()
    else:
        action = np.argmax(Q_sa[state])
    return action


   def greedy(state):
        return np.argmax(Q_sa[state])


   def softmax(state, tau):
        values = Q_sa[state]
        probabilities = np.exp(values / tau) / np.sum(np.exp(values / tau))
        action = np.random.choice(len(probabilities), p=probabilities)
        return action


   def randomPolicy():
        return environment.action_space.sample()
   
   def controlEpsilon():
        max_epsilon = 1
        min_epsilon = 0.001
        epsilon_decay = 0.01
        epsilon = min_epsilon + (max_epsilon - min_epsilon) * np.exp(-epsilon_decay * _)
        return epsilon

   # Training
   for _ in range(epoch_number):
        state = environment.reset()
        stop = False
        state = 0
        step = 0
        
        # Until the agent gets stuck in a hole or reaches the goal, keep training it
        while not stop:
            
            step += 1
 
            #  la valeur d'epsilon diminue exponentiellement à mesure que le nombre d'épisodes augmente.
            if controlMode == True:
             epsilon = controlEpsilon() 

 
            # Select policy
            if policy_type == 'epsilon-greedy':
                action = epsilon_greedy(state, epsilon)
            elif policy_type == 'greedy':
                action = greedy(state)
            elif policy_type == 'softmax':
                action = softmax(state, tau) 
            else:
                action = randomPolicy()

                
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






