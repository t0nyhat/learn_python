"""
4. Создать (не программно) текстовый файл со следующим содержимым:

One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу,
открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

file = open("4_task.txt", "r")
out_f = open("4_task_out.txt", "w")
content = file.readlines()
d = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_content = [el.replace(el.split()[0], d[el.split()[0]]) for el in content]
out_f.writelines(new_content)
out_f.close()
file.close()
