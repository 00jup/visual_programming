
def function(n, a, b):
    sum = 0
    for i in range(1, n+1, 1):
        if (i % a == 0 and i % b == 0):
            sum += i

    return sum


print(function(6, 2, 3))
