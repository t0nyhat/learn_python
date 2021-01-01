"""
Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.
"""


def div(first_num, second_num):
    """Возвращает результат делениия"""
    return first_num / second_num if second_num != 0 else 'На ноль делить нельзя'


input_numbers = input('Введите 2 числа через пробел: ').split(' ')
div_result = div(int(input_numbers[0]), int(input_numbers[1]))
print(div_result)
