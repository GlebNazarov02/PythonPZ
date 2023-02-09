list_1 = list(map(int,input().split(" "))) 
print(list_1)

for i in range(len(list_1)):
    if list_1[i] == max(list_1):
        list_1[i] = min(list_1)

print(list_1)

# def max_to_min(list):
    # Min = min(list)
    # MAx = max(list)
    # return [ Min if i == MAx else i for i in list ]
# print(*max_to_min([int(i) for i in input().split()]))
