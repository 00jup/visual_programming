from collections import defaultdict

words = defaultdict(int)

with open("hamlet.txt", "r") as f:
    data = f.readline()
    while (data != ""):
        row = data.lower().strip().split()
        for word in row:
            words[word] += 1
        data = f.readline()

words = dict(sorted(words.items(), key=lambda x: x[1], reverse=True))

with open("result.csv", "w") as f:
    for key, value in words.items():
        f.write(f"{key},{value}\n")
