"""
Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов
(не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
Выполнить подсчёт средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""
with open('task_5_3.txt', encoding='utf-8') as f:
    content_line = f.readlines()
    SALARY = 20000
    salary = '\n'.join([i.strip() for i in content_line if float(i.split()[1]) < SALARY])
    average_salary = [float(i.split()[1]) for i in content_line]
    print(f'Сотрудники с окладом меньше {SALARY} руб.\n{salary}')
    print()
    print(f'Средняя зарплата {sum(average_salary) / len(average_salary)}')


