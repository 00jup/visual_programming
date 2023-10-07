a = set()

print(a)

a = {1, 2, 3, 4, }
print(a)
a = set((1, 2, 3, 3, 3, 3))
# 편리한 기능 -> 누구는 배고파서 학식을 2개 먹을 수도 있다. 중복을 없앨 때 간단하게 set하고 묶어버린다.
# 중복을 제거하는 활용법!!!!!!

print(a)

# 유일하게 집합만 공집합을 만드는 코드가 다르다.

# () [] {}
# 집합은 애매하다
# 사전과 똑같은 기호를 쓴다. 그래서 공집합 {} -> 이렇게 만들 수 없다.
# set() 유일하게 공집합 만드려면 이렇게 적어야 함.

a = set('abcc')
print(a)
## 순서가 섞인다. -> 순서가 상관없기 때문에 ##
# 저희가 배우고 있는 건 cpython임 세부적으로 멋대로 만든 부분이 있다. -> 순서가 섞이는 경우있음

# 수학적 집학과 Python 집합 뭐가 다르지? ### -> 물어보기

ㅁ = set({1, 2, 3, 4})
ㅁ.add(1)
ㅁ.add(5)
print(ㅁ)
####### 딕셔너리도 중복 안 되나? #######

a = {1, 2, 3, 4, 5}
a.discard(10)

# a.remove(10) -> 에러남 ##3
a = set('abcc')

print(a.pop())
## pop하면 random하게 하나씩 추출하는 거 아니야? -> python에서는 다름 ##
## 가장 앞에 있는 거 하나를 빼주는 역할, 정렬이 되어있지 않다는 거지 add한 건 그대로 있다. ##
print(a)

entire = {1, 2, 3, 4}
print(entire.issubset(entire))

print(entire <= entire)

print(entire < entire)

##### 집합처럼 사용하기 #####
a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
c = {5, 6, 7, 8}
print()
print(a.isdisjoint(b))
print(a.isdisjoint(c))

print(a.union(b))
print(a.intersection(b))

print(a.difference(b))

print(a.symmetric_difference(b))
# a-b -> 1,5가 출력된다.

print()
a, b = {1, 2, 3, 4}, {2, 3, 4, 5}
a.update(b)
## 새로 b에 있는 걸 바탕으로 a에 있는 것을 업데이트 하겠다. ##
print(a)

a, b = {1, 2, 3, 4}, {2, 3, 4, 5}
a.intersection_update(b)
print(a)

### 딕셔너리, 리스트 ### 개발자한테 중요함

