def fibonacci(n):
    a, b = 0, 1
    while a < n:
        print(a, end="\n")
        a, b = b, a+b


fibonacci(100)


def return_funtion():
    x = 1
    y = 2
    return x, y


a = return_funtion()
b, c = return_funtion()
print(a)
print(type(a))
print(b, c)


def return_funtion():
    x = 1
    y = 2
    return [x, y]
    

a = return_funtion()

print(a)
print(type(a))


def return_funtion():
    return 123, "123"
### -> 튜플이기 때문에 a, b, c = [1, 2, 3]에서 하나씩 들어감 ###


### 함수의 입력값과 출력값 없을 수도 있고 있을 수도 있고 여러개가 있을 수도 있다. ###
a = return_funtion()

print(a)
print(type(a))
