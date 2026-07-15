'''criando series anuais'''

# importando bibliotecas necessárias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

from matplotlib.pylab import rcParams # dimensionamento
rcParams['figure.figsize'] = 15, 6

# gerando dados
# np.random.seed(5)
dataset = np.random.normal(0, 1, 41) # (media, std_dev, qtd)
# dataset = np.random.random(50)

data_frame = pd.DataFrame(dataset)
data_frame.columns = ['Valores']

# gerando anos
indices = pd.date_range('1980', periods=len(dataset), freq='Y')

# criando a serie
serie = pd.Series(data_frame['Valores'].values, index=indices)

# plotando a serie
serie.plot()
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

