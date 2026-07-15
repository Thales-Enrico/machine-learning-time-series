'''decomposição serie temporal: exercicio manchas solares'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

from matplotlib import rcParams
rcParams['figure.figsize'] = 15, 6

data_frame = pd.read_csv('datasets_importados\\sunspots.csv')
data_frame.reset_index(drop=True, inplace=True)
date_range = pd.date_range('1749', periods=len(data_frame), freq='M')
serie = pd.Series(data_frame['x'].values, index=date_range)

# se ajusta observando os padrões da sazonalidade
comprimento_sazonalidade = 25 * 12 # sazonalidade a cada 25 anos
decompose = seasonal_decompose(serie, period=comprimento_sazonalidade)

plt.subplot(411)
plt.title("Análise da decomposição das observações de manchas solares")
plt.plot(decompose.observed, label='Original')
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

# ATENÇÃO ==============================>>>>>>>>>>>>>>>>>>>>>>>>>>> ValueError: Multiplicative seasonality is not appropriate for zero and negative values

# decompose = seasonal_decompose(serie, period=comprimento_sazonalidade, model='multiplicative')
# decompose.plot()
# plt.show()