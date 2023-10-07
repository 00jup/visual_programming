a = ()
print(a)

a = (1, 2, 3)
a = 1, 2, 3
print(a)
# 괄호가 없어도 튜플로 인식한다.

a = (1)
print(a)
# 튜플이 아니다.
a = (1,)
print(a)
# 튜플이다.

a = ("1", 2.1, True)
print(a)
a = tuple(("1", 2.1, True))

print(a[0:2])
# heterogeneous

# a = ((1, 2), (3, 4))
# print(a)
# print(a[0:100])
# # nested tuple
# # 좌표에 대한 나열 1시간 마다의 좌표라고 붙일 수도 있다.

# print(None)
# # NoneType
# (None, None)
# # tuple
# (1,)  # 여기에는 아무것도 없는 걸 명시하고 싶으면 none을 쓰면 된다.
# (1, None)

# print(len("abc"))
# print(len((1, 2,)))
# print(len((1, 2, None)))

# a = ("1", 2.1, True)
# print(False in a)
# print(2.1 in a)
# print(2.2 in a)
# b = (1, 2, 2)

# print(a in b)  # 집합
# print(a + b)  # concatenation
# # print(a * b)  # error
# print(a * 2)

# print(a.index(2.1))
# # print(a.index(False))
# # 있는 걸 요청해야 한다.
# # 안에 있는 지를 확인해야 한다.
# # True in a -> True or False 인지 확인하기
# if False in a:
#     location = a.index(False)


# # 와우우우우우
# location = a.index(True) if True in a else None


# print(a.count(False))

# b = (1, 2, 2)
# a = (2, 2, 2)
# print(a*b)
