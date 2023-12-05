import pandas as pd
import numpy as np

df = pd.DataFrame(
    {
        "A": ["foo", "bar", "bar", "foo", "bar", "foo"],
        "B": ["one", "one", "two", "two", "one", "three"],
        "C": np.random.random(6),
        "D": np.random.random(6),
    }
)

# print(df.groupby("A").sum())
# print(df.groupby("A")[["C", "D"]].sum())
new = df.groupby(["A", "B"]).sum()
print(new)
print()
# 모두 다 DataFrame의 형태임

# # print(new["A"])
# # print(new["B"])
# ## 출력이 안 되는 이유는 multi index가 되기 때문이다. ##
# print(new["C"])
# print(new["D"])
# # print(new.loc["bar"])
# print(new.loc[("bar", "one")])
# print(new.iloc[0])
