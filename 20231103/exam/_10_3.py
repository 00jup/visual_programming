class Course:
    # 공유되어야 하는가 아니면 독자적으로 가져야 하는지 생각하기.
    def __init__(self, name, code, grade):
        self.name = name
        self.code = code
        self.grade = grade
        match grade:
            case 'A+':
                gpa = 4.5
            case 'A':
                gpa = 4
            case 'B+':
                gpa = 3.5
            case 'B':
                gpa = 3
            case 'C+':
                gpa = 2.5
            case 'C':
                gpa = 2
            case 'F':
                gpa = 0
        self.gpa = gpa

    def __repr__(self):
        # return str(code) + " " + str(grade) + " " + str(gpa)
        # 여기서 이걸 쓰려면 그냥 class 변수로 code, grade, gpa가 있어야 함.
        # return str(self.code) + " " + str(self.grade) + " " + str(self.gpa)
        return "{:<4} {:<2} {:<4}".format(self.code, self.grade, self.gpa)


a = Course('python', 1001, 'A+')
b = Course('c', 1002, 'B')
c = Course('python', 1001, 'C')

print(repr(c))
print(c)
print(a)
print(b)

(a.gpa + b.gpa + c.gpa) / 3

history = []
history.append(a)
history.append(b)
history.append(c)
print(history)

score = 0
for course in history:
    score += course.gpa
    print(course)
score /= len(history)
print(score)
