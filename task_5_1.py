"""
Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании
ввода данных будет свидетельствовать пустая строка.
"""
with open('task_5_1.txt', 'w+', encoding='utf-8') as f:
    text = input('Введите текст: ')
    while text:
        print(text, file=f)
        text = input('Введите текст: ')
        if not text:
            break
    f.seek(0)
    content = f.read()
    print(content)
