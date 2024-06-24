import pandas as pd
import seaborn as sns


df = sns.load_dataset('diamonds')

print(df.head())
print(df.size)
print(df.head)
print(df.shape)

print('This is what we have :')
print(df.info())

print('This what we about to describe :')
print(df.describe())

print(df.isnull().sum())

