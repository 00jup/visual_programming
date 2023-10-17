a = ["1"]
a.append(100)
print(a)

a.extend([200, 300])
print(a)
# 위 아래는 다르다. extend 공간을 확장 append는 안에 집어 넣는다.
a.append([200, 300])
a.append(400)
# a.append(500, 600)
a.append((200, 300))
print(a)

a.remove(100)
print(a)

b = 1,

print(b)

c = 2, 3, 4
print(c)

a = 1, 2, 3, 4, 5, 6, 7
print()
print(a)
print(a[-1])
print(a[:-1])
print(a[-1:])
print(a[:-1:2])


a = [1, 2, 3, 4, 5, 6, 7]
print()
print(a)
print(a[-1])
print(a[:-1])
print(a[-1:])
print(a[:-1:2])

print()
print()
print(a[-1:])
print(a[-2:])
print(a[-1:-4:-1])


A = if int(input("숫자 입력 : ")) in a else None

print(A)
