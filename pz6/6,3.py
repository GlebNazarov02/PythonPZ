m = int(input())
for i in range(1, m):
    k = 0
    n = 0
    for x in range(1, i):
        if i % x == 0:
            k += x
    for j in range(1, k):
        if k % j == 0:
            n += j
    if i == n and i != k and i == min(i, k):
        print(i, k)