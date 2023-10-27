class Int:
    value = -1

    def absolute():
        return abs(Int.value)

    class PosiInt:
        value = 2

        def square():
            # return PosiInt.value * PosiInt.value
            return Int.PosiInt.value * Int.PosiInt.value


print(Int.value, Int.absolute())
# class 이름 안에 있는 것을 가져오겠다.
# 무조건 앞에서부터 끊어서 하나씩 하나씩 생각하기

print(Int.PosiInt.value)

print(Int.PosiInt.square())
