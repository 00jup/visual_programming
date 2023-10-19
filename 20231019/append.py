a = ["1"]
a.append(100)
print(a)

a.extend([200, 300])
a.extend([1000])
print(a)
# -> [100, 200, 300]

# 위 아래는 다르다. extend 공간을 확장 append는 안에 집어 넣는다.
a.append([200, 300])
# -> [100, [200, 300]]
a.append((200, 300))
# -> [100, (200, 300)]
print(a)
# tuple을 넣는 것도 가능하다.

for i in range(None):
    print(i + ' ')
    if (i == 100):
        break
