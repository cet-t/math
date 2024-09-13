from dataclasses import dataclass
import numpy as np


RAD_TO_DEG: float = 180 / np.pi
DEG_TO_RAD: float = np.pi / 180


@dataclass
class Vector2:
    x: float
    y: float

    def __str__(self) -> str:
        return f'({self.x},{self.y})'

    @property
    def magnitude(self) -> float:
        return np.sqrt(self.x ** 2 + self.y ** 2)

    @property
    def normalized(self) -> 'Vector2':
        mag = self.magnitude
        return Vector2(self.x / mag, self.y / mag)

    @staticmethod
    def dot(a: 'Vector2', b: 'Vector2') -> float:
        return a.x * b.x + a.y * b.y

    @staticmethod
    def angle(a: 'Vector2', b: 'Vector2') -> float:
        # cosθ = \a･\b / |\a||\b|
        lal: float = a.magnitude
        lbl: float = b.magnitude
        dot: float = Vector2.dot(a, b)
        cos: float = np.arccos(dot / lal / lbl)
        return cos * RAD_TO_DEG

    @staticmethod
    def polar_to_rectangular(a: 'Vector2') -> 'Vector2':
        return Vector2(a.x * np. cos(a.y), a.x * np. sin(a.y))

    def __pos__(self) -> 'Vector2':
        return self

    def __neg__(self) -> 'Vector2':
        return Vector2(-self.x, -self.y)

    def __add__(self, a: 'Vector2') -> 'Vector2':
        return Vector2(self.x + a.x, self.y + a.y)

    def __sub__(self, a: 'Vector2') -> 'Vector2':
        return Vector2(self.x - a.x, self.y + a.y)

    def __mul__(self, a: 'Vector2') -> 'Vector2':
        return Vector2(self.x * a.x, self.y * a.y)

    def __truediv__(self, a: 'Vector2') -> 'Vector2':
        return Vector2(self.x / a.x, self.y / a.y)

    def __floordiv__(self, a: 'Vector2') -> 'Vector2':
        return Vector2(self.x // a.x, self.y // a.y)
