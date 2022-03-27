from Model.Answer import Answer
from Model.Integral import Integral, get_function_result

MAX_DEPTH = 2**20


def calculate_integral(h: float, n: int, start: float, integral: Integral):
    sum_y = 0
    current_x = start
    for i in range(n):
        current_y = get_function_result(integral.function_type, current_x)
        sum_y += current_y
        current_x += h

    return h * sum_y


def solve_integral_rectangles(integral: Integral) -> Answer:
    print('Метод прямоугольников')
    print('-----------------------')
    if integral.solution_type % 10 == 0:
        return solve_integral_rectangles_left(integral)
    elif integral.solution_type % 10 == 1:
        return solve_integral_rectangles_middle(integral)
    else:
        return solve_integral_rectangles_right(integral)


def solve_integral_rectangles_left(integral: Integral) -> Answer:
    n = 4
    h = (integral.b - integral.a) / n
    integral_pred = calculate_integral(h, n, integral.a, integral) * integral.sign

    n *= 2
    h = (integral.b - integral.a) / n
    integral_curr = calculate_integral(h, n, integral.a, integral) * integral.sign
    print('integral_pred =', integral_pred, 'integral_curr =', integral_curr, 'n =', n)
    print('difference =', abs(integral_pred - integral_curr))

    while abs(integral_curr - integral_pred) > integral.accuracy and n <= MAX_DEPTH:
        integral_pred = integral_curr
        n *= 2
        h = (integral.b - integral.a) / n
        integral_curr = calculate_integral(h, n, integral.a, integral) * integral.sign
        print('integral_pred =', integral_pred, 'integral_curr =', integral_curr, 'n =', n)
        print('difference =', abs(integral_pred - integral_curr))

    if n > MAX_DEPTH:
        return Answer(0, 0, True)
    return Answer(integral_curr, n, False)


def solve_integral_rectangles_middle(integral: Integral) -> Answer:
    n = 4
    h = (integral.b - integral.a) / n
    integral_pred = calculate_integral(h, n, integral.a + (h / 2), integral) * integral.sign

    n *= 2
    h = (integral.b - integral.a) / n
    integral_curr = calculate_integral(h, n, integral.a + (h / 2), integral) * integral.sign
    print('integral_pred =', integral_pred, 'integral_curr =', integral_curr, 'n =', n)
    print('difference =', abs(integral_pred - integral_curr) / 3)

    while abs(integral_pred - integral_curr) / 3 > integral.accuracy and n <= MAX_DEPTH:
        integral_pred = integral_curr
        n *= 2
        h = (integral.b - integral.a) / n
        integral_curr = calculate_integral(h, n, integral.a + (h / 2), integral) * integral.sign
        print('integral_pred =', integral_pred, 'integral_curr =', integral_curr, 'n =', n)
        print('difference =', abs(integral_pred - integral_curr) / 3)

    if n > MAX_DEPTH:
        return Answer(0, 0, True)
    return Answer(integral_curr, n, False)


def solve_integral_rectangles_right(integral: Integral) -> Answer:
    n = 4
    h = (integral.b - integral.a) / n
    integral_pred = calculate_integral(h, n, integral.a + h, integral) * integral.sign

    n *= 2
    h = (integral.b - integral.a) / n
    integral_curr = calculate_integral(h, n, integral.a + h, integral) * integral.sign
    print('integral_pred =', integral_pred, 'integral_curr =', integral_curr, 'n =', n)
    print('difference =', abs(integral_pred - integral_curr))

    while abs(integral_curr - integral_pred) > integral.accuracy and n <= MAX_DEPTH:
        integral_pred = integral_curr
        n *= 2
        h = (integral.b - integral.a) / n
        integral_curr = calculate_integral(h, n, integral.a + h, integral) * integral.sign
        print('integral_pred =', integral_pred, 'integral_curr =', integral_curr, 'n =', n)
        print('difference =', abs(integral_pred - integral_curr))

    if n > MAX_DEPTH:
        return Answer(0, 0, True)
    return Answer(integral_curr, n, False)
