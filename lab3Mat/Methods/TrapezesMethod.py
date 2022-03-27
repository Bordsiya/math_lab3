from Model.Answer import Answer
from Model.Integral import Integral, get_function_result

MAX_DEPTH = 2**20


def calculate_integral(h: float, n: int, integral: Integral) -> float:
    y_sum = 0
    x_curr = integral.a + h
    for i in range(1, n):
        y_curr = get_function_result(integral.function_type, x_curr)
        y_sum += y_curr
        x_curr += h

    y_0 = get_function_result(integral.function_type, integral.a)
    y_n = get_function_result(integral.function_type, x_curr)

    return h * (((y_0 + y_n) / 2) + y_sum)


def solve_integral_trapezes(integral: Integral) -> Answer:
    print('Метод трапеций:')
    print('-----------------')
    n = 4
    h = (integral.b - integral.a) / n
    integral_pred = calculate_integral(h, n, integral) * integral.sign

    n *= 2
    h = (integral.b - integral.a) / n
    integral_curr = calculate_integral(h, n, integral) * integral.sign
    print('integral_pred =', integral_pred, 'integral_curr =', integral_curr, 'n =', n)
    print('difference =', abs(integral_pred - integral_curr) / 3)

    while abs(integral_pred - integral_curr) / 3 > integral.accuracy and n <= MAX_DEPTH:
        integral_pred = integral_curr
        n *= 2
        h = (integral.b - integral.a) / n
        integral_curr = calculate_integral(h, n, integral) * integral.sign
        print('integral_pred =', integral_pred, 'integral_curr =', integral_curr, 'n =', n)
        print('difference =', abs(integral_pred - integral_curr) / 3)

    if n > MAX_DEPTH:
        return Answer(0, 0, True)
    return Answer(integral_curr, n, False)