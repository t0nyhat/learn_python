"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
 Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
  Напишите решения через list и через dict.

"""
import math
month_number = int(input('Введите номер месяца'))
month_number = 0 if month_number == 12 else month_number
season_string = 'зима весна лето осень'
seasons = list(season_string.split(' '))
seasons_dic = {0: seasons[0], 1: seasons[1], 2: seasons[2], 3: seasons[3]}

print(f'Время года - {seasons_dic[math.floor(month_number / 3)]}')
print(f'Время года - {seasons[math.floor(month_number / 3)]}')
