chis = int(input("Введите трехзначное число"))
i = 0
s = 0
if (chis < 100) or (chis > 999):
    print('не трехзачное')
else:
    while i < 3:
        s += chis % 10
        i += 1
        chis = chis//10
    print(s)
