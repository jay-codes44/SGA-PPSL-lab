# PRN: 26070122272
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("students.csv")
print(data.head())

data['Average'] = data[['Maths', 'Science', 'English']].mean(axis=1)
print(data[['Name', 'Average']])

plt.pie(data['Average'], labels=data['Name'], autopct='%1.1f%%', startangle=90)
plt.title("Share of Average Marks by Student")
plt.show()

data.to_csv("students_cleaned.csv", index=False)