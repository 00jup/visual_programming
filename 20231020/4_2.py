product = {}
sum = 0

for _ in range(1, 6):
    name, price = input().split()
    product[name] = int(price)
# () 상관 없나?
for value in product.values():
    sum += int(value)

print(f"{sum}원")
print(product)
