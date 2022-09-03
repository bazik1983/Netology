import numpy as np

n = int(input('введите количество элементов: '))
matrix = np.diag(np.arange(n, 0, -1))
print('сумма: {}'.format(sum(sum(matrix))))
