num = int(input())
f1 = 0
f2 = 1
i = 2

while f2 <= num:
    if f2 == num:
        print(i)
        break
    f1, f2 = f2, f1+f2
    i += 1
else:
    print(-1)
