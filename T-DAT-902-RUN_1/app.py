from flask import Flask, request, jsonify
from flask_cors import CORS
from data_interface import detect_faces_emotions_v3
from data_interface import get_main_secondary_colors
from data_interface import in_number
from model import model_
import os
import json

app = Flask(__name__)
CORS(app)


@app.route('/predict', methods=['POST'])
def predict():
    
    # Récupère le fichier envoyé par l'interface
    file = request.files['file']

    genre_prediction = make_prediction(file)

    # Convertir le tableau NumPy en liste
    genre_prediction['image'] = list(genre_prediction['image'])

    genre_prediction['couleurs'] = [couleur[0] for couleur in genre_prediction['couleurs']]
    genre_prediction['emotions'] = genre_prediction['emotions']

    # Retourner la prédiction au format JSON
    return json.dumps({'prediction': genre_prediction})




def make_prediction(file):
    # Enregistre le fichier dans un emplacement temporaire
    temp_path =  r"./temp_path/" + file.filename
    file.save(temp_path)

    # Obtiens le chemin d'accès complet vers l'image
    image_path = os.path.abspath(temp_path)
    print(image_path)

    result = detect_faces_emotions_v3(image_path)

    # Appelle la fonction get_main_secondary_colors avec le chemin d'accès à l'image
    couleurs = get_main_secondary_colors(image_path)

    # Supprime le fichier temporaire
    os.remove(temp_path)
    print(result['emotions'])
    if len(result['emotions'] ) == 1 and result['emotions'] == "Neutral" :
        genre = model_(in_number(couleurs[0][0],couleurs[1][0],result['num_faces'], result['face_position'], result['emotions'][0], result['emotions'][0],0,0))
    elif len(result['emotions'] ) == 1 and result['emotions'] != "Neutral" :
        genre = model_(in_number(couleurs[0][0],couleurs[1][0],result['num_faces'], result['face_position'], result['emotions'][0],"Neutral",0,0))
    elif len(result['emotions'] ) > 1 :
        genre = model_(in_number(couleurs[0][0],couleurs[1][0],result['num_faces'], result['face_position'], result['emotions'][0],result['emotions'][1],0,0))

    print(genre)

    return {'image': result['image'], 'couleurs': couleurs, 'emotions': result['emotions'], 'num_faces': result['num_faces'], 'face_position': result['face_position'], 'genre':genre}




if __name__ == '__main__':
    app.run(debug=True)
