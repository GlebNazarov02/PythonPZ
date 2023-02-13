a = list(map(int,input().split(" ")))
counte = 0

for i in range(1,len(a)-1):
    if a[i] == max(a[i-1:i+2]):
        counte += 1

print(counte)