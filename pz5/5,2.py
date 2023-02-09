def cratn(n):
    if n == 1:
        return'net'
    if n == 2:
        return'da'
    for i in range(3,n,2):
        if n % i == 0:
            return 'net'
    return 'da'

print(cratn(int(input())))


# def is_prime_number(n):
    # if n == 2:
        # return True
    # elif n == 1 or n % 2 == 0:
        # return False
    # for i in range(3, int((n ** 0.5) + 1), 2):
        # if (n % i == 0):
            # return False
    # return True


# print(is_prime_number(int(input())))
