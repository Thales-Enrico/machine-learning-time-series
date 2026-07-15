'''decomposição serie temporal: exercicio manchas solares'''

import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
import statsmodels.api as sm

from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6

data_frame = sm.datasets.sunspots.load_pandas().data
serie = pd.Series(data_frame['SUNACTIVITY'].values, index=data_frame['YEAR'])

# se ajusta observando os padrões da sazonalidade
comprimento_sazonalidade = 5 # sazonalidade a cada 25 anos
decompose = seasonal_decompose(serie, period=comprimento_sazonalidade)

plt.subplot(411)
plt.title("Análise da decomposição das observações de manchas solares")
plt.plot(decompose.observed, label='Original')
plt.legend(loc='best')

plt.subplot(412)
plt.plot(decompose.trend, label='Tendência', color='r')
plt.legend(loc='best')

plt.subplot(413)
plt.plot(decompose.seasonal, label='Sazonalidade')
plt.legend(loc='best')

plt.subplot(414)
plt.plot(decompose.resid, label='Resíduos')
plt.legend(loc='best')

plt.tight_layout()
plt.show()