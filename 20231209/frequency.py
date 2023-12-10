import pandas as pd
import numpy as np

hamlet = {}
row = []

with open("hamlet.txt", "r") as f:
    data = f.readline()

    while data:
        row = data.strip().split(' ')
        for word in row:
            if word not in hamlet:
                hamlet[word] = 0
            hamlet[word] += 1
        # for index in range(len(row)):
        #     if hamlet[row[index]] not in hamlet:
        #         hamlet[row[index]] = 0
        #     else:
        #         hamlet[row[index]] += 1
        data = f.readline()


sorted_dictionary = dict(sorted(
    hamlet.items(), key=lambda x: x[1], reverse=True))

with open("result.csv", 'w') as f:
    for key, value in sorted_dictionary.items():
        f.write(f"{key},{value}\n")
