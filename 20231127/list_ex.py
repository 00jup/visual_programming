value_list = list('111234')

print(value_list[:2])
print(value_list[2:])
print(set(value_list[:2]) < set(value_list[2:]))
value_list = list('121134')

print(set(value_list[:2]) < set(value_list[2:]))
print(set(value_list[:2]) ^ set(value_list[2:]))
