# 7: Написать функцию, которая принимает в качестве аргумента число и возвращает True, если это число делиться без остатка только на себя и на единицу и False, если нет.

import math

def task_7 (n):
    if (math.factorial(n - 1) + 1) % n != 0:
        return False
    else:
        return True

print(task_7(7))
