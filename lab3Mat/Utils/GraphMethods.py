import matplotlib.pyplot as plt
import numpy as np
from Model.Integral import get_function


def get_linspace_equation(func_type: int):
    if func_type == 0:
        return np.linspace(-3, 3, 300)
    elif func_type == 1:
        return np.linspace(-4, 4, 300)
    elif func_type == 2 or func_type == 3:
        return np.linspace(-3, 3, 300)
    elif func_type == 4:
        return np.concatenate([np.linspace(-2, -0.01, 100), np.linspace(0.01, 5, 100)])
    elif func_type == 5:
        return np.linspace(-2.9, 2.9, 300)


def draw_graph_integral(function_type: int):
    plt.gcf().canvas.set_window_title("График функции")
    plt.grid()
    axes = plt.gca()

    axes.spines['right'].set_color('none')
    axes.spines['top'].set_color('none')
    axes.spines['left'].set_position('zero')
    axes.spines['bottom'].set_position('zero')
    axes.set_xlabel('x', loc='right')
    axes.set_ylabel('y', loc='top')
    axes.plot(1, 0, marker=">", ms=5, color='k', transform=axes.get_yaxis_transform(), clip_on=False)
    axes.plot(0, 1, marker="^", ms=5, color='k', transform=axes.get_xaxis_transform(), clip_on=False)

    X = get_linspace_equation(function_type)
    F = get_function(function_type)

    plt.xticks(np.arange(min(X), max(X) + 1, 1.0))
    axes.plot(X, F(X))

    plt.savefig('graph')
