#%%
import pandas as pd
import matplotlib.pyplot as plt

driversData = pd.read_csv('data/2021results.csv')

D1 = 'Max Verstappen'
D2 = 'Lewis Hamilton'

driversData['GAINED D1'] = driversData['ST D1'] - driversData['POS D1']

driversData['SP GAIN D1'] = driversData['S ST D1'] - driversData['SPRINT D1']

driversData['GAINED D2'] = driversData['ST D2'] - driversData['POS D2']

driversData['SP GAIN D2'] = driversData['S ST D2'] - driversData['SPRINT D2']

gareD1 = driversData[driversData['GAINED D1'] > 0]['GAINED D1'].sum()

sprintD1 = driversData[driversData['SP GAIN D1'] > 0]['SP GAIN D1'].sum()

gareD2 = driversData[driversData['GAINED D2'] > 0]['GAINED D2'].sum()

sprintD2 = driversData[driversData['SP GAIN D2'] > 0]['SP GAIN D2'].sum()

sommaD1 = gareD1 + sprintD1

sommaD2 = gareD2 + sprintD2

posgained = [sommaD1,sommaD2]

#driversData.head()
print(gareD1, sprintD1)


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
