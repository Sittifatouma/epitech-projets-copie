import random
import gymnasium as gym
import numpy as np
import json
from src.Sarsa_epsilon_greedy import Sarsa_epsilon_greedy
from src.Display import display_data



import pandas as pd
import seaborn
import matplotlib.pyplot as plt

import time


    


#    ____             _                     _____             __ _                       _   _             
#   |  _ \           | |                   / ____|           / _(_)                     | | (_)            
#   | |_) | __ _  ___| | ___   _ _ __     | |     ___  _ __ | |_ _  __ _ _   _ _ __ __ _| |_ _  ___  _ __  
#   |  _ < / _` |/ __| |/ / | | | '_ \    | |    / _ \| '_ \|  _| |/ _` | | | | '__/ _` | __| |/ _ \| '_ \ 
#   | |_) | (_| | (__|   <| |_| | |_) |   | |___| (_) | | | | | | | (_| | |_| | | | (_| | |_| | (_) | | | |
#   |____/ \__,_|\___|_|\_\\__,_| .__/     \_____\___/|_| |_|_| |_|\__, |\__,_|_|  \__,_|\__|_|\___/|_| |_|
#                               | |                                 __/ |                                  
#                               |_|                                |___/                                  

output_file = "data/QLEps.json"
qsa_file = "data/qsa-Qlearning-taxi.json"

#     _____      _     _       _____             __ _                       _   _             
#    / ____|    (_)   | |     / ____|           / _(_)                     | | (_)            
#   | |  __ _ __ _  __| |    | |     ___  _ __ | |_ _  __ _ _   _ _ __ __ _| |_ _  ___  _ __  
#   | | |_ | '__| |/ _` |    | |    / _ \| '_ \|  _| |/ _` | | | | '__/ _` | __| |/ _ \| '_ \ 
#   | |__| | |  | | (_| |    | |___| (_) | | | | | | | (_| | |_| | | | (_| | |_| | (_) | | | |
#    \_____|_|  |_|\__,_|     \_____\___/|_| |_|_| |_|\__, |\__,_|_|  \__,_|\__|_|\___/|_| |_|
#                                                      __/ |                                  
#                                                     |___/                                  
test_epoch = 1000
grid_steps = 5
mail = {
    "training_number":{
        "start": 2000,
        "end": 2000,
        "steps": grid_steps,
    },
    "epsilon": {
        "start": 0.5,
        "end": 0.98,
        "steps": grid_steps,
    },
    "alpha": {
        "start": 0.1,
        "end": 0.98,
        "steps": grid_steps,
    },
    "gamma": {
        "start": 0.8,
        "end": 0.98,
        "steps": grid_steps,
    },
}
seed = 0

#    ______            _                                      _         _____             __ _                       _   _             
#   |  ____|          (_)                                    | |       / ____|           / _(_)                     | | (_)            
#   | |__   _ ____   ___ _ __ ___  _ __  _ __ ___   ___ _ __ | |_     | |     ___  _ __ | |_ _  __ _ _   _ _ __ __ _| |_ _  ___  _ __  
#   |  __| | '_ \ \ / / | '__/ _ \| '_ \| '_ ` _ \ / _ \ '_ \| __|    | |    / _ \| '_ \|  _| |/ _` | | | | '__/ _` | __| |/ _ \| '_ \ 
#   | |____| | | \ V /| | | | (_) | | | | | | | | |  __/ | | | |_     | |___| (_) | | | | | | | (_| | |_| | | | (_| | |_| | (_) | | | |
#   |______|_| |_|\_/ |_|_|  \___/|_| |_|_| |_| |_|\___|_| |_|\__|     \_____\___/|_| |_|_| |_|\__, |\__,_|_|  \__,_|\__|_|\___/|_| |_|
#                                                                                               __/ |                                  
#                                                                                              |___/                                  

environment = gym.make('Taxi-v3')
#    __  __       _           _                       
#   |  \/  |     (_)         | |                      
#   | \  / | __ _ _ _ __     | |     ___   ___  _ __  
#   | |\/| |/ _` | | '_ \    | |    / _ \ / _ \| '_ \ 
#   | |  | | (_| | | | | |   | |___| (_) | (_) | |_) |
#   |_|  |_|\__,_|_|_| |_|   |______\___/ \___/| .__/ 
#                                              | |    
#                                              |_|    


stepResult = []
rewardResult = []

cpt = 0
#epoch_number = 1000
epsilon = 0.2
alpha = 0.7
gamma = 0.7


for epoch_number in np.linspace(mail["training_number"]["start"], mail["training_number"]["end"], mail["training_number"]["steps"]):
    random.seed(seed)
    environment.reset(seed=seed)

    # Learning QSA with Sarsa algorithme and epsilon greedy policy
    q_sa = Sarsa_epsilon_greedy(environment, epsilon, alpha, gamma, int(epoch_number))
   # environment_space_length: int = environment.observation_space.n # type: ignore
   # action_space_length: int = environment.action_space.n # type: ignore
   # q_sa = np.zeros(environment_space_length, action_space_length)

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

        toto = 0
        tata = 0
        # Use to print graphe 
        nameStep = 'Step_'
        nameStep = nameStep + str(int(epoch_number))
        action = np.argmax(q_sa[state])

        while not stop:
            '''
               Run the game 
            '''
            step += 1
            
            # next_action = policy(next_state, epsilon)
            next_action = np.argmax(q_sa[state])
            state, reward, done, trunc, info = environment.step(next_action)

     
            # If we have a reward, it means that our outcome is a success
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



# Stok JSON data
with open(output_file, 'w') as the_file:
# Serializing json
# Globally, may be faster here
# See https://stackoverflow.com/a/57087055
    json_object = json.dumps(stepResult, indent=4)
    the_file.write(json_object)



##########################################################################################################
#    
#                                            To display graph 
#    
##########################################################################################################
#stepGraph = pd.DataFrame(stepResult)
#print(stepGraph)

#seaborn.boxplot(stepGraph)
#plt.ylim(-10, 30)
#plt.show()

rewardGraph = pd.DataFrame(rewardResult)
print(rewardGraph)
seaborn.boxplot(rewardGraph)
plt.ylim(-150, 10)
plt.show()





