class Library:

    def __init__(self, hello):
        self.hello = hello

    def __repr__(self):
        return str(self.hello)


lib = []
lib.append(Library("11"))
lib.append(Library("12"))
lib.append(Library("13"))

print(lib)
print(lib[0])
