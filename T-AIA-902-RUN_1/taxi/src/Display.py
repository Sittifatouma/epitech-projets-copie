import numpy as np
import time

def display_data(total, start, epoch_training, nbsuccess, mean_steps, max_steps, mean_result):
      print()
      print(
          "[{} LOOP DONE - Succes = {} - {} SECONDES] - [{} EPOCH ] Mean Steps Per Loop: {} - Min Steps For a Loop: {} - Max Steps For a Loop: {} - Mean Reward Per Loop: {}"
          .format(total, nbsuccess,  np.round(time.time() - start, 4),
                  epoch_training, 
                  np.round(mean_steps / total, 2),
                    np.min(max_steps),
                      np.max(max_steps),
                  np.round(mean_result / total, 2)))
    
