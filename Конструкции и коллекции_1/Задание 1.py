word = input()
dlina = len(word)
if dlina % 2 == 0:
    print(word[int(dlina / 2 - 1):int(dlina / 2 + 1)])
else:
    print(word[int(dlina / 2)])
