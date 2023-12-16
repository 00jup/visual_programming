class Worker:
    def __init__(self, name=None, rank=None, department=None, worker_id=None):
        self.name = name
        self.rank = rank
        self.department = department
        self.worker_id = worker_id

    def __str__(self):
        return f"{self.name} {self.rank} {self.department} {self.worker_id}"


class Company:
    worker_id = 2000

    def __init__(self):
        self.workers = []

    def come_in(self):
        department = input("부서를 입력하세요: ")
        rank = input("직급을 입력하세요: ")
        name = input("이름을 입력하세요: ")

        NEW_WORKER = Worker(name, rank, department, Company.worker_id)
        Company.worker_id += 1

        self.workers.append(NEW_WORKER)
        print(str(NEW_WORKER))

    def quit(self):
        id = int(input("사번을 입력하세요: "))
        worker_index = 0

        for worker in self.workers:
            if worker.worker_id == id:
                break
            worker_index += 1

        print(str(self.workers[worker_index]))
        self.workers.pop[worker_index]

        return

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
