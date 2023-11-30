import time


class MyClass:
    def __init__(self):
        print("I'm born!")
        time.sleep(2)

    def __del__(self):
        print("bye bye")


MyClass()
