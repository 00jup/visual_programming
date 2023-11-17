# # while True:

#     for value in range(10):
#         if value % 2 == 0:
#             continue
#         if value % 7 == 0:
#             break
#         print(value)
# 그냥 tab 하는 것도 안 됨


for value in range(10):
    if value % 2 == 0:
        continue
    if value % 7 == 0:
        break
    print(value)

print("----------------------------------------")
# for value in range(2.0, 11.0, 1.5):
#     print(value)

a = 10
a = 1 if a > 1 else 0

# 영어랑 어순 값음
print(a)

flag = False
for i in range(5):
    if i > 10:
        print("i>10")
        flag = True
    # 출력될 일 없음
    # 한번도 이런 구문이 실행되지 않는다면 이걸 하세요 이렇게 만들 수 있다.


if flag:
    print("flag is True")

# 불편함 c언어 스러움


for i in range(5):
    if i > 10:
        print("i>10")
    # 출력될 일 없음
    # 한번도 이런 구문이 실행되지 않는다면 이걸 하세요 이렇게 만들 수 있다.
else:
    print("flag is True")
# 만약 이 안에서 흐름을 해치는 구문이 실행되면 이걸 실행해라
# 비밀번호 최대 3번 입력 다 틀리면? 아무것도 못하게 만들어야 하는데 그게 else안에 들어가는 것
