from pprint import pprint

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


# pprint(f"Кулинарная книга = {cook_book}")
# pprint()

def get_shop_list_by_dishes(*dishes, person_count):
    res = {}
    cook_book_lower = dict((k.lower(), v) for k, v in cook_book.items())
    for dish in dishes:
        if dish.lower() in cook_book_lower:
            for sostav in cook_book[dish]:
                if sostav['ingredient_name'] not in res:
                    res[sostav['ingredient_name']] = {}
                    res[sostav['ingredient_name']]['measure'] = res['measure']
                    res[sostav['ingredient_name']]['quantity'] = int(sostav['quantity']) * person_count
                else:
                    res[sostav['ingredient_name']]['quantity'] += int(sostav['quantity']) * person_count
        else:
            print(f"В кулинарной книге нет блюда под названием {dish}\n")
    return res



get_shop_list_by_dishes("Фахитос", "Омлет", person_count=2)
