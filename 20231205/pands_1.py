import pandas as pd

filename = "titanic.csv"
read_csv = pd.read_csv(filename)

print(read_csv.describe())
