# librerias
 
import os
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns 
pd.set_option('display.max_columns', 500)  # Ver más columnas de los dataframes


def grafico_vote_average(df2)->pd.DataFrame:
    
    X = df2[['vote_average','vote_count']].values
    y = df2['popularity']
    
    x_range = np.arange(0.1,0.5,0.1)
        
    df_plot = pd.DataFrame({'x':X[:,0],
                            'y_true':y})

    df = pd.DataFrame({'x':X[:,0],
                               'y_true':y})

    fig, ax = plt.subplots(figsize=(11, 8.5))


    sns.scatterplot(x='x', y='y_true', data=df, ax=ax)

    plt.xlabel('vote_average')
    plt.ylabel('popularity')
    plt.show()
    return

def grafico_vote_count(df2)->pd.DataFrame:
    
    X = df2[['vote_average','vote_count']].values
    y = df2['popularity']
        
    x_range = np.arange(0.1,0.5,0.1)
        
    df_plot = pd.DataFrame({'x':X[:,1],
                            'y_true':y})

    df = pd.DataFrame({'x':X[:,1],
                               'y_true':y})

    fig, ax = plt.subplots(figsize=(11, 8.5))


    sns.scatterplot(x='x', y='y_true', data=df, ax=ax)

    plt.xlabel('vote_count')
    plt.ylabel('popularity')
    plt.show()
    return

def peliculas_populares(df2)->pd.DataFrame:
    
    pop= df2.sort_values('popularity', ascending=False)
    
    plt.figure(figsize=(12,4))

    plt.barh(pop['title'].head(6),pop['popularity'].head(6), align='center',
            color='skyblue')
    plt.gca().invert_yaxis()
    plt.xlabel("Popularity")
    plt.title("Popular Movies")
    return