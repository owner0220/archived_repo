def sum_sq(n):
    s = 0
    for i in range(1, n + 1):
        s = s + i * i
    return s

def sum_sq2(n):
    return n * (n + 1) * (2*n + 1) // 6