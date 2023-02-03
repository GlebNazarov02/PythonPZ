# a = [i+ 10 if i % 2 == 0 else i**3 for i in range(26)]

# print(a)

#a = {k:v**3 for k,v in zip("ABCDEFGH" , range(1,11))}

#print(a)

n = int(input())
a = [int(input()) for i in range (n)]
print("vsgo:{0}".format (len(set(a))))