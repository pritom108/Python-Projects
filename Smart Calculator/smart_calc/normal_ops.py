import math
from typing import Union


Number = Union[int, float]


class NormalOps:
    @staticmethod
    def add(a: Number, b: Number) -> Number:
        return a + b


    @staticmethod
    def sub(a: Number, b: Number) -> Number:
        return a - b


    @staticmethod
    def mul(a: Number, b: Number) -> Number:
        return a * b


    @staticmethod
    def div(a: Number, b: Number) -> Number:
        if b == 0:
            raise ZeroDivisionError("Division by zero")
        return a / b


    @staticmethod
    def pow(a: Number, b: Number) -> Number:
        return a ** b


    @staticmethod
    def sqrt(a: Number) -> float:
        if a < 0:
            raise ValueError("Negative square root")
        return math.sqrt(a)


    @staticmethod
    def trig(func: str, x: Number, degrees: bool = False) -> float:
        if degrees:
            x = math.radians(x)
        if func == 'sin':
            return math.sin(x)
        if func == 'cos':
            return math.cos(x)
        if func == 'tan':
            return math.tan(x)
        raise ValueError('Unknown trig function')


    @staticmethod
    def log(x: Number, base: float = math.e) -> float:
        if x <= 0:
            raise ValueError('log domain error')
        return math.log(x, base)


    @staticmethod
    def factorial(n: int) -> int:
        if n < 0:
            raise ValueError('factorial domain error')
        return math.factorial(n)