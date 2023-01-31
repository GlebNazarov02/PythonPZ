n = int(input("vvedite dni:"))
maximum_row = current_row = 0
for i in range (n):
    temp = int(input())
    if temp > 0:
        current_row += 1
    elif current_row > maximum_row:
        maximum_row,current_row = current_row,0
        current_row = 0
print(maximum_row)
