import os
from pprint import pprint


def strings_counting(file: str) -> int:
    with open("../cook_book.txt", 'r', encoding='utf-8') as f:
        return sum(1 for _ in f)


def catalog_reader(file_name: str) -> dict:
    with open("../cook_book.txt", 'r', encoding='utf-8') as file:
        dict = {}
        for line in file:
            dish_name = line.strip()
            dict[dish_name] = []
            for j in range(int(file.readline())):
                consist = file.readline().split(' | ')
                dict[dish_name].append({'ingredient_name': consist[0],
                                        'quantity': int(consist[1]),
                                        'measure': consist[2].strip()})
            # file.readline()
    return dict
# pprint(catalog_reader("../cook_book.txt"))

def shop_list_by_dishes(dishes: list, person_count: int, cook_book: dict) -> dict:
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for consist in cook_book[dish]:
                if consist['ingredient_name'] in result:
                    result[consist['ingredient_name']]['quantity'] += consist['quantity'] * person_count
                else:
                    result[consist['ingredient_name']] = {'measure': consist['measure'],
                                                          'quantity': (consist['quantity'] * person_count)}
        else:
            print(f'Блюда "{dish}" нет в книге рецептов')
    return result

if __name__ == '__main__':
    dishes = ['Омлет', 'Фахитос', 'Селедь под шубой', 'Запеченный картофель', 'Утка по-пекински']
pprint(shop_list_by_dishes(dishes, 3, catalog_reader("../cook_book.txt")))
# print(shop_list_by_dishes('Фахитос', "Омлет", 2))