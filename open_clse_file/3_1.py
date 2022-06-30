import os
from pprint import pprint

data = {}
for filename in os.listdir("sorted"):
    with open(os.path.join("sorted", filename), 'r', encoding='utf-8') as file_obj:
        values = []

        for line in file_obj:

            values.append(line.strip())
            data[filename] = values

# pprint(data)

def sorted_tuple(tuple_1):
    return len(tuple_1[1])


sorted_tuples = sorted(data.items(), key=sorted_tuple)

for i in sorted_tuples:
    print(i)


