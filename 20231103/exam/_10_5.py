class Imagine_numb:

    # def __init__(self, *values):
    #     self.values = tuple(self.values[:-1])
    def __init__(self, a, b, op, c, d):
        self.a, self.b = int(a), int(b)
        self.op = op
        self.c, self.d = int(c), int(d)
        if op == "+":
            self.__add__()

    def __add__(self):
        return f"{self.a + self.c} + {self.b + self.d}i"

    def __sub__(self):
        return f"{self.a - self.c} + {self.b - self.d}i"

    def __mul__(self):
        return f"{self.a * self.c + self.b * self.d} + {self.b * self.c + self.a * self.d}i"

    def __repr__(self):
        pass


class Complex:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __str__(self):
        return f"{self.real} + {self.imag}i"

    def __add__(self, complex):
        new_complex = Complex()
        new_complex.real = self.real + complex.real
        new_complex.imag = self.imag + complex.imag
        return new_complex


x = Complex(1, -1)
print(x)
y = Complex(2, 3)
print(x+y)
A = list(map(str, input("식을 입력하세요 : ").split()))
Imagine_numb(A)
