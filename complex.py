from __future__ import annotations
from typing import List
import math


class Complex:
    def __init__(self, real: float = 0, img: float = 0) -> None:
        self.real = real
        self.img = img

    @property
    def real(self) -> int | float:
        return self._real

    @real.setter
    def real(self, value) -> None:
        if abs(value - int(value)) < 1e-5:
            if value <= 0:
                value = math.ceil(value)
            else:
                value = math.floor(value)
        self._real = value

    @property
    def img(self) -> int | float:
        return self._img

    @img.setter
    def img(self, value) -> None:
        if abs(value - int(value)) < 1e-5:
            if value <= 0:
                value = math.ceil(value)
            else:
                value = math.floor(value)
        self._img = value

    @property
    def polar(self) -> List[int | float]:
        r = (self.real ** 2 + self.img ** 2) ** 0.5
        if r == abs(self.img):
            if r == self.img:
                theta = math.pi / 2
            else:
                theta = 270 * math.pi / 180
        elif r == abs(self.real):
            if r == self.real:
                theta = 0
            else:
                theta = math.pi
        else:
            theta = math.atan(self.img / self.real)

        return [r, theta]

    def __repr__(self) -> str:
        return f'Complex(real={self.real}, img={self.img}, polar={self.polar})'

    def __str__(self) -> str:
        if self.img > 0:
            if self.real != 0:
                return f'{self.real} + {self.img}i'
            return f'{self.img}i'
        if self.img == 0:
            return f'{self.real}'
        if self.real == 0:
            return f'{self.img}i'
        return f'{self.real} - {abs(self.img)}i'

    def __add__(self, other) -> Complex:
        if isinstance(other, Complex):
            return Complex(real=self.real + other.real, img=self.img + other.img)
        elif isinstance(other, (int, float)):
            return Complex(real=self.real + other, img=self.img)
        else:
            raise TypeError('Addition with complex numbers only supported by int, float, or Complex')

    def __iadd__(self, other) -> Complex:
        if isinstance(other, Complex):
            self.real += other.real
            self.img += other.img

        elif isinstance(other, (int, float)):
            self.real += other

        else:
            raise TypeError('Addition with complex numbers only supported by int, float, or Complex')

        return self

    def __neg__(self) -> Complex:
        return Complex(real=-self.real, img=-self.img)

    def __pos__(self) -> Complex:
        return Complex(real=abs(self.real), img=abs(self.img))

    def __rsub__(self, other) -> Complex:
        return -self + other

    def __eq__(self, other) -> bool:
        if isinstance(other, Complex):
            return self.real == other.real and self.img == other.img
        return False

    def __ne__(self, other) -> bool:
        if isinstance(other, Complex):
            return self.real != other.real or self.img != other.img
        return False

    def __sub__(self, other) -> Complex:
        if isinstance(other, Complex):
            return Complex(real=self.real - other.real, img=self.img - other.img)
        elif isinstance(other, (int, float)):
            return Complex(real=self.real - other, img=self.img)
        else:
            raise TypeError('Subtraction with complex numbers only supported with int, float, or Complex')

    def __isub__(self, other) -> Complex:
        if isinstance(other, Complex):
            self.real -= other.real
            self.img -= other.img

        elif isinstance(other, (int, float)):
            self.real -= other

        else:
            raise TypeError('Subtraction with complex numbers only supported with int, float, or Complex')

        return self

    def __mul__(self, other) -> Complex:
        if isinstance(other, Complex):
            real = self.real * other.real - self.img * other.img
            img = self.real * other.img + self.img * other.real
            return Complex(real=real, img=img)

        elif isinstance(other, (int, float)):
            return Complex(real=other * self.real, img=other * self.img)

        else:
            raise TypeError('Multiplication with complex numbers only supported by int, float, or Complex')

    def __truediv__(self, other) -> Complex:
        if isinstance(other, Complex):
            conjugate = other.conjugate()
            divisor = (other * conjugate).real
            numerator = (self * conjugate)
            numerator.real /= divisor
            numerator.img /= divisor
            return numerator

        elif isinstance(other, (int, float)):
            return Complex(real=self.real / other, img=self.img / other)

        else:
            raise TypeError('Division with complex numbers only supported with int, float, or complex')

    def __rtruediv__(self, other):
        conjugate = self.conjugate()
        if isinstance(other, (Complex, int, float)):
            divisor = (self * conjugate).real
            numerator = (other * conjugate)
            numerator.real /= divisor
            numerator.img /= divisor
            return numerator

        else:
            raise TypeError('Division with complex numbers only supported with int, float, or complex')

    def __rfloordiv__(self, other) -> Complex:
        result = other / self
        result.real //= 1
        result.img //= 1
        return result

    def __floordiv__(self, other):
        result = self / other
        result.real //= 1
        result.img //= 1
        return result

    def __pow__(self, power) -> Complex:
        if isinstance(power, Complex) and self.img != 0:
            if power.img != 0:
                polar_form = power.polar
                complex_log = Complex(real=math.log(polar_form[0]), img=polar_form[1])
                exponent = self * complex_log
                real_part = math.exp(exponent.real)
                imaginary = Complex(real=math.cos(exponent.img), img=math.sin(exponent.img))
                return imaginary * real_part
            else:
                power = power.real
        if isinstance(power, (int, float)):
            polar = self.polar
            polar[0] **= power
            polar[1] *= power
            return Complex(real=polar[0] * math.cos(polar[1]), img=polar[0] * math.sin(polar[1]))

        if self.img == 0:
            return self.real ** power

    def __rpow__(self, other) -> Complex:
        real_part = pow(other, self.real)
        e = math.log(other) * self.img
        imaginary = Complex(real=math.cos(e), img=math.sin(e))  # Euler's formula
        return imaginary * real_part

    def __abs__(self):
        return self.polar[0]

    def conjugate(self) -> Complex:
        return Complex(real=self.real, img=-self.img)

    __radd__ = __add__
    __rmul__ = __mul__



