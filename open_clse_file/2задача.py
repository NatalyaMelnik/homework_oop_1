from pprint import pprint

def cook_book_read(file_name):
    with open("../cook_book.txt", 'r', encoding='utf-8') as file_obj:
        cook_book = {}
        for line in file_obj:
            dish = line.strip()
            cook_book[dish] = []
            for item in range(int(file_obj.readline())):
                ingredients = file_obj.readline()
                ingredients_list = ingredients.split(sep=" | ")
                ingredients_dictionary = {}
                ingredients_dictionary['ingredient_name'] = ingredients_list[0]
                ingredients_dictionary['quantity'] = int(ingredients_list[1])
                ingredients_dictionary['measure'] = ingredients_list[2].strip()
                cook_book[dish].append(ingredients_dictionary)
            # file_obj.readline()
    return cook_book


# pprint(cook_book_read("../cook_book.txt"))
# pprint(f"Кулинарная книга = {cook_book}")


# pprint()

def get_shop_list_by_dishes(dishes: list, person_count: int, cook_book: dict) -> dict:
    res = {}
    for dish in dishes:
        if dish in cook_book:
            for sostav in cook_book[dish]:
                if sostav['ingredient_name'] in res:
                    res[sostav['ingredient_name']]['quantity'] += sostav['quantity'] * person_count
                else:
                    res[sostav['ingredient_name']] = {'measure': sostav['measure'],
                                                      'quantity': (sostav['quantity'] * person_count)}
        else:
            print(f"Блюда под названием {dish} нет в кулинарной книге")

    return res


if __name__ == '__main__':
    dishes = ['Омлет', 'Фахитос', 'Торт Прага', 'Запеченный картофель', 'Утка по-пекински']
pprint(get_shop_list_by_dishes(dishes, 3, cook_book_read("../cook_book.txt")))
