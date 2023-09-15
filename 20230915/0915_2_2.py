A = float(input("점수 입력 : "))

match A:
    case 4.5:
        print("A+")
    case 4:
        print("A")
    case 3.5:
        print("B+")
    case 3:
        print("B")
    case 2.5:
        print("C+")
    case 2:
        print("C")
    case 1.5:
        print("D+")
    case 1:
        print("D")
    case _:
        print("F")
