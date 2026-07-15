'''análise e preparação'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa import stattools
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from scipy import stats
import seaborn as sns

from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6

from projeto_chuva import serie


# média móvel =================================================================
# mms = media móvel simples
# mmsc = media móvel simples centralizada 
# mme = media móvel exponencial
# mms = serie.rolling(window=5 + 1).mean()
# mme = serie.ewm(alpha=.5).mean()

# testando a normalidade ======================================================
if __name__ == '__main__':
    '''análise de média móvel'''
    # plt.plot(serie, label='serie')
    # plt.plot(mms, label='mms', color='y')
    # plt.plot(mme, label='mme', color='r')
    # plt.legend()
    # plt.show()

    '''análise de decomposição'''
    # decompose = seasonal_decompose(serie, period=12)
    # decompose.plot()
    # plt.show()

    '''análise de normalidade'''
    ################## QQ Plot ##################
    # stats.probplot(serie, dist='norm', plot=plt)
    # plt.title('Normal QQ plot')
    # plt.show()

    ################ Shapiro-Wilk ################
    # e, p = stats.shapiro(serie)
    # print("Normal") if p > 0.05 else print("Não normal")





    '''transformação por log''' 
    # diminuir a variancia e melhorar a normalidade
    # serie2 = np.log(serie)

    '''análise de normalidade'''
    ################## QQ Plot ##################
    # stats.probplot(serie2, dist='norm', plot=plt)
    # plt.title('Normal QQ plot')
    # plt.show()

    ################ Shapiro-Wilk ################
    # e, p = stats.shapiro(serie2)
    # if e % e == 0: # se e == nan ele dá false
    #     print("Normal") if p > 0.05 else print("Não normal")





    '''transformação por raiz cubica'''
    # quando há dados zero ou negativos
    serie_raiz_tres = np.sign(serie) * (abs(serie) ** (1 / 3))
    # print(serie_raiz_tres)

    '''análise de normalidade'''
    ################## QQ Plot ###################
    # stats.probplot(serie3, dist='norm', plot=plt)
    # plt.title('Normal QQ plot')
    # plt.show()

    ################ Shapiro-Wilk ################
    # e, p = stats.shapiro(serie3)
    # if e % e == 0: # se e == nan ele dá false
    #     print("Normal") if p > 0.05 else print("Não normal")
    #     print('p-valor: ', p)

    ################# Histograma #################
    # sns.histplot(serie_raiz_tres)
    # plt.show()

    '''RESULTADO: SÉRIE NÃO NORMAL, MAS SIMILAR'''


# estacionaride ===============================================================
    
    #################### KPSS ####################
    # (H0) não é estacionária se a estatis de teste > valor crítico 
    # (H1) é estacionária se a estatis de teste < valor crítico 
    # kpss = stattools.kpss(serie_raiz_tres)
    # print("Estacionária") if kpss[0] < kpss[3]['5%'] else print("Não Estacionária")
    # print(f'kpss: {kpss[0]}', f'valor crítico: {kpss[3]["5%"]}', sep='\n')

    '''RESULTADO: SÉRIE ESTACIONÁRIA'''
    
    # se não fosse:
    # serie_dif = np.diff(serie_raiz_tres)
    # quantas vezes o necessário

# autocorrelação ==============================================================
    
    ########## Função de Autocorrelação ##########
    # plot_acf(serie_raiz_tres, lags=20)
    # plot_pacf(serie_raiz_tres, lags=20)
    # plt.show()

    '''A SÉRIE É AUTOCORRELACIONADA'''
    ''' mas isso não é um problema '''
    '''é um pressuposto da analise '''
    '''  dos resíduos dos modelos  '''

serie_raiz_tres = np.sign(serie) * (abs(serie) ** (1 / 3))
