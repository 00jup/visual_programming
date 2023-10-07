order = {}

for i in range(5):
    user_input, price = input('품목을 입력하세요: ').split()
    price = int(price)

    order[user_input] = price

list(order.values())  # 뭐로 보고 싶은지 명시해줘야 함.
print(sum(list(order.values())))


print(order)
