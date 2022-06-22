import pandas as pd
import numpy as np

#Reading dataset
data = pd.read_csv(r'C:\Users\pulke\OneDrive\Desktop\Advertisment\Hero Motocorp.csv')
print(data.head())

print(data.tail())

#printing dataset coloums
print(data.columns)

#Shape of the dataset
print(data.shape)

#DataType and missing value check
print(data.info())

#Statistical Summary of Numerical features
print(data.describe())





