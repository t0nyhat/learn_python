"""
5. Запросите у пользователя значения выручки и издержек фирмы. Определите,
с каким финансовым результатом работает фирма (прибыль — выручка больше
издержек, или убыток — издержки больше выручки). Выведите соответствующее
сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки
(соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и
определите прибыль фирмы в расчете на одного сотрудника
"""
gain = int(input('Введите выручку'))
charge = int(input('Введите издержки'))
if gain > charge:
    print(f'Вы работате в прибыль. Рентабельность {(gain - charge) / gain}')
    emp = int(input('Введите количество сотрудников'))
    print(f'Прибыль на каждого сотрудника {(gain - charge) / emp}')
elif (gain - charge) == 0:
    print('Нет прибыли, вы работаете в ноль')
else:
    print('Вы работате в убыток')
