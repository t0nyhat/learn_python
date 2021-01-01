"""
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти чётные числа от 100 до 1000 (включая границы).
Нужно получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().

"""
from random import randint
from functools import reduce


def multiply(prev_el, el):
    """Возвращает результат умножения двух аргументов"""
    return prev_el * el


list = [el for el in range(100, 1001) if el % 2 == 0]
print(reduce(multiply, list))
