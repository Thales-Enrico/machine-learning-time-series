'''autocorrelação com dados aleatórios'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6

np.random.seed(5)
dataset = np.random.normal(0, 1, 72)

serie = pd.Series(dataset)
# serie.plot()
# plt.show()

plot_acf(serie, lags=8)
plt.show()
