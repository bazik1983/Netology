Month = input("Месяц рождения:")
Day = input("Дата рождения:")
if ((Month == 'Декабрь') and (Day >= '23')) or ((Month == 'Январь') and (Day <= '20')):
    zodiac = "Козерог"
elif (Month == 'Январь' and Day >= '21') or (Month == 'Февраль' and Day <= '19'):
    zodiac = "Водолей"
elif (Month == 'Февраль' and Day >= '20') or (Month == 'Март' and Day <= '20'):
    zodiac = "Рыбы"
elif (Month == 'Март' and Day >= '21') or (Month == 'Апрель' and Day <= '20'):
    zodiac = "Овен"
elif (Month == 'Апрель' and Day >= '21') or (Month == 'Май' and Day <= '21'):
    zodiac = "Телец"
elif (Month == 'Май' and Day >= '22') or (Month == 'Июнь' and Day <= '21'):
    zodiac = "Близнецы"
elif (Month == 'Июнь' and Day >= '22') or (Month == 'Июль' and Day <= '22'):
    zodiac = "Рак"
elif (Month == 'Июль' and Day >= '23') or (Month == 'Август' and Day <= '21'):
    zodiac = "Лев"
elif (Month == 'Август' and Day >= '22') or (Month == 'Сентябрь' and Day <= '23'):
    zodiac = "Дева"
elif (Month == 'Сентябрь' and Day >= '24') or (Month == 'Октябрь' and Day <= '23'):
    zodiac = "Весы"
elif (Month == 'Октябрь' and Day >= '24') or (Month == 'Ноябрь' and Day <= '23'):
    zodiac = "Скорпион"
elif (Month == 'Ноябрь' and Day >= '23') or (Month == 'Декабрь' and Day <= '22'):
    zodiac = "Стрелец"
print(zodiac)