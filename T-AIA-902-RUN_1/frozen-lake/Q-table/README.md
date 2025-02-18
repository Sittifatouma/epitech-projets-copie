frozenLake_qTable.pkl est un fichier qui contient la Q table généré à partir de Epsilon-Greedy.py

forPlay.py prend en entrée la Q table en entrée et effectue le frozen lake


(S_t, A_t) <--  Q(S_t, A_t) + alpha * [ R_{t+1} + gamma * max_{a} Q(S_{t+1}, a) - Q(S_t, A_t) \right]\]

au début , on va exploer et mettre à jour la Q-table

ensuite on va faire de l'exploitation

Hyper paramètre: 
alpha = learning rate => quelle vitesse on va apprendre entre 0 et 1. A quelle fréquence on va mettre à jour la Q-table
gamma = futur récompense, discount factor, entre 0 et 1. Si 0 on ne voit pas trop sur le long terme.

Limit => si info en continue => Q-table infini 


