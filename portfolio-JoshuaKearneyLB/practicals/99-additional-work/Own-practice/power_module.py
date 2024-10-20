# X raised to the power n


def my_power(x, n):
    total = 1
    for i in range(abs(n)):
        total *= x
    if n < 0:
        return 1/total
    else:
        return total


print(my_power(3, 45))








