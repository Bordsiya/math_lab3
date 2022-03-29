from Methods.RectanglesMethod import solve_integral_rectangles
from Methods.SimpsonMethod import solve_integral_simpson
from Methods.TrapezesMethod import solve_integral_trapezes
from Model.Integral import check_breakpoints, get_certain_integral
from Utils.IOMethods import read_integral
import numpy as np

integral = read_integral()
#print(integral)

arr_integral = check_breakpoints(integral)

ans_sum = 0
n_sum = 0
for i in arr_integral:
    #print('//', i)
    if i.solution_type == 0:
        answer = solve_integral_trapezes(i)
    elif i.solution_type == 1:
        answer = solve_integral_simpson(i)
    else:
        answer = solve_integral_rectangles(i)
    #print(answer)
    if answer.is_diverge:
        print('Интеграл расходится')
        exit(0)
    ans_sum += answer.answer
    n_sum += answer.n

print('-------------------------------')
print('Значение интеграла = ', ans_sum)
print('Число разбиений интервала = ', n_sum)





#print(get_certain_integral(integral.function_type, integral.a, integral.b))

