#%%
import pandas as pd
import matplotlib.pyplot as plt

driversData = pd.read_csv('data/1984results_new.csv')

D1 = 'Niki Lauda'
D2 = 'Alain Prost'

driversData['GAINED D1'] = driversData['QUALI D1'] - driversData['POS D1']

driversData['GAINED D2'] = driversData['QUALI D2'] - driversData['POS D2']

sommaD1 = driversData[driversData['GAINED D1'] > 0]['GAINED D1'].sum()

sommaD2 = driversData[driversData['GAINED D2'] > 0]['GAINED D2'].sum()

posgained = [sommaD1,sommaD2]

#driversData.head()

#per aggiungere i label sulle barre
def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i], ha = 'center')

fig, ax = plt.subplots()
ax.barh([D1, D2], posgained, 0.4)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(True)
ax.spines['left'].set_visible(True)
#ax.invert_yaxis()   # labels read top-to-bottom
ax.set_xlabel('Posizioni')
addlabels(posgained, posgained)
plt.title('Posizioni conquistate nella stagione')

plt.show()

# %%
