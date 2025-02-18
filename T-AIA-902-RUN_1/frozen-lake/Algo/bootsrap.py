import gym

# create Frozen Lake environment
env = gym.make('FrozenLake-v1')

# render the lake
env.render()

# initialize the environment
env.reset()

# loop through a fixed number of steps
for i in range(20):
    # sample a random action
    action = env.action_space.sample()
    
    # take the action and get the resulting state, reward, and done flag
    state, reward, done, _ = env.step(action)
    
    # print the current state, reward, and done flag
    print(f"Step {i}: state={state}, reward={reward}, done={done}")
    
    # if the done flag is True, restart the environment
    if done:
        env.reset()
        
# close the environment
env.close()


