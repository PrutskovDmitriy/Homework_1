duration = int(input('Введите секунды: '))
if duration < 60:
    print(str(duration) + 'сек ')
elif duration < 3600:
    print(str(duration // 60) + 'мин ' + str(duration % 60))
elif duration < 86400:
    print(str(duration // 3600) + 'час ' + str(duration % 3600 // 60) + 'мин ' + str(duration % 60) + 'cек')
else:
    print(str(duration // 86400) + 'дни ' + str(duration % 84600 // 3600) + 'час '
          + str(duration % 84600 % 3600 // 60) + 'мин ' + str(duration % 60) + 'сек')
