number = int(input('Введите номер билета: '))
a = (number // 100000) % 10
b = (number // 10000) % 10
c = (number // 1000) % 10
d = (number // 100) % 10
e = (number // 10) % 10
f = number % 10
if a + b + c == d + e + f:
    print('Cчастливый билет')
else:
    print('Несчастливый билет')
