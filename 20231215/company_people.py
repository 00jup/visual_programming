from collections import defaultdict


class Company:

    def __init__(self):
        self.people = {}
        self.company_id = 2000

    def come_in(self):
        department = input("부서를 입력하세요: ")
        rank = input("직급을 입력하세요: ")
        name = input("이름을 입력하세요: ")
        if name not in self.people:
            self.people[name] = {}
        self.people[name]['팀'] = department
        self.people[name]['직급'] = rank
        self.people[name]['사번'] = self.company_id
        print(f"사번은 {self.people[name]['사번']}입니다.")
        self.company_id += 1

    def quit(self):
        id = int(input("사번을 입력하세요: "))
        for key, value in self.people.items():
            if id in value:
                print(value)

    def show(self):
        for key, value in self.people.items():
            print(key, value)

    def search(self):
        pass


start = Company()

while (True):
    control = int(
        input("\n작업을 선택하세요.\n\t1.입사\n\t2.퇴사\n\t3.목록\n\t4.조회\n\t5.종료\n"))
    match control:
        case 1:
            start.come_in()
        case 2:
            start.quit()
        case 3:
            start.show()
        case 4:
            start.search()
        case 5:
            break
        case _:
            print("잘못 입력하셨습니다.")
