import pandas as pd

data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}

#Converting the data to DataFrme
df = pd.DataFrame(data)

#Printing the DataFrame
print(df)

#Selecting the two col
print(df[['Name','Age']])

