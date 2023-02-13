a = list(map(int,input().split()))
b = list(map(int,input().split()))
print(*(item for item in a if item not in b))