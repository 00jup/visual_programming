class Library:

    def __init__(self, student_id):
        self.books = {'python': 0, 'C': 0, '맨먼스 미신': 0, '뇌를 자극하는 C언어': 0}
        self.borrows = {student_id: 0}
        self.borrows[student_id] = 0

    def rent_process(self, book_name, student_id):
        if self.books[book_name] == 0:
            self.books[book_name] = 1
            print("대출 되었습니다.\n")
            self.borrows[student_id] = 1

        elif self.books[book_name] == 1:
            print("이미 대여된 도서입니다.\n")

        elif self.borrows[student_id] == 1:
            print("대출한 도서를 먼저 반납하시기 바랍니다.\n")

        else:
            print("잘못 입력했습니다.\n\n")

    def return_process(self, book_name, student_id):
        if self.books[book_name] == 1:
            self.books[book_name] = 0
            print("반납되었습니다.\n")
            self.borrows[student_id] = 0

        elif self.books[book_name] == 0:
            print("반납 대상 도서가 아닙니다.\n")

        elif self.borrows[student_id] == 0:
            print("대출 이력이 없습니다.\n")

        else:
            print("잘못 입력했습니다.\n")


lib = {}
while (True):
    control = int(input("작업을 선택하세요. \n\t1.대출\n\t2.반납\n\t3.종료\n"))

    if control in [1, 2]:
        book_name = input("도서명을 입력하세요: ")
        student_id = int(input("학번을 입력하세요: "))
        if student_id not in lib:
            lib[student_id] = Library(student_id)

        if control == 1:
            lib[student_id].rent_process(book_name, student_id)

        elif control == 2:
            lib[student_id].return_process(book_name, student_id)

    elif control == 3:
        break
    else:
        print("잘못 입력하셨습니다.\n")

print(lib)
