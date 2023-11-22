import dataclasses
from typing import Any, Callable
from numpy import *

r2d: float = 180 / pi
d2r: float = pi / 180


@dataclasses.dataclass
class V:
    x: float
    y: float

    def __str__(self) -> str:
        return f'({self.x},{self.y})'

    def mag(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    @staticmethod
    def dot(a, b) -> float:
        return a.x * b.x + a.y * b.y

    @staticmethod
    def angle(a, b) -> float:
        # cosθ = \a･\b / |\a||\b|
        lal: float = a.mag()
        lbl: float = b.mag()
        dot: float = V.dot(a, b)
        theta: float = arccos(dot / (lal * lbl))
        return theta * r2d

    @staticmethod
    def polar_to_rectangular(a):
        x: float = a.x * cos(a.y)
        y: float = a.x * sin(a.y)
        return V(x, y)


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
    lal: float = sqrt(a.x ** 2 + a.y ** 2)
    lbl: float = sqrt(b.x ** 2 + b.y ** 2)
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
    theta = arccos(cos8) * r2d
    theta2 = arccos(cos82) * r2d
    print('θ:', theta, '\nθ2:', theta2)  # cos45°


@prefix('polor')
def polar():
    #! x=rcosθ, y=rsinθ
    a = V(2, pi/3)
    ax = a.x * cos(a.y)
    ay = a.x * sin(a.y)
    print('a:', V(ax, ay))  # (1, √3)

    b = V(sqrt(2), pi/4)
    bx = b.x * cos(b.y)
    by = b.x * sin(b.y)
    print('b:', V(bx, by))  # (1, 1)

    c = V(4, 5/6*pi)
    cx = c.x * cos(c.y)
    cy = c.x * sin(c.y)
    print('c:', V(cx, cy))  # (-2√3, 2)

    d = V(3, pi)
    dx = d.x * cos(d.y)
    dy = d.x * sin(d.y)
    print('d:', V(dx, dy))  # (-3, 0)


@prefix("sannkakuhi")
def tri() -> None:
    # cos(x) = sin(90°-x)
    # sin(x) = cos(90°-x)
    # 1/tan(x) = tan(90°-x)

    print('---', 1, '---')
    sin1 = 1/sqrt(10)
    cos1 = 3/sqrt(10)
    tan1 = 1/3
    print(sin1, cos1, tan1)

    print('---', 2, '---')
    sin2 = 5 / 12
    cos2 = 5/13
    tan2 = 13/12
    print(sin2, cos2, tan2)

    #! 底辺はマイナス
    # sin(135) = 1/√2
    # cos(135) = -(1/√2)
    # tan(135) = -1


if __name__ == '__main__':
    # angle()
    # polar()

    # print(V.angle(V(1, 2), V(3, 1)))
    # print(V.polar_to_rectangular(V(5, 30)))

    tri()
