is_alive = 2
status = 400
match status:
    case 400 if is_alive:
        print("Bad")
    case 404 if is_alive:
        print("Not found")
    case 418 | 419 | 420:
        print("I'm a teapot")
    case _:
        print("hi")
