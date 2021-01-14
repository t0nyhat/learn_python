"""
1. Создать программно файл в текстовом формате, записать в него построчно данные,
 вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
"""
all_text = ''
print('Пишите текст, для записи в файл дважды нажмите enter')
while True:
    input_string = input()
    all_text += input_string + '\r\n'
    if len(input_string) == 0:
        break

out_f = open("1_task.txt", "w")
out_f.write(all_text)
out_f.close()
