import random

list = []
for i in range(1, 46):
    list.append(i)

random.shuffle(list)

rotto_list = list[0:6]
input_list = map(int, input("로또 번호를 입력하세요 : ").split())

count = 0
for i in input_list:
    if i in rotto_list:
        count += 1

print(rotto_list)
print("당첨 횟수 " + str(count))
