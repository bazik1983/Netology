from typing import List

stream = [
    '2018-01-01,user1,3',
    '2018-01-07,user1,4',
    '2018-03-29,user1,1',
    '2018-04-04,user1,13',
    '2018-01-05,user2,7',
    '2018-06-14,user3,4',
    '2018-07-02,user3,10',
    '2018-03-21,user4,19',
    '2018-03-22,user4,4',
    '2018-04-22,user4,8',
    '2018-05-03,user4,9',
    '2018-05-11,user4,11',
]
user_stream = []
summa = 0
for i in stream:
    i = i.split(',')
    summa = summa + int(i[2])
    user_stream.append(i[1])
print('Среднее количество просмотров на уникального пользователя: ', round(summa / len(set(user_stream)), 2))
