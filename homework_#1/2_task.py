"""
2. Пользователь вводит время в секундах. Переведите время в часы,
 минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
"""
total_seconds = int(input('Введите количество секунд'))
hours = total_seconds // 3600
min = (total_seconds - hours * 3600) // 60
seconds = total_seconds - hours * 3600 - min * 60
print(f'{hours:02d}:{min:02d}:{seconds:02d}')
