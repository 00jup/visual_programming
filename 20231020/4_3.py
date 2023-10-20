duplicated = int(input("허용 중복수를 입력하세요: "))
number_list = list(map(int, input("값을 입력하세요: ").split()))
result_list = {}
result = []

for i in range(1, len(number_list)+1):
    result_list[i] = number_list.count(i)
    if result_list[i] > duplicated:
        result.append(i)

print("중복된 수: ", end=" ")
for i in result:
    print(i, end=" ")
