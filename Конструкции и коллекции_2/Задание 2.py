queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
]

storage = {}

for query in queries:
    words = query.split()

    if len(words) in storage.keys():
        storage[len(words)] += 1
    else:
        storage.update({
            len(words): 1
        })

for key, value in sorted(storage.items()):
    percentage = round((value / len(queries)) * 100, 2)
    print(f'Поисковых запросов, содержащих {key} слов(а): {percentage}%')