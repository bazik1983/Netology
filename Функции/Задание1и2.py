documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def owner():
    """
    Функция возвращает по номеру документа данные о его владельце
    """
    ndoc = input("Номер документа:")
    for i in documents:
        if i['number'] == ndoc:
            return print(f"Владелец документа: {i['name']}")
    else:
        print('Документ не найден в базе')


def shelf():
    """
    Функция возвращает по номеру документа данные о месте хранения
    """
    ndoc = input("Номер документа:")
    for i in directories.items():
        if ndoc in i[1]:
            return print(f"Документ хранится на полке: {i[0]}")
    else:
        print('Документ не найден в базе')


def list_doc():
    """
    Функция возвращает список документов на полках
    """
    for i in documents:
        for item, values in directories.items():
            if i['number'] in values:
                print(f"№ {i['number']}, тип: {i['type']}, владелец: {i['name']}, полка хранения: {item}")


def add_shelf():
    """
    Функция добавляет полку, если такой ещё нет
    """
    shelf = input("Введите номер полки: ")
    for i in directories.items():
        if shelf in i[0]:
            print(f"Такая полка уже существует. Текущий перечень полок: {list(directories.keys())}")
            break
    else:
        directories[shelf] = []
        print(f"Полка добавлена. Текущий перечень полок: {list(directories.keys())}")


def del_shelf():
    """
    Функция удаляе полку, если она не пустая
    """
    shelf = input("Введите номер полки: ")
    if shelf not in directories.keys():
        print(f"Такой полки не существует. Текущий перечень полок:' {list(directories.keys())}")
    elif directories.keys():
        print(
            f"На полке есть документы, удалите их перед удалением полки. Текущий перечень полок:' {list(directories.keys())}")
    else:
        del directories[0]
        print(f"Полка удалена. Текущий перечень полок:' {list(directories.keys())}")


def main():
    """
    Основная функция автоматизации работы секретаря
    """
    a = 0
    while a < 1:
        command_input = input('Введите команду: \n')
        if command_input == 'p':
            owner()
        elif command_input == 's':
            shelf()
        elif command_input == 'l':
            list_doc()
        elif command_input == 'as':
            number_input = input('Введите номер полки: \n')
            add_shelf()
        elif command_input == 'ds':
            del_shelf()
        elif command_input == 'q':
            break
        else:
            print('Нет такой команды')


main()
