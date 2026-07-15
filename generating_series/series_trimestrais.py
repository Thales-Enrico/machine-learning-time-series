'''criando series temporais diarias'''

# importando módulos
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
from scipy import stats

# configurando proporcao
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6

n = 164
'''número de meses'''

# gerando dados aleatórios
np.random.seed(5)
data_set = np.random.normal(0, 1, n)

# criando data frame
data_frame = pd.DataFrame(data_set)

data_indexes = pd.date_range('2000-01-01', periods=n, freq='3M')
data_frame_index = pd.DataFrame(data_indexes)

data_frame = pd.concat([data_frame, data_frame_index], axis=1)
data_frame.columns = ["Values", "Date"]

# criando serie
serie = pd.Series(data_frame['Values'].values, index=data_frame['Date'].values)
serie.plot()

# configurando gráfico
plt.title("Desvios Trimestrais")
plt.xlabel("# trimestres")
plt.ylabel("# desvios")
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