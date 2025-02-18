import random
import gymnasium as gym
import numpy as np
import json
from src.Q_learning_policy import Q_learning_policy
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
test_epoch = 10
grid_steps = 10
mail = {
    "training_number":{
        "start": 1500,
        "end": 1500,
        "steps": grid_steps,
    },
    "epsilon": {
        "start": 0.34,
        "end": 0.34,
        "steps": grid_steps,
    },
    "alpha": {
        "start": 0.71,
        "end": 0.71,
        "steps": grid_steps,
    },
    "gamma": {
        "start": 0.58,
        "end": 0.58,
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


for epoch_number in np.linspace(mail["training_number"]["start"], mail["training_number"]["end"], mail["training_number"]["steps"]):
    for epsilon in np.linspace(mail["epsilon"]["start"], mail["epsilon"]["end"], mail["epsilon"]["steps"]):
        for alpha in np.linspace(mail["alpha"]["start"], mail["alpha"]["end"], mail["alpha"]["steps"]):
            for gamma in np.linspace(mail["gamma"]["start"], mail["gamma"]["end"], mail["gamma"]["steps"]):
                random.seed(seed)
                environment.reset(seed=seed)

                # Learning QSA with Q-learning algorithme and epsilon greedy policy
                q_sa = Q_learning_policy(environment, epsilon, alpha, gamma, int(epoch_number),'epsilon_greedy')

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
                    ## STEP ##
                    # nameStep = 'Step_'
                    # nameStep = nameStep + str(int(epoch_number))

                    ## EPSILON ##
                    r_epsilon = float(epsilon)
                    r_epsilon = "{:.3f}".format(r_epsilon)
                    resultEpsilon = str(r_epsilon)

                    ## ALPHA ##
                    r_alpha = float(alpha)
                    r_alpha = "{:.3f}".format(r_alpha)
                    resultAlpha = str(r_alpha)

                    ## GAMMA ##
                    r_gamma = float(gamma)
                    r_gamma = "{:.3f}".format(r_gamma)
                    resultGamma = str(r_gamma)
                    
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
                                "Success": point,
                                "Q_learning": "Q_learning",
                            })
                            max_steps.append(int(step))
                            mean_steps += step
                            mean_result += point


                # To summarize data for each loop
                display_data(test_epoch, start, success, gamma, mean_steps, max_steps,  mean_result)           



# Stok JSON data
with open(output_file, 'w') as the_file:
    json_object = json.dumps(stepResult, indent=4)
    the_file.write(json_object)



##########################################################################################################
#                                                                                                        #
#                                            To display graph                                            #
#                                                                                                        #
##########################################################################################################
#stepGraph = pd.DataFrame(stepResult)
#print(stepGraph)

#seaborn.boxplot(stepGraph)
#plt.ylim(-10, 30)
#plt.show()

rewardGraph = pd.DataFrame(rewardResult)
print(rewardGraph)
seaborn.boxplot(rewardGraph, y="Success", x="Q_learning")
plt.ylim(-20, 20)
plt.show()






