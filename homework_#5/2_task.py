"""
2. Создать текстовый файл (не программно),
сохранить в нем несколько строк,
выполнить подсчет количества строк,
количества слов в каждой строке.
"""
file = open("2_task.txt", "r")
content = file.readlines()
lines_count = len(content)
print(f'количество строк - {lines_count}')
for line in content:
    line=line.replace('\n','')
    words_count = len(line.split())
    print(f'В строке "{line}" - {words_count} слов')
file.close()
