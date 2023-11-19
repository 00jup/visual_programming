
sum = 0
try:
    for i in range(10):
        num = int(input(f"{i+1}번째 값을 입력 하세요 : "))
        sum += num
except:
    pass
finally:
    print(sum)


a = 0


def test():
    print("Hi")


class Myclass:
    b = 0
