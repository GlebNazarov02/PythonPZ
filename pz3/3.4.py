a = [0, -1, 5, 2, 3]

print(sum([1 if a[i] < a[i+1] else 0 for i in range(len(a)-1)]))