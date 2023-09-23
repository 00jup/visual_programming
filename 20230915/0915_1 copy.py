import sys

a, b, c = map(int, sys.stdin.readline().split())

if c < a:
    print(a)
elif c > b:
    print(b)
else:
    print((a+b)/2)


if a <= c <= b :
    print((a+b)/2)
## 이게 pythonic한 코드
## if a <= c <= b :

a = 10
b = 30
c = 20
## 회사마다 쓰는 방법이 다르다. 띄어쓰기도 어떻게 할지 이런 것도


