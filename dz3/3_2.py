n = int(input())
a = [int(input()) for i in range (n)]
x = int(input())
s = x
i1 = 0

for i in range (n):
    if abs(a[i]-x) < s:
        s = abs(a[i]-x)
        i1 = i

print(a[i1])