with open("cook_book.txt", 'r', encoding="utf-8") as f:
    cook_booking = {}
    for line in f:
        dish = line.strip()
        ingredients = []
        for i in range(int(f.readline())):
            ingredient = f.readline()
            ingredient_list = ingredient.split(sep='|')
            product_dict = {}
            product_dict['ingredient_name']=ingredient_list[0]
            product_dict['quantity']=ingredient_list[1]
            product_dict['measure'] = ingredient_list[2]
            product_list = [product_dict]
            cook_booking[dish] = product_list
            print(cook_booking)
            # print(product_list)
            # print(product_dict)
            # print(list(cook_booking.keys()))
        # f.readline()


            # ingredients.append(ingredient.strip())
            # cook_booking[dish] = ingredients



# print(ingredients)
            print(f"кулинарная книга = {cook_booking}")

        # f.readline()
        # print(line.strip())
