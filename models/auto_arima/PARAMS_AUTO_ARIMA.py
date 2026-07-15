'''Módulo para conseguir os parâmetros'''

import pandas as pd
from pmdarima.arima import auto_arima

import sys
sys.path.append('modelos')
from analise_preparacao import serie_raiz_tres

auto_arima_model = auto_arima(serie_raiz_tres, stepwise=False, seasonal=True,\
                              max_p=3, max_q=3, max_P=0, max_Q=0, start_p=2,\
                              start_q=2, start_P=0, start_Q=0, m=12,\
                              trace=False if __name__ == '__main__' else False)

parametros = auto_arima_model.get_params()
df = pd.DataFrame([parametros]) # [parametros] coloca dentro de uma lista
df.to_csv('modelos\\auto_arima\\parametros_arima.csv', index=False)