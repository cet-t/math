import matplotlib.pyplot as plt
import numpy as np
import dataclasses


@dataclasses.dataclass
class PltSet:
    title: str
    x_label: str
    y_label: str

    def draw(self, t, P) -> None:
        plt.title(self.title)
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        plt.grid(True)
        plt.plot(t, P)
        plt.show()


if __name__ == '__main__':
    # イージングをグラフ化

    t: np.ndarray = np.linspace(-10, 10, 100)

    # 直線
    straight = PltSet(title='P(t)=t', x_label='t', y_label='P(t)')
    straight.draw(t, t)

    # +放物線
    parabora_plus = PltSet(title='P(t)=t^2', x_label='t', y_label='P(t)')
    parabora_plus.draw(t, t**2)

    # -放物線
    parabora_minus = PltSet(title='P(t)=-t^2+2t', x_label='t', y_label='P(t)')
    parabora_minus.draw(t, -t**2+2*t)

    # ±放物線
    parabora_plus_minus = PltSet(
        title='P(t)=-2t^3+3t^2', x_label='t', y_label='P(t)')
    parabora_plus_minus.draw(t, -2*t**3+3*t**2)
