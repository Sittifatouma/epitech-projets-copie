SARS : https://www.kaggle.com/code/viznrvn/rl-frozenlake-with-sarsa

Initialize state_action_vals (an array of shape states x actions (16 x 4))
Repeat for each episode:
    Select action A and state S (epsilon-greedy)
    Repeat for each step:
        Perform action A, observe reward R and next state S'
        Choose next action A' using the current policy Q (epsilon-greedy)
        delta = R + gamma * state_action_vals[S'][A'] - state_action_vals[S][A]
        state_action_vals[S][A] = state_action_vals[S][A] + alpha * delta
        S=S', A=A'
until S is terminal