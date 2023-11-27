dictionary = {}
row = []
file_path = '/Users/parkjeong-uk/CODING/비쥬얼프로그래밍/20231113/hamlet.txt'
store_file_path = '/Users/parkjeong-uk/CODING/비쥬얼프로그래밍/20231113/frequency_result.csv'

with open(file_path, 'r') as f:
    data = f.readline()
    while (data):
        row = data.strip().split(" ")
        for word in row:
            if word:
                dictionary[word] = dictionary.get(word, 0) + 1
        data = f.readline()


sorted_dictionary = dict(sorted(
    dictionary.items(), key=lambda x: x[1], reverse=True))

with open(store_file_path, 'w') as f:
    for key, value in sorted_dictionary.items():
        f.write(f"{key},{value}\n")
