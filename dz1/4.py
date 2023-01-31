n = int(input('1storona:'))
m = int(input('2storona:'))
k = int(input('dolki:'))
if k < m*n and (k % m == 0 or k % n == 0):
    print('YES')
else:
    print('NO')
