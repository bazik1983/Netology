width = int(input('Ширина: '))
length = int(input('Длина: '))
height = int(input('Высота: '))
if width <= 15 and length <= 15 and height <= 15:
    print('Коробка №1')
elif (width > 15 or length > 15 or height > 15) and (width < 50 and length < 50 and height < 50):
    print('Коробка №2')
elif length > 200:
    print('Упаковка для лыж')
else:
    print('Стандартная коробка №3')
