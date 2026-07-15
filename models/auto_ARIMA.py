'''Modelo ARIMA'''

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import seaborn as sns
from scipy import stats
from analise_preparacao import serie, serie_raiz_tres
from tratamento_dataset_chuva import ultimo_ano
from pmdarima.arima import auto_arima # pip install pmdarima

from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6

# criando modelo ==============================================================
# modelo AR:    AIC: 1482.930, order=(0, 0, 8)
# modelo MA:    AIC: 1397.269, order=(7, 0, 0)
# modelo ARMA:  AIC: 1329.245, order=(3, 0, 7)
# modelo ARIMA: AIC: 1332.377, order=(3, 1, 7)
auto_arima_model = auto_arima(serie_raiz_tres, trace=True if __name__ == '__main__' else False,\
                              stepwise=False, seasonal=True,\
                              max_p=3, max_q=3, max_P=0, max_Q=0, start_p=2,\
                              start_q=2, start_P=0, start_Q=0, m=12)
# Best model:  ARIMA(2,0,2)(0,0,0)[12] intercept
# Total fit time: 520.907 seconds
# AIC=1324.816, Time=1.34 sec

'''parâmetros'''
# serie: serie a ser analizada
# trace: console log da lista dos modelos
# stepwise: seleção gradual (processo mais rápido, menos minucioso) 
#           o que significa que a busca pode explorar várias combinações
#           simultaneamente, tornando-a mais abrangente.
# seasonal: Indica que o modelo deve considerar componentes sazonais.
# max_p=10, max_q=10: Define os valores máximos para a ordem dos componentes
#           autoregressivos (p) e de média móvel (q) no modelo ARIMA.
# max_P=4, max_Q=4: Define os valores máximos para a ordem dos componentes
#           autoregressivos (P) e de média móvel (Q) no componente sazonal do modelo ARIMA.
# start_p=0, start_q=0, start_P=0, start_Q=0: Define os valores iniciais para os parâmetros
#           p, q, P e Q na busca do modelo.
# m: Define o número de períodos em uma temporada para considerar na parte sazonal do modelo. 
#           Neste caso, assume-se uma sazonalidade mensal, pois m é definido como 12.

# é possível remover a sazonalidade em stationary=True

# conferindo aic
'''print(auto_arima_model.aic())'''

resultado = auto_arima_model.fit(serie_raiz_tres)
# print(resultado.summary())

# # analisando resíduos =========================================================
resid = resultado.resid() # retorna uma serie (tem método plot())

if __name__ == '__main__':

    ################ Plotando ################
    '''
    resid.plot()
    plt.show()
    '''

    ############### Normalidade ##############
    '''
    stats.probplot(resid, dist='norm', plot=plt)
    plt.title('Normal QQ Plot')
    plt.show()
    '''

    '''
    e, p = stats.shapiro(resid)
    print(p, p > 0.05)
    '''

    '''
    sns.distplot(resid)
    plt.show()
    '''

    '''
    plot_acf(resid)
    plot_pacf(resid)
    plt.show()
    '''

    # >>>>> RESULTADO: VISUALMENTE NORMAL E SEM AUTOCORRELAÇÃO

'''
plt.plot(serie_raiz_tres, label='Série')
plt.plot(serie_raiz_tres-resid, label='Modelo MA')
plt.legend()
plt.show()
'''

# FORECAST ====================================================================
forecast = resultado.predict(n_periods=12)
forecast = forecast ** 3 # retornando à escala original

if __name__ == '__main__':
    plt.plot(serie, label='Série')
    plt.plot(forecast, label='Previsão')
    plt.plot(forecast.index, ultimo_ano[1:], label='Valores Reais', color='green')
    plt.legend()
    plt.show()