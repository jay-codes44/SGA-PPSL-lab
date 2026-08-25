import pandas as pd
from pathlib import Path

csv_file = Path(__file__).parent / "csvsample.csv"
data = pd.read_csv(csv_file)

data["Average"] = data[["Maths", "Science", "English"]].mean(axis=1)
print(data[["Name", "Average"]])