#%%
import pandas as pd
import matplotlib.pyplot as plt

driversData = pd.read_csv('data/1984results.csv')

D1 = 'Niki Lauda'
D2 = 'Alain Prost'

driversData['GAINED D1'] = driversData['ST D1'] - driversData['POS D1']

driversData['GAINED D2'] = driversData['ST D2'] - driversData['POS D2']

sommaD1 = driversData[driversData['GAINED D1'] > 0]['GAINED D1'].sum()

sommaD2 = driversData[driversData['GAINED D2'] > 0]['GAINED D2'].sum()

posgained = [sommaD1,sommaD2]

#driversData.head()



fig, ax = plt.subplots()
bars = ax.barh([D1, D2], posgained, 0.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(True)
ax.spines['left'].set_visible(True)
#ax.invert_yaxis()   # labels read top-to-bottom
ax.bar_label(bars, padding=10)
ax.set_xlabel('Posizioni')
plt.title('Posizioni conquistate nella stagione')

plt.show()


# %%
