# Задача 3. Контроль

def checker(txt):
    flag = True
    for i in txt:
        if i not in '123456789':
            flag = False
            break
    return flag


def finder(id_st, ids_workers):
    if id_st in ids_workers:
        return 'Сотрудник на месте.'
    else:
        return 'Сотрудник не работает!'


workers_id = []

while True:
    workers = input("Введите количество сотрудников в офисе: ")
    if checker(workers):
        workers = int(workers)
        break
    else:
        print("Ошибка в количестве сотрудников. Необходимо вводить только цифры...")

while workers:
    while True:
        id_stuff = input("ID сотрудника: ")
        if checker(id_stuff):
            workers_id.append(int(id_stuff))
            break
        else:
            print("Ошибка в ID. Необходимо вводить только цифры...")
    workers -= 1

while True:
    search = input("Какой ID ищем? ")
    if checker(search):
        search = int(search)
        break
    else:
        print("Ошибка в ID. Необходимо вводить только цифры...")

print(finder(search, workers_id))
