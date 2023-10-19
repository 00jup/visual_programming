A = [1, 2, 3, 4, 5]

print(A[-1:3:-1])
print(max(A))

print((lambda A, b: (A+b))(10, 20))

a = 5


def helle():
    print(a)


print(helle())

print(type(None))

count = 0
while count < 5:
    print(f"Count is {count}")
    count += 1
else:
    print("While loop is complete")
