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
class CourseHistory:

    def __init__(self):
        self.history = []

    def get_gpa(self):
        gpa = 0
        for course in self.history:
            gpa += course.gpa
        return gpa / len(self.history)
    
    def add_course(self, course):
        self.history.append(course)

A = CourseHistory()
a.add_course(a)
b.add_course(a)
a.add_course(c)

print(a.get_gap(), b.get_gpa())

class CourseManager:
    # def __init__(self, Course):
    #     pass
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        self.average = (self.x.gpa + self.y.gpa + self.z.gpa)/3

    def average(self):
        return self.average

    def search(self, number):
        if self.x.code == number:
            return "{:<4} {:<2} {:<4}".format(self.x.code, self.x.grade, self.x.gpa)
        elif self.y.code == number:
            return "{:<4} {:<2} {:<4}".format(self.y.code, self.y.grade, self.y.gpa)
        elif self.z.code == number:
            return "{:<4} {:<2} {:<4}".format(self.z.code, self.z.grade, self.z.gpa)


manager = CourseManager(a, b, c)
print(manager.average())
print(manager.search(1002))
