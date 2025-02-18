import cv2
from matplotlib import pyplot as plt
from sklearn.metrics.pairwise import pairwise_distances
import numpy as np
from keras.models import load_model
import os
import csv
from sklearn.neighbors import NearestNeighbors

def detect_faces_emotions(image_path):
    classCascade = cv2.CascadeClassifier(r'visage\ressources\haarcascade_frontalface_alt2.xml')
    profile_cascade = cv2.CascadeClassifier(r'visage\ressources\haarcascade_profileface.xml')
    emotion_model = load_model(r"/Users/dimitriraymond/Documents/Epitech/Semestre 2/DAT/github/gi/T-DAT-902-RUN_1/visage/ressources/FER_model.h5")

    # Réinitialiser les listes pour les informations de l'image actuelle
    tab_face = []
    emovisages = []
    print(image_path)

    # Charger l'image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Effectuer la détection des visages
    faces = classCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Ajouter les coordonnées des visages détectés à la liste
    for (x, y, w, h) in faces:
        tab_face.append((x, y, x+w, y+h))

    # Effectuer la détection des visages de profil
    profiles = profile_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Ajouter les coordonnées des visages de profil détectés à la liste
    for (x, y, w, h) in profiles:
        tab_face.append((x, y, x+w, y+h))

    # Inverser l'image en niveaux de gris
    width = gray.shape[1]
    gray2 = cv2.flip(gray, 1)

    # Effectuer la détection des visages de profil inversés
    profiles_inv = profile_cascade.detectMultiScale(
        gray2,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Ajouter les coordonnées des visages de profil inversés détectés à la liste
    for (x, y, w, h) in profiles_inv:
        tab_face.append((width - (x + w), y, width - x, y + h))

    # Vérifier s'il y a des visages détectés
    if len(tab_face) != 0:
        # Vérifier la similarité des coordonnées des visages pour supprimer les doublons
        unique_faces = []
        for (x1, y1, x2, y2) in tab_face:
            is_duplicate = False
            for (ux1, uy1, ux2, uy2) in unique_faces:
                dist = pairwise_distances([[x1, y1, x2, y2]], [[ux1, uy1, ux2, uy2]], metric='euclidean')
                if dist < 50:  # Seuil de similarité pour considérer les visages comme identiques
                    is_duplicate = True
                    break
            if not is_duplicate:
                unique_faces.append((x1, y1, x2, y2))

        # Obtenir les émotions pour chaque visage unique
        for (x1, y1, x2, y2) in unique_faces:
            face_gray = gray[y1:y2, x1:x2]
            face_resized = cv2.resize(face_gray, (48, 48))
            face_normalized = face_resized.astype("float") / 255.0
            face_array = np.expand_dims(face_normalized, axis=0)

            prediction = emotion_model.predict(face_array)[0]
            max_index = np.argmax(prediction)
            emotions = ["Angry", "Disgust", "Fear", "Happy", "Sad", "Surprise", "Neutral"]
            emotion = emotions[max_index]
            emovisages.append(emotion)

        # Dessiner les rectangles autour des visages détectés
        for (x, y, x2, y2) in unique_faces:
            cv2.rectangle(image, (x, y), (x2, y2), (0, 255, 0), 2)

        # Afficher les émotions détectées
        for i, (x1, y1, x2, y2) in enumerate(unique_faces):
            text = emovisages[i]
            cv2.putText(image, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Convertir l'image en un format compatible avec l'affichage web
    _, image_encoded = cv2.imencode('.png', image)
    image_data = image_encoded.tobytes()

    return {'image': image_data, 'emotions': emovisages}




def get_image_colors(image_path):
    # Charger l'image avec OpenCV
    image = cv2.imread(image_path)

    # Convertir l'image de BGR à RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Redimensionner l'image pour accélérer le calcul de l'histogramme
    resized_image = cv2.resize(image_rgb, (100, 100), interpolation=cv2.INTER_AREA)

    # Aplatir l'image en un tableau 2D
    flattened_image = resized_image.reshape((-1, 3))

    # Calculer l'histogramme des couleurs
    histogram = np.zeros((256, 256, 256), dtype=np.uint8)
    for pixel in flattened_image:
        histogram[pixel[0], pixel[1], pixel[2]] += 1

    # Trouver les indices des deux pixels les plus fréquents dans l'histogramme
    indices_max = np.argsort(histogram.flatten())[:-3:-1]
    couleurs_dominantes = np.unravel_index(indices_max, histogram.shape)
    
    # Convertir les couleurs dominantes en format approprié
    couleurs_dominantes = np.transpose(couleurs_dominantes).tolist()

    return couleurs_dominantes

def convertir_en_couleur_nominale(couleur_rgb):
    # Définir une liste de couleurs nominatives
    couleurs_nominatives = ['noir', 'blanc', 'gris', 'rouge', 'vert', 'bleu', 'jaune', 'orange', 'rose', 'violet', 'marron']

    # Définir les valeurs RVB correspondantes aux couleurs nominatives
    couleurs_rgb = np.array([
        [0, 0, 0],     # noir
        [255, 255, 255],   # blanc
        [128, 128, 128],   # gris
        [255, 0, 0],   # rouge
        [0, 255, 0],   # vert
        [0, 0, 255],   # bleu
        [255, 255, 0],   # jaune
        [255, 165, 0],   # orange
        [255, 192, 203],   # rose
        [128, 0, 128],   # violet
        [165, 42, 42]   # marron
    ])

    # Créer un modèle Nearest Neighbors et ajuster les données RVB
    knn = NearestNeighbors(n_neighbors=1)
    knn.fit(couleurs_rgb)

    # Trouver le voisin le plus proche des valeurs RVB données
    _, indices_plus_proches = knn.kneighbors(couleur_rgb)
    indices_plus_proches = indices_plus_proches.flatten()

    # Récupérer les noms de couleur correspondant aux indices
    couleurs_nominatives = [couleurs_nominatives[indice] for indice in indices_plus_proches]

    return couleurs_nominatives

def get_main_secondary_colors(image_path):
    # Obtenir les couleurs dominantes de l'image
    couleurs_dominantes = get_image_colors(image_path)

    # Convertir les couleurs dominantes en couleurs nominatives
    couleurs_nominatives = []
    for couleur_rgb in couleurs_dominantes:
        couleur_nominale = convertir_en_couleur_nominale([couleur_rgb])
        couleurs_nominatives.append(couleur_nominale)

    return couleurs_nominatives


def detect_faces_emotions_v2(image_path):
    classCascade = cv2.CascadeClassifier(r'visage\ressources\haarcascade_frontalface_alt2.xml')
    profile_cascade = cv2.CascadeClassifier(r'visage\ressources\haarcascade_profileface.xml')
    emotion_model = load_model(r'visage\ressources\FER_model.h5')

    # Réinitialiser les listes pour les informations de l'image actuelle
    tab_face = []
    emovisages = ["Neutral"]
    num_faces = 0
    print(image_path)

    # Charger l'image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Effectuer la détection des visages
    faces = classCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Ajouter les coordonnées des visages détectés à la liste
    for (x, y, w, h) in faces:
        tab_face.append((x, y, x+w, y+h))

    # Effectuer la détection des visages de profil
    profiles = profile_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Ajouter les coordonnées des visages de profil détectés à la liste
    for (x, y, w, h) in profiles:
        tab_face.append((x, y, x+w, y+h))

    # Inverser l'image en niveaux de gris
    width = gray.shape[1]
    gray2 = cv2.flip(gray, 1)

    # Effectuer la détection des visages de profil inversés
    profiles_inv = profile_cascade.detectMultiScale(
        gray2,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Ajouter les coordonnées des visages de profil inversés détectés à la liste
    for (x, y, w, h) in profiles_inv:
        tab_face.append((width - (x + w), y, width - x, y + h))

    # Vérifier s'il y a des visages détectés
    if len(tab_face) != 0:
        
        # Vérifier la similarité des coordonnées des visages pour supprimer les doublons
        unique_faces = []
        emovisages= []
        for (x1, y1, x2, y2) in tab_face:
            is_duplicate = False
            for (ux1, uy1, ux2, uy2) in unique_faces:
                dist = pairwise_distances([[x1, y1, x2, y2]], [[ux1, uy1, ux2, uy2]], metric='euclidean')
                if dist < 50:  # Seuil de similarité pour considérer les visages comme identiques
                    is_duplicate = True
                    break
            if not is_duplicate:
                unique_faces.append((x1, y1, x2, y2))

        # Obtenir les émotions pour chaque visage unique
        for (x1, y1, x2, y2) in unique_faces:
            face_gray = gray[y1:y2, x1:x2]
            face_resized = cv2.resize(face_gray, (48, 48))
            face_normalized = face_resized.astype("float") / 255.0
            face_array = np.expand_dims(face_normalized, axis=0)

            prediction = emotion_model.predict(face_array)[0]
            max_index = np.argmax(prediction)
            emotions = ["Angry", "Disgust", "Fear", "Happy", "Sad", "Surprise", "Neutral"]
            emotion = emotions[max_index]
            emovisages.append(emotion)

        # Dessiner les rectangles autour des visages détectés
        for (x, y, x2, y2) in unique_faces:
            cv2.rectangle(image, (x, y), (x2, y2), (0, 255, 0), 2)

        # Afficher les émotions détectées
        for i, (x1, y1, x2, y2) in enumerate(unique_faces):
            text = emovisages[i]
            cv2.putText(image, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        num_faces = len(unique_faces)

    # Convertir l'image en un format compatible avec l'affichage web
    _, image_encoded = cv2.imencode('.png', image)
    image_data = image_encoded.tobytes()

      # Nombre de visages détectés

    return {'image': image_data, 'emotions': emovisages, 'num_faces': num_faces}

def detect_faces_emotions_v3(image_path):
    classCascade = cv2.CascadeClassifier(r'visage\ressources\haarcascade_frontalface_alt2.xml')
    profile_cascade = cv2.CascadeClassifier(r'visage\ressources\haarcascade_profileface.xml')
    emotion_model = load_model(r'visage\ressources\FER_model.h5')

    # Réinitialiser les listes pour les informations de l'image actuelle
    tab_face = []
    emovisages = ["Neutral"]
    num_faces = 0
    face_position = "Neutral"  

    # Charger l'image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Effectuer la détection des visages
    faces = classCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Ajouter les coordonnées des visages détectés à la liste
    for (x, y, w, h) in faces:
        tab_face.append((x, y, x+w, y+h))

    # Effectuer la détection des visages de profil
    profiles = profile_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Ajouter les coordonnées des visages de profil détectés à la liste
    for (x, y, w, h) in profiles:
        tab_face.append((x, y, x+w, y+h))

    # Inverser l'image en niveaux de gris
    width = gray.shape[1]
    gray2 = cv2.flip(gray, 1)

    # Effectuer la détection des visages de profil inversés
    profiles_inv = profile_cascade.detectMultiScale(
        gray2,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Ajouter les coordonnées des visages de profil inversés détectés à la liste
    for (x, y, w, h) in profiles_inv:
        tab_face.append((width - (x + w), y, width - x, y + h))

    # Vérifier s'il y a des visages détectés
    if len(tab_face) != 0:
        
        # Vérifier la similarité des coordonnées des visages pour supprimer les doublons
        unique_faces = []
        emovisages= []
        for (x1, y1, x2, y2) in tab_face:
            is_duplicate = False
            for (ux1, uy1, ux2, uy2) in unique_faces:
                dist = pairwise_distances([[x1, y1, x2, y2]], [[ux1, uy1, ux2, uy2]], metric='euclidean')
                if dist < 50:  # Seuil de similarité pour considérer les visages comme identiques
                    is_duplicate = True
                    break
            if not is_duplicate:
                unique_faces.append((x1, y1, x2, y2))

        # Obtenir les émotions pour chaque visage unique
        for (x1, y1, x2, y2) in unique_faces:
            face_gray = gray[y1:y2, x1:x2]
            face_resized = cv2.resize(face_gray, (48, 48))
            face_normalized = face_resized.astype("float") / 255.0
            face_array = np.expand_dims(face_normalized, axis=0)

            prediction = emotion_model.predict(face_array)[0]
            max_index = np.argmax(prediction)
            emotions = ["Angry", "Disgust", "Fear", "Happy", "Sad", "Surprise", "Neutral"]
            emotion = emotions[max_index]
            emovisages.append(emotion)

        # Dessiner les rectangles autour des visages détectés
        for (x, y, x2, y2) in unique_faces:
            cv2.rectangle(image, (x, y), (x2, y2), (0, 255, 0), 2)

        # Afficher les émotions détectées
        for i, (x1, y1, x2, y2) in enumerate(unique_faces):
            text = emovisages[i]
            cv2.putText(image, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        num_faces = len(unique_faces)

        if num_faces > 0:
            face_positions = [((y1 + y2) / 2) < gray.shape[0] / 2 for (_, y1, _, y2) in unique_faces]
            if all(face_positions):
                face_position = "haut"
            elif not any(face_positions):
                face_position = "bas"
        
        if len(emovisages) == 0:
                face_position = "Neutral"
        elif len(emovisages) == 1:
                face_position = "Haut" if (y1 + y2) / 2 < gray.shape[0] / 2 else "Bas"
                
        else:
                emotions = ["Neutral"] * min(2, len(emovisages))  # Initialiser les émotions à "Neutral" pour les deux premiers visages ou moins
                face_positions = ["Neutral"] * min(2, len(emovisages))  # Initialiser les positions à "Neutral" pour les deux premiers visages ou moins

                visages_tries = sorted(unique_faces, key=lambda rect: (rect[2] - rect[0]) * (rect[3] - rect[1]), reverse=True)[:2]  # Sélectionner les deux plus grands visages

                for i, visage in enumerate(visages_tries):
                   #print("i = ",i)
                   #print("visage = ",visage)
                   x1, y1, x2, y2 = visage
                   face_positions[i] = "Haut" if (y1 + y2) / 2 < gray.shape[0] / 2 else "Bas"
                   emotions[i] = emovisages[unique_faces.index(visage)]
                emovisages=[]
                emovisages = emotions
                face_position = face_positions[0]

    # Convertir l'image en un format compatible avec l'affichage web
    _, image_encoded = cv2.imencode('.png', image)
    image_data = image_encoded.tobytes()

    return {'image': image_data, 'emotions': emovisages, 'num_faces': num_faces, 'face_position': face_position}


def in_number(Couleur1, couleur2, nb_visages, position_visage,	emotion1, emotion2, cluster, number):
    data = []
    color_mapping = {
    'noir': '0',
    'blanc': '1',
    'gris': '2',
    'rose': '3',
    'orange': '4',
    'marron': '5',
    'bleu': '6',
    'violet': '7',
    'rouge': '8',
    'jaune': '9',
    'vert': '10'
    }
    postion_mapping = {
    'Neutral': '0',
    'Haut': '1',
    'Bas': '2'
    }
    emotion_mapping = {
        'Neutral': 0, 
        'Sad': 1, 
        'Happy': 2, 
        'Surprise': 3, 
        'Angry': 4, 
        'Fear': 5
        }
    data.append(color_mapping.get(Couleur1, 0))
    data.append(color_mapping.get(couleur2, 0))
    data.append(nb_visages)
    data.append(postion_mapping.get(position_visage,0))
    data.append(emotion_mapping.get(emotion1,0))
    data.append(emotion_mapping.get(emotion2,0))
    
    
    data.append(0)
    data.append(0)

    return data



