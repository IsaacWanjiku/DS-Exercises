import plotly.express as px
import seaborn as sns

x = [1,2 ,3,4]

y = [1,2,3,4]

fig = px.line(x,y)
fig.show()

df = sns.load_dataset('diamonds')
fig = px.line(df, x='price', y='z')

fig = px.imshow(df,x='cut',y='carat')
fig.show()

sample_df= px.df.medals_wide(indexed=True)
fig = px.imshow(sample_df)
fig.show()
