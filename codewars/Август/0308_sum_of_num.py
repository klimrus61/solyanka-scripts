# Сумму чисел между a и b вкл их
def get_sum(a,b):
    l = sorted([a,b])
    return a if a == b else sum([i for i in range(l[0], l[1]+1)])

def get_sum(a,b):
    return sum(range(min(a, b), max(a, b) + 1))
