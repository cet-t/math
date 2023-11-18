import dataclasses
import numpy as np


@dataclasses.dataclass
class V:
    x: float
    y: float


def deco_s_deco(func):
    '''https://qiita.com/nshinya/items/b6746a0c07e9e20389e8'''
    def param(*args, **kwargs):
        def wrap(f):
            return func(f, *args, **kwargs)
        return wrap
    return param


@deco_s_deco
def prefix(func, prefix: str):
    def wrap(*args, **kwargs):
        line = '*---*'
        print(line, prefix, line)
        r = func(*args, **kwargs)
        sfx: str = ''
        for i in range(end := len(prefix) + 2 + len(line) * 2):
            sfx += '*' if i == 0 or i == end-1 else '-'
        print(sfx)
        return r
    return wrap


@prefix('angle')
def angle():
    # \a･\b / |\a||\b|
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
    deg = np.arccos(cos_theta) * (180 / np.pi)
    print('deg:', deg)

    # print(np.cos(deg))


if __name__ == '__main__':
    angle()
