import math
import numpy as np
from dataclasses import dataclass

MAX_DEPTH = 2**20
OFFSET = 0.0001


@dataclass
class Integral:
    function_type: int
    solution_type: int
    a: float
    b: float
    accuracy: float
    sign: int


function_types_arr = [
    'f(x) = -x^3 - x^2 + x + 3',
    'f(x) = x^3/(9 + 16x^4)',
    'f(x) = 2sin(x) + 6 - 3x^2',
    'f(x) = (3x + 1)^3',
    'f(x) = 1/x',
    'f(x) = (2 * x)/((9 - x**2)**0.5)'
]


def get_function_result(func_type: int, x0: float):
    try:
        if func_type == 0:
            return -x0**3 - x0**2 + x0 + 3
        elif func_type == 1:
            return x0**3 / (9 + 16 * x0**4)
        elif func_type == 2:
            return 2 * math.sin(x0) + 6 - 3 * x0**2
        elif func_type == 3:
            return (3 * x0 + 1)**3
        elif func_type == 4:
            return 1 / x0
        elif func_type == 5:
            return (2 * x0) / ((9 - x0**2)**0.5)
    except ZeroDivisionError or ValueError:
        return False


def get_function(func_type: int):
    if func_type == 0:
        return lambda x: -x**3 - x**2 + x + 3
    elif func_type == 1:
        return lambda x: x**3 / (9 + 16 * x**4)
    elif func_type == 2:
        return lambda x: 2 * np.sin(x) + 6 - 3 * x**2
    elif func_type == 3:
        return lambda x: (3 * x + 1)**3
    elif func_type == 4:
        return lambda x: 1 / x
    elif func_type == 5:
        return lambda x: (2 * x) / ((9 - x**2)**0.5)


def check_breakpoints(integral: Integral) -> [Integral]:
    if not get_function_result(integral.function_type, integral.a):
        integral.a += OFFSET
        return [integral]
    elif not get_function_result(integral.function_type, integral.b):
        integral.b -= OFFSET
        return [integral]
    arr = []
    h = (integral.b - integral.a) / MAX_DEPTH
    current_x = integral.a + h
    while current_x < integral.b:
        if not get_function_result(integral.function_type, current_x):
            arr.append(Integral(
                integral.function_type,
                integral.solution_type,
                integral.a,
                current_x - OFFSET,
                integral.accuracy,
                integral.sign)
            )
            arr.append(Integral(
                integral.function_type,
                integral.solution_type,
                current_x + OFFSET,
                integral.b,
                integral.accuracy,
                integral.sign)
            )
            return arr
        current_x += h
    return [integral]
