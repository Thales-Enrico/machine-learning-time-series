'''media movel'''
# exemplo: Desvios da temperatura média global da terra-oceano 
# (1951 - 1980), medidos em graus Celsius, para os anos de 1880 - 2015

# importação bibliotecas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6

# importação do dataset
dataset = pd.read_csv('datasets_importados\\temp_global.csv')
date_range = pd.date_range('1880 Jan 1', periods=len(dataset), freq='Y')
serie = pd.Series(dataset['x'].values, index=date_range)
# serie.plot()
# plt.show()

# cálculo da média móvel ======================================================
# mms = media móvel simples
# mmsc = media móvel simples centralizada 
# mme = media móvel exponencial

mms = serie.rolling(window=3) # --> criando um objeto rolling de janela 3
mms = mms.mean() # --> método que retorna uma série com as medias

mmsc = serie.rolling(window=3, center=True)
mmsc = mmsc.mean()

mme = serie.ewm(alpha=.5).mean()

# plotagem ====================================================================
plt.title('Desvios da temperatura média global (1880-2015)')
plt.plot(serie, label='Série')
plt.plot(mms, label='MMS', color='orange')
plt.plot(mmsc, label='MMSC', color='purple')
plt.plot(mme, label='MME', color='red')
plt.legend()
plt.show()