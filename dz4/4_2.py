n = int(input())
a = [int(input()) for _ in range(n)]
max = 0

for i in range(1, n-1):
    if (a[i-1]+a[i]+a[i+1]) > max:
        max = a[i-1]+a[i]+a[i+1]

print(max)
