def catalog_reader(fil_name):
    with open("cook_book.txt", 'r', encoding="utf-8") as file:
        for line in file:
            dish_name = line.strip()
            name_key = ['ingredient_name', 'quantity', 'measure']
            for item in range(int(file.readline())):
                product = file.readline()
                product_list = product.split('| ')
                dict_product = {}
                dict_product[name_key[0]] = product_list[0]
                dict_product[name_key[1]] = product_list[1]
                dict_product[name_key[2]] = product_list[2].strip()
                list_product = [dict_product]
                cook_book = {}
                cook_book[dish_name] = list_product
            print(cook_book)
            # file.readline()

catalog_reader('cook_book')
# print(f"кулинарная книга = {cook_book}")

