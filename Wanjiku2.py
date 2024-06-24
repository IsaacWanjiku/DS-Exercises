
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

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(df[['latitude','longitude']], df[['median_house_value']], test_size = 0.33, random_state=0)

from sklearn import preprocessing
x_train_norm=preprocessing.normalize(x_train)
x_test_norm=preprocessing.normalize(x_test)

from sklearn.cluster import KMeans

exercise=KMeans(n_clusters=3, random_state=0, n_init=10)
exercise.fit(x_train_norm)

sns.scatterplot(data=x_train,x='longitude',y='latitude',hue=exercise.labels_)
plt.show()

sns.boxplot(x=exercise.labels_,y=y_train['median_house_value'])
plt.show()
