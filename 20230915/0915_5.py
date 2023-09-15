value = int(input("숫자를 입력하세요: "))



for i in range(3):
    
    if value> target:
        print('up')
    elif value < target:
        print('down')
    else:
        print('correct')
        break
else:
    print("failed")
    