e_dic = {'one': 1, 'two': 2, 'three': [3, 4], '5': 8}


print(e_dic['three'])

print(e_dic.setdefault('5'))
print(e_dic.setdefault('6'))
print(e_dic.setdefault('7', 70))

print(e_dic)
