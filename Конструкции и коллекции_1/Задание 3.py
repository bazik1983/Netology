boys = input('Введите имена парней через запятую: ').split(',')
girls = input('Введите имена девушек через запятую: ').split(',')
if len(boys) != len(girls):
    print('Внимание, кто-то может остаться без пары!')
else:
    boys_sorted = sorted(boys)
    girls_sorted = sorted(girls)
    ideal_couples = dict(zip(boys_sorted, girls_sorted))
    print('Идеальные пары:')
    for boy, girl in ideal_couples.items():
        print(f"{boy} и {girl}")
