import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6

data_path = "datasets_importados\\E3-262_Chuva_Mensal.csv"
dataset = pd.read_csv(data_path, sep=';')


# analisando os tipos dos dados ===============================================
# object: string
# int64: int
# float64: float
# complex;: complexos

'''print(dataset.dtypes)''' ########################

# substituit vírgulas por pontos ================
dataset = dataset.apply(lambda x: x.str.replace(',','.')) # para todas as colunas str
# dataset = dataset.apply(lambda x: x.replace(',', '.', regex=True)) # aqui Ano é int

'''print(dataset.dtypes)''' ########################

# substituir não valores pela média e convertendo em float =====================
dataset = dataset.replace('---', np.nan) # substituindo por NaN
dataset = dataset.iloc[:-1] # excluindo a ultima linha -> como em str[:-1] = st
dataset = dataset.map(pd.to_numeric) # transformando tudo em numerico
dataset.fillna(round(dataset.mean(), 1), inplace=True) # substituindo tudo pela media com uma casa depois da vírgula

'''
print(dataset.dtypes)
print(dataset.isna().sum())
'''

# removendo o ultimo ano para posteriormente confirmar previsões ===============
ultimo_ano = dataset.iloc[-1]
dataset = dataset.iloc[:-1]
# dataset = dataset.drop([36, 37]) # támbem remove as linhas


# criando um arquivo csv com o novo dataframe ===================================
# esse float format em razão da tabela original
# dataset.to_csv('datasets_importados\\chuva_tratado.csv', index=False, sep=';', float_format='%.1f') 
dataset.to_csv('datasets_importados\\chuva_tratado.csv', index=False, sep=';') 

# novo = pd.read_csv('datasets_importados\\chuva_tratado.csv', sep=';')
# print(novo['Janeiro'][34])