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
    for shelf in directories:
        for num in directories[shelf]:
            found = next(e for e in documents if e['number'] == num)
            print(f'№: {num}, тип:{found["type"]}, владелец:{found["name"]}, полка хранения: {shelf}')


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
    Функция удаляет полку, если она не пустая
    """
    shelf = input("Введите номер полки: ")
    if shelf in directories:
        if directories[shelf]:
            return print(f"На полке есть документы, удалите их перед удалением полки. Текущий перечень полок: {list(directories.keys())}")
        del directories[shelf]
        return print(f"Полка удалена. Текущий перечень полок: {list(directories.keys())}")
    return print(f"Такой полки не существует. Текущий перечень полок: {list(directories.keys())}")


def add_doc():
    """
    Функция добавляет документ
    """
    doc_type = input("Введите тип документа: ")
    doc_number = input("Введите номер документа: ")
    doc_owner = input("Введите имя владельца документа: ")
    shelf = input("Введите номер полки: ")
    if shelf not in directories:
        print(f"Такой полки не существует. Добавьте полку командой ads.\nТекущий список документов:")
        return list_doc()
    else:
        new_doc = dict(type = doc_type, number = doc_number, name = doc_owner)
        documents.append(new_doc)
        directories[shelf] += [doc_number]
        print(f"Документ добавлен. Текущий список документов:")
        return list_doc()

def del_doc():
    doc_number = input("Введите номер документа, который хотите удалить: ")
    initial_len = len(documents)
    for i, d in enumerate(documents):
        if d["number"] == doc_number:
            documents.pop(i)
    if initial_len == len(documents):
        print(f"Документ не найден в базе. Добавьте полку командой ads.\nТекущий список документов:")
        return list_doc()
    for key, value in directories.items():
        if doc_number in value:
            value.remove(doc_number)
        print(f"Документ удален. Добавьте полку командой ads.\nТекущий список документов:")
        return list_doc()


def move_doc():
    doc_number = input("Введите номер документа,который хоитите переместить: ")
    shelf = input("Введит номер полки, на которую хоиите перемести документ: ")
    doc_existence = False

    if shelf not in directories:
        return print(f"Полки не существует. Текущий перечень полок: {list(directories.keys())}")

    for key, value in directories.items():
        if doc_number in value:
            doc_existence = True
            directories[shelf] += [doc_number]
            value.remove(doc_number)

    if doc_existence == True:
        print(f"Документ перемещен.\nТекущий список документов:")
        return list_doc()
    else:
        print(f"Документ не найден в базе.\nТекущий список документов:")
        return list_doc()

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
        elif command_input == 'ads':
            add_shelf()
        elif command_input == 'ds':
            del_shelf()
        elif command_input == 'ad':
            add_doc()
        elif command_input == 'd':
            del_doc()
        elif command_input == 'm':
            move_doc()
        elif command_input == 'q':
            break
        else:
            print('Нет такой команды')


main()
