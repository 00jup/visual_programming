import numpy as np
import pandas as pd

filename = "titanic.csv"
read_csv = pd.read_csv(filename)
read_csv = read_csv[["Survived", "Age"]].dropna()
read_csv["Age-band"] = np.floor(read_csv["Age"]/10)*10
read_csv = read_csv.astype({"Age-band": int})
read_csv = read_csv.groupby(["Age-band"]).count()["Survived"]
print(read_csv)
