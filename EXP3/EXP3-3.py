# PRN: 26070122272
import pandas as pd
data = pd.read_csv("students.csv")
print(data.head())
data['Average'] = data[['Maths', 'Science', 'English']].mean(axis=1)
print(data[['Name', 'Average']])