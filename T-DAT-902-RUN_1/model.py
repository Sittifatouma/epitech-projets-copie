import pandas as pd 
import seaborn as sns
import numpy as np
#from sklearn.neighbors import KNeighborsClassifier
#from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv(r"new_dataset_model.csv")
data.dropna(inplace=True)

#model = MultiOutputClassifier(KNeighborsClassifier())
#model = MultiOutputClassifier(RandomForestClassifier())
model = RandomForestClassifier()

# Spécifiez une liste des noms de colonnes à supprimer
data_sup = [ 'id', 'Couleur nominale', 'couleur_secondaire', 'nb_visages',
       'position_visage', 'emotion1', 'emotion2','cluster', 'number']

# Utilisez la méthode drop() en spécifiant les noms de colonnes et l'axe (axis=1 pour les colonnes)
datay = data.drop(data_sup, axis=1)

# Spécifiez une liste des noms de colonnes à supprimer
data_sa  = [ 'id', 'Comedy', 'Documentary',
       'Horror', 'N/A', 'Short', 'Sport', 'Western', 'Action_Adventure_Sci-Fi',
       'Animation_Family_Fantasy', 'Music_Musical', 'Crime_Mystery_Thriller',
       'Drama_Romance', 'History_Biography_War', 'Reality_TV_News']

# Utilisez la méthode drop() en spécifiant les noms de colonnes et l'axe (axis=1 pour les colonnes)
datax = data.drop(data_sa, axis=1)

y = datay
x = datax

model.fit(x, y)
model.score(x, y)

def get_genres_from_mapping(mapping, input_array):
    genres = []
    for i, value in enumerate(input_array):
        if value == 1 and i < len(mapping):
            genres.append(mapping[i])
    return genres

# Mapping des genres
genre_mapping = [
    'Comedy', 'Documentary', 'Horror', 'N/A', 'Short', 'Sport', 'Western',
    'Action_Adventure_Sci-Fi', 'Animation_Family_Fantasy', 'Music_Musical',
    'Crime_Mystery_Thriller', 'Drama_Romance', 'History_Biography_War',
    'Reality_TV_News'
]





def model_(data):
    nouvelle_instance = np.array([data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7]]).reshape(1, -1)  # Votre nouvelle instance 1D remodelée en 2D

    prediction = model.predict(nouvelle_instance)
    genre = get_genres_from_mapping(genre_mapping, prediction[0])

    return genre