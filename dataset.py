import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

titanic_df = sns.load_dataset('titanic')
print(titanic_df.head())
print(f"DataFrame shape : {titanic_df.shape}\n=================================")
print(f"DataFrame info : {titanic_df.info()}\n=================================")
print(f"DataFrame columns : {titanic_df.columns}\n=================================")
print(f"The type of each column : {titanic_df.dtypes}\n=================================")
print(f"How much missing value in every column : {titanic_df.isna().sum()}\n=================================")
sns.set(style="ticks")
plt.style.use("fivethirtyeight")
sns.catplot(x='sex', data=titanic_df, kind='count')
print(plt.show())
sns.catplot(x='pclass', data=titanic_df, hue='sex', kind='count')
print(plt.show())
titanic_df['person'] = titanic_df.sex
titanic_df.loc[titanic_df['age'] < 16, 'person'] = 'child'
print(f"person categories : {titanic_df.person.unique()}\n=================================")
print(f"distribution of person : {titanic_df.person.value_counts()}\n=================================")
print(f"mean age : {titanic_df.age.mean()}\n=================================")
sns.catplot(x='pclass', data=titanic_df, hue='person', kind='count')
print(plt.show())
titanic_df.age.hist(bins=80)
print(plt.show())

fig = sns.FacetGrid(titanic_df, hue="sex", aspect=4)
fig.map(sns.kdeplot, 'age', shade=True)

oldest = titanic_df['age'].max()

fig.set(xlim=(0, oldest))

fig.add_legend()
print(plt.show())
fig = sns.FacetGrid(titanic_df, hue="person",aspect=4)
fig.map(sns.kdeplot, 'age', shade=True)

oldest = titanic_df['age'].max()

fig.set(xlim=(0, oldest))

fig.add_legend()
print(plt.show())
fig = sns.FacetGrid(titanic_df, hue="pclass",aspect=4)
fig.map(sns.kdeplot, 'age', shade=True)

oldest = titanic_df['age'].max()

fig.set(xlim=(0, oldest))

fig.add_legend()
print(plt.show())
print(titanic_df.head())
deck = titanic_df['cabin'].dropna()

