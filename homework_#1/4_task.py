"""
4. Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе. Для решения
используйте цикл while и арифметические операции.
"""
num = int(input('Введите число'))
maximum = 0

while num > 0:
    if num % 10 > maximum:
        maximum = num % 10
        if maximum == 9:
            break
    num = num // 10

print(maximum)
