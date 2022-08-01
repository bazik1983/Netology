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
def get_info():
    dishes = input('Введите блюда через запятую')
    persons = int(input('Введите количество гостей'))
    return (dishes.split(','), persons)

def get_shop_list_by_dishes(dishes, person_count):
    shop_dict = {}
    for dish in dishes:
        for ingr in cook_book[dish]:
            key = (ingr['ingridient_name'], ingr['measure'])
            if key not in shop_dict:
                shop_dict[key] = ingr['quantity'] * person_count
            else:
                shop_dict[key] += ingr['quantity'] * person_count
    return shop_dict

dishes, persons = get_info()
print(get_shop_list_by_dishes(dishes, persons))

def print_info(shop_list):
    for ingr, q in shop_list.items():
        return f'{ingr[0]}: {q}{ingr[1]}'

dishes, persons = get_info()
shop_list = get_shop_list_by_dishes(dishes, persons)
print(print_info(shop_list))