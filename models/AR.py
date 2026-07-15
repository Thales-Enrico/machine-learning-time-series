'''Modelo AR'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from scipy import stats
import seaborn as sns
from analise_preparacao import serie_raiz_tres

from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6

# criando modelo ==============================================================
ar_model = ARIMA(serie_raiz_tres, order=(7, 0, 0))
# melhor valor: order=(7, 0, 0) -> AIC 1397.269

# verificando o ajuste (fit) ==================================================
resultado = ar_model.fit()
'''print(fit.summary())'''

'''
plot_acf(serie_raiz_tres, lags=12)
plt.show()
'''

# análise de resíduos =========================================================
resid = resultado.resid

if __name__ == '__main__':

    ########## Plot dos resíduos ##########
    # resid.plot()
    # plt.show()

    ######### Teste de normalidade ########
    '''stats.probplot(resid, dist='norm', plot=plt)'''
    # plt.title("Normal QQ Plot")
    # plt.show()
    '''e, p = stats.shapiro(resid)'''
    # print(p)
    # H0: p > 0.05 -> dist normal
    '''sns.histplot(serie_raiz_tres)'''
    # plt.show()

    ############ Autocorrelação ###########
    # plot_acf(resid)
    # plt.show()
    # plot_pacf(resid)
    # plt.show()

    # >>>>> RESULTADO: VISUALMENTE NORMAL E SEM AUTOCORRELAÇÃO

'''
plt.plot(serie_raiz_tres, label='Série')
plt.plot(serie_raiz_tres-resid, label='Resíduos relativos')
plt.legend()
plt.show()
'''

# PREVISÃO ====================================================================
valores_modelo = resultado.fittedvalues
# print(valores_modelo)

'''
######### COMPARAÇÃO MODELO E SÉRIE REAL #########
plt.plot(serie_raiz_tres, label='Série')
plt.plot(valores_modelo, label='Modelo AR')
plt.plot(serie_raiz_tres-resid, label='Resíduos relativos', color='r')
plt.legend()
plt.show()
'''

# comando de previsão (start, stop)
forecast1 = resultado.predict(456, 468)
# print(forecast)

'''
######### COMPARAÇÃO MODELO E SÉRIE REAL #########
plt.plot(serie_raiz_tres, label='Série')
plt.plot(forecast, label='Modelo AR')
plt.legend()
plt.show()
'''

# maneira alternativa
forecast2 = resultado.forecast(12)
# print(serie_raiz_tres)
# print(forecast2)

forecast_scale = pd.DataFrame(forecast1 ** 3)
# print(forecast_scale)

###### PREVISÃO COM INTERVALOS DE CONFIANÇA
# retorna uma pd.Series e os intervalos de confiança
forecast = resultado.get_forecast(steps=12) # previsões e significancia
forecast_values = forecast.predicted_mean
confidence_intervals = forecast.conf_int(alpha=0.05) # retorna um dataframe com os min e max

'''convertendo para a escala real (após radiciação cúbica)'''
forecast_values_scale = pd.DataFrame(forecast_values.values ** 3, index=forecast_values.index, columns=['Forecast'])
confidence_intervals_scale = pd.DataFrame(confidence_intervals.values ** 3, index=confidence_intervals.index, columns=['lower', 'upper'])


######### PREVISÃO COM VALORES REAIS ##########
from projeto_chuva import serie
if __name__ == '__main__':
    plt.plot(serie, label='Série')
    plt.plot(forecast_values_scale['Forecast'], label='Previsão', color='red')
    plt.fill_between(confidence_intervals_scale.index, confidence_intervals_scale['lower'], confidence_intervals_scale['upper'], label='Intervalo de Confiança', color='pink')
    plt.legend()
    plt.show()

# ##### maneira alternativa
# # pd.concat([serie, forecast_scale]).plot() 
# # plt.show()