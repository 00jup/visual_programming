class Library:
    def __init__(self):
        self.books = {'파이썬 프로그래밍': 0,
                      'C언어 정복': 0,
                      '맨먼스 미신': 0,
                      "뇌자극 C": 0}
        self.borrows = {}

    def borrow_book(self):
        book_name = input("도서명을 입력하세요: ")
        student_id = input("학번을 입력하세요: ")
        if student_id not in self.borrows:
            self.borrows[student_id] = {0}

        if book_name not in self.books:
            print("소장하지 않은 도서입니다.")
        elif self.books[book_name] == 1:
            print("이미 대여된 도서입니다.")
        elif self.borrows[student_id] == 1:
            print("대출한 도서를 먼저 반납하시기 바랍니다.")
        elif self.books[book_name] == 0:
            self.books[book_name] = 1
            self.borrows[student_id] = 1
            print("대출되었습니다.")
        else:
            print("잘못된 접근입니다.")
        return

    def return_book(self):
        book_name = input("도서명을 입력하세요: ")
        student_id = int(input("학번을 입력하세요: "))


start = Library()

while (1):
    control = int(input("\n작업을 선택하세요.\n\t1.대출\n\t2.반납\n\t3.종료\n"))
    match control:
        case 1:
            start.borrow_book()
        case 2:
            start.return_book()
        case 3:
            break
        case _:
            print("잘못된 접근입니다.")
