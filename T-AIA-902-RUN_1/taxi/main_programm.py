from src.func_main_programm import func_mode

aleatoire_episode = input("Souhaitez-vous lancer le programme avec des épisodes aléatoires ? \n - NON : Tapez 0 \n - OUI : Tapez 1\n\n\n")


if(aleatoire_episode == "1" ):
    
    print("Nous lançons le programme avec des episodes aléatoires \n")


    mode = input("Choisissez le mode de lancement : \n - Tapez 1 pour le mode Utilisateur\n - Tapez 2 pour le mode Limité\n")
   
    if(mode =="1"):
      print("\n\nVous avez choisi le mode Utilisateur. \n")
      epoch_number = input("Donnez le nombre d'episode pour l'entrainement :   ")
      test_epoch = input("Donnez le nombre d'episode pour le test :   ")

      print("\nchoississez maintanant les valeurs parametres:   \n")
      alpha = input("\nDonnez la valeur d'Alpha :   ")
      gamma = input("\nDonnez la valeur de Gamma :   ")

      print("\nwait ...")

      func_mode(aleatoire_episode, int(test_epoch), int(epoch_number),0.1, float(alpha),  float(gamma))
    elif (mode =="2") :
       print("\n\nVous avez choisi le mode Limité. \n")
       epoch_number = input("Donnez le nombre d'episode pour l'entrainement :   ")
       test_epoch = input("Donnez le nombre d'episode pour le test :   ")

       print("\nwait ...")
   
       func_mode(aleatoire_episode,int(test_epoch), int(epoch_number), 0.1, 0.42,  0.58)

    else:
       print("Vous n'avez saisi ni 1 ni 2.")


elif(aleatoire_episode == "0"):
    mode = input("\nChoisissez le mode de lancement : \n - Tapez 1 pour le mode Utilisateur\n - Tapez 2 pour le mode Limité\n")
   
    if(mode =="1"):
      print("\n\nVous avez choisi le mode Utilisateur. \n")
      epoch_number = input("Donnez le nombre d'episode pour l'entrainement :   ")
      test_epoch = input("Donnez le nombre d'episode pour le test :   ")

      print("\nchoississez maintanant les valeurs parametres:   \n")
      epsilon = input("Donnez la valeur d'Epsilon :   ")
      alpha = input("\nDonnez la valeur d'Alpha :   ")
      gamma = input("\nDonnez la valeur de Gamma :   ")

      print("\nwait ...")

      func_mode(aleatoire_episode, int(test_epoch), int(epoch_number), float(epsilon), float(alpha),  float(gamma))
    elif (mode =="2") :
       print("\n\nVous avez choisi le mode Limité. \n")
       epoch_number = input("Donnez le nombre d'episode pour l'entrainement :   ")
       test_epoch = input("Donnez le nombre d'episode pour le test :   ")

       print("\nwait ...")

      #les valeurs optimales epsilon : 0.396, alpha : 0.78, gamma : 0.78
   
       func_mode(aleatoire_episode, int(test_epoch), int(epoch_number), 0.393 , 0.78,  0.78)

    else:
       print("Vous n'avez saisi ni 1 ni 2.")
else :
   print("Vous n'avez saisi ni 0 ni 1.")



