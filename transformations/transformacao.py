'''transformações'''
# fazer a serie ter uma transformação aproximadamente normal

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import stats
import seaborn as sns

from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6

data_frame = pd.read_csv('datasets_importados\\AirPassengers.csv')
serie = pd.Series(data_frame['#Passengers'].values, index=data_frame['Month'].values)

def shapiro_wilk(seriex):
    # teste de shapiro-wilk
    # ATENÇÃO: SOMENTE ATÉ 5000 LINHAS
    e, p = stats.shapiro(seriex)
    print(f'Porcentagem de Teste: {e}\
        \np-value: {p}')
    if p > 0.05:
        print(f'\033[32mA serie possui distribuição normal\033[0m')
    else:
        print(f'\033[31mA distribuição não é normal\033[0m')

def normal_qq_plot(seriex):
    stats.probplot(seriex, dist='norm', plot=plt)
    plt.title("Normal QQ Plot")
    plt.show()

if __name__ == '__main__':
    shapiro_wilk(serie)

    # TRANSFORMAÇÃO POR LOG ===================================================================
    serie2 = np.log(serie)
    shapiro_wilk(serie2)

    # TRANSFORMAÇÃO POR RAIZ CÚBICA ===========================================================
    # quando possui valores zero ou negativos
    #             sinal           valor absoluto
    serie3 = np.sign(serie)* ((abs(serie)) ** (1 / 3))
    shapiro_wilk(serie3)

    # VERIFICAÇÃO DAS DISTRIBUIÇÕES ===========================================================
    # sns.distplot(serie)
    # sns.distplot(serie2)
    # sns.distplot(serie3)
    # plt.show()
