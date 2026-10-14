# Name : Jay mangukiya
# PRN : 26070122272
# Batch : CSE C3
import requests
from bs4 import BeautifulSoup
import pandas as pd

# 1. URL of our Canteen webpage
url = "http://127.0.0.1:5000/menu"

# 2. Get webpage
response = requests.get(url)
response.raise_for_status()

# 3. Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# 4. Find all menu items
items = soup.find_all("li")

# 5. Store extracted data
data = []
for item in items:
    text = item.text.strip()
    name, price = text.split(" - ")
    data.append({"Item": name, "Price": price})

# 6. Convert to DataFrame
df = pd.DataFrame(data)

# 7. Display data
print(df)

# 8. Save to CSV
df.to_csv("canteen_menu.csv", index=False)

print("\nSaved to canteen_menu.csv")

