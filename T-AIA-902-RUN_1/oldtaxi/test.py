import pickle
import random
import gymnasium as gym
from nptyping import Float, NDArray, Shape
import numpy as np
import json

from src.Algorithms.Monte_Carlo import MC

from src.Classes.Policy import Policy
from src.Classes.Agent import Agent
from src.Functions.run import run_static

#    ____             _                     _____             __ _                       _   _             
#   |  _ \           | |                   / ____|           / _(_)                     | | (_)            
#   | |_) | __ _  ___| | ___   _ _ __     | |     ___  _ __ | |_ _  __ _ _   _ _ __ __ _| |_ _  ___  _ __  
#   |  _ < / _` |/ __| |/ / | | | '_ \    | |    / _ \| '_ \|  _| |/ _` | | | | '__/ _` | __| |/ _ \| '_ \ 
#   | |_) | (_| | (__|   <| |_| | |_) |   | |___| (_) | | | | | | | (_| | |_| | | | (_| | |_| | (_) | | | |
#   |____/ \__,_|\___|_|\_\\__,_| .__/     \_____\___/|_| |_|_| |_|\__, |\__,_|_|  \__,_|\__|_|\___/|_| |_|
#                               | |                                 __/ |                                  
#                               |_|                                |___/                                  

print("start test.py")
output_file = "data/bbbbb.json"
qsa_file = "data/qsa-mc-100.json"

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
    "epoch_number":{
        "start": 25000,
        "end": 50000,
        "steps": grid_steps,
    }
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
#environment = gym.make('Taxi-v3', render_mode="human")
#environment = gym.make('Taxi-v3')
desc=["SFFF", "FHFH", "FFFH", "HFFG"] # Same as the map called "4*4"
environment = gym.make('FrozenLake-v1', desc=desc, is_slippery=True, render_mode="rgb_array")

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
#for epoch_number in np.linspace(mail["epoch_number"]["start"], mail["epoch_number"]["end"], mail["epoch_number"]["steps"]):
epoch_number = 3000
random.seed(seed)
environment.reset(seed=seed)

#==========================================================================================================================================#
#=========================       To load new QSA                                                ===========================================#
##==========================================================================================================================================#
q_sa = MC(environment, epoch_number = int(epoch_number))
#with open(qsa_file, 'w') as the_file2:
#    # Serializing json
    # Globally, may be faster here
    # See https://stackoverflow.com/a/57087055
#    json_object = json.dumps(q_sa.tolist(), indent=4)
#    the_file2.write(json_object)


#==========================================================================================================================================#
#=========================       To use loaded file QSA                                         ===========================================#
#==========================================================================================================================================#
#with open("data/qsa-mc-10000.json", 'rb') as f:
#   json_data = f.read()

# Parser le JSON et le convertir en une liste
#q_sa_list = json.loads(json_data)
# Convertir la liste en une matrice QSA (numpy array)
#q_sa = np.array(q_sa_list)

#==========================================================================================================================================#

#print(q_sa)
	

deterministic_policy = Policy.buildOptimalPolicyFrom(q_sa)
print(deterministic_policy.state_dimension)
print(deterministic_policy.action_dimension)
print(deterministic_policy._next_function)
success = 0
random.seed(seed)
environment.reset(seed=seed)
for epoch in range(test_epoch):
    test_agent = Agent(deterministic_policy)
    run_static(environment = environment, agent = test_agent)
    print("success" + str(success))
    print("test_agent current_state_index:" + str(test_agent.current_state_index))
    # On check qu'on est bien sur la case 15 pour savoir si c'est un succès
    success += test_agent.current_state_index == (environment.observation_space.n - 1) # type: ignore                   
result.append({
    "algorithm": "MC",
    "success": success / test_epoch,
    "epoch_number": epoch_number,
    "q_sa": q_sa.tolist() # tolist() required for json dump
})

with open(output_file, 'w') as the_file:
    # Serializing json
    # Globally, may be faster here
    # See https://stackoverflow.com/a/57087055
    json_object = json.dumps(result, indent=4)
    the_file.write(json_object)
cpt += 1
print(str(cpt) + "/" + str(mail["epoch_number"]["steps"]))