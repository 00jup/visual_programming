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
# heterogeneous

a = ((1, 2), (3, 4))
print(a)
# nested tuple
# 좌표에 대한 나열 1시간 마다의 좌표라고 붙일 수도 있다.
