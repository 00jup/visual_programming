
row = "1, 2, 3, 4, 5, 1, 2, 3, 4, 5\n"
print(row)

m_row = row.strip('\n').strip().split(", ")

dictionary = {}
print(m_row)
for word in m_row:
    if word:
        dictionary[word] = dictionary.get(word, 0) + 1


print(dictionary)
hello = {"a": 1, "b": 2}

# hello["c"] = hello.get("c")
hello["c"] = hello.get("c", 0)
hello["c"] += 1

print(hello)
