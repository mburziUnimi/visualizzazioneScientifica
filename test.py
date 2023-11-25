import pandas as pd
import matplotlib.pyplot as plt

driversData = pd.read_csv('data/F1DriversDataset.csv')
#print(driversData)
plt.bar(driversData["Driver"][1:5], height = driversData["Years_Active"][1:5])
plt.show()

#commento di prova
#driversData.head()