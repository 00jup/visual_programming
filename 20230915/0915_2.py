grade = input("점수 입력 : ")
repeat = True if input("재수강 여부 입력 : ") == "Y" else False

match grade:
    case 'A+' if not repeat:
        print(4.5)
    case 'A+' if repeat:
        print(4)
    case 'A':
        print(4)
    case 'B':
        print("3.5")
    case 'B+':
        print("3")
    case 'C+':
        print("2.5")
    case 'C':
        print("2")
    case 'D+':
        print("1.5")
    case 'D':
        print("1")
    case 'F':
        print("0")
    case _:
        print("잘못된 입력입니다.")
