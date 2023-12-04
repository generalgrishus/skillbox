import random
import os
os.chdir('D:/УрфуМомент/Python/skillboxs-tasks/module10/task2')

with open('out_file.txt', 'w') as file:
    total = 0
    while total < 777:
        if random.randint(1, 13) == 1:
            raise Exception("Ошибка")
        try:
            number = int(input("Введите число: "))
            file.write(str(number) + '\n')
            total += number
        except ValueError:
            print("Введено некорректное число. Попробуйте еще раз.")

print("Вы успешно выполнили условие для выхода из порочного цикла!")