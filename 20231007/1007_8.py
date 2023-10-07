order = {}

for i in range(6):
    # name, price = map(str, input("물건"), int, input("가격"))
    name, price = input("물건 이름과 금액 입력 : ").split()
    order[name] = int(price)

sum = 0

for i in order.values():
    sum += i


print(f"{sum}원")
