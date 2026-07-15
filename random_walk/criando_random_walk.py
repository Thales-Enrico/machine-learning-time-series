'''criando random walk'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from random import sample, random

from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6



# primeira forma de criar ==============
# dataset = sample(range(100), k=41)
# data_range = list(range(1980, 2021))
# serie = pd.Series(dataset, index=data_range)
# serie.plot()
# plt.show()

# segunda forma de criar ===============
random_walk = []
random_walk.append(-1 if random() < 0.5 else 1)
for i in range(1, 1000):
    val = -1 if random() < 0.5 else 1
    random_walk.append(random_walk[i - 1] + val)

random_walk = pd.Series(random_walk)
random_walk.plot()
plt.show()