"""
Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает. У пользователя
нужно запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то новый
элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать сразу в коде, например, my_list = [7, 5, 3, 3, 2].
"""
my_list = [7, 5, 3, 3, 2]
num = int(input("Введите число: "))
for el in range(len(my_list)):
    if my_list[0] < num:
        my_list.insert(0, num)
        break
    elif my_list[-1] >= num:
        my_list.append(num)
        break
    elif my_list[el] >= num > my_list[el + 1]:
        my_list.insert(el + 1, num)
        break

print(f"Новый список рейтинга - {my_list}")