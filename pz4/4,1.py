sp = input().upper().split(" ")
a = []
for i in sp:
   a += i.split()
print(len(set(a)))