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


def document_owner():
    num_doc = input('\nВведите номер документа: ')

    for dicts in documents:
        if num_doc in dicts["number"]:
            return f'n\Документ пернадлежит: {dicts["name"]}'
    else:
        return f'\nВведен неверный номер документа.'


#print(document_owner())


def number_of_shelf():
    num_doc = input('Введите номер документа: ')
    for shelf in directories:
        if num_doc in directories[shelf]:
            return print(shelf)
    else:
        return f'\nВведен неверный номер документа.'


def list_of_documents():
    list_docs = ''
    for dicts in documents:
        list_docs += f'\n{dicts["type"]} {dicts["number"]} {dicts["name"]}'
    return list_docs
#print(list_of_documents())

def delete_documents():
    num_doc = input('\nВведите номер документа: ')
    i = 0
    for dicts in documents:
        if num_doc in dicts["number"]:
            del documents[i]
        else:
            i += 1
    if i == len(documents):
        return f'\nВведен неверный номер документа.'

print(delete_documents())