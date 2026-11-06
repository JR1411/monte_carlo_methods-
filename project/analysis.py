import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv("phi4_results.csv")

plt.plot(df["action_density"])
plt.show()
