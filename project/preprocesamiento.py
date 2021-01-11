# librerias
 
import os
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns 
pd.set_option('display.max_columns', 500)  # Ver más columnas de los dataframes

def filtro_nulos(df2)->pd.DataFrame:   
    # ocupar masking
    mask = lambda df2: df2.notnull().all(axis=1)
    df2 = df2[mask]
    return

def obtener_valores(df2)->pd.DataFrame:
    C= df2['vote_average'].mean()
    m= df2['vote_count'].quantile(0.9)
    return C,m

def filtro_votos(df2,m)->pd.DataFrame:
    q_movies = df2.copy().loc[df2['vote_count'] >= m]
    return q_movies

# Funcion que limpia los string, sacando mayusculas, espacios, etc.
def clean_data(x):
    if isinstance(x, list):
        return [str.lower(i.replace(" ", "")) for i in x]
    else:
        if isinstance(x, str):
            return str.lower(x.replace(" ", ""))
        else:
            return ''