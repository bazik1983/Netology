dubli = []
spisok = input('Введите числа разделенные пробелом: ').split()
for i in spisok:
    if spisok.count(i) > 1:
        dubli.append(i)
if len(dubli) > 0:
    print(*set(filter(lambda x: spisok.count(x) > 1, spisok)))
else:
    print('Повторяющихся чисел нет')
