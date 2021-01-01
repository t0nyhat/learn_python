"""
Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
"""


def int_func(word):
    return str(word)[0].upper() + str(word)[1:]


def line_func(line):
    out_words = []
    for word in line.split(' '):
        out_words.append(int_func(word))
    return ' '.join(out_words)


input_text = input('Введите слово или строку их слов, разделенных пробелом: ')
print(line_func(input_text))
