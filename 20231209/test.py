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

# print(df["B"])
print(df[[df.columns[0]]])
print(df[['A']])

new = df.groupby(["A", "B"]).sum()
# 모두 다 DataFrame의 형태임

# print(new["C"])
# print(new["D"])
## 출력이 안 되는 이유는 multi index가 되기 때문이다. ##

## 이건 columns에 속하기 때문에 출력이 가능함 ##

## multi index에 속하기 때문에 아래와 같이 사용가능하다. ##
# print(new.loc["bar"])
# print(new.loc[("bar", "one")])
# print(new.iloc[0])
