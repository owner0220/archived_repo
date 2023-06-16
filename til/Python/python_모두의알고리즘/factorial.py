def fact(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f


def factrecul(n):
    if n <= 1:
        return 1
    return n*factrecul(n-1)