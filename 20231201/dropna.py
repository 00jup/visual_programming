import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.random((20, 5)),
                  columns=["A", "B", "C", "D", "E"])

print(df[df > 0.5], end="\n\n")
print(df[df > 0.5].dropna(how="all"))
