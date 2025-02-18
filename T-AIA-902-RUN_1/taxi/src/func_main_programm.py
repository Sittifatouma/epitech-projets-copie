import random
import gymnasium as gym
import numpy as np
import json
from src.Q_learning_policy import Q_learning_policy
from src.Q_learning_episode_aleatoire import Q_learning_episode_aleatoire

from src.Display import display_data



import pandas as pd
import seaborn
import matplotlib.pyplot as plt

import time

seed = 0
environment = gym.make('Taxi-v3')

stepResult = []
rewardResult = []

cpt = 0

#epoch_number : nbre episode pour entrainement
#test_epoch : nbre episode test

def func_mode(aleatoire_episode, test_epoch, epoch_number, epsilon, alpha, gamma) :
    random.seed(seed)
    environment.reset(seed=seed)

    if (aleatoire_episode == "0") :
      # Learning QSA with Q-learning algorithme and epsilon greedy policy
      q_sa = Q_learning_policy(environment, epsilon, alpha, gamma, epoch_number)
    else :
      q_sa = Q_learning_episode_aleatoire(environment, alpha, gamma, epoch_number)



    random.seed(seed)
    environment.reset(seed=seed)

    start = time.time()

    # use for final calculation
    success = 0
    mean_steps = 0
    mean_result = 0
    max_steps = []


    for epoch in range(test_epoch):

        point = 0
        step = 0
        stop = False
        state = environment.reset()
        state = 0


        # Use to print graphe 
        nameStep = 'Step_'
        nameStep = nameStep + str(int(epoch_number))

        while not stop:
            '''
               Run the game 
            '''
            step += 1

            # Select best action from q_sa
            action = np.argmax(q_sa[state])
                
            # Implement action and retreive game information
            new_state, reward, done,  trunc, info= environment.step(action)

            # Update our current state
            state = new_state

            # Update point
            point += reward

            if done:
              success += 1

            stop = done or trunc
            if stop:
             #   stepResult.append({
             #     nameStep: step,
             #    })
                rewardResult.append({
                  nameStep: point,
                 })
                max_steps.append(int(step))
                mean_steps += step
                mean_result += point


    # To summarize data for each loop
    display_data(test_epoch, start, epoch_number, success, mean_steps, max_steps,  mean_result)  

