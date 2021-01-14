"""
6. Необходимо создать (не программно) текстовый файл,
где каждая строка описывает учебный предмет и наличие
лекционных, практических и лабораторных занятий по этому
предмету и их количество. Важно, чтобы для каждого предмета
не обязательно были все типы занятий. Сформировать словарь,
содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.

Примеры строк файла:

Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря:

{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

from random import randint
from functools import reduce

d = {}
with open('6_task.txt', 'r') as f:
    for line in f.readlines():
        subject = line.split()[0]
        counts = line.split(subject)[1].replace('—', '').split()
        all_count = reduce(lambda x, y: x + int(y.split('(')[0]), counts, 0)
        d[subject.replace(':', '')] = all_count
print(d)
