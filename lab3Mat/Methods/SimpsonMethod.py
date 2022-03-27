from Model.Answer import Answer
from Model.Integral import Integral, get_function_result

MAX_DEPTH = 2**20


def calculate_integral(h: float, n: int, integral: Integral) -> float:
    sum_y_even = 0
    sum_y_odd = 0
    current_x = integral.a + h
    for i in range(1, n):
        current_y = get_function_result(integral.function_type, current_x)
        if i % 2 == 0:
            sum_y_even += current_y
        else:
            sum_y_odd += current_y
        current_x += h

    y_0 = get_function_result(integral.function_type, integral.a)
    y_n = get_function_result(integral.function_type, current_x)

    return (h / 3) * (y_0 + y_n + 4 * sum_y_odd + 2 * sum_y_even)


def solve_integral_simpson(integral: Integral) -> Answer:
    print('Метод Симпсона')
    print('-----------------')
    n = 4
    h = (integral.b - integral.a) / n
    integral_pred = calculate_integral(h, n, integral) * integral.sign

    n *= 2
    h = (integral.b - integral.a) / n
    integral_curr = calculate_integral(h, n, integral) * integral.sign
    print('integral_pred =', integral_pred, 'integral_curr =', integral_curr, 'n =', n)
    print('difference =', abs(integral_pred - integral_curr) / 15)

    while abs(integral_pred - integral_curr) / 15 > integral.accuracy and n <= MAX_DEPTH:
        integral_pred = integral_curr
        n *= 2
        h = (integral.b - integral.a) / n
        integral_curr = calculate_integral(h, n, integral) * integral.sign
        print('integral_pred =', integral_pred, 'integral_curr =', integral_curr, 'n =', n)
        print('difference =', abs(integral_pred - integral_curr) / 15)

    if n > MAX_DEPTH:
        return Answer(0, 0, True)
    return Answer(integral_curr, n, False)