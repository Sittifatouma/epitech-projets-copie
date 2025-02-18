import random
import gymnasium as gym
import numpy as np
import json

from src.Algorithms.SARSA import SARSA
from src.Algorithms.Q_learning import Q_learning

from src.Classes.Policy import Policy
from src.Classes.Agent import Agent
from src.Functions.run import run_static

import pandas as pd
import seaborn
import matplotlib.pyplot as plt

#    ____             _                     _____             __ _                       _   _             
#   |  _ \           | |                   / ____|           / _(_)                     | | (_)            
#   | |_) | __ _  ___| | ___   _ _ __     | |     ___  _ __ | |_ _  __ _ _   _ _ __ __ _| |_ _  ___  _ __  
#   |  _ < / _` |/ __| |/ / | | | '_ \    | |    / _ \| '_ \|  _| |/ _` | | | | '__/ _` | __| |/ _ \| '_ \ 
#   | |_) | (_| | (__|   <| |_| | |_) |   | |___| (_) | | | | | | | (_| | |_| | | | (_| | |_| | (_) | | | |
#   |____/ \__,_|\___|_|\_\\__,_| .__/     \_____\___/|_| |_|_| |_|\__, |\__,_|_|  \__,_|\__|_|\___/|_| |_|
#                               | |                                 __/ |                                  
#                               |_|                                |___/                                  

output_file = "data/testFL.json"
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
grid_steps = 1
mail = {
    "training_number":{
        "start": 2000,
        "end": 3000,
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
#desc=["SFFF", "FHFH", "FFFH", "HFFG"] # Same as the map called "4*4"
#environment = gym.make('FrozenLake-v1', desc=desc, is_slippery=True, render_mode="rgb_array")
environment = gym.make('Taxi-v3')
#    __  __       _           _                       
#   |  \/  |     (_)         | |                      
#   | \  / | __ _ _ _ __     | |     ___   ___  _ __  
#   | |\/| |/ _` | | '_ \    | |    / _ \ / _ \| '_ \ 
#   | |  | | (_| | | | | |   | |___| (_) | (_) | |_) |
#   |_|  |_|\__,_|_|_| |_|   |______\___/ \___/| .__/ 
#                                              | |    
#                                              |_|    


result = []
cpt = 0
#epoch_number = 1000
epsilon = 0.9
alpha = 0.7
gamma = 0.7




for epoch_number in np.linspace(mail["training_number"]["start"], mail["training_number"]["end"], mail["training_number"]["steps"]):
    random.seed(seed)
    environment.reset(seed=seed)
    q_sa = Q_learning(environment, epsilon, alpha, gamma, int(epoch_number))
    with open(qsa_file, 'w') as the_file2:
        json_object = json.dumps(q_sa.tolist(), indent=4)
        the_file2.write(json_object)

    deterministic_policy = Policy.buildOptimalPolicyFrom(q_sa)
    success = 0
    random.seed(seed)
    environment.reset(seed=seed)

    for epoch in range(test_epoch):
        test_agent = Agent(deterministic_policy)

        test_agent.current_state_index = environment.reset()[0] # Initial state
        stop = False    
        point = 0
        step = 0
        while not stop:
            '''
            While Agent is not stopped
            Agent perform the action
            Agent pick an action from its state and its policy
            Agent update its trajectory: action taken, new state, new reward
            Update the stop condition if Goal reached or terminated
            '''
            step += 1
            next_action_index = test_agent.pick_next()
            observation, reward, terminated, truncated, info = environment.step(next_action_index)
            test_agent.trajectory.append(observation, next_action_index, float(reward))
            test_agent.current_state_index = observation

            if reward:
              point += reward
              if (reward == 20):
                success += 1
              if (reward == -10):
                print('faillllllllllllllllllllllllllllllllllllllllllllll')
            stop = terminated or truncated  
            if (stop):
              print("[End of game epoch = {}] - Total point = {} - Tot Step = {}".format(epoch, point, step))
              result.append({
                  "Game_Number": epoch,
                  "Steps": step,
                  "Points": point,
                  "Training_number": epoch_number
                 })



    print("[Tot Episodes = {}] - Succes = {}".format(test_epoch, success))             
##
#result.append({
#    "success/epoch": success / test_epoch,
#    "epoch_number": epoch_number,
#    "epsilon": epsilon,
#    "alpha": alpha,
#    "gamma": gamma,
#    "q_sa": q_sa.tolist() # tolist() required for json dump
#})


with open(output_file, 'w') as the_file:
    # Serializing json
    # Globally, may be faster here
    # See https://stackoverflow.com/a/57087055
    json_object = json.dumps(result, indent=4)
    the_file.write(json_object)


# To display graph : 
big_df = pd.DataFrame(result)
print(big_df)
seaborn.lineplot(big_df, x = "Game_Number", y= "Points", hue="Training_number").tick_params(axis='x', rotation=90)
plt.show()
            





