'''projeto chuva'''

# importação dos módulos
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

# dimensionamento
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6

# importação do dataset =======================================================
dataset = pd.read_csv('datasets_importados\\chuva_tratado.csv', sep=';')

# formatando dataset ==========================================================
# removendo a coluna do ano
dataset_f = dataset.drop(columns='Ano') 
# colocando em sequencia
dataset_f = dataset_f.values # data_frame -> matriz
dataset_f = list(dataset_f.flatten()) # list(matriz -> array_unidimensional)

# criando série ===============================================================
date_range = pd.date_range('1985', periods=len(dataset_f), freq='M')
serie = pd.Series(dataset_f, index=date_range)

if __name__ == '__main__':
    print(dataset_f)
    serie.plot()
    plt.show()

