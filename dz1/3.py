chis = int(input("Введите номер билета:"))
i = 0
right = 0
left = 0
if (chis < 100000) or (chis > 999999):
    print('не шесть знаков')
else:
    while i < 3:
        right += chis % 10
        i += 1
        chis = chis//10
    while i < 6:
        left += chis % 10
        i += 1
        chis = chis//10
    if left == right:
        print('yes')
    else:
        print('no')
