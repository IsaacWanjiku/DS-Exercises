import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

x = np.arange(10).reshape(-1,1)
y = np.array([0,0,0,0,1,1,1,1,1,1])

print('For x, have:', x)
print('...and for y:', y)


Ex4_2 = LogisticRegression(solver='liblinear', random_state=0)

#to fit, or train it
Ex4_2.fit(x,y)

#evaluate the model
print('answer:',)
print(Ex4_2.predict_proba(x))

#the actual predictions
print('This are the predictions :')
print(Ex4_2.predict)

#accuracy
print(Ex4_2.score(x,y))

print(confusion_matrix(y, Ex4_2.predict(x)))
cm = confusion_matrix(y,Ex4_2.predict(x))

#plotting
fig,ax = plt.subplots(figsize=(8,8))
ax.imshow(cm)
ax.grid(False)

ax.xaxis.set(ticks=(0,1),ticklabels=('predicted 0s','predicted 1s'))
             
ax.yaxis.set(ticks=(0,1),ticklabels=('Actual 0s', 'Actual 1s'))
ax.set_ylim(1.5,-0.5)

for i in range (2):
             
             for j in range(2):
                 ax.text(j,i,cm[i,j], ha='center',va='center',color='brown')

plt.show()
             


             
