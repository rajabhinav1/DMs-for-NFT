import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df = pd.read_csv('Nomics-CurrencyHistory-NFTS-USD-1d-2021-10-05T19_03_07.498Z.csv')
print (df)

#Matplotlib analysis frame GUI

from matplotlib import pyplot as plt
plt.rcParams["figure.figsize"] = [9.00, 3.50]
plt.rcParams["figure.autolayout"] = True
columns = ["timestamp", "transparent_volume","open"]
df = pd.read_csv("Nomics-CurrencyHistory-NFTS-USD-1d-2021-10-05T19_03_07.498Z.csv", usecols=columns)
print("Contents in csv file:\n", df)
plt.plot(df.timestamp, df.transparent_volume,df.open)
plt.show()

# Data Analysis through seaborn
#sns.set(style='darkgrid')
#churn = pd.read_csv("Nomics-CurrencyHistory-NFTS-USD-1d-2021-10-05T19_03_07.498Z.csv")
#print(churn.shape)
#(10127, 20)
#print(churn.head)
#churn.isna().sum().sum()
