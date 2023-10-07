max_duplicate = int(input("허용 중복수를 입력하세요: "))
number_list = list(map(int, input("값을 입력하세요: ").split()))
duplicate_number = {}
_number = []

for i in range(len(number_list)):
    duplicate_number[i] = number_list.count(i)
    if number_list.count(i) > max_duplicate:
        _number.append(i+1)

print("중복된 수: "+' '.join(map(str, _number)))
