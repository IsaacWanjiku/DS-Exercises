
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
'''

df = pd.read_csv('../Downloads/housing.csv')

print(df.head())


plt.figure(figsize=(10,15))
sns.histplot(df['population'],kde=True)
plt.show()



plt.figure(figsize=(10,15))
sns.histplot(df['latitude'],kde=True)
plt.show()
'''
df = pd.read_csv('../Downloads/housing.csv', usecols=['longitude','latitude','median_house_value'])

print(df)

sns.scatterplot(data=df,x='longitude',y='latitude',hue='median_house_value')

plt.show()
