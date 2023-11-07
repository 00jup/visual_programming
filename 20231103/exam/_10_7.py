class Company:
    people = {}

    def __init__(self):
        self.people = {'봉준호': 12345, '박찬욱': 12340, '최동훈': 21131}
        self.department = {'봉준호': {'팀': '개발팀', '직급': '대리'},
                           '박찬욱': {'팀': '개발팀', '직급': '대리'},
                           '최동훈': {'팀': '서비스팀', '직급': '과장'}}

    def join(self):
        name = input("이름을 입력하세요: ")
        team = input("부서를 입력하세요: ")
        rank = input("직급을 입력하세요: ")
        company_number = int(input("사번을 입력하세요: "))
        self.people[name] = company_number
        self.department[name] = {'팀': team, '직급': rank}
        print("입력되었습니다.\n")

    def leave(self):
        company_number = int(input("사번을 입력하세요: "))
        for key, value in self.people.items():
            if company_number == value:
                print(f"{self.department[key]['팀']}"
                      f"{self.department[key]['직급']}"
                      f"{key}"
                      f"({self.people[key]})에 대해 퇴사 처리 되었습니다.\n")
                del self.people[key]
                del self.department[key]
                break
            else:
                print("존재하지 않는 사번입니다.\n")

    def list(self):
        for key, value in self.people.items():
            print(f"{self.department[key]['팀']}"
                  f"{self.department[key]['직급']}"
                  f"{key}"
                  f"({self.people[key]})")
        print()

    def search(self):
        company_number = int(input("사번을 입력하세요: "))
        for key, value in self.people.items():
            if company_number == value:
                print(f"{self.department[key]['팀']}"
                      f"{self.department[key]['직급']}"
                      f"{key}"
                      f"({self.people[key]})\n")
                break
            else:
                print("존재하지 않는 사번입니다.\n")

    def __repr__(self):
        pass


company = Company()
repeat_flag = True

while repeat_flag:
    control = int(
        input("작업을 선택하세요.\n\t1.입사\n\t2.퇴사\n\t3.목록\n\t4.조회\n\t5.종료\n"))
    match control:
        case 1:
            company.join()
        case 2:
            company.leave()
        case 3:
            company.list()
        case 4:
            company.search()
        case 5:
            break
        case _:
            print("잘못 입력하셨습니다.\n")
