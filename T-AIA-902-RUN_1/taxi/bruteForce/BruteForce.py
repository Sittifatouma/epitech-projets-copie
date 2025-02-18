import numpy as np
import argparse
import time
import gym
import sys

import pandas as pd
import seaborn
import matplotlib.pyplot as plt


def play(env=gym.make("Taxi-v3", render_mode="human"), is_debug: bool = False, episode: int = 1) -> tuple[int, int]:
    total_steps = 0
    total_reward = 0
    passenger_found = False

    state = env.reset()

    while True:
        stop = False
        while not stop:  #int(state / 100) != 0:
            new_state, reward, toto, tata, titi = env.step(1)

            if state == new_state:
                stop = True

            state = new_state
            total_steps += 1
            total_reward += reward

        if is_debug:
            print("TOP reached")
        #    env.render()

        stop = False
        while not stop:  # int(state / 10) != 0:
            new_state, reward, _, _ , _= env.step(3)
            total_steps += 1
            total_reward += reward

            if new_state == state:

                for s in [0, 0, 3, 3, 1, 1]:
                    new_state, reward, _, _ , _ = env.step(s)
                    total_reward += reward
                    total_steps += 1

                stop = False
                while not stop:  #int(state / 100) != 0:
                    new_state, reward, _, _, _ = env.step(1)

                    if state == new_state:
                        stop = True

                    state = new_state
                    total_steps += 1
                    total_reward += reward

            state = new_state

################################################ TOP LEFT REACHED ################################################################
        if is_debug:
            print("Top left reached")
            #env.render()

        if not passenger_found:
            if is_debug:
                print("Attempting Pickup")
            new_state, reward, _, _ , _= env.step(4)
            total_reward += reward
            total_steps += 1
            state = new_state

            if reward == -1:
                passenger_found = True
               

                if is_debug:
                     print("Passenger found in top left")

        else:
            if is_debug:
                print("Attempting Dropoff")
            new_state, reward, done, _ , _= env.step(5)
            total_reward += reward
            total_steps += 1

            if done:
                if is_debug:
                    print("Passenger Dropped Off in top left")
                break

            else:
                if is_debug:
                    print("Damn -10 ... wrong dropped off in top left")
                new_state, reward, done, _, _ = env.step(4)
                total_reward += reward
                total_steps += 1


        for s in [0, 0, 0, 0]:
            new_state, reward, _, _ , _ = env.step(s)
            total_reward += reward
            total_steps += 1

################################################ BOTTOM LEFT REACHED ############################################################

        if is_debug:
            print("Bottom left reached ")
     #       env.render()

        if not passenger_found:
            if is_debug:
                print("Attempting Pickup")
            new_state, reward, _, _, _ = env.step(4)
            total_reward += reward
            total_steps += 1

            if reward == -1:
                passenger_found = True

                if is_debug:
                    print("Passenger Found in bottom left")

        else:
            if is_debug:
                print("Attempting Dropped off")
            new_state, reward, done, _ , _ = env.step(5)
            total_reward += reward
            total_steps += 1

            if done:
                if is_debug:
                    print("Passenger Dropped Off in bottom left")

                break

            else:
                if is_debug:
                    print("Damn -10 ... wrong dropped off")
                new_state, reward, done, _, _ = env.step(4)
                total_reward += reward
                total_steps += 1


        for s in [1, 1, 2, 2, 2, 2, 1, 1]:
            new_state, reward, _, _ , _  = env.step(s)
            total_reward += reward
            total_steps += 1

################################################ TOP RIGHT REACHED #############################################################

        if is_debug:
            print("Top right reached")
            #env.render()

        if not passenger_found:
            if is_debug:
                print("Attempting Pickup")
            new_state, reward, _, _, _ = env.step(4)
            total_reward += reward
            total_steps += 1

            if reward == -1:
                passenger_found = True

                if is_debug:
                    print("Passenger Found in top right")

        else:
            if is_debug:
                print("Attempting Dropoff")
            new_state, reward, done, _ , _ = env.step(5)
            total_reward += reward
            total_steps += 1

            if done:


                if is_debug:
                    print("Passenger Dropped Off in top right")

                break

            else:
                if is_debug:
                    print("Damn -10 ... wrong dropped off")
                new_state, reward, done, _, _ = env.step(4)
                total_reward += reward
                total_steps += 1


        for s in [0, 0, 0, 0, 3]:
            new_state, reward, _, _ , _ = env.step(s)
            total_reward += reward
            total_steps += 1

