def step(a,b):
    if b == 0:
        return 1
    return step(a,b-1) * a

print(step(int(input()),int(input())))