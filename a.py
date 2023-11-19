import dataclasses
from typing import Any, Callable
import numpy as np

rad2deg: float = 180 / np.pi


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
        return theta * rad2deg

    @staticmethod
    def polor_to_rectangular(a):
        x: float = a.x * np.cos(a.y)
        y: float = a.x * np.sin(a.y)
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
    lal = np.sqrt(a.x ** 2 + a.y ** 2)
    lbl = np.sqrt(b.x ** 2 + b.y ** 2)
    print('|a|:', lal)
    print('|b|:', lbl)

    # dot
    dot = a.x * b.x + a.y * b.y
    print('dot:', dot)

    # cosθ
    cos_theta = dot / (lal * lbl)
    print('θ: ', cos_theta)

    # radian to degree
    theta = np.arccos(cos_theta) * rad2deg
    theta2 = np.arccos(dot / lal / lbl) * rad2deg
    print('θ:', theta, '\nθ2:', theta2)  # θ ≒ 45


@prefix('polor')
def polor():
    #! x=rcosθ, y=rsinθ
    a = V(2, np.pi/3)
    ax = a.x * np.cos(a.y)
    ay = a.x * np.sin(a.y)
    print('a:', V(ax, ay))  # (1, √3)

    b = V(np.sqrt(2), np.pi/4)
    bx = b.x * np.cos(b.y)
    by = b.x * np.sin(b.y)
    print('b:', V(bx, by))  # (1, 1)

    c = V(4, 5/6*np.pi)
    cx = c.x * np.cos(c.y)
    cy = c.x * np.sin(c.y)
    print('c:', V(cx, cy))  # (-2√3, 2)

    d = V(3, np.pi)
    dx = d.x * np.cos(d.y)
    dy = d.x * np.sin(d.y)
    print('d:', V(dx, dy))  # (-3, 0)


if __name__ == '__main__':
    # angle()
    # polor()

    print(V.angle(V(1, 2), V(3, 1)))
    print(V.polor_to_rectangular(V(5, 30)))
