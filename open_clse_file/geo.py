list_1 = ['2018-01-01', 'yandex', 'cpc', 100, 200, 43, 43,32,532]



for i in range(len(list_1)-1):
    last = list_1.pop()
    pred_last = list_1.pop()
    new_dict = {pred_last: last}
    list_1.append(new_dict)
print(list_1[0])


# f1 = " "
# for i in list_1:
#     f1 += str(i) + " "
# print(f1)
# list_2= list_1[2:]
# print(list_2)
# list_3=list_1[1:2]
# print(list_3)
# dd={}
# d = dict([list_2])
# print(d)
# list_3.append(list_2)
# print(list_3)
# str1=str(list_1[1])
# print(str1)
# dd[str1] = d
# print(dd)
# str2=str(list_1[0])
# print(str2)
# dd1={}
# dd1[str2] = dd
# print(dd1)
