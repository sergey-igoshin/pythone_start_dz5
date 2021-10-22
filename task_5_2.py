"""
Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.
"""
with open('task_5_2.txt', encoding='utf-8') as f:
    content = f.read()
    f.seek(0)
    content_line = f.readlines()

    print('*' * 5, 'Содержимое файла', '*' * 5, '\n', content)
    for key, val in enumerate(content_line, 1):
        print(f'Строка {key}: {len(val.split())} слов, {len(val)} символов')
    print(f'Всего: строк {len(content_line)}, слов {len(content.split())}, символов {len(content)} ')
