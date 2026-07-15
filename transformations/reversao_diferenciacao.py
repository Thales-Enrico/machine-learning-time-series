'''reversao da diferenciacao'''

# importando módulos
import numpy as np 
import pandas as pd

# importando dataset
dataset = pd.read_csv('datasets_importados\\AirPassengers.csv')
serie = pd.Series(dataset['#Passengers'].values, index=dataset['Month'].values)

# reversão da diferenciação ===================================================
serie_dif = serie.diff()
# revertendo
serie_dif_revertida = serie.shift(1) + serie_dif


# dataframe de reversões ======================================================
dataset['Valores_Diferenciados'] = dataset['#Passengers'].diff()
dataset['Valores_Revertidos'] = dataset['Valores_Diferenciados'] + dataset['#Passengers'].shift()

# dataset.to_csv('reversoes.csv')