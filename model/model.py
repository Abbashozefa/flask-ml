from sklearn import linear_model
import pandas as pd 
import pickle

df=pd.read_csv('prices.csv')
y=df['Value']
X=df[['Rooms','Distance']]

lm=linear_model.LinearRegression()
lm.fit(X,y)

pickle.dump(lm,open('model.pkl','wb'))

print(lm.predict([[10,60]]))
print(f'Accuracy:{lm.score(X,y)}')
