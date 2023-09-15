is_alive = False
status = 400
match status:
    case 400 if is_alive:
        print("Bad Request")
    case 401 if is_alive:
        print("Unauthorized")
    case 418 | 419 | 420:
        print("I'm a teapot")
    case _:
        print("OK")
