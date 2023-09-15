value = int(input("숫자를 입력하세요: "))

target = random.randrange(1, 101)
numb = 50

#### 하나씩 넣으면서 3번 확인하고 값을 찾는다.


def upDown(numb):
    if value >= numb:
        numb /= 2
        return "up"
    else:
        numb /= 2
        return "down"


for i in range(3):

    if value > target:
        print('up')
    elif value < target:
        print('down')
    else:
        print('correct')
        break
else:
    print("failed")
