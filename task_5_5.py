"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами. Программа должна
подсчитывать сумму чисел в файле и выводить её на экран.
"""
import random
with open('task_5_5.txt', 'w', encoding='utf-8') as f:
    num_list = [random.randint(0, 100) for _ in range(10)]
    print(' '.join(map(str, num_list)), file=f)
    print(f'Сумма всех чисел: {sum(num_list)}')
