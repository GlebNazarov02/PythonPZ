n = int(input())
m = int(input())
a = {int(input()) for _ in range(n)}
b = {int(input()) for _ in range(m)}
c = list(a.intersection(b))
print(sorted(c))
