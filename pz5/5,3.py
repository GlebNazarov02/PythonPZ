def fun(n):
    if n == 0:
        return ''
    nums = input()
    return fun(n-1) + f"{nums} "

print(fun(int(input())))