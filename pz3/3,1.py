n = int(input())
a = [int(input()) for i in range(n)]
k = int(input("k="))
a1 = a[k%n:]+a[:k%n]
print(a1)

# vtoroi sposob
for i in range (k%n+1):
    a.insert(0,a.pop())
print(a)