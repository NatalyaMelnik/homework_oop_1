from typing import List, Dict

documents: list[dict[str, str] | dict[str, str] | dict[str, str]] = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def whose_document():
    number_document = input("Введите номер документа: ")
    for dct in documents:
        if number_document in dct["number"]:
            return f'Такой номер документа принадлежит {dct["name"]}'
    return f'Такого номера документа нет'


whose_document()


def number_shelf():
    number_document = input("Введите номер документа: ")
    for shelf in directories:
        if number_document in directories[shelf]:
            return f'Номер полки {shelf}'
    return f'Вы неправильно ввели номер документа'


# print(number_shelf())


def document_numberdoc_fullname():
    list_of_all_documents: str = ''
    for dct in documents:
        list_of_all_documents += f'\n{dct["type"]} {dct["number"]} {dct["name"]}'
    return list_of_all_documents


# print(document_numberdoc_fullname())

def new_document():
    shelf = input('Введите номер полки на которую надо положить новый документ: ')
    if shelf not in directories:
        return ('Несуществующая полка')

    else:
        type = input('Введите новый тип документа: ')
        number = input('Введите новый номер документа: ')
        fullname = input('Введите новое имя владельца документа: ')
        add_dict = {"type": type, "number": number, "name": fullname}
        documents.append(add_dict)
        directories[shelf].append(number)
        return 'Документ добавлен'





        print(documents)
        print(directories)

print(new_document())


def del_document():
    number_doc = input("Введите номер документа: ")
    for index in range(len(documents)):
        dct = documents[index]
        if number_doc == dct["number"]:
            del documents[index]
            break
    else:
        print(f'Такого {number_doc} документа нет')

    for dct in directories:
        if number_doc in directories[dct]:
            directories[dct].remove(number_doc)


def move():
    number_doc = input("Введите номер документа: ")
    old_shelf = None
    for dct in directories:
        if number_doc in directories[dct]:
            old_shelf = dct
    if old_shelf is None:
        print('Несуществующий документ')
        return
    new_shelf = input("Введите номер полки: ")
    if new_shelf not in directories:
        print('Несуществующая полка')
        return
    directories[old_shelf].remove(number_doc)
    directories[new_shelf].append(number_doc)

print(move())
print(documents)
print(directories)

def add_shelf():
    number_new_shelf = input("Введите номер полки: ")
    #for shelf in directories:
    if number_new_shelf in directories:
        return 'Такой номер полки уже есть'



    else:
        directories.update({number_new_shelf: []})
        return 'Новая полка добавлена'

print(add_shelf())
print(directories)

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def main():
    while True:
        '''p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
    s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
    l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
    a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться. 
    d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок. 
    m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую. 
    as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень. '''

        print("Возможные команды: p, s, l, a, d, m, as")

        comand = input('Введите название команды: ')
        if comand == 'p':
            print(whose_document())
        elif comand == 's':
            print(number_shelf())
        elif comand == 'l':
            print(document_numberdoc_fullname())
        elif comand == 'a':
            print(new_document())
        elif comand == 'd':
            print(del_document())
        elif comand == 'm':
            print(move())
        elif comand == 'as':
            print(add_shelf())
            break

print(main())



#
# def add_shelf():
#     number_new_shelf = input("Введите номер полки: ")
#     for shelf in directories:
#         if number_new_shelf in directories[shelf]:
#             print('Такой номер полки уже есть')
#
#         else:
#             directories.update({number_new_shelf: []})
#             return
#
# print(add_shelf())
# print(directories)
