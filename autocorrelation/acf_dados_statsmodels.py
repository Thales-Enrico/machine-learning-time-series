'''função de autocorrelação (ACF)'''
# https://www.statsmodels.org/devel/datasets/index.html 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import statsmodels.api as sm

from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6

data_frame = sm.datasets.sunspots.load_pandas().data
serie = pd.Series(data_frame['SUNACTIVITY'].values, index=data_frame['YEAR'].values)
# serie.plot()

from statsmodels.graphics import tsaplots
tsaplots.plot_acf(serie)

tsaplots.plot_pacf(serie)

plt.show()
