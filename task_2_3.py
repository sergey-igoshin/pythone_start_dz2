"""
Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года относится месяц
(зима, весна, лето, осень). Напишите решения через list и dict.
"""
seasons_list = ['зима', 'весна', 'лето', 'осень']
seasons_dict = {0: 'зима', 1: 'весна', 2: 'лето', 3: 'осень'}
month = int(input("Введите месяц в виде целого числа от 1 до 12: "))
if 1 <= month <= 2 or month == 12:
    print(seasons_dict.get(0))
    print(seasons_list[0])
elif 3 <= month <= 5:
    print(seasons_dict.get(1))
    print(seasons_list[1])
elif 6 <= month <= 8:
    print(seasons_dict.get(2))
    print(seasons_list[2])
elif 9 <= month <= 11:
    print(seasons_dict.get(3))
    print(seasons_list[3])
else:
    print("Такого месяца не существует")
