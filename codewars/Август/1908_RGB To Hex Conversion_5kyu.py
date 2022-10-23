def rgb(r, g, b):
    res = []
    for i in (r, g, b):
        if i < 0:
            i = 0
        elif i > 255:
            i = 255
        s = f'{i:X}'
        if len(s) == 1:
            res.append('0'+s)
        else:
            res.append(s)
    return ''.join(res)

# чужые примеры
def rgb(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))

# Второй пример
def limit(num):
    if num < 0:
        return 0
    if num > 255:
        return 255
    return num


def rgb(r, g, b):
    return "{:02X}{:02X}{:02X}".format(limit(r), limit(g), limit(b))