n = int(input("Ввести n:"))
fact = 1

if n >= 0:
    while n != 0:
        fact *= n
        n -= 1
    print(fact)
else:
    print("n0pe")
