# librerias
 
import os
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns 
pd.set_option('display.max_columns', 500)  # Ver más columnas de los dataframes

def lectura():
    df1=pd.read_csv('data/tmdb_5000_credits.csv') 
    df2=pd.read_csv('data/tmdb_5000_movies.csv')
    
    df1.columns = ['id','tittle','cast','crew']
    df2= df2.merge(df1,on='id')
    return df2