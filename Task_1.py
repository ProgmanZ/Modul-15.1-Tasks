# Задача 1. Таблица степеней

numbers = [3, 7, 5]

while True:
    number = int(input('Новое число: '))
    numbers.append(number)
    print('Текущий список чисел:', numbers)

    for i in numbers:
        print(int(i) ** 2, int(i) ** 3, int(i) ** 4)
    print()
