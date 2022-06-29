queris = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
    'сериалы',
]

storage = {}
for i in queris:
    count_words = i.split()
    print(count_words)
    if len(count_words) in storage.keys():
        storage[len(count_words)] += 1
    else:
        storage.update({len(count_words): 1})
for k, v in storage.items():
    percent = round((v / len(queris)) * 100, 2)
    print(f'Запросов из {k} слов: {percent}% ({v} запроса)')
