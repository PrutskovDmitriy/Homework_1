for i in range(1, 101):
    if i in range(5, 21):
        print(i, 'процентов')
    elif i % 10 in range(2, 5):
        print(i, 'процента')
    elif i % 10 == 1:
        print(i, 'процент')
    else:
        print(i, 'процентов')
