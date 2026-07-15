'''Decomposição de series teporais'''
# serie = tendencia + sazonalidade + ruído
# tendencia -> propensão de crecimento dos valores
# sazonalidade -> fenômenos eventuais
# ruído -> desvios do modelo

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from statsmodels.tsa.seasonal import seasonal_decompose
import statsmodels.api as sm

from matplotlib.pylab import rcParams
# rcParams['figure.figsize'] = 15, 6


data_frame = sm.datasets.co2.load_pandas().data
serie = pd.Series(data_frame['co2'].values, index = data_frame.index)  # série com missing values
# https://www.statsmodels.org/devel/datasets/generated/co2.html
# x = seasonal_decompose(serie) ##### ValueError: This function does not handle missing values

# print(serie.isnull().sum()) # 59 valores falando
# pode se substituir pela media, mediana... ou excluir dependando do tamanho do dataset

# deletando valores
serie.dropna(inplace=True)
# serie = serie.dropna() # -> mesma coisa

# decomposição da serie temporal ==========================================================
quinto = round(.2 * len(serie))
decompose = seasonal_decompose(serie, period=quinto) #20% da quantidade
# decompose.plot()

# plotando ================================================================================

plt.subplot(411)
plt.title('Análise da concentração de CO2 em ppm') # pp = partes por milhao
plt.plot(serie, label='Original')
plt.legend(loc='best')

plt.subplot(412)
plt.plot(decompose.trend, label='Tendência')
plt.legend(loc='best')

plt.subplot(413)
plt.plot(decompose.seasonal, label='Sazonalidade')
plt.legend(loc='best')

plt.subplot(414)
plt.plot(decompose.resid, label='Resíduos')
plt.legend(loc='best')

plt.tight_layout()
plt.show()


# decomposição multiplicativa =============================================================
# apenas em valores >= 0
mult_decompose = seasonal_decompose(serie, period=100, model='multiplicative')
mult_decompose.plot()
plt.show()