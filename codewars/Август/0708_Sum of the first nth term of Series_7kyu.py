def series_sum(n):
    s = 0
    for i in range(n):
        a = i * 3
        s += 1 / (1 + a)
    return f"{s:.{2}f}"

