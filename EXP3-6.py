# PRN: 26070122272
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("students.csv")
print(data.head())

data['Average'] = data[['Maths', 'Science', 'English']].mean(axis=1)
print(data[['Name', 'Average']])

plt.hist(data['Maths'], bins=5, color='green', alpha=0.7)
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.title("Distribution of Maths Marks")
plt.show()