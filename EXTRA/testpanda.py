import pandas as pd
import matplotlib.pyplot as plt

print("Pandas version:", pd.__version__)
print("Matplotlib imported successfully!")

data = [10, 20, 30, 40, 50]

plt.plot(data)
plt.show()