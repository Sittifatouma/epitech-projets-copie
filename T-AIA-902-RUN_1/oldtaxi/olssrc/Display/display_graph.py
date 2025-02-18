
import numpy as np
import json


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

#==========================================================================================================================================#
#=========================       To use loaded file QSA                                         ===========================================#
#==========================================================================================================================================#
with open("../../data/ComparaisonTrainingNumber.json", 'rb') as f:
   json_data = f.read()

# Parser le JSON et le convertir en une liste
result = json.loads(json_data)
# Convertir la liste en une matrice QSA (numpy array)
q_sa = np.array(result)

#==========================================================================================================================================#

# To display graph : 
big_df = pd.DataFrame(result)
print(big_df)
seaborn.lineplot(big_df, x = "Game_Number", y= "Points", hue="Training_number").tick_params(axis='x', rotation=90)
plt.ylim(-30, 30) 
plt.show()
            