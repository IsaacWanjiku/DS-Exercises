
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

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


from sklearn.metrics import silhouette_score
perf=silhouette_score(x_train_norm,exercise.labels_,metric='euclidean')
print(perf)

K=range(2,8)
fits=[]

score=[]
for k in K:
    new_exercise_model=KMeans(n_clusters=k,random_state=0, n_init=10).fit(x_train_norm)
    fits.append(new_exercise_model)
    score.append(silhouette_score(x_train_norm,exercise.labels_,metric='euclidean'))
print(fits)
print(score)

sns.scatterplot(data=x_train,x='longitude',y='latitude',hue=fits[0].labels_)
plt.show()

sns.scatterplot(data=x_train,x='longitude',y='latitude',hue=fits[2].labels_)
plt.show()

sns.scatterplot(data=x_train,x='longitude',y='latitude',hue=fits[5].labels_)
plt.show()



sns.lineplot(x=k,y=score)
plt.show()


sns.scatterplot(data=x_train,x='longitude',y='latitude',hue=fits[3].labels_)
plt.show()
sns.boxplot(x=fits[3].labels_,y=y_train['median_house_value'])
plt.show()
                


                      
