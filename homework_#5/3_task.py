"""
3. Создать текстовый файл (не программно),
построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
"""
from functools import reduce

file = open("3_task.txt", "r")
content = file.readlines()
average = 0
rich_staff = [el.split()[0] for el in content if int(el.split()[1]) > 20000]
all_money = reduce(lambda x, y: x + int(y.split()[1]), content, 0) / len(content)
print(rich_staff)
print(all_money)
file.close()
