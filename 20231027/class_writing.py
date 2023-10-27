## class 안의 값을 바꿀 수 있다. ##

class Int:
    value = -1

    def absolute():
        return abs(Int.value)

    class PosiInt:
        value = 2
        # value 값이 따로 있는 게 이상해..

        def square():
            # return PosiInt.value * PosiInt.value
            return Int.PosiInt.value * Int.PosiInt.value


Int.value, Int.PosiInt.value = -10, 20
print(Int.value, Int.PosiInt.value)

Int.PosiInt.value = abs(Int.value)
print(Int.PosiInt.value)

Int.value = -10
Int.PosiInt.value = Int.value
print(Int.PosiInt.value)

print(Int.PosiInt.square())
