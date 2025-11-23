import cmath
import math
from typing import Tuple


class ComplexOps:
    @staticmethod
    def rect_to_polar(x: float, y: float) -> Tuple[float, float]:
        r = math.hypot(x, y)
        theta = math.degrees(math.atan2(y, x))
        return r, theta


    @staticmethod
    def polar_to_rect(r: float, theta_deg: float) -> Tuple[float, float]:
        theta = math.radians(theta_deg)
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        return x, y


    @staticmethod
    def add(a: complex, b: complex) -> complex:
        return a + b


    @staticmethod
    def sub(a: complex, b: complex) -> complex:
        return a - b


    @staticmethod
    def mul(a: complex, b: complex) -> complex:
        return a * b


    @staticmethod
    def div(a: complex, b: complex) -> complex:
        return a / b


    @staticmethod
    def to_polar(z: complex) -> Tuple[float, float]:
        return ComplexOps.rect_to_polar(z.real, z.imag)


    @staticmethod
    def to_rect(z: complex) -> Tuple[float, float]:
        return (z.real, z.imag)