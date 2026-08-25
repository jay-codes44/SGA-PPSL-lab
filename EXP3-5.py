# PRN: 26070122272
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("students.csv")
print(data.head())

data['Average'] = data[['Maths', 'Science', 'English']].mean(axis=1)
print(data[['Name', 'Average']])

plt.plot(data['Name'], data['Maths'], marker='o', label='Maths')
plt.plot(data['Name'], data['Science'], marker='o', label='Science')
plt.plot(data['Name'], data['English'], marker='o', label='English')
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Subject-wise Performance")
plt.legend()
plt.show()