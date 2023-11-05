class Course:

    def __init__(self, code, grade):
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


a = Course(1001, 'A+')
b = Course(1002, 'B')
c = Course(1001, 'C')

print(repr(a))
print(repr(b))
print(repr(c))
