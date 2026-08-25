# PRN: 26070122272
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("students.csv")
print(data.head())

data['Average'] = data[['Maths', 'Science', 'English']].mean(axis=1)
print(data[['Name', 'Average']])

import matplotlib.pyplot as plt
plt.bar(data['Name'], data['Average'], color='skyblue')
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.title("Average Marks of Students")
plt.show()