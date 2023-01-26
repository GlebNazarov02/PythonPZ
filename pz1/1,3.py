i = int(input("Year: "))


if (i % 4 == 0) and (i % 100 != 0) or (i % 400 == 0):
    print('yes')
else:
    print('no')
