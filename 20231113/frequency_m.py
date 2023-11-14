dictionary = {}
row = []

with open("hamlet.txt", 'r') as f:
    data = f.readline()
    while (data != ''):
        row = data.strip().split(" ")
        for word in row:
            if word:
                dictionary[word] = dictionary.get(word, 0) + 1
        data = f.readline()


sorted_dictionary = dict(sorted(
    dictionary.items(), key=lambda x: x[1], reverse=True))

with open("result.csv", 'w') as f:
    for key, value in sorted_dictionary.items():
        f.write(f"{key},{value}\n")
