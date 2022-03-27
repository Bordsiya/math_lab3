from Model.Integral import function_types_arr, Integral
from Utils.Exceptions import exceptions_arr
from Utils.GraphMethods import draw_graph_integral

solution_types_arr = [
    'Метод трапеций',
    'Метод Симпсона',
    'Метод прямоугольников'
]


method_rectangles_types_arr = [
    'Метод левых прямоугольников',
    'Метод средних прямоугольников',
    'Метод правых прямоугольников'
]


def read_integral() -> Integral:
    function_type = read_function()
    draw_graph_integral(function_type)
    solution_type = read_solution_type()
    limits = read_limits()
    accuracy = read_accuracy()
    if limits[0] > limits[1]:
        limits[0], limits[1] = limits[1], limits[0]
        sign = -1
    else:
        sign = 1
    integral = Integral(function_type, solution_type, limits[0], limits[1], accuracy, sign)

    return integral


def read_function() -> int:
    print('Представлены следующие функции:')
    for i in range(len(function_types_arr)):
        print(i, ': ', function_types_arr[i])

    inp = input('Введите номер функции: ').strip()

    try:
        inp = int(inp)
        if 0 <= inp < len(function_types_arr):
            return inp
        else:
            print('Ошибка: ', exceptions_arr['WrongLimitsArgument'])
            exit(1)
    except ValueError:
        print('Ошибка: ', exceptions_arr['ValueError'])
        exit(1)


def specify_rectangle_method() -> int:
    print('Представлены следующие модификации метода:')
    for i in range(len(method_rectangles_types_arr)):
        print(i, ': ', method_rectangles_types_arr[i])

    inp = input('Введите номер метода: ').strip()

    try:
        inp = int(inp)
        if 0 <= inp < len(function_types_arr):
            return inp
        else:
            print('Ошибка: ', exceptions_arr['WrongLimitsArgument'])
            exit(1)
    except ValueError:
        print('Ошибка: ', exceptions_arr['ValueError'])
        exit(1)


def read_solution_type() -> int:
    print('Представлены следующие методы решения:')
    for i in range(len(solution_types_arr)):
        print(i, ': ', solution_types_arr[i])

    inp = input('Введите номер метода: ').strip()

    try:
        inp = int(inp)
        if 0 <= inp < len(function_types_arr):
            if inp == 2:
                inp = inp * 10 + specify_rectangle_method()
            return inp
        else:
            print('Ошибка: ', exceptions_arr['WrongLimitsArgument'])
            exit(1)
    except ValueError:
        print('Ошибка: ', exceptions_arr['ValueError'])
        exit(1)


def read_limits() -> [float, float]:
    try:
        inp = input('Введите пределы интегрирования (пример: 0 3): ').strip()
        interval = list(inp.split(" "))
        if len(interval) > 2:
            print('Ошибка: ', exceptions_arr['TooMuchLimits'])
            exit(1)
        a = float(interval[0].replace(',', '.'))
        b = float(interval[1].replace(',', '.'))
        return [a, b]
    except ValueError or IndexError:
        print('Ошибка: ', exceptions_arr['ValueError'])
        exit(1)


def read_accuracy() -> float:
    try:
        inp = input('Введите погрешность вычисления: ').strip()
        accuracy = float(inp.replace(',', '.'))
        if accuracy < 0:
            print('Ошибка: ', exceptions_arr['NegativeAccuracy'])
            exit(1)
        return accuracy
    except ValueError:
        print('Ошибка: ', exceptions_arr['ValueError'])
        exit(1)

