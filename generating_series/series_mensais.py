'''criando series mensais'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import datetime

from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6

np.random.seed(5)
dataset = np.random.normal(0, 1, 72)

data_frame = pd.DataFrame(dataset)
data_frame.columns = ['Valores']

# criando data
datas = np.array('2015-01', dtype = np.datetime64())
datas = datas + np.arange(len(dataset))
# print(data.__repr__())

datas = pd.DataFrame(datas)
datas.columns = ['Datas']

# criando dataframe com as colunas
data_frame = pd.concat([datas, data_frame], axis=1)


#criando serie
serie = pd.Series(data_frame['Valores'].values, index = data_frame['Datas'].values)
serie.plot()
plt.title('Serie Mensal')
plt.show()





# testes ==============================================================

# descrição
print(data_frame.describe())



# teste de shapiro-wilk
# ATENÇÃO: SOMENTE ATÉ 5000 LINHAS
e, p = stats.shapiro(serie)
print(f'Porcentagem de Teste: {e}\
      \np-value: {p}')
if p > 0.05:
    print(f'\033[32mA serie possui distribuição normal\033[0m')
else:
    print(f'\033[31mA distribuição não é normal\033[0m')




# gráfico de comparação de quantis
# stats.probplot(serie, dist='norm', plot=plt)
# plt.title('Normal QQ plot')
# plt.show()