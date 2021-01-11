# librerias
 
import os
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns 
pd.set_option('display.max_columns', 500)  # Ver más columnas de los dataframes

def vectorizacion(df2)->pd.DataFrame:
    #Importamos TfIdfVectorizer desde sklearn
    from sklearn.feature_extraction.text import TfidfVectorizer

    #definimos el objeto. Removemos las palabras que no son claves
    tfidf = TfidfVectorizer(stop_words='english')

    #Limpiamos el dataframe
    df2['overview'] = df2['overview'].fillna('')

    #Construimos tfidf dataframe a partir de los datos filtrados
    tfidf_matrix = tfidf.fit_transform(df2['overview'])
    return tfidf_matrix

#Funcion que entrega las peliculas similares a la pelicula de entrada
def get_recommendations(title, cosine_sim,indices):
    # Obtenemos el indice de la pelicula
    idx = indices[title]

    # Vemos la similitud pelicula por pelicula
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Ordenamos las peliculas por el score de similitud
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Tomamos las primeras 10 peliculas
    sim_scores = sim_scores[1:11]

    # Recuperamos los indices
    movie_indices = [i[0] for i in sim_scores]

    # Reotrnamos las 10 mejores peliculas en cuanto a nuestro score
    return movie_indices 