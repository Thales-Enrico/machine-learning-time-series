'''Análise final'''
# MAE: ERRO MÉDIO ABSOLUTO
# MSE: ERRO QUADRÁTICO MÉDIO
# RMSE: RAIZ DO ERRO QUADRÁTICO MÉDIO

import warnings
from statsmodels.tools.sm_exceptions import ConvergenceWarning
warnings.filterwarnings("ignore", category=ConvergenceWarning)

import pandas as pd
from tratamento_dataset_chuva import ultimo_ano
from AR import forecast_values_scale as ar
from MA import forecast_values as ma 
from ARMA import forecast_values as arma
from ARIMA import forecast_values as arima
from SARIMA import forecast_values as sarima
from auto_ARIMA import forecast as auto_ARIMA
from sklearn.metrics import mean_absolute_error, mean_squared_error, root_mean_squared_error



valores_reais = pd.DataFrame(ultimo_ano.iloc[1:].values, index=ar.index) 
modelos = pd.concat([valores_reais, ar, ma, arma, arima, sarima, auto_ARIMA], axis=1)
modelos.columns = ['Valores Reais', 'Modelo AR', 'Modelo MA', 'Modelo ARMA',\
                   'Modelo ARIMA', 'Modelo SARIMA', 'Modelo auto ARIMA']

#             Valores Reais   Modelo AR   Modelo MA  Modelo ARMA  Modelo ARIMA  Modelo SARIMA  Modelo auto ARIMA
# 2023-01-31          377.6  244.750665  185.382137   271.187376    274.466585     286.165260         267.927371
# 2023-02-28          452.0  212.568320  171.956405   239.184385    234.813577     230.786023         234.175865
# 2023-03-31          138.2  134.931050  126.518224   175.291228    176.264992     187.576866         167.167311
# 2023-04-30          165.7   84.137981  103.819819   104.323757    102.060151      93.152325         101.032382
# 2023-05-31           43.3   63.238197  106.176612    58.042103     58.968896      61.458237          56.566776
# 2023-06-30           85.2   49.196895  102.179514    34.922247     34.113855      39.542452          35.035011
# 2023-07-31           15.0   49.771467  101.509137    29.268276     30.065052      31.394682          30.074312
# 2023-08-31           28.6   59.229138  107.136597    37.178156     36.529633      30.379711          39.133613
# 2023-09-30           85.1   86.841294  109.298999    63.572496     65.036367      66.335975          66.492203
# 2023-10-31          139.6  127.146690  109.298999   113.614184    112.180833     123.685487         117.797271
# 2023-11-30          145.5  164.883608  109.298999   184.137942    186.652620     165.640002         187.051962
# 2023-12-31          235.4  185.861446  109.298999   247.452007    244.247687     238.728546         248.007382

# ERRO MÉDIO ABSOLUTO ===========================================================================

def desempenho_mae(modelo):
    mae = mean_absolute_error(modelos['Valores Reais'], modelos[f'Modelo {modelo}'])
    print(f'MAE {modelo}: {mae}')

desempenho_mae('AR')
desempenho_mae('MA')
desempenho_mae('ARMA')
desempenho_mae('ARIMA')
desempenho_mae('SARIMA')
desempenho_mae('auto ARIMA')

print(80 * '=')
# ERRO MÉDIO QUADRÁTICO =========================================================================
# comparável á variancia

def desempenho_mse(modelo):
    mse = mean_squared_error(modelos['Valores Reais'], modelos[f'Modelo {modelo}'])
    print(f'MSE {modelo}: {mse}')

desempenho_mse('AR')
desempenho_mse('MA')
desempenho_mse('ARMA')
desempenho_mse('ARIMA')
desempenho_mse('SARIMA')
desempenho_mse('auto ARIMA')

print(80 * '=')
# ERRO MÉDIO QUADRÁTICO =========================================================================
# comparável ao desvio padrão

def desempenho_rmse(modelo):
    mse = root_mean_squared_error(modelos['Valores Reais'], modelos[f'Modelo {modelo}'])
    print(f'RMSE {modelo}: {mse}')

desempenho_rmse('AR')
desempenho_rmse('MA')
desempenho_rmse('ARMA')
desempenho_rmse('ARIMA')
desempenho_rmse('SARIMA')
desempenho_rmse('auto ARIMA')