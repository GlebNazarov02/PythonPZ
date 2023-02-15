a = list(map(int,input().split()))
b = max(a)
c = min(a)
print(list(i for i in range(len(a)) if a[i] > c and a[i] < b ))