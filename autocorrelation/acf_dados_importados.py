'''função de autocorrelação (ACF)'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6

data_frame = pd.read_csv('datasets_importados\\sunspots.csv')
data_frame = data_frame.reset_index(drop=True) # começa os indices do zero
times = pd.date_range('1749', periods=len(data_frame), freq='M')
serie = pd.Series(data_frame['x'].values, index=times)
serie.plot()
# plt.show()

# FUNÇÃO DE AUTOCORRELAÇÃO ============================================
from statsmodels.graphics import tsaplots
tsaplots.plot_acf(serie)

tsaplots.plot_pacf(serie)
plt.show()
