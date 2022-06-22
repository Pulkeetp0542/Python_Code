import pandas as pd
import numpy as np

#Read the csv File
data = pd.read_csv(r'C:\Users\pulke\Downloads\Housing.csv')

#Print the head of the data
print(data.head())

#Print the tail of the data
print(data.tail())

#Print the mean of the Price
print(data['price'].mean())

#Print the max Price
print(data['price'].max())

#Print the min Price
print(data['price'].min())

#Print the shape of Data
print(data.shape)

#Statistical Summary of Numerical features 
print(data.describe())

print(data.info())

#Print the columns
print(data.columns)


#Yes/No Variables
varlist=['mainroad','guestroom','basement','hotwaterheating','airconditioning','prefarea']
data[varlist]=data[varlist].apply(lambda x:x.map({'yes':1,'no':0}))
print(data[varlist].head())

#Data
print(data)

#Dummies Variable

status = pd.get_dummies(data['furnishingstatus'])
print(status.head())

#Dummy variable for furnishingstatus
#Droping redundant
status=pd.get_dummies(data['furnishingstatus'],drop_first=True)
print(status.head())

#Concat
data=pd.concat([data,status],axis=1)
print(data.head())

#Droping Furniturestatus
data=data.drop('furnishingstatus',axis=1)
print(data.head())

#Columns
print(data.columns)

