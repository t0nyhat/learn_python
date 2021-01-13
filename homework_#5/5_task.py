"""
5. Создать (программно) текстовый файл,
записать в него программно набор чисел,
разделенных пробелами. Программа должна
подсчитывать сумму чисел в файле и выводить ее на экран.

"""
from random import randint
from functools import reduce

numbers = [randint(50, 100) for el in range(10)]
with open('5_task.txt', 'w') as f:
    for n in numbers:
        f.write(str(n) + ' ')
with open('5_task.txt', 'r') as f:
    print(reduce(lambda x, y: x + int(y), f.read().split(), 0))
