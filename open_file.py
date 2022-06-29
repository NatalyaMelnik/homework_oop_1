with open("cook_book.txt", 'r', encoding="utf-8") as f:
    cook_booking = {}
    # lines = f.readlines()
    for line in f:
        dish = line.strip()
        print(f"Название блюда: {dish}")
        cook_booking[dish] = []
        ingredients = f.readline()
        for i in range(int(ingredients)):
            ingredients_list = ingredients.split(sep=" | ")
            print(f"Ингредиенты: {f.readline()}")
        #     ingredients_dict = {}
        #     ingredients_dict["ingredient_name"] = ingredients_list[0]
        #     ingredients_dict["quantity"] = ingredients_list[1]
        #     ingredients_dict["measure"] = ingredients_list[2]
        # print(dish)


        # cook_booking[dish].append(ingredients_dict)

print(f"кулинарная книга = {cook_booking}")

        # f.readline()
        # print(line.strip())
