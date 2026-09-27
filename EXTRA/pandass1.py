import pandas as pd
import matplotlib.pyplot as plt



data = pd.read_csv("SGA3.csv")  
print(data)
print(data["maths"].mean())

data["average"] = data[["maths", "physics", "chemistry"]].mean(axis=1)
data["allaverage"] = data[["maths", "physics", "chemistry"]].mean()




print(data)
data["allaverage"].plot(kind="bar")