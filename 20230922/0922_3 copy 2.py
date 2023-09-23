a = [1, 3, 2, 4]

a_sorted = sorted(a)
numb = []

for i in a_sorted:
    numb.append(a.index(i)+1)

print(numb)
