'''diferenciação'''
# series virarem estacionarias

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa import stattools
from statsmodels.tsa.seasonal import seasonal_decompose

from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6

data_frame = pd.read_csv('datasets_importados\\AirPassengers.csv')
serie = pd.Series(data_frame['#Passengers'].values, index=data_frame['Month'].values)
# serie.plot()
# plt.show()


# NORMALIZANDO SERIE ======================================================================
# normalizando pela raiz cúbica
serie = np.sign(serie) * (abs(serie) ** (1 / 3))

# TESTE ESTACIONARIDADE ===================================================================
def print_stats(teste, res):
    i = 3 if teste == 'kpss' else 4

    print(f'{teste:=^50}')
    print(f'Estatística {teste}: \033[47m{res[0]}\033[0m')
    print(f'p-value: {res[1]}')
    print(f'lags: {res[2]}')
    print(f'Valores críticos:')
    for chave, valor in res[i].items():
        print(f'|-> {chave}:  {valor}')
    
def print_est(teste, res):
    i = 3 if teste == 'kpss' else 4

    print(f'{teste:=^50}')
    if res[0] < res[i]['5%']:
        print(f'Segundo {teste}: \033[32ma série é estacionária\033[0m')
        print(f'{res[0]} < {res[i]["5%"]}')
    else:
        print(f'Segundo {teste}: \033[31ma série NÃO é estacionária\033[0m')
        print(f'{res[0]} > {res[i]["5%"]}')
    

class Estacionaridade():
    def __init__(self, serie):
        self.serie = serie
    
    def kpss(self):
        res = stattools.kpss(self.serie)
        print_stats('kpss', res)
        print_est('kpss', res)
    
    def df(self):
        res = stattools.adfuller(self.serie)
        print_stats('df', res)
        print_est('df', res)


# ver_serie = Estacionaridade(serie)
# ver_serie.kpss()
# ver_serie.df()

# DIFERENCIAÇÃO ===========================================================================
serie_dif = np.diff(serie) # diferenciar serie ==========================================
# serie_dif = serie.diff()
# serie_dif = serie - serie.shift() ##### >>>>>>>> diferenciação = subtrair um periodo por um anterior
plt.plot(serie_dif)
plt.show()

ver_serie_dif = Estacionaridade(serie_dif)
ver_serie_dif.kpss()
ver_serie_dif.df()