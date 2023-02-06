sp = input().split()
result = {}.fromkeys(sp,0)

for i in sp:
    print(f"{i}_{result[i]}" if result[i] else i,end = ' ')
    result[i] += 1