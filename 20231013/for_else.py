for i in range(5):
    if i > 10:
        print("i>10")
    else:
        break
    # 출력될 일 없음
    # 한번도 이런 구문이 실행되지 않는다면 이걸 하세요 이렇게 만들 수 있다.
else:
    print("flag is True")
# 만약 이 안에서 흐름을 해치는 구문이 실행되면 이걸 실행해라
# 비밀번호 최대 3번 입력 다 틀리면? 아무것도 못하게 만들어야 하는데 그게 else안에 들어가는 것

for i in range(5):
    if i == 3:
        break
else:
    print("Loop finished")

for i in range(5):
    if i == 3:
        print(10)
else:
    print("Loop finished")
