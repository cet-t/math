from typing import *  # type: ignore
import numpy as np
import math

from vector2 import *


class mathematics:
    __MAX_DIGIT: int = 16

    @staticmethod
    def sin(deg: float, digit: int = 16) -> float:
        # 0以下なら0、__MAX_DIGIT未満ならdigit、__MAX_DIGIT以上なら__MAX_DIGIT
        return np.sin(deg * mathematics.__MAX_DIGIT) if digit <= 0 else np.round(np.sin(deg * DEG_TO_RAD), digit if digit < mathematics.__MAX_DIGIT else mathematics.__MAX_DIGIT)

    @staticmethod
    def cos(deg: float, digit: int = 16) -> float:
        return np.cos(deg * mathematics.__MAX_DIGIT) if digit <= 0 else np.round(np.cos(deg * DEG_TO_RAD), digit if digit < mathematics.__MAX_DIGIT else mathematics.__MAX_DIGIT)

    @staticmethod
    def tan(deg: float, digit: int = 16) -> float:
        return np.tan(deg * mathematics.__MAX_DIGIT) if digit <= 0 else np.round(np.tan(deg * DEG_TO_RAD), digit if digit < mathematics.__MAX_DIGIT else mathematics.__MAX_DIGIT)


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
        line = '*----------*'
        print(line, prefix, line)
        r: Any = func(*args, **kwargs)
        sfx: str = ''
        for i in range(end := len(prefix) + 4 + 1 + len(line) * 2):
            sfx += '*' if i == 0 or i == end-1 else '-'
        print(sfx)
        return r
    return wrap


@prefix('ベクトル間の角度')
def angle():
    a = Vector2(1, 2)
    b = Vector2(3, 1)

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
    theta = np.arccos(cos8) * RAD_TO_DEG
    theta2 = np.arccos(cos82) * RAD_TO_DEG
    print('θ:', theta, '\nθ2:', theta2)  # cos45°


@prefix('極座標<->直交座標')
def polar():
    #! x=rcosθ, y=rsinθ
    a = Vector2(2, np. pi/3)
    ax = a.x * np.cos(a.y)
    ay = a.x * np.sin(a.y)
    print('a:', Vector2(ax, ay))  # (1, √3)

    b = Vector2(np.sqrt(2), np.pi/4)
    bx = b.x * np. cos(b.y)
    by = b.x * np.sin(b.y)
    print('b:', Vector2(bx, by))  # (1, 1)

    c = Vector2(4, 5/6*np.pi)
    cx = c.x * np.cos(c.y)
    cy = c.x * np.sin(c.y)
    print('c:', Vector2(cx, cy))  # (-2√3, 2)

    d = Vector2(3, np.pi)
    dx = d.x * np.cos(d.y)
    dy = d.x * np.sin(d.y)
    print('d:', Vector2(dx, dy))  # (-3, 0)


@prefix("tri")
def tri() -> None:
    # cosx=sin(90°-x)
    # sinx=cos(90°-x)
    # 1/tanx=tan(90°-x)

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
    # sin135°=√2/2
    print(mathematics.sin(135))
    # cos135°=-(√2/2)
    print(mathematics.cos(135))
    # tan135°=-1
    print(mathematics.tan(135))


@prefix('円周率の導出')
def pie():
    print(np.arccos(-1))
    print(1/(((2*np.sqrt(2))/9801)*sum([(math.factorial(4*k)*(1103+26390*k))/((math.factorial(k)**4)*(396**(4*k))) for k in range(0, 2**8)])))
    print(sum([(1/(16**k))*((4/(8*k+1))-(2/(8*k+4))-(1/(8*k+5))-(1/(8*k+6))) for k in range(0, 2**8)]))
    print((2**10)*np.sin(np.pi/(2**10)))
    print(4*(4*np.arctan(1/5)-np.arctan(1/239)))


if __name__ == '__main__':
    tri()
    angle()
    polar()
    pie()
