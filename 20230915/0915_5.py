5import random

target = random.randrange(1, 101)


low = 0
high = 100
mid = 50


def binary_search(target):
    global low, high, mid
    if target < mid:
        high = mid
        mid = (low + mid) // 2
        binary_search(mid)
    elif target > mid:
        low = mid
        mid = (high + mid) // 2
        binary_search(mid)
    elif target == mid:
        print("mid is", mid)


print("target is", target)
binary_search(target)
