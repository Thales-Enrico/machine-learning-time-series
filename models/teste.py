import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.arima.model import ARIMAResults
from scipy import stats
from analise_preparacao import serie_raiz_tres
from projeto_chuva import serie

from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6

# Criando modelo
ar_model = ARIMA(serie_raiz_tres, order=(7, 0, 0))
resultado = ar_model.fit()

# Previsão
forecast = resultado.get_forecast(steps=12, alpha=0.05)

# Obtendo os valores previstos e os intervalos de confiança
forecast_values = forecast.predicted_mean
confidence_intervals = forecast.conf_int()
print(type(forecast_values))

# Convertendo os valores para a escala original
# forecast_values_scale = pd.DataFrame(forecast_values.values ** 3, index=forecast_values.index, columns=['Forecast'])
# confidence_intervals_scale = pd.DataFrame(confidence_intervals.values ** 3, index=confidence_intervals.index, columns=['lower', 'upper'])

# # Plotando a série real, previsão e intervalo de confiança
# plt.plot(serie, label='Série Real')
# plt.plot(forecast_values_scale['Forecast'], label='Previsão', color='red')
# plt.fill_between(confidence_intervals_scale.index, confidence_intervals_scale['lower'], confidence_intervals_scale['upper'], color='pink', alpha=0.3, label='Intervalo de Confiança (95%)')
# plt.legend()
# plt.show()