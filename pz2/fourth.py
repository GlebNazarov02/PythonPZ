n = int(input())
i = 0

for i in range(n):
    arb = int(input())
    if i == 0:
        maximum = arb
        minimum = arb
    if arb > maximum:
        maximum = arb
    elif arb < minimum:
        minimum = arb
print(minimum,maximum)