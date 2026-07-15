'''serie, media e variancia'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6

# criando serie
np.random.seed(5)
dataset = np.random.normal(0, 1, 41)
data_frame = pd.DataFrame(dataset)
data_frame.columns = ['Values']
date_range = pd.date_range('2000', periods=len(dataset), freq='Y')
serie = pd.Series(data_frame['Values'].values, index=date_range)
serie.plot(label='Série Temporal')

# definindo media
# media temporal ======================================================
def media(lista):
    return sum(lista) / len(lista)

def media_temporal(lista):
    mi = []
    for i in range(len(lista)):
        mi.append(media(lista[:i + 1]))
    return mi

media_movel = media_temporal(data_frame['Values'].values)

media_movel = pd.DataFrame(media_movel)
media_movel.columns = ['Mean']
serie_m = pd.Series(media_movel['Mean'].values, index=date_range)
serie_m.plot(label='Média', style='--', color='r')

# definindo variancia ================================================
def delta(lista):
    # lista.pop(0)
    return lista[1:].copy()

def variancia(valores):
    
    valores_delta = delta(valores)
    
    med_val = media(valores)
    med_val_del = media(valores_delta)

    somatoria = 0
    for i, j in zip(valores, valores_delta):
        somatoria += (i - med_val) * (j - med_val_del)
    
    return somatoria / (len(valores_delta))

# temporal ============================================================
def vari_temporal(lista):
    res = []
    for i in range(1, len(lista)):
        res.append(variancia(lista[:i + 1]))
    return res

vari_movel = vari_temporal(data_frame['Values'].values)
vari_movel = [0] + vari_movel
vari_movel = pd.DataFrame(vari_movel)
vari_movel.columns = ['Vari']
serie_v = pd.Series(vari_movel['Vari'].values, index=date_range)
serie_v.plot(label='Variância', style='--', color='g')

plt.title('Processo Estocástico')
plt.xlabel('Tempo')
plt.ylabel('Desvios')
plt.legend()
plt.grid()
plt.show()
