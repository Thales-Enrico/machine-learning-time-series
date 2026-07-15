'''projeto analise media móvel da pandemia de covid em São Paulo-SP'''

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6

# importação do dataset =======================================================
# https://www.seade.gov.br/coronavirus/#
# https://github.com/seade-R/dados-covid-sp
# https://www.seade.gov.br/

dataset = pd.read_csv('datasets_importados\\dados_covid_sp.csv', sep=';')





# analisando os tipos dos dados ===============================================
# object: string
# int64: int
# float64: float
# complex;: complexos

'''print(dataset.dtypes)''' ########################






# é necessário trocar colunas de string para inteiros =========================

# trocar , por .
dataset['casos_mm7d'] = dataset['casos_mm7d'].str.replace(',', '.')
# transformar str em int
dataset['casos_mm7d'] = pd.to_numeric(dataset['casos_mm7d'])


# trocar , por .
dataset['obitos_mm7d'] = dataset['obitos_mm7d'].str.replace(',', '.')
# transformar str em int
dataset['obitos_mm7d'] = pd.to_numeric(dataset['obitos_mm7d'])

'''print(dataset.dtypes)''' ###################### deu certo!






# VERIFICAR MISSING VALUES ====================================================

'''print(dataset.isnull().sum())''' # dos dados que importam, nenhum falta



# se tivesse que substituir por zero, seria aplicado fillna()
'''dataset_tratado = dataset.fillna(0)'''
'''print(dataset_tratado.isnull().sum())''' # tudo está preenchido


# se tivesse que excluir seria aplicado o dropna()
'''dataset_tratado = dataset.dropna()'''
'''print(dataset_tratado.shape)''' # (322500, 26), 500 valores descartados




# filtrar SOMENTE a cidade de São Paulo =======================================
dataset_cidade = dataset.loc[dataset.nome_munic == 'Motuca']
# print(dataset_cidade)




# criando série ===============================================================
serie = pd.Series(dataset_cidade['casos_novos'].values, index=dataset_cidade['datahora'])
# serie.plot()
# plt.show()



# Análise média móvel casos novos =============================================
# mms que já esta no dataset
'''
plt.plot(dataset_cidade.casos_mm7d)
plt.title('Média móvel - casos')
plt.show()
'''


# criando médias móveis =======================================================

mms = serie.rolling(window=7)
mms = mms.mean()

mme = serie.ewm(alpha=.5).mean()

plt.plot(serie, label='Série')
# plt.plot(dataset_cidade.casos_mm7d.values, label='media do dataset', color='red')
plt.plot(mms, label='MMS 7 dias', color='orange')
plt.plot(mme, label='MME', color='red')
plt.legend()
plt.show()
