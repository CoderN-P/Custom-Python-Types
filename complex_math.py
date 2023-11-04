from complex import Complex
import math


def exp(x):
    return sum([
        (x ** n) / math.factorial(n)
        for n in range(0, 100)
    ])


def euler_formula(n):
    if n.real != 0:
        return
    return Complex(real=math.cos(n.img), img=math.sin(n.img))
print(oct(123))
