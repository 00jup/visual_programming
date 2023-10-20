import random

goal = random.randint(1, 100)

for count in range(1, 11):
    num = int(input("맞춰보세요 : "))
    if num == goal:
        print("정답!\n")
    elif count == 10:
        print("실패!")
        print(goal)
