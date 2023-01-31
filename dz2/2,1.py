n = int(input())
i = 0
s = 0
m = 0

for i in range(n):
    a = int(input())
    if a == 1:
        s += 1
    elif a == 0:
        m += 1
    else:
        break

if i < n-1:
    print("неккоректное значение")
elif s > m:
    print(n - s)
else:
    print(n - m)