################################################ BOTTOM RIGHT REACHED ##########################################################

        if is_debug:
            print("Bottom right reached")
            #env.render()

        if not passenger_found:
            if is_debug:
                print("Attempting Pickup")

            new_state, reward, _, _ , _ = env.step(4) 

            total_reward += reward
            total_steps += 1

            if reward == -1:
                passenger_found = True

                if is_debug:
                    print("Passenger Found in bottom right")

        else:
            if is_debug:
                print("Attempting Dropoff")
            new_state, reward, done, _, _ = env.step(5)
            total_reward += reward
            total_steps += 1

            if done:
                if is_debug:
                    print("Passenger Dropped Off in bottom right")

                break


            else:
                if is_debug:
                    print("Damn -10 ... wrong dropped off")
                new_state, reward, done, _, _ = env.step(4)
                total_reward += reward
                total_steps += 1


    print("Episode n°{} [SUCCESSFUL]  STEPS TOTAL = {} /  REWARD TOTAL = {}".format(episode, total_steps, total_reward))
    return total_steps, total_reward


def display_data(total, start, mean_steps, mean_result):
    print()
    print(
        "[{} LOOP DONE -  {} SECONDES] - Mean Steps Per Loop: {} - Min Steps For a Loop: {} - Max Steps For a Loop: {} - Mean Reward Per Loop: {} - Mean Time Per Loop: {}s"
        .format(total, np.round(time.time() - start, 4),
                np.round(mean_steps / total, 2),
                  np.min(max_steps),
                     np.max(max_steps),
                np.round(mean_result / total, 2),
                np.round((time.time() - start) / total), 6))


def error_args(args):
    attempt = args.attempt

    if attempt < 0:
        return 1, "Time can not be negative or null."
    
    return 0, ""


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Create a simple brute force to solve taxi driver"
    )

    parser.add_argument("-t",
                        "--attempt",
                        type=int,
                        help="How many times to play the game?",
                        default=1)
    
    parser.add_argument("-d",
                    "--debug",
                    type=bool,
                    help="Do you want to print some log?",
                    default=False)
    

    parser.add_argument("-v",
                "--visualize",
                type=bool,
                help="Do you want to see the screen?",
                default=False)

    args = parser.parse_args()

    code, msg = error_args(args)

    # Controle nb episode
    if code != 0:
        print("[ERROR] - {}".format(msg))
        sys.exit(1)

    # Retreive visualization information
    if type(args.visualize) is bool and  args.visualize == True:
        env = gym.make('Taxi-v3', render_mode="human")
    else:
       env = gym.make("Taxi-v3")

    # Setting debug mod 
    if type(args.debug) is bool and  args.debug == True:
       is_debug = True
    else:
       is_debug = False

    start = time.time()

    # use for final calculation
    mean_steps = 0
    mean_result = 0
    max_steps = []

    result = []


    
    for episode in range(args.attempt):
        steps, reward = play(env=env, is_debug=is_debug, episode=episode)
        max_steps.append(steps)
        mean_steps += steps
        mean_result += reward
        result.append({
            #      "Game_Number": episode,
                  "Steps": steps,
                  "Reward": reward
                 })

    display_data(args.attempt, start, mean_steps, mean_result)



    big_df = pd.DataFrame(result)
    print(big_df)
    seaborn.boxplot(big_df, showmeans=True, meanline=True, whis=[0, 100])
  #  seaborn.lineplot(big_df, x = "Game_Number", y= "Points").tick_params(axis='x', rotation=90)


    # Affichage du graphique
    plt.show()
    print("END")