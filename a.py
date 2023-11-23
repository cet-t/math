import dataclasses
from typing import Any, Callable
import numpy as np
import math

r2d: float = 180 / math.pi
d2r: float = math.pi / 180


@dataclasses.dataclass
class V:
    x: float
    y: float

    def __str__(self) -> str:
        return f'({self.x},{self.y})'

    def mag(self) -> float:
        return np.sqrt(self.x ** 2 + self.y ** 2)

    @staticmethod
    def dot(a, b) -> float:
        return a.x * b.x + a.y * b.y

    @staticmethod
    def angle(a, b) -> float:
        # cosθ = \a･\b / |\a||\b|
        lal: float = a.mag()
        lbl: float = b.mag()
        dot: float = V.dot(a, b)
        theta: float = np.arccos(dot / (lal * lbl))
        return theta * r2d

    @staticmethod
    def polar_to_rectangular(a):
        x: float = a.x * np. cos(a.y)
        y: float = a.x * np. sin(a.y)
        return V(x, y)


class mathematics:
    __MAX_DIGIT: int = 16
    RAD_TO_DEG: float = 180 / np.pi
    DEG_TO_RAD: float = np.pi / 180

    @staticmethod
    def sin(theta_deg: float, digit: int = 1) -> float:
        # 0以下なら0、__MAX_DIGIT未満ならdigit、__MAX_DIGIT以上なら__MAX_DIGIT
        return np.sin(theta_deg * mathematics.__MAX_DIGIT) if digit <= 0 else np.round(np.sin(theta_deg * mathematics.DEG_TO_RAD), digit if digit < mathematics.__MAX_DIGIT else mathematics.__MAX_DIGIT)

    @staticmethod
    def cos(theta_deg: float, digit: int = 1) -> float:
        return np.cos(theta_deg * mathematics.__MAX_DIGIT) if digit <= 0 else np.round(np.cos(theta_deg * mathematics.DEG_TO_RAD), digit if digit < mathematics.__MAX_DIGIT else mathematics.__MAX_DIGIT)

    @staticmethod
    def tan(theta_deg: float, digit: int = 1) -> float:
        return np.tan(theta_deg * mathematics.__MAX_DIGIT) if digit <= 0 else np.round(np.tan(theta_deg * mathematics.DEG_TO_RAD), digit if digit < mathematics.__MAX_DIGIT else mathematics.__MAX_DIGIT)


def deco_s_deco(func) -> Callable[..., Any]:
    '''https://qiita.com/nshinya/items/b6746a0c07e9e20389e8'''
    def param(*args, **kwargs) -> Callable[..., Any]:
        def wrap(f) -> Any:
            return func(f, *args, **kwargs)
        return wrap
    return param


@deco_s_deco
def prefix(func, prefix: str) -> Callable[..., Any]:
    def wrap(*args, **kwargs) -> Any:
        line = '*---*'
        print(line, prefix, line)
        r: Any = func(*args, **kwargs)
        sfx: str = ''
        for i in range(end := len(prefix) + 2 + len(line) * 2):
            sfx += '*' if i == 0 or i == end-1 else '-'
        print(sfx)
        return r
    return wrap


@prefix('angle')
def angle():
    a = V(1, 2)
    b = V(3, 1)

    # magnitude
    lal: float = np.sqrt(a.x ** 2 + a.y ** 2)
    lbl: float = np.sqrt(b.x ** 2 + b.y ** 2)
    print('|a|:', lal)
    print('|b|:', lbl)

    # dot
    dot: float = a.x * b.x + a.y * b.y
    print('dot:', dot)

    # cosθ
    cos8: float = dot / (lal * lbl)
    cos82: float = dot / lal / lbl
    print(cos8)

    # radian to degree
    theta = np.arccos(cos8) * r2d
    theta2 = np.arccos(cos82) * r2d
    print('θ:', theta, '\nθ2:', theta2)  # cos45°


@prefix('polor')
def polar():
    #! x=rcosθ, y=rsinθ
    a = V(2, math. pi/3)
    ax = a.x * np.cos(a.y)
    ay = a.x * np.sin(a.y)
    print('a:', V(ax, ay))  # (1, √3)

    b = V(np.sqrt(2), math.pi/4)
    bx = b.x * np. cos(b.y)
    by = b.x * np.sin(b.y)
    print('b:', V(bx, by))  # (1, 1)

    c = V(4, 5/6*math.pi)
    cx = c.x * np.cos(c.y)
    cy = c.x * np.sin(c.y)
    print('c:', V(cx, cy))  # (-2√3, 2)

    d = V(3, math.pi)
    dx = d.x * np.cos(d.y)
    dy = d.x * np.sin(d.y)
    print('d:', V(dx, dy))  # (-3, 0)


@prefix("sannkakuhi")
def tri() -> None:
    # cos(x) = sin(90°-x)
    # sin(x) = cos(90°-x)
    # 1/tan(x) = tan(90°-x)

    print('---', 1, '---')
    sin1 = 1/np.sqrt(10)
    cos1 = 3/np.sqrt(10)
    tan1 = 1/3
    print(sin1, cos1, tan1)

    print('---', 2, '---')
    sin2 = 5/12
    cos2 = 5/13
    tan2 = 13/12
    print(sin2, cos2, tan2)

    print('------')
    # sin135° = √2/2
    print(mathematics.sin(135, 3))
    # cos135° = -(√2/2)
    print(mathematics.cos(135))
    # tan135° = -1
    print(mathematics.tan(135))


if __name__ == '__main__':
    tri()
    # angle()
    # polar()

    # print(V.angle(V(1, 2), V(3, 1)))
    # print(V.polar_to_rectangular(V(5, 30)))
