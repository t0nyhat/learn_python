"""
Выполнить функцию, которая принимает несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать
параметры как именованные аргументы. Осуществить вывод данных
о пользователе одной строкой.
"""


def stringify(first_name, last_name, birth_year, live_city, email, phone):
    """Возвращает введенные аргументы в виде строки"""
    return f'Имя: {first_name}, Фамилия: {last_name}, Год рождения: {birth_year}, ' \
           f'Город проживания: {live_city}, Email: {email}, Телефон: {phone}.'


string_result = stringify(phone=8999999999, email='one@one.com', live_city='Москва',
                          birth_year=2021, last_name='Иванов', first_name='Петр')
print(string_result)
