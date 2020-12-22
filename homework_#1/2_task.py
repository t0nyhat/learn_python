"""
2. Пользователь вводит время в секундах. Переведите время в часы,
 минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
"""
totalSeconds = int(input('Введите количество секунд'))
hours = totalSeconds//3600
min = (totalSeconds - hours*3600)//60
seconds = totalSeconds - hours*3600 - min*60
print(f'{hours:02d}:{min:02d}:{seconds:02d}')

