a = int(input())
b = int(input())
c = 0
for i in range(1000):
    if c:
        break
    for j in range(1000):
        if i + j == a and i * j == b:
            print(i, j)
            c = 1
            break
