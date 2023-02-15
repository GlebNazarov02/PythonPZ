a = int(input())
d = int(input())
n = int(input())

print(list(a + (i-1) * d for i in range(1,n+1)))