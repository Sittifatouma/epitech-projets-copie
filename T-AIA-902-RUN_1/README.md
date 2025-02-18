# Projet T-AIA-902-RUN_1 -  Résolution du problème du Taxi Driver


## Définition:
Ce projet vise à résoudre le problème classique du Taxi Driver à l'aide de différentes approches **d'apprentissage par renforcement**, notamment les algorithmes Q-Learning, SARSA, Monte Carlo et une approche brute force. L'objectif est de former un agent intelligent capable de naviguer dans un environnement complexe et d'effectuer des actions optimales pour transporter des passagers vers leur destination.

## Description du problème

Le problème du Taxi Driver consiste à déplacer un taxi dans un environnement discret comprenant des rues et des emplacements pour les passagers et les destinations. L'objectif est de ramasser les passagers à leur emplacement actuel et de les déposer à leur destination respective en évitant les obstacles. Le taxi doit prendre les décisions appropriées pour optimiser le temps et les mouvements nécessaires pour effectuer les déplacements.
Méthodes d'apprentissage

## Méthode:

Nous utilisons les méthodes suivantes pour résoudre le problème du Taxi Driver :

  **Q-Learning** : Cet algorithme d'apprentissage par renforcement utilise une fonction de valeur Q pour estimer la valeur des états-action et détermine la meilleure politique à suivre.

  **SARSA** : Également connu sous le nom de State-Action-Reward-State-Action, cet algorithme apprend une politique basée sur les états, les actions, les récompenses et les états futurs.

  **Monte Carlo** : Dans cette approche, nous évaluons les états et les états-actions en observant le taux de réussite après un épisode complet. Cela permet d'obtenir une estimation relative de la valeur des états et des actions.

  **Brute Force** : Cette méthode consiste à explorer toutes les combinaisons possibles d'actions pour trouver la meilleure politique en évaluant chaque état et action.

# Fichiers utiles

  >>ComparaisonEpochTrainingMonteCarlo.py: Ficher de test de l'algo Monte Carlo
  >>ComparaisonEpochTrainingQlearning.py : Ficher de test de l'algo Qlearning
  >>ComparaisonEpochTrainingSarsa.py : Ficher de test de l'algo Sarsa
  >>ComparaisonPolicy.py : Comparaison de différente policy
  >>BruteForce.py : Brute force pour résoudre le taxi driver

# Rapport de recherche
  
  Toute notre analyse se situe dans le pdf Rapport.pdf
  Lien: https://docs.google.com/document/d/1Sg6SZyO6j92xip4m0eZE30gAWvxKBNf803o5rb3oQt8/edit?usp=sharing

# Rejets
  Tout se qui ne se situe pas dans le dossier /taxi, et le travail que nous avons fait en amont pour comprendre les algorithmes d'apprentissages, ainsi que la correction proposée par l'intervenant de notre école pour la résolution du jeu frozen-lake