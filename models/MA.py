'''Modelo de Média Móvel'''

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import seaborn as sns
from scipy import stats
from analise_preparacao import serie, serie_raiz_tres
from tratamento_dataset_chuva import ultimo_ano

from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6

# criando modelo ==============================================================
ma_model = ARIMA(serie_raiz_tres, order=(0, 0, 8))
# melhor valor de AIC: 1482.930 (0, 0, 8)
# melhor valor: order=(7, 0, 0) -> AIC 1397.269

resultado = ma_model.fit()
'''print(resultado.summary())'''

# analisando resíduos =========================================================
resid = resultado.resid # retorna uma serie (tem método plot())

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
forecast = resultado.get_forecast(steps=12)
forecast_values_r3 = forecast.predicted_mean
conf_int_r3 = forecast.conf_int(alpha=0.05)

forecast_values = pd.DataFrame(forecast_values_r3.values ** 3, index=forecast_values_r3.index, columns=['Forecast'])
conf_int = pd.DataFrame(conf_int_r3.values ** 3, index=conf_int_r3.index, columns=['lower', 'upper'])

if __name__ == '__main__':
    plt.plot(serie, label='Série')
    plt.plot(conf_int.index, ultimo_ano[1:], label='Valores Reais', color='green')
    plt.plot(forecast_values['Forecast'], label='Previsão', color='red')
    plt.fill_between(conf_int.index, conf_int['lower'], conf_int['upper'], label='Intervalo de Confiança 95%', color='pink')
    plt.legend()
    plt.show()


