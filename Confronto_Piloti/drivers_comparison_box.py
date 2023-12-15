#%%
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

d = pd.read_csv('data/2021results.csv')

no_dnf1 = d['POS D1'].dropna().values

pos1 = [no_dnf1, d['ST D1']]
#print(no_dnf)

fig, ax = plt.subplots()
ax.boxplot(pos1, True, meanline = True, showmeans = True)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(True)
ax.spines['left'].set_visible(True)
ax.set_xlabel('Max Verstappen')
plt.xticks([1, 2], ['Arrivo', 'Partenza'])
ax.yaxis.set_major_locator(ticker.MultipleLocator(base=1))
plt.title('Confronto tra la posizione di partenza e la posizione di arrivo')

plt.show()

no_dnf2 = d['POS D2'].dropna().values

pos2 = [no_dnf2, d['ST D2']]

fig, ax = plt.subplots()
ax.boxplot(pos2, True, meanline = True, showmeans = True)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(True)
ax.spines['left'].set_visible(True)
ax.set_xlabel('Lewis Hamilton')
plt.xticks([1, 2], ['Arrivo', 'Partenza'])
plt.title('Confronto tra la posizione di partenza e la posizione di arrivo')

plt.show()

# %%
