def sum(a, b):
    if b == 0:
        return a
    return sum(a, b-1) + 1


print(sum(int(input()), int(input())))
