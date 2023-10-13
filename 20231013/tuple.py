a, b, *c = (1, 2, 3, 4, 5)
print(a, b, c)
a, b, *c, d = (1, 2, 3, 4, 5)
print(a, b, c, d)

# a, *b, *c, d = (1, 2, 3, 4, 5) ## 이건 안 됨.
print(a, b, c, d)
