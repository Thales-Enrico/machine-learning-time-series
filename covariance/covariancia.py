'''covariancia'''

# importando bibliotecas necessárias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

from matplotlib.pylab import rcParams # dimensionamento
rcParams['figure.figsize'] = 15, 6

# gerando dados
# np.random.seed(5)
# data_set = np.random.normal(0, 1, 10) # (media, std_dev, qtd)
data_set = [10, 20, 30, 40, 50]
# data_set = []
# for i in range(1000):
#     data_set.append(i * 10)
data_frame = pd.DataFrame(data_set)
data_frame.columns = ['Vendas']

# gerando anos
indices = pd.date_range('2000-01', periods=len(data_set), freq='M')
data_frame_index = pd.DataFrame(indices)
data_frame_index.columns = ['Meses']
data_frame_index['Meses'] = indices.strftime('%B')

data_frame = pd.concat([data_frame, data_frame_index], axis=1)

# cáculo covariancia ==================================================
def media(lista):
    return sum(lista)/len(lista)

def delta(lista):
    # lista.pop(0)
    return lista[1:].copy()

def autocovariancia(valores):
    
    valores_delta = delta(valores)
    
    med_val = media(valores)
    med_val_del = media(valores_delta)

    somatoria = 0
    for i, j in zip(valores, valores_delta):
        somatoria += (i - med_val) * (j - med_val_del)
    
    return somatoria / (len(valores_delta))

# calculo correlacao ==================================================
def autocorrelacao(valores):
    valores_delta = delta(valores)
    return autocovariancia(valores) / (np.std(valores_delta) ** 2)

# resultados ==========================================================
if __name__ == '__main__':
    print(autocovariancia(list(data_frame['Vendas'])))
    print(autocorrelacao(list(data_frame['Vendas'])))


# valores = list(data_frame['Vendas'])
# valores_delta = delta(valores)

# zipado = zip(valores, valores_delta)
# val1, val2 = zip(*zipado)

# plt.scatter(val1, val2)
# plt.plot(val1, val2)
# plt.show()
# plotagem ============================================================

indices = pd.date_range('2000-01-01', periods=len(data_set), freq='D')
serie = pd.Series(data_frame['Vendas'].values, index=indices)
serie.plot()
plt.show()