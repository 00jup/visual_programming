a = [1, 2, 3, 4, 5]
b = [a for i in range(2)]
a[0] += 10
b[0][2] += 20
print(f'\n[3. List multiply by list comprehension]')
print(f'{a=} # Weird')  # [11, 2, 13, 4, 5]
print(f'{b=} # Weird')  # [[11, 2, 13, 4, 5], [11, 2, 13, 4, 5]]