### 데이터를 쌓고 싶을 때 쓴다 ###

### 갚을 입력하고 빼는 게 알아서 된다. ###

# a['LA'] = 'A+'

a = dict()
print(a)

a = {1: 1, 2: 2, 3: 3}
print(a)

a = dict(one=1, two=2, three=3)
#### 튜플을 쓸 수도 있다. ####
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
f = dict({'one': 1, 'three': 3}, two=2)

print(a == b == c == d == e == f)

a = {}

a['1'] = 1
print(a)

a['two'] = 2

print(a)

a['2'] = []
print(a)

a['3'] = (4, 5)
a['3'] = (1, 2, 3)
print(a)
a['2'].append(1)
print(a)

print('\n\n\n')

a = {'one': 1, 'two': 2, 'three': 3}

print(3 in a)
### key만 확인한다. ###
print(3 not in a)  # -> 이것도 가능함 ##
print('three' in a)

##### 학번을 넣고 이름이 나오고, 이름을 넣고 학번을 찾고 싶을 때의 코드 #####
## -> 하나의 dictionary에 다 넣는다. ##
## -> 두 개의 dictionary를 만든다. ##

print(a.keys())

print('\n\n\n')

print(a.get('10'))

print(a.setdefault('10'))

print(a.setdefault('10', 100))  # -> None을 가지고 옴
print(a.setdefault('5', 100))
############ 왜 안 되지###########
print(a.items())

## 정의 -> 사전 키와 vlaue을 원소로 하는 tuple, tuple을 list로 하는 것 ##

del a['10']
print(a)

print(a)

# print(a.pop('5'))
print(a.popitem())
print(a.popitem())
print(a.popitem())
print(a)

a = {}
a['1'] = 1
a['2'] = 2
a['3'] = 3
print(a)
a['3'] = 111
print(a)
### LIFO ###

b = {'3': 3, '4': 4, '5': 5}
a.update(b)  # a |= b
print(a)
#### 생각보다 정말 많이 씀 ####
## 어제 출석부, 오늘 출석부 ##
## 부를 때 어제 출석부에 오늘 출석을 이어서 부르고 싶다 할 때 쓰는 것 ##

print(len(a))

### 집어넣으면 알아서 들어간다는 것을 기억하기 ###

### 기존 정보가 존재하면 그대로 유지하고 없으면 새로 집어넣는다.    ###

a['A'] = None
if 'A' not in a:
    a['A'] = 1
### A라는 사람이 만약에 없다면 새로 쓰겠다. ###
print()
print(a)


# count['나는'] += 1
# count['밥을'] += 1
# count['먹었다'] += 1

## -> 단어가 몇 번 출연했는지 바로 알 수 있게 된다. ##
# split하고 집어넣으면 단어의 빈도 확인하는 거, 7줄로 해결이 가능하다.

################ 시험 ####################

# 20문제 문제 유형도 공개해줄 것. 다음주 금요일 3시에 풀린다.
# 전공자반 시험이라서 문제가 어렵다. 그래서 준비는 잘 해야 한다.
# 문제 어려움.
## 7,9는 나중에 해도 됌 ##
