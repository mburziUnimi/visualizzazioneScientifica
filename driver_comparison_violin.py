#%%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import seaborn as sns

d = pd.read_csv('data/1984results.csv')

cond1 = (d['ST D1'] - d['POS D1']) > 0
cond2 = (d['ST D2'] - d['POS D2']) > 0

d.loc[cond1, 'GAINED D1'] = d['ST D1'] - d['POS D1']
d['GAINED D1'].fillna(0, inplace=True)

d.loc[cond2, 'GAINED D2'] = d['ST D2'] - d['POS D2']
d['GAINED D2'].fillna(0, inplace=True)

d.head(n = 17)

condizione1 = d['POS D1'] != None
posconq = d.loc[condizione1, 'GAINED D1']

data = [7, 8, 6, 2, 5, 3, 4, 3, 11, 9]

sns.violinplot(x = data, inner="point")
#sns.violinplot(x = d['GAINED D2'], inner="point")
# %%
