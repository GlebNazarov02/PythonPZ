def rifma(strocka):
    a = strocka.lower().split()
    f = lambda x: sum(1 for i in x if i in 'аеёиоуыэюя')
    temp = f(a[0])
    if all([f(i) == temp for i in a]):
        return 'Парам пам-пам'
    return 'Пам парам'


print(rifma(input()))
