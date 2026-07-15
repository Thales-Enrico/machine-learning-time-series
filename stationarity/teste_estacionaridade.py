'''teste de estacionaridade'''

# importando bibliotecas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.tsa.stattools 

# dimensionando
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6

# criação da série
np.random.seed(10)
data_set = np.random.normal(0, 1, 41)
data_frame = pd.DataFrame(data_set)
data_frame.columns = ['Values']
tempo = pd.date_range('1980', periods=len(data_set), freq='Y')
serie = pd.Series(data_frame['Values'].values, index=tempo)

# teste KPSS ==========================================================
'''
H0 -> é estácionário: estatística do teste < valor crítico
H1 -> não é estacionário: estatística do teste > valor crítico
'''
kpss, p_value, lags, valores_criticos = statsmodels.tsa.stattools.kpss(serie)

print(f'Estatística KPSS: \033[47m{kpss}\033[0m')
print(f'p-value: {p_value}')
print(f'Número de defasagens (lags): {lags}')
print(f'Valores críticos:') # níveis de sigificância (1%, 5%, 10%)
for significancia, v_critico in valores_criticos.items():
    print(f'\t{significancia}: {v_critico}')

if kpss < valores_criticos['5%']:
    print(f'Segundo o teste KPSS, \033[32ma série é estacionária\033[0m')
else:
    print(f'Segundo o teste KPSS, \033[31ma série NÃO é estacionária\033[0m')

print(72 * '=')
# teste df (Dickey Fuller) ============================================
'''
H0 -> é estácionário: estatística do teste < valor crítico
H1 -> não é estacionário: estatística do teste > valor crítico
'''
df = statsmodels.tsa.stattools.adfuller(serie)

print(f'Estatística Dickey Fuller: \033[47m{df[0]}\033[0m')
print(f'p-value: {df[1]}')
print(f'Número de defasagens (lags): {lags}')
print(f'Valores críticos:') # níveis de sigificância (1%, 5%, 10%)
for significancia, v_critico in df[4].items():
    print(f'\t{significancia}: {v_critico}')

if df[0] < df[4]['5%']:
    print(f'Segundo o teste df, \033[32ma série é estacionária\033[0m')
else:
    print(f'Segundo o teste df, \033[31ma série NÃO é estacionária\033[0m')