from collections import defaultdict

# 내부 딕셔너리를 위한 defaultdict 생성 함수


def nested_dict():
    return defaultdict(nested_dict)


# defaultdict를 사용하여 중첩 딕셔너리 생성
my_dict = defaultdict(nested_dict)

# 값 할당
my_dict["Hello"]["1"] = 1
my_dict["HEllo"]["2"] = 2

print(my_dict)
