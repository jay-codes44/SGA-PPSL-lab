import pandas as pd
data = pd.read_csv("csvsample.csv")
print(data.head())
print(data.describe())
print(data.columns.tolist())

data['Average'] = data[['Maths', 'Science', 'English']].mean(axis=1)
print(data[['Name', 'Average']])  