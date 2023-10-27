# 개념과 외형

class Human:

    number_of_arms = 2

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


me, you = Human("park", 60), Human("kim", 70)

me.age, you.age = 20, 30

print(me.age, you.age)
## 인스턴스 변수라서 서로 공유하지 않아서 다른 값을 가질 수 있음 ##
## Human에는 존재하지 않았기 때문에 ##
## class에서 instance 변수에 접근할 수 없다. ##

## 개념은 구체적인 개념을 포함할 수 없다. ##

print(me.number_of_arms, you.number_of_arms)
## 개별적이고 보편적인 것들은 개념을 포함하고 있다. ##
## 모든 사람들은 팔 정보를 가지고 있고 공유하고 있다.##

### 인스턴스 변수를 바꾼다고 다른 사람의 나이가 바뀌지는 않는다. ###

Human.number_of_arms = 3
print(me.number_of_arms, you.number_of_arms)
# 보편적 class 개념은 instance가 가지지만 instance가 가진건 class가 가지지 않는다. #
