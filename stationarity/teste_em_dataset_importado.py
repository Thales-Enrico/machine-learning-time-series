'''teste de estacionaridade em datset importado'''

# importando bibliotecas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.tsa.stattools

# dimensionando
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6

data_frame = pd.read_csv('.\\datasets_importados\\AirPassengers.csv')
serie = pd.Series(data_frame['#Passengers'].values,  index=data_frame['Month'].values)
serie.plot(label='Série Temporal') # VISIVELMENTE NÃO ESTACIONÁRIA (TENDENCIA)

# definindo media
# media temporal ======================================================
def media(lista):
    return sum(lista) / len(lista)

def media_temporal(lista):
    mi = []
    for i in range(len(lista)):
        mi.append(media(lista[:i + 1]))
    return mi

media_movel = media_temporal(data_frame['#Passengers'].values)

media_movel = pd.DataFrame(media_movel)
media_movel.columns = ['Mean']
serie_m = pd.Series(media_movel['Mean'].values, index=data_frame['Month'].values)
serie_m.plot(label='Média', style='--', color='r')

plt.legend()
# plt.grid()
plt.show() 

print(80 * '=')
# teste KPSS ==========================================================
kpss = statsmodels.tsa.stattools.kpss(serie)
if kpss[0] < kpss[3]['5%']:
    print(f'Segundo KPSS: \033[32ma série é estacionária\033[0m')
    print(f'{kpss[0]} < {kpss[3]["5%"]}')
else:
    print(f'Segundo KPSS: \033[31ma série NÃO é estacionária\033[0m')
    print(f'{kpss[0]} > {kpss[3]["5%"]}')

print(80 * '=')
# teste Dickey Fuller =================================================
df = statsmodels.tsa.stattools.adfuller(serie)
if df[0] < df[4]['5%']:
    print(f'Segundo df: \033[32ma série é estacionária\033[0m')
    print(f'{df[0]} < {df[4]["5%"]}')
else:
    print(f'Segundo df: \033[31ma série NÃO é estacionária\033[0m')
    print(f'{df[0]} > {df[4]["5%"]}')
    
print(80 * '=')