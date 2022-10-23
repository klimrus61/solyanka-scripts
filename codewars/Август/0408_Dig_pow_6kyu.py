def dig_pow(n, p):
    s = 0
    for i, d in enumerate(str(n)):
        s += int(d) ** (p+i)
    if s % n == 0:
        k = s / n
        return k
    return -1

print(dig_pow(89, 1))
