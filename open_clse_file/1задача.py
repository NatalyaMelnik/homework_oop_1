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

pprint(f"Кулинарная книга = {cook_book}")


