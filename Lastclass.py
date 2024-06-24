import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
dates = pd.date_range(start='2022-01-01' ,periods=100,freq='D')

values = np.random.randn(100).cumsum()

data = pd.DataFrame({'date': dates, 'value': values})

data.set_index('date', inplace=True)

plt.plot(data.index,data['value'])
plt.xlabel('value')
plt.xticks(rotation=45)
plt.title('Time Series Data')

plt.show()

from statsmodels.tsa.stattools import adfuller

result=adfuller(data)
print('ADF statics:',result[0])
print('p-value', result[1])
