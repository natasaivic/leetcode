# 50. Pow(x, n)

# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).


def myPow(x, n):
    # deal with negative power, negative value of n
    if n < 0:
        x = 1/x
        n = abs(n)

    # iteration
    res = 1
    while n > 0:
        if n % 2 == 1:
            res = res * x
        x = x * x
        n = n // 2

    return res
        