cook_book = {
    'салат': [
        {'ingridient_name': 'сыр', 'quantity': 50, 'measure': 'гр'},
        {'ingridient_name': 'томаты', 'quantity': 2, 'measure': 'шт'},
        {'ingridient_name': 'огурцы', 'quantity': 20, 'measure': 'гр'},
        {'ingridient_name': 'маслины', 'quantity': 10, 'measure': 'гр'},
        {'ingridient_name': 'оливковое масло', 'quantity': 20, 'measure': 'мл'},
        {'ingridient_name': 'салат', 'quantity': 10, 'measure': 'гр'},
        {'ingridient_name': 'перец', 'quantity': 20, 'measure': 'гр'}
    ],
    'пицца': [
        {'ingridient_name': 'сыр', 'quantity': 20, 'measure': 'гр'},
        {'ingridient_name': 'колбаса', 'quantity': 30, 'measure': 'гр'},
        {'ingridient_name': 'бекон', 'quantity': 30, 'measure': 'гр'},
        {'ingridient_name': 'оливки', 'quantity': 10, 'measure': 'гр'},
        {'ingridient_name': 'томаты', 'quantity': 20, 'measure': 'гр'},
        {'ingridient_name': 'тесто', 'quantity': 100, 'measure': 'гр'},
    ],
    'лимонад': [
        {'ingridient_name': 'лимон', 'quantity': 1, 'measure': 'шт'},
        {'ingridient_name': 'вода', 'quantity': 200, 'measure': 'мл'},
        {'ingridient_name': 'сахар', 'quantity': 10, 'measure': 'гр'},
        {'ingridient_name': 'лайм', 'quantity': 20, 'measure': 'гр'},
    ]
}
my_dict = {}

persons = int(input('Введите количество порций: '))

for item in cook_book.items():
    for ingridient in item[1]:
        ingridient_measure = ingridient['ingridient_name'].replace(' ', '_') + ' ' + ingridient['measure']
        quantity = ingridient['quantity']
        if ingridient_measure in my_dict:
            my_dict[ingridient_measure] += quantity * persons
        else:
            my_dict.setdefault(ingridient_measure, quantity * persons)

for ing, values in my_dict.items():
    name = ing.split()
    print(name[0].capitalize().replace('_', ' ') + ':', values, name[1])