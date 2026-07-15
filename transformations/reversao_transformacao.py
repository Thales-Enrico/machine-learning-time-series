'''reversão da transformação de uma serie temporal'''

# importando bibliotecas
import numpy as np
import pandas as pd

# importando dataset
dataset = pd.read_csv('datasets_importados\\AirPassengers.csv')
serie = pd.Series(dataset['#Passengers'].values, index=dataset['Month'].values)

# revertendo por log ==========================================================
# log base e
serie_log_e = np.log(serie) 
# revertendo
serie_log_e_revertida = np.e ** serie_log_e

# log base 10 ==============================
serie_log_10 = np.log10(serie)
# revertendo 
serie_log_10_revertida = 10 ** serie_log_10





 
# revertendo por exeponenciação ===============================================
serie_raiz_tres = np.sign(serie) * (abs(serie) ** (1 / 3))
# revertendo
serie_raiz_tres_revertida = serie_raiz_tres ** 3